# FilterBlade Automation — Claude Code Notes

This project automates color scheme application to FilterBlade.xyz (NeverSink PoE2 filter) using Playwright MCP browser automation.

## Goal

Apply a custom color theme ("Cosmic Gold") to a NeverSink Semi-Strict filter on FilterBlade.xyz, save it to FilterBlade's server so it persists, and upload it to PoE via OAuth sync.

## Environment

- **Site**: https://www.filterblade.xyz/?game=Poe2
- **Filter**: NeverSink SC Semi-Strict Normal, PoE2
- **Tool**: Playwright MCP (`mcp__playwright__browser_evaluate`)

---

## FilterBlade Internal Architecture

### Key Global Objects

```javascript
gFilterBlade                            // root namespace
gFilterBlade.changeStorage              // change tracking system
gFilterBlade.filterData                 // the parsed filter
gFilterBlade.filterData.filterEntryStyles.styleToDetails  // map: styleId → FilterEntryStyle (COLORS)
gFilterBlade.filterData.strictnessCluster  // map: groupName → FilterEntry[] (SHOW/HIDE)
gFilterBlade.filterData.filterEntries   // array of all 1270 FilterEntry objects
gFilterBlade.filterData.waypoints       // named anchor points into the filter (64 total)
gFilterBlade.styleEditor                // style editor UI
gFilterBlade.styleEditor.styleCombiEditor  // per-theme editor
```

### styleToDetails Structure

Each entry in `styleToDetails[styleId]`:
- `.styleContentFilterEntry.lineList` — array of FilterLine objects
  - Each line: `{ ident, param: [r,g,b,a], raw, rebuiltLine, isEverModified }`
  - `ident` values: `'SetTextColor'`, `'SetBorderColor'`, `'SetBackgroundColor'`
- `.filterEntries` — array of actual filter rules using this style
- `.updateAllConnectedEntries()` — propagates lineList changes to all connected filter rules

### changeStorage Structure

```javascript
cs = gFilterBlade.changeStorage
cs.changeGroups[0].changes          // array of AbstractChange objects (NOT groupChanges)
cs.unsavedChanges                   // boolean
cs.savable                          // must be true for addChange to work
cs.addChange(type, valueObj, skipLS)  // records a change, returns AbstractChange or null
cs.updateLocalStorage()             // persists to browser localStorage
```

### Change Object Format (style color changes)

```javascript
// Type: "dynamic"
// valueObj:
{
  styleId: "apex_stier",            // GFT style key
  identifier: {
    identifier: "SetTextColor",     // or "SetBorderColor"
    mode: "normal",
    index: 1,
    version: 3,
    isReal: true
  },
  newValue: "rgb(184, 240, 255)",   // CSS rgb string
  logicName: "editStyleCombi",
  version: 1
}
```

---

## Customize Tab — Show/Hide Rules

The Customize tab controls **filter behavior** (what items are shown/hidden at what strictness levels).
This is a completely separate system from color styles.

### strictnessCluster Structure

`gFilterBlade.filterData.strictnessCluster` is a map of **group name → FilterEntry[]**.
Each FilterEntry is one Show/Hide rule block in the filter.

```javascript
const sc = gFilterBlade.filterData.strictnessCluster;
// Groups (16 total):
// Gold, SpecialCases, Exotics, Technical, Crafting, ModTierRare, ModTierMagic,
// SalvageMisc, Rares, Socketables, Fragments, Gems, Maps, Leveling, Currency, Uniques
```

The full dump of all groups and entries is saved at `strictnessCluster-dump.json` (537 entries).

### FilterEntry Key Fields

Each FilterEntry has:
- `entryId` — numeric index into `filterData.filterEntries`
- `tagID` — string key like `"currency;s"`, `"gold;stack3"` (type;tier)
- `tierTagType` — the item category (`"currency"`, `"gold"`, `"uniques"`, etc.)
- `tierTagTier` — the tier within that category (`"s"`, `"a"`, `"supplieslow"`, etc.)
- `strictnessGroup` — which Customize UI section this belongs to
- `dataType` — current `"Show"` or `"Hide"`
- `active` / `frozen` / `conditional` — state flags
- `displayName` — human label (e.g. `"Gold Pile: Gigantic"`, `"S Tier"`)

### Reading & Setting Show/Hide

```javascript
// Find entry by tagID
const sc = gFilterBlade.filterData.strictnessCluster;
const entry = sc['Currency'].find(e => e.tagID === 'currency;s');
entry.get_ShowHide()          // → "Show" or "Hide"
entry.set_ShowHide("Hide")    // mutates in-memory state only (like setColor)
```

`set_ShowHide(e)` sets `lineList[0].ident` and calls `setExplicitShd(e)`. It does **not** auto-record to changeStorage.

### Recording Show/Hide Changes

After calling `set_ShowHide`, record the change so FilterBlade can persist it.
Use `recordAllShowHideChanges()` to batch-record all entries at once (parallel to `recordAllColorChanges`):

```javascript
function recordAllShowHideChanges() {
  const sc = gFilterBlade.filterData.strictnessCluster;
  const cs = gFilterBlade.changeStorage;

  // These are the neutral/default stat values FilterBlade auto-supplies per entry.
  // Observed by clicking a UI checkbox and inspecting changeStorage.
  const defaultStats = {
    StackSize:          { value: 1,       isDerivable: true, isExpanded: false },
    GemLevel:           { value: 1,       isDerivable: true, isExpanded: false },
    Quality:            { value: 0,       isDerivable: true, isExpanded: false },
    Identified:         { value: "False", isDerivable: true, isExpanded: false },
    Corrupted:          { value: "False", isDerivable: true, isExpanded: false },
    HasImplicitMod:     { value: "False", isDerivable: true, isExpanded: false },
    AnyEnchantment:     { value: "False", isDerivable: true, isExpanded: false },
    Mirrored:           { value: "False", isDerivable: true, isExpanded: false },
    CorruptedMods:      { value: 0,       isDerivable: true, isExpanded: false },
    UnidentifiedItemTier: { value: 1,     isDerivable: true, isExpanded: false },
    HasVaalUniqueMod:   { value: "False", isDerivable: true, isExpanded: false },
    TwiceCorrupted:     { value: "False", isDerivable: true, isExpanded: false },
    AlwaysShow:         { value: "False", isDerivable: true, isExpanded: false },
    IsVaalUnique:       { value: "False", isDerivable: true, isExpanded: false }
  };

  let added = 0, skipped = 0;

  for (const entries of Object.values(sc)) {
    for (const entry of entries) {
      const res = cs.addChange("normal", {
        version: 3,
        items: [{
          stats: defaultStats,
          gameOnlyStats: {},
          utilStats: {
            cName:    { value: entry.getDisplayName?.() ?? entry.tagID, isExpanded: false },
            cVers:    { value: "3.0", isExpanded: false },
            itemTag:  { value: entry.tagID, isExpanded: false }
          },
          isSupplied: true,
          isAutoSupplyingStats: true
        }],
        identifier: { identifier: "ShowHide", mode: "normal", index: 1, version: 3, isReal: true },
        newValue: entry.get_ShowHide()
      }, true);
      res ? added++ : skipped++;
    }
  }

  cs.updateLocalStorage();
  return { added, skipped, total: cs.changeGroups[0].changes.length };
}
```

### Waypoints — Section Anchors

`gFilterBlade.filterData.waypoints.lookUp` maps 64 named anchor IDs to FilterEntry objects.
These are the "insert custom rules here" points for the Customize UI's "Add custom Show/Hide rule" sections.

```javascript
const wp = gFilterBlade.filterData.waypoints.lookUp;
// Example keys: "c9.currency.single", "c11.uniques.all", "c21.leveling.gear.all"
const entry = wp['c9.currency.single'].entry;
```

Full waypoint ID list saved in `strictnessCluster-dump.json` exploration.

### Customize Tab → strictnessGroup Mapping

| Customize UI Section | strictnessGroup(s) |
|---|---|
| General Currency | Currency |
| Socketables | Socketables |
| Campaign & Exotics | Exotics, SpecialCases |
| Uniques | Uniques |
| Gems | Gems |
| Gold | Gold |
| Waystones | Maps |
| Tablets / Map-like | Fragments |
| Endgame Rares & Crafting | Rares, Crafting |
| Endgame Salvageable | SalvageMisc |
| Flasks & Charms | (within Leveling/Technical) |
| Campaign | Leveling, Technical |
| Exceptional & Identified | ModTierRare, ModTierMagic |
| Special Rules | SpecialCases, Technical |

---

## Workflow: Applying a Color Scheme

### Step 1 — Set colors in filter data

Use `setColor()` for styles that already have text/border lines:

```javascript
function setColor(styleId, textHex, borderHex) {
  const styleToDetails = gFilterBlade.filterData.filterEntryStyles.styleToDetails;
  const style = styleToDetails[styleId];
  if (!style) return `MISSING: ${styleId}`;
  const lineList = style.styleContentFilterEntry.lineList;

  function hexToRgba(hex) {
    return [parseInt(hex.slice(1,3),16), parseInt(hex.slice(3,5),16), parseInt(hex.slice(5,7),16), 255];
  }

  if (textHex) {
    const line = lineList.find(l => l.ident === 'SetTextColor');
    if (line) {
      const [r,g,b,a] = hexToRgba(textHex);
      line.param[0]=r; line.param[1]=g; line.param[2]=b; line.param[3]=a;
      line.raw=`\tSetTextColor ${r} ${g} ${b} ${a}`;
      line.rebuiltLine=`SetTextColor ${r} ${g} ${b} ${a}`;
      line.isEverModified=true;
    }
  }
  if (borderHex) {
    const line = lineList.find(l => l.ident === 'SetBorderColor');
    if (line) {
      const [r,g,b,a] = hexToRgba(borderHex);
      line.param[0]=r; line.param[1]=g; line.param[2]=b; line.param[3]=a;
      line.raw=`\tSetBorderColor ${r} ${g} ${b} ${a}`;
      line.rebuiltLine=`SetBorderColor ${r} ${g} ${b} ${a}`;
      line.isEverModified=true;
    }
  }
  style.updateAllConnectedEntries();
  return `OK: ${styleId}`;
}
```

Use `addColorToBackgroundTheme()` for styles that only have a background color (need text/border added):

```javascript
function addColorToBackgroundTheme(styleId, textHex, borderHex) {
  const styleToDetails = gFilterBlade.filterData.filterEntryStyles.styleToDetails;
  const style = styleToDetails[styleId];
  if (!style) return `MISSING: ${styleId}`;
  const entry = style.styleContentFilterEntry;
  const lineList = entry.lineList;

  function hexToRgba(hex) {
    return [parseInt(hex.slice(1,3),16), parseInt(hex.slice(3,5),16), parseInt(hex.slice(5,7),16), 255];
  }

  // Find a reference text line to clone from any style that has one
  const refStyle = Object.values(styleToDetails).find(s =>
    s.styleContentFilterEntry.lineList.find(l => l.ident === 'SetTextColor')
  );
  const refTextLine = refStyle.styleContentFilterEntry.lineList.find(l => l.ident === 'SetTextColor');
  const refBorderLine = refStyle.styleContentFilterEntry.lineList.find(l => l.ident === 'SetBorderColor');

  const added = [];
  if (textHex && !lineList.find(l => l.ident === 'SetTextColor')) {
    const [r,g,b,a] = hexToRgba(textHex);
    const newLine = refTextLine.clone();
    newLine.param = [r,g,b,a];
    newLine.raw = `\tSetTextColor ${r} ${g} ${b} ${a}`;
    newLine.rebuiltLine = `SetTextColor ${r} ${g} ${b} ${a}`;
    newLine.isEverModified = true;
    entry.addLine(newLine);
    added.push('text');
  }
  if (borderHex && !lineList.find(l => l.ident === 'SetBorderColor')) {
    const [r,g,b,a] = hexToRgba(borderHex);
    const newLine = refBorderLine.clone();
    newLine.param = [r,g,b,a];
    newLine.raw = `\tSetBorderColor ${r} ${g} ${b} ${a}`;
    newLine.rebuiltLine = `SetBorderColor ${r} ${g} ${b} ${a}`;
    newLine.isEverModified = true;
    entry.addLine(newLine);
    added.push('border');
  }
  style.updateAllConnectedEntries();
  return `OK ${styleId}: added [${added.join(',')}]`;
}
```

### Step 2 — Record changes to changeGroups

After setting filter data, iterate all styles and add changes so FilterBlade can persist them:

```javascript
function recordAllColorChanges() {
  const styleToDetails = gFilterBlade.filterData.filterEntryStyles.styleToDetails;
  const cs = gFilterBlade.changeStorage;
  const mkId = (colorType) => ({identifier: colorType, mode: "normal", index: 1, version: 3, isReal: true});

  let added = 0, skipped = 0;

  for (const [styleId, style] of Object.entries(styleToDetails)) {
    const lineList = style.styleContentFilterEntry?.lineList;
    if (!lineList) continue;

    const textLine = lineList.find(l => l.ident === 'SetTextColor');
    const borderLine = lineList.find(l => l.ident === 'SetBorderColor');

    if (textLine) {
      const [r,g,b] = textLine.param;
      const res = cs.addChange("dynamic", {
        styleId,
        identifier: mkId('SetTextColor'),
        newValue: `rgb(${r}, ${g}, ${b})`,
        logicName: 'editStyleCombi',
        version: 1
      }, true);
      res ? added++ : skipped++;
    }

    if (borderLine) {
      const [r,g,b] = borderLine.param;
      const res = cs.addChange("dynamic", {
        styleId,
        identifier: mkId('SetBorderColor'),
        newValue: `rgb(${r}, ${g}, ${b})`,
        logicName: 'editStyleCombi',
        version: 1
      }, true);
      res ? added++ : skipped++;
    }
  }

  cs.updateLocalStorage();
  return { added, skipped, total: cs.changeGroups[0].changes.length };
}
```

### Step 3 — Save & Upload

Click the "Save & Upload once" button (or "Save as new"):

```javascript
document.getElementById('dlScreen_SyncContent').click();
// A browser confirm() dialog appears — accept it
```

**Known issue**: The FilterBlade profile save to AWS (profileSaveStates API) returns 401 if the session token has expired. This only affects the FilterBlade save-state; the PoE filter upload still succeeds. Fix: log out and back in to refresh the OAuth token, then save again.

---

## Common Pitfalls

| Problem | Cause | Fix |
|---|---|---|
| Changes not recorded | Modified `lineList` directly, bypassing `addChange` | Call `recordAllColorChanges()` after setting colors |
| `isRedundantChange` returns true | Trying to add same change twice | Skip — `addChange` returns null, not an error |
| `addLine()` adds to wrong entry | Wrong `styleContentFilterEntry` | Use `style.styleContentFilterEntry`, not `.filterEntries[0]` |
| Error modal after save | Part of the save flow failed | Check console; the PoE upload may have still succeeded |
| 401 on profile save | Session token expired | Log out, log back in, save again |
| Page reload loses all changes | In-memory JS edits are not persisted | Re-apply all `setColor` calls and re-run `recordAllColorChanges` |

---

## Reference Data Files

Two JSON snapshots are saved in the project root. They capture the **default state** of the filter and serve as a lookup reference — no need to recreate them unless the filter version changes.

| File | Contents | Use |
|---|---|---|
| `styleToDetails-dump.json` | All 93 style IDs, which color lines each has (text/border/background), default RGBA values | Know which styles exist and whether to use `setColor` vs `addColorToBackgroundTheme` |
| `strictnessCluster-dump.json` | All 537 show/hide entries grouped by category, with `tagID`, `displayName`, default show/hide state | Look up `tagID` values to pass to `set_ShowHide` / `recordAllShowHideChanges` |

---

## Verifying Changes

```javascript
// Count recorded changes
gFilterBlade.changeStorage.changeGroups[0].changes.length

// Inspect a specific change
JSON.parse(gFilterBlade.changeStorage.changeGroups[0].changes[0].changeValue)

// Verify a style's current text color
const s = gFilterBlade.filterData.filterEntryStyles.styleToDetails['apex_stier'];
s.styleContentFilterEntry.lineList.find(l => l.ident === 'SetTextColor').param
// → [184, 240, 255, 255]
```

## Exporting the Filter File

On the EXPORT tab, click "Download Filter" to save a `.filter` file. This bakes in all current in-memory colors — useful as a backup even if the FilterBlade save fails.

The exported filter is saved to:
- `~/Documents/My Games/Path of Exile 2/` (for in-game use)
- The project root as `Cosmic-Gold.filter` (backup copy)
