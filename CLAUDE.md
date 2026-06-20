# FilterBlade Automation — Claude Code Notes

This project automates color scheme application to FilterBlade.xyz (NeverSink PoE2 filter) using Playwright MCP browser automation.

## Goal

Apply a custom color theme ("Dark Moody Amethyst") to a NeverSink Semi-Strict filter on FilterBlade.xyz, save it to FilterBlade's server so it persists, and upload it to PoE via OAuth sync.

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

### Change Object Formats

FilterBlade uses two `logicName` values for `addChange("dynamic", ...)`. **Use the wrong one and the change is silently ignored.**

#### `editStyleCombi` — style-level changes (colors, beams)

Target by `styleId`. Covers: `SetTextColor`, `SetBorderColor`, `SetBackgroundColor`, `PlayEffect`.

```javascript
// Color (newValue must be a CSS rgb string — NOT hex)
cs.addChange("dynamic", {
  styleId: "apex_stier",
  identifier: { identifier: "SetTextColor", mode: "normal", index: 1, version: 3, isReal: true },
  newValue: "rgb(199, 125, 255)",
  logicName: "editStyleCombi",
  version: 1
}, true);

// Beam — permanent only (no "Temp"); null = beam off
cs.addChange("dynamic", {
  styleId: "apex_stier",
  identifier: { identifier: "PlayEffect", mode: "normal", index: 1, version: 3, isReal: true },
  newValue: ["Purple"],
  logicName: "editStyleCombi",
  version: 1
}, true);
```

#### `editFilterEntry` — per-rule changes (sounds, icons)

Target by `itemTag` instead of `styleId`. Covers: `PlayAlertSound`, `MinimapIcon`.

```javascript
// Sound
cs.addChange("dynamic", {
  identifier: { identifier: "PlayAlertSound", mode: "normal", index: 1, version: 3, isReal: true },
  newValue: ["CustomAlertSound", ["Stefan Gold_6veryvaluable.mp3", 300]],
  logicName: "editFilterEntry",
  version: 1,
  itemTag: "currency;s"
}, true);

// Map icon — size: "0"=large "1"=medium "2"=small
cs.addChange("dynamic", {
  identifier: { identifier: "MinimapIcon", mode: "normal", index: 1, version: 3, isReal: true },
  newValue: ["0", "Purple", "Star"],
  logicName: "editFilterEntry",
  version: 1,
  itemTag: "currency;s"
}, true);
```

Available icon colors: Blue, Green, Brown, Red, White, Yellow, Cyan, Grey, Orange, Pink, Purple.
Available icon shapes: Circle, Diamond, Hexagon, Square, Star, Triangle, Cross, Moon, Raindrop, Kite, Pentagon, UpsideDownHouse.

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

### Customize Tab: Gem Icon Overrides

Gem icon shapes **cannot** be set on a style key — skill, spirit, and support gems all share the same style keys (`typebased_gems1/2/3`). Icon shape must be set per-rule via `editFilterEntry` targeting each gem's `itemTag`.

Navigate to **Customize → Gems** and expand each subsection, or apply programmatically:

```javascript
function setIcon(itemTag, size, color, shape) {
  const cs = gFilterBlade.changeStorage;
  cs.addChange('dynamic', {
    identifier: { identifier: 'MinimapIcon', mode: 'normal', index: 1, version: 3, isReal: true },
    newValue: [size, color, shape],
    logicName: 'editFilterEntry',
    version: 1,
    itemTag
  }, true);
}
```

Dark Moody Amethyst gem icon assignments:

| itemTag | Size | Color | Shape |
|---|---|---|---|
| `gems->uncut;skill20` | `"0"` | Purple | Triangle |
| `gems->uncut;skill19` | `"1"` | Purple | Triangle |
| `gems->uncut;skillgemprogression18` through `14` | `"2"` | Purple | Triangle |
| `gems->uncut;spirit20` | `"0"` | Purple | Kite |
| `gems->uncut;spirit19` | `"1"` | Purple | Kite |
| `gems->uncut;spiritgemprogression18` through `14` | `"2"` | Purple | Kite |
| `gems->uncut;supportearlymaps` | `"1"` | Blue | Diamond |
| `gems->uncut;othersupporteg` | `"2"` | Blue | Diamond |
| `gems->lineage;s` | `"0"` | Pink | Diamond |
| `gems->lineage;a` | `"1"` | Pink | Diamond |
| `gems->lineage;b` | `"2"` | Pink | Diamond |
| `gems;upgradedgemstwice` | `"2"` | Grey | Diamond |
| `gems;upgradedgemslevel` | `"2"` | Grey | Diamond |

See `dark-moody-amethyst-MANUAL.md` "CUSTOMIZE TAB — Gem Icon Overrides" for the full UI navigation path per rule.

### Customize Tab: Waystone Per-Rule Colors (Normal Section)

Waystones do **not** connect to style keys in the usual way — per-tier colors must be set directly on individual rules in **Customize → Other Endgame Items → Waystones → Normal**.

Do not touch the Decorators (advanced) section — leave at default.

Dark Moody Amethyst waystone color tiers:

| Tier | Text | Border | BG | Icon Size | Icon Color |
|---|---|---|---|---|---|
| T16 | — | — | — | — | — | DO NOT TOUCH — uses apex/stier theme |
| T13–T15 | `rgb(0,0,0)` | unchecked | `rgb(235,235,235)` | Medium (1) | Red/Yellow | Square |
| T8–T12 | `#8A9AAA` | `#5A6A7A` | `#0A0E12` | Medium (1) | Grey | Square |
| T4–T7 | `#6A7A8A` | `#4A5A6A` | transparent | Small (2) | Grey | Square |
| T1–T3 | `#7A7060` | `#5A5048` | transparent | — | — | — |

See `dark-moody-amethyst-MANUAL.md` "CUSTOMIZE TAB — Waystone Colors" for the full per-tier table with exact values and sounds.

---

## Workflow: Applying a Color Scheme

### Step 1 — Set colors in filter data

Use `setColor()` for styles that already have text/border lines. The `bgHex` parameter is optional — pass `null` to leave background unchanged:

```javascript
function setColor(styleId, textHex, borderHex, bgHex) {
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
  if (bgHex) {
    const line = lineList.find(l => l.ident === 'SetBackgroundColor');
    if (line) {
      const [r,g,b,a] = hexToRgba(bgHex);
      line.param[0]=r; line.param[1]=g; line.param[2]=b; line.param[3]=a;
      line.raw=`\tSetBackgroundColor ${r} ${g} ${b} ${a}`;
      line.rebuiltLine=`SetBackgroundColor ${r} ${g} ${b} ${a}`;
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

After setting filter data, iterate all styles and add changes so FilterBlade can persist them.
This version records text, border, **and background** colors:

```javascript
function recordAllColorChanges() {
  const styleToDetails = gFilterBlade.filterData.filterEntryStyles.styleToDetails;
  const cs = gFilterBlade.changeStorage;
  const mkId = (colorType) => ({identifier: colorType, mode: "normal", index: 1, version: 3, isReal: true});

  let added = 0, skipped = 0;

  for (const [styleId, style] of Object.entries(styleToDetails)) {
    const lineList = style.styleContentFilterEntry?.lineList;
    if (!lineList) continue;

    const textLine   = lineList.find(l => l.ident === 'SetTextColor');
    const borderLine = lineList.find(l => l.ident === 'SetBorderColor');
    const bgLine     = lineList.find(l => l.ident === 'SetBackgroundColor');

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

    if (bgLine && bgLine.param[3] > 0) {  // skip transparent (alpha = 0)
      const [r,g,b] = bgLine.param;
      const res = cs.addChange("dynamic", {
        styleId,
        identifier: mkId('SetBackgroundColor'),
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

### Step 3 — Apply per-rule changes (sounds, icons, beams)

Per-rule changes target individual filter entries by `itemTag`. See `dark-moody-amethyst-colors-2.md` Sections 6, 8, 9 for the full Dark Moody Amethyst scripts.

```javascript
// Sound (editFilterEntry + itemTag)
function setSound(itemTag, filename, volume = 300) {
  const cs = gFilterBlade.changeStorage;
  cs.addChange('dynamic', {
    identifier: { identifier: 'PlayAlertSound', mode: 'normal', index: 1, version: 3, isReal: true },
    newValue: ['CustomAlertSound', [filename, volume]],
    logicName: 'editFilterEntry',
    version: 1,
    itemTag
  }, true);
}

// Map icon (editFilterEntry + itemTag)
function setIcon(itemTag, size, color, shape) {
  const cs = gFilterBlade.changeStorage;
  cs.addChange('dynamic', {
    identifier: { identifier: 'MinimapIcon', mode: 'normal', index: 1, version: 3, isReal: true },
    newValue: [size, color, shape],
    logicName: 'editFilterEntry',
    version: 1,
    itemTag
  }, true);
}

// Beam (editStyleCombi + styleId — NOT itemTag)
function setBeam(styleId, color) {
  const cs = gFilterBlade.changeStorage;
  cs.addChange('dynamic', {
    styleId,
    identifier: { identifier: 'PlayEffect', mode: 'normal', index: 1, version: 3, isReal: true },
    newValue: [color],  // null to disable beam
    logicName: 'editStyleCombi',
    version: 1
  }, true);
}

cs.updateLocalStorage();
```

### Step 4 — Save & Upload

Click the "Save & Upload once" button (or "Save as new"):

```javascript
document.getElementById('dlScreen_SyncContent').click();
// A browser confirm() dialog appears — accept it
```

**Known issue**: The FilterBlade profile save to AWS (profileSaveStates API) returns 401 if the session token has expired. This only affects the FilterBlade save-state; the PoE filter upload still succeeds. Fix: log out and back in to refresh the OAuth token, then save again.

---

## Save File Fix Script

FilterBlade stores "off" states (disabled beams, transparent backgrounds, no sound) as `null` or `false` internally. When you download and re-upload a save file, these values crash FilterBlade on load with `TypeError: Cannot read properties of undefined`.

**Run `fix_savefile.py` on every downloaded save file before loading it back into FilterBlade.**

```bash
python3 fix_savefile.py YourFilter.filterBladeSaveFile
# Creates YourFilter_fixed.filterBladeSaveFile automatically

python3 fix_savefile.py input.filterBladeSaveFile output.filterBladeSaveFile
```

What it fixes:
- Removes `null`/`false` no-op entries for: `SetBackgroundColor`, `SetTextColor`, `SetBorderColor`, `PlayEffect`, `PlayAlertSound`, `MinimapIcon`, `UsedEntryStyleCombi`
- Converts hex color values (`#C77DFF`) to rgb format (`rgb(199, 125, 255)`) — FilterBlade accepts hex in the live editor but its save/load parser requires rgb strings

---

## Dark Moody Amethyst Color Palette

Theme files: `dark-moody-amethyst-colors.md` (style key → color map + scripts), `dark-moody-amethyst-MANUAL.md` (UI walkthrough).

| Name | Hex | Purpose |
|---|---|---|
| Amethyst | `#C77DFF` | S-tier apex, top fragments/splinters, gem labels |
| Amethyst Border | `#E0AAFF` | Border accent for Amethyst items |
| Amethyst BG | `#1A0030` | Background for apex/top items |
| Dark Gold | `#C9A84C` | Currency T1–T2, gigantic gold, top fragments |
| Dark Gold BG | `#2A1A00` | Background for top currency |
| Antique Gold | `#A08030` | Currency T3–T4, mid-high currency |
| Antique Gold BG | `#1E1200` | Background for mid-high currency |
| Faded Gold | `#7A6020` | Currency T5, wisdom scrolls, supply shards |
| Sienna | `#A0522D` | Uniques, exotics B-tier, high waystones |
| Sienna BG | `#1A0A00` | Background for uniques/high value |
| Sienna Border | `#7A3B1E` | Border for Sienna items |
| Crimson Rose | `#8B3A62` | Rare jewels, exotics C-tier, mid waystones |
| Crimson Rose BG | `#120008` | Background for mid-value items |
| Crimson Rose Border | `#6B2040` | Border for Crimson Rose items |
| Steel Blue | `#3A6BBF` | Magic jewels, exotics D-tier, lower waystones |
| Steel Blue BG | `#000A18` | Background for lower-mid items |
| Steel Blue Border | `#2A4F9A` | Border for Steel Blue items |
| Blood Red | `#C0243C` | Artifacts, corrupted exotics, xeno A |
| Blood Red BG | `#1A0008` | Background for corrupted/artifact items |
| Blood Red Border | `#8B0000` | Border for Blood Red items |
| Forest Green | `#2A8B6A` | Flasks, charms, xeno B–C, crafting bases |
| Forest Border | `#1A5A44` | Border for Forest items |
| Ash | `#7A7060` | Salvageables, filler, low-value xeno |
| Ash Border | `#5A5048` | Border for Ash items |
| Charcoal | `#3A3530` | Unremarkable drops (invisible filler) |
| Gem Purple Border | `#9B4FCC` | Border for gem labels (darker than Amethyst) |
| Lineage Pink | `#FF69B4` | Lineage gems |
| Lineage Pink Border | `#CC3380` | Border for lineage gem labels |
| Silver (Jewellery T1) | `#D0C8C0` | Jewellery T1, highlighted drops, tiered jewellery |
| Silver Border T1 | `#9A9088` | Border for Silver T1 items |
| Silver BG T1 | `#1A1814` | Background for Silver T1 items |
| Silver (Jewellery T2) | `#B8B0A8` | Jewellery T2 |
| Silver Border T2 | `#787068` | Border for Silver T2 items |
| Silver BG T2 | `#120E0C` | Background for Silver T2 items |

Full style key → color mapping: `dark-moody-amethyst-colors.md` Section 2.
Per-rule scripts (sounds, icons, beams): Sections 6, 8, 9.

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
| Save file crashes on load | null/false/hex values in save file | Run `fix_savefile.py` before loading any downloaded save file |
| Sound/icon change ignored | Used `editStyleCombi` instead of `editFilterEntry` | Per-rule changes (sounds, icons) require `logicName: 'editFilterEntry'` with `itemTag` |
| Beam change ignored | Used `editFilterEntry` instead of `editStyleCombi` | Beams require `logicName: 'editStyleCombi'` with `styleId` |
| Background color not saved | Old `recordAllColorChanges` skipped bg lines | Use the updated version above that handles `SetBackgroundColor` |

---

## Reference Data Files

| File | Contents | Use |
|---|---|---|
| `styleToDetails-dump.json` | All 93 style IDs, which color lines each has (text/border/background), default RGBA values | Know which styles exist and whether to use `setColor` vs `addColorToBackgroundTheme` |
| `strictnessCluster-dump.json` | All 537 show/hide entries grouped by category, with `tagID`, `displayName`, default show/hide state | Look up `tagID` values to pass to `set_ShowHide` / `recordAllShowHideChanges` |
| `dark-moody-amethyst-colors.md` | Full scheme: color mapping, re-apply script, sounds, icons, beams | Primary reference for re-applying the full Dark Moody Amethyst scheme |
| `dark-moody-amethyst-MANUAL.md` | Per-rule UI walkthrough: label sizes, icons, beams, sounds, Customize tab gem/waystone rules | Use when applying the scheme manually in the FilterBlade UI |
| `fix_savefile.py` | Fixes null/hex values in downloaded save files | Run before every save file reload into FilterBlade |

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
// → [199, 125, 255, 255]
```

## Exporting the Filter File

On the EXPORT tab, click "Download Filter" to save a `.filter` file. This bakes in all current in-memory colors — useful as a backup even if the FilterBlade save fails.

The exported filter is saved to:
- `~/Documents/My Games/Path of Exile 2/` (for in-game use)
- The project root as `Dark-Moody-Amethyst.filter` (backup copy)
