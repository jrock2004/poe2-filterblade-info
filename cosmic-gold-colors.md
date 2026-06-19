# Cosmic Gold — Color Scheme Reference

Base filter: NeverSink SC Semi-Strict Normal (PoE2)
Applied via: FilterBlade.xyz GFT (Global Filter Themes) → Themes tab

**Color palette:**
| Name | Hex | RGB | Purpose |
|---|---|---|---|
| Cosmic Blue | `#B8F0FF` | rgb(184, 240, 255) | S-tier, top fragments/splinters, special maps |
| White | `#FFFFFF` | rgb(255, 255, 255) | Border accent for Cosmic Blue items |
| Gold | `#FFD700` | rgb(255, 215, 0) | Currency, quest, top-tier fragments |
| Orange | `#FF9A00` | rgb(255, 154, 0) | Uniques, exotics b-tier, maps high, xeno b |
| Magenta | `#FF4DFF` | rgb(255, 77, 255) | Rare jewels, exotics c-tier, maps regularhigh |
| Cyan | `#00E6FF` | rgb(0, 230, 255) | Magic jewels, exotics d-tier, gems 2, maps mid |
| Red | `#FF4040` | rgb(255, 64, 64) | Artifacts, corrupted exotics, xeno a |
| Silver | `#E6E6E6` | rgb(230, 230, 230) | Low-value / filler items text |
| Charcoal | `#6B6B6B` | rgb(107, 107, 107) | Low-value / filler items border |

---

## Style Key → Color Mapping

Each row: `styleId` (FilterBlade key) | Text color | Border color

### apex

| Style Key | Text | Border | Notes |
|---|---|---|---|
| `apex_stier` | `#B8F0FF` | `#FFFFFF` | Best-in-slot / S-tier items |

### currency

| Style Key | Text | Border | Notes |
|---|---|---|---|
| `currency_a` | `#FFD700` | `#FFD700` | Top currency (Divine, Mirror, etc.) |
| `currency_b` | `#FFD700` | `#FFD700` | High currency |
| `currency_c` | `#FFD700` | `#FFD700` | Mid currency |
| `currency_d` | `#FFD700` | `#FFD700` | Common currency |
| `currency_e` | `#FFD700` | `#FFD700` | Low currency |

### uniques

| Style Key | Text | Border | Notes |
|---|---|---|---|
| `uniques_a` | `#FF9A00` | `#FF9A00` | Top uniques |
| `uniques_b` | `#FF9A00` | `#FF9A00` | Good uniques |
| `uniques_c` | `#FF9A00` | `#FF9A00` | Common uniques |
| `uniques_exceptional` | `#FF9A00` | `#FF9A00` | Exceptional uniques |
| `uniques_x` | `#FF9A00` | `#FF9A00` | Special uniques |
| `uniques_xbossdrop` | `#FF9A00` | `#FF9A00` | Boss-drop uniques |

### exotics

| Style Key | Text | Border | Notes |
|---|---|---|---|
| `exotics_artifact` | `#FF4040` | `#FF4040` | Artifact items |
| `exotics_artifacthigh` | `#FF4040` | `#FF4040` | High-tier artifacts |
| `exotics_btier` | `#FF9A00` | `#FF9A00` | B-tier exotics |
| `exotics_ctier` | `#FF4DFF` | `#FF4DFF` | C-tier exotics |
| `exotics_identifiedmod` | `#FF4DFF` | `#FF4DFF` | Identified mod exotics |
| `exotics_dtier` | `#00E6FF` | `#00E6FF` | D-tier exotics |
| `exotics_corrupt` | `#FF4040` | `#FF4040` | Corrupted exotics |
| `exotics_corrupthigh` | `#FF4040` | `#FF4040` | High-tier corrupted exotics |

### fragments

| Style Key | Text | Border | Notes |
|---|---|---|---|
| `fragments_a` | `#B8F0FF` | `#FFFFFF` | Top fragments |
| `fragments_b` | `#FFD700` | `#FFD700` | High fragments |
| `fragments_c` | `#FFD700` | `#FFD700` | Mid fragments |
| `fragments_d` | `#FF4DFF` | `#FF4DFF` | Low fragments |
| `fragments_e` | `#00E6FF` | `#00E6FF` | Common fragments |
| `fragments_splinter1` | `#B8F0FF` | `#FFFFFF` | Top splinters |
| `fragments_splinter2` | `#FFD700` | `#FFD700` | High splinters |
| `fragments_splinter3` | `#FFD700` | `#FFD700` | Mid splinters |
| `fragments_splinter4` | `#FF4DFF` | `#FF4DFF` | Low splinters |
| `fragments_splinter5` | `#00E6FF` | `#00E6FF` | Common splinters |

### typebased (gems & quest)

| Style Key | Text | Border | Notes |
|---|---|---|---|
| `typebased_gems1` | `#FFFFFF` | `#FFFFFF` | Top gems |
| `typebased_gems2` | `#00E6FF` | `#00E6FF` | Good gems |
| `typebased_gems3` | `#FF4DFF` | `#FF4DFF` | Common gems |
| `typebased_quest` | `#FFD700` | — | Quest items |

### gear (jewels & jewellery)

| Style Key | Text | Border | Notes |
|---|---|---|---|
| `gear_jewelmagic` | `#00E6FF` | `#00E6FF` | Magic jewels |
| `gear_jewelmagiclow` | `#00E6FF` | `#00E6FF` | Low-tier magic jewels |
| `gear_jewelrare` | `#FF4DFF` | `#FF4DFF` | Rare jewels |

### gold (currency piles)

| Style Key | Text | Border | Notes |
|---|---|---|---|
| `gold_pilehuge` | `#FFD700` | `#FFD700` | Huge gold pile |
| `gold_pilelarge` | `#FFD700` | `#FFD700` | Large gold pile |
| `gold_pilemedium` | `#E6E6E6` | `#6B6B6B` | Medium gold pile |
| `gold_pilesmall` | `#E6E6E6` | `#6B6B6B` | Small gold pile |

### maps

| Style Key | Text | Border | Notes |
|---|---|---|---|
| `maps_regularhighest` | `#FF9A00` | `#FF9A00` | Highest tier maps |
| `maps_regularhigh` | `#FF4DFF` | `#FF4DFF` | High tier maps |
| `maps_regularmid` | `#00E6FF` | `#00E6FF` | Mid tier maps |
| `maps_regularlow` | `#E6E6E6` | `#E6E6E6` | Low tier maps |
| `maps_specialb` | `#B8F0FF` | `#FFFFFF` | Special maps B-tier |
| `maps_specialc` | `#FFD700` | `#FFD700` | Special maps C-tier |

### xeno

| Style Key | Text | Border | Notes |
|---|---|---|---|
| `xeno_a` | `#FF4040` | `#FF4040` | Xeno tier A |
| `xeno_b` | `#FF9A00` | `#FF9A00` | Xeno tier B |
| `xeno_c` | `#FF4DFF` | `#FF4DFF` | Xeno tier C |
| `xeno_d` | `#00E6FF` | `#00E6FF` | Xeno tier D |
| `xeno_e` | `#E6E6E6` | `#6B6B6B` | Xeno tier E (filler) |

### utility

| Style Key | Text | Border | Notes |
|---|---|---|---|
| `utility_unknownitem` | `#00E6FF` | `#00E6FF` | Unknown/unrecognized items |

### gear — background-only styles (text/border added)

These styles originally only had `SetBackgroundColor`. Text and border lines were added via `addColorToBackgroundTheme()`.

| Style Key | Text | Border | Notes |
|---|---|---|---|
| `gear_weakrare1` | `#E6E6E6` | `#6B6B6B` | Weak rare gear tier 1 |
| `gear_weakrare2` | `#FF4DFF` | `#FF4DFF` | Weak rare gear tier 2 |
| `gear_highlightedsize` | `#FF4DFF` | `#FF4DFF` | Highlighted size gear |
| `gear_jewellery2` | `#FF4DFF` | `#FF4DFF` | Jewellery tier 2 |
| `gear_highlightdrop2` | `#00E6FF` | `#00E6FF` | Highlight drop tier 2 |
| `gear_highlightdrop3` | `#FF9A00` | `#FF9A00` | Highlight drop tier 3 |
| `gear_jewellery1` | `#FF9A00` | `#FF9A00` | Jewellery tier 1 |

---

## Applying This Scheme in a New Session

If FilterBlade was reloaded and all in-memory changes were lost, re-apply the full scheme programmatically. See `CLAUDE.md` for the `setColor()` and `addColorToBackgroundTheme()` helper functions.

Quick re-apply script (paste in browser console on filterblade.xyz):

```javascript
// 1. setColor: styles that already have text/border lines
const colors = [
  // [styleId, textHex, borderHex]
  ['apex_stier', '#B8F0FF', '#FFFFFF'],
  ['currency_a', '#FFD700', '#FFD700'],
  ['currency_b', '#FFD700', '#FFD700'],
  ['currency_c', '#FFD700', '#FFD700'],
  ['currency_d', '#FFD700', '#FFD700'],
  ['currency_e', '#FFD700', '#FFD700'],
  ['uniques_a', '#FF9A00', '#FF9A00'],
  ['uniques_b', '#FF9A00', '#FF9A00'],
  ['uniques_c', '#FF9A00', '#FF9A00'],
  ['uniques_exceptional', '#FF9A00', '#FF9A00'],
  ['uniques_x', '#FF9A00', '#FF9A00'],
  ['uniques_xbossdrop', '#FF9A00', '#FF9A00'],
  ['exotics_artifact', '#FF4040', '#FF4040'],
  ['exotics_artifacthigh', '#FF4040', '#FF4040'],
  ['exotics_btier', '#FF9A00', '#FF9A00'],
  ['exotics_ctier', '#FF4DFF', '#FF4DFF'],
  ['exotics_identifiedmod', '#FF4DFF', '#FF4DFF'],
  ['exotics_dtier', '#00E6FF', '#00E6FF'],
  ['exotics_corrupt', '#FF4040', '#FF4040'],
  ['exotics_corrupthigh', '#FF4040', '#FF4040'],
  ['fragments_a', '#B8F0FF', '#FFFFFF'],
  ['fragments_b', '#FFD700', '#FFD700'],
  ['fragments_c', '#FFD700', '#FFD700'],
  ['fragments_d', '#FF4DFF', '#FF4DFF'],
  ['fragments_e', '#00E6FF', '#00E6FF'],
  ['fragments_splinter1', '#B8F0FF', '#FFFFFF'],
  ['fragments_splinter2', '#FFD700', '#FFD700'],
  ['fragments_splinter3', '#FFD700', '#FFD700'],
  ['fragments_splinter4', '#FF4DFF', '#FF4DFF'],
  ['fragments_splinter5', '#00E6FF', '#00E6FF'],
  ['typebased_gems1', '#FFFFFF', '#FFFFFF'],
  ['typebased_gems2', '#00E6FF', '#00E6FF'],
  ['typebased_gems3', '#FF4DFF', '#FF4DFF'],
  ['typebased_quest', '#FFD700', null],
  ['gear_jewelmagic', '#00E6FF', '#00E6FF'],
  ['gear_jewelmagiclow', '#00E6FF', '#00E6FF'],
  ['gear_jewelrare', '#FF4DFF', '#FF4DFF'],
  ['gold_pilehuge', '#FFD700', '#FFD700'],
  ['gold_pilelarge', '#FFD700', '#FFD700'],
  ['gold_pilemedium', '#E6E6E6', '#6B6B6B'],
  ['gold_pilesmall', '#E6E6E6', '#6B6B6B'],
  ['maps_regularhighest', '#FF9A00', '#FF9A00'],
  ['maps_regularhigh', '#FF4DFF', '#FF4DFF'],
  ['maps_regularmid', '#00E6FF', '#00E6FF'],
  ['maps_regularlow', '#E6E6E6', '#E6E6E6'],
  ['maps_specialb', '#B8F0FF', '#FFFFFF'],
  ['maps_specialc', '#FFD700', '#FFD700'],
  ['xeno_a', '#FF4040', '#FF4040'],
  ['xeno_b', '#FF9A00', '#FF9A00'],
  ['xeno_c', '#FF4DFF', '#FF4DFF'],
  ['xeno_d', '#00E6FF', '#00E6FF'],
  ['xeno_e', '#E6E6E6', '#6B6B6B'],
  ['utility_unknownitem', '#00E6FF', '#00E6FF'],
];

// 2. addColorToBackgroundTheme: styles that only had background
const bgOnlyColors = [
  ['gear_weakrare1', '#E6E6E6', '#6B6B6B'],
  ['gear_weakrare2', '#FF4DFF', '#FF4DFF'],
  ['gear_highlightedsize', '#FF4DFF', '#FF4DFF'],
  ['gear_jewellery2', '#FF4DFF', '#FF4DFF'],
  ['gear_highlightdrop2', '#00E6FF', '#00E6FF'],
  ['gear_highlightdrop3', '#FF9A00', '#FF9A00'],
  ['gear_jewellery1', '#FF9A00', '#FF9A00'],
];
```

---

## Version History

| Date | Changes | Notes |
|---|---|---|
| 2026-06-18 | Initial Cosmic Gold scheme applied | 144 changes recorded, PoE filter uploaded successfully |
