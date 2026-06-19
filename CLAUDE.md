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
gFilterBlade.filterData.filterEntryStyles.styleToDetails  // map: styleId → FilterEntryStyle
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
