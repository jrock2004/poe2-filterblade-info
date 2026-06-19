# Dark Moody Amethyst — Color Scheme Reference

Base filter: NeverSink SC Semi-Strict Normal (PoE2)
Applied via: FilterBlade.xyz GFT (Global Filter Themes) → Themes tab
Gem icon overrides: Applied via individual rule changes (see Section 3)

---

## Section 1 — Color Palette

| Name | Hex | RGB | Purpose |
|---|---|---|---|
| Amethyst | `#C77DFF` | rgb(199, 125, 255) | S-tier apex, top fragments/splinters |
| Amethyst Border | `#E0AAFF` | rgb(224, 170, 255) | Border accent for Amethyst items |
| Amethyst BG | `#1A0030` | rgb(26, 0, 48) | Background for apex/top fragment items |
| Dark Gold | `#C9A84C` | rgb(201, 168, 76) | Currency T1–T2, huge gold, top fragments |
| Dark Gold BG | `#2A1A00` | rgb(42, 26, 0) | Background for top currency items |
| Antique Gold | `#A08030` | rgb(160, 128, 48) | Currency T3–T4, large gold, artifact currency |
| Antique Gold BG | `#1E1200` | rgb(30, 18, 0) | Background for mid-high currency |
| Faded Gold | `#7A6020` | rgb(122, 96, 32) | Currency T5–T6, wisdom scrolls, supply shards |
| Sienna | `#A0522D` | rgb(160, 82, 45) | Uniques, exotics B-tier, high waystones, jewellery T1 |
| Sienna BG | `#1A0A00` | rgb(26, 10, 0) | Background for uniques / high value |
| Sienna Border | `#7A3B1E` | rgb(122, 59, 30) | Border for Sienna items |
| Crimson Rose | `#8B3A62` | rgb(139, 58, 98) | Rare jewels, exotics C-tier, mid waystones |
| Crimson Rose BG | `#120008` | rgb(18, 0, 8) | Background for mid-value items |
| Crimson Rose Border | `#6B2040` | rgb(107, 32, 64) | Border for Crimson Rose items |
| Steel Blue | `#3A6BBF` | rgb(58, 107, 191) | Magic jewels, exotics D-tier, mid waystones, support gems |
| Steel Blue BG | `#000A18` | rgb(0, 10, 24) | Background for lower-mid items |
| Steel Blue Border | `#2A4F9A` | rgb(42, 79, 154) | Border for Steel Blue items |
| Blood Red | `#C0243C` | rgb(192, 36, 60) | Artifacts, corrupted exotics, xeno A |
| Blood Red BG | `#1A0008` | rgb(26, 0, 8) | Background for corrupted/artifact items |
| Blood Red Border | `#8B0000` | rgb(139, 0, 0) | Border for Blood Red items |
| Forest Green | `#2A8B6A` | rgb(42, 139, 106) | Flasks, charms, xeno B–C, crafting bases |
| Forest Border | `#1A5A44` | rgb(26, 90, 68) | Border for Forest items |
| Ash | `#7A7060` | rgb(122, 112, 96) | Salvageables, ilvl 82 bases, xeno D–E, filler |
| Ash Border | `#5A5048` | rgb(90, 80, 72) | Border for Ash items |
| Charcoal | `#3A3530` | rgb(58, 53, 48) | Unremarkable drops, invisible filler |
| Charcoal Border | `#252220` | rgb(37, 34, 32) | Border for Charcoal items |
| Gem Purple | `#C77DFF` | rgb(199, 125, 255) | All gem types (skill, spirit, support) |
| Gem Purple BG | `#0E0018` | rgb(14, 0, 24) | Background for high-tier gems |
| Gem Purple Border | `#9B4FCC` | rgb(155, 79, 204) | Border for gem labels |
| Lineage Pink | `#FF69B4` | rgb(255, 105, 180) | Lineage gems |
| Lineage Pink BG | `#180010` | rgb(24, 0, 16) | Background for lineage gems |
| Lineage Pink Border | `#CC3380` | rgb(204, 51, 128) | Border for lineage gem labels |
| Cut Gem Grey | `#AAAAAA` | rgb(170, 170, 170) | Twice-corrupted cut gems |
| Cut Gem Border | `#666666` | rgb(102, 102, 102) | Border for cut gem labels |

---

## Section 2 — Style Key → Color Mapping

Format: `styleId` | Text | Border | Background | Notes

`transparent` = no background (FilterBlade: BG checkbox unchecked)

### apex

| Style Key | Text | Border | Background | Notes |
|---|---|---|---|---|
| `apex_stier` | `#C77DFF` | `#E0AAFF` | `#1A0030` | S-tier best-in-slot |

### currency

| Style Key | Text | Border | Background | Notes |
|---|---|---|---|---|
| `currency_a` | `#C9A84C` | `#8B6914` | `#2A1A00` | Top currency (Divine, Mirror) |
| `currency_b` | `#C9A84C` | `#8B6914` | `#2A1A00` | High currency (Exalted) |
| `currency_c` | `#A08030` | `#6B5010` | `#1E1200` | Mid-high currency (Annulment) |
| `currency_d` | `#A08030` | `#6B5010` | `#1E1200` | Mid currency (Chaos) |
| `currency_e` | `#7A6020` | `#4A3A10` | transparent | Low currency (Transmutation) |
| `currency_supply2` | `#7A6020` | `#4A3A10` | transparent | Wisdom Scrolls, higher shards |
| `currency_supply4` | `#7A6020` | `#4A3A10` | transparent | Splinter shards, low supply |
| `currency_specialartifact` | `#A08030` | `#6B5010` | `#1E1200` | Artifact-type currency |

### gold

| Style Key | Text | Border | Background | Notes |
|---|---|---|---|---|
| `gold_pilehuge` | `#C9A84C` | `#8B6914` | `#2A1A00` | Gigantic gold pile |
| `gold_pilelarge` | `#C9A84C` | `#8B6914` | `#1E1200` | Large gold pile |
| `gold_pilemedium` | `#A08030` | `#6B5010` | transparent | Medium gold pile |
| `gold_pilesmall` | `#7A7060` | `#5A5048` | transparent | Small gold pile |

### uniques

| Style Key | Text | Border | Background | Notes |
|---|---|---|---|---|
| `uniques_a` | `#A0522D` | `#7A3B1E` | `#1A0A00` | Top uniques |
| `uniques_exceptional` | `#A0522D` | `#7A3B1E` | `#1A0A00` | Exceptional (over-socketed/quality) |
| `uniques_x` | `#A0522D` | `#7A3B1E` | `#1A0A00` | Special uniques |
| `uniques_xbossdrop` | `#A0522D` | `#7A3B1E` | `#1A0A00` | Boss-drop uniques |
| `uniques_b` | `#A0522D` | `#7A3B1E` | `#120800` | Good uniques |
| `uniques_c` | `#A0522D` | `#7A3B1E` | transparent | Common uniques |

### exotics

| Style Key | Text | Border | Background | Notes |
|---|---|---|---|---|
| `exotics_btier` | `#A0522D` | `#7A3B1E` | `#1A0A00` | B-tier exotics |
| `exotics_ctier` | `#8B3A62` | `#6B2040` | `#120008` | C-tier exotics |
| `exotics_identifiedmod` | `#8B3A62` | `#6B2040` | `#120008` | Identified mod exotics |
| `exotics_dtier` | `#3A6BBF` | `#2A4F9A` | `#000A18` | D-tier exotics |
| `exotics_artifact` | `#C0243C` | `#8B0000` | `#1A0008` | Artifact items |
| `exotics_artifacthigh` | `#C0243C` | `#8B0000` | `#1A0008` | High-tier artifacts |
| `exotics_corrupt` | `#C0243C` | `#8B0000` | `#1A0008` | Corrupted exotics |
| `exotics_corrupthigh` | `#C0243C` | `#8B0000` | `#1A0008` | High-tier corrupted exotics |

### fragments

| Style Key | Text | Border | Background | Notes |
|---|---|---|---|---|
| `fragments_a` | `#C77DFF` | `#E0AAFF` | `#1A0030` | Top fragments |
| `fragments_splinter1` | `#C77DFF` | `#E0AAFF` | `#1A0030` | Top splinters |
| `fragments_splinter2` | `#C77DFF` | `#E0AAFF` | `#1A0030` | High splinters |
| `fragments_b` | `#C9A84C` | `#8B6914` | `#2A1A00` | High fragments |
| `fragments_splinter3` | `#C9A84C` | `#8B6914` | `#2A1A00` | Mid splinters |
| `fragments_c` | `#C9A84C` | `#8B6914` | `#1E1200` | Mid fragments |
| `fragments_splinter4` | `#8B3A62` | `#6B2040` | `#120008` | Low splinters |
| `fragments_d` | `#8B3A62` | `#6B2040` | `#120008` | Low fragments |
| `fragments_splinter5` | `#7A7060` | `#5A5048` | transparent | Common splinters |
| `fragments_e` | `#7A7060` | `#5A5048` | transparent | Common fragments |
| `fragments_fragdmuted` | `#7A7060` | `#5A5048` | transparent | Muted fragments |

### maps (waystones)

| Style Key | Text | Border | Background | Notes |
|---|---|---|---|---|
| `maps_specialb` | `#C77DFF` | `#E0AAFF` | `#1A0030` | Pinnacle keys, special maps B |
| `maps_specialc` | `#C9A84C` | `#8B6914` | `#2A1A00` | Special maps C |
| `maps_regularhighest` | `#A0522D` | `#7A3B1E` | `#1A1000` | Waystones T13–T16 |
| `maps_regularhigh` | `#8B3A62` | `#6B2040` | `#0E0008` | Waystones T8–T12 |
| `maps_regularmid` | `#3A6BBF` | `#2A4F9A` | `#000A18` | Waystones T4–T7 |
| `maps_regularlow` | `#7A7060` | `#5A5048` | transparent | Waystones T1–T3 |

### maps — decorator/overlay styles

`maps_deco1`, `maps_deco2`, `maps_deco3`, `maps_deco4`, `maps_decotierupgrade`, `maps_decooverlevel` — border overlays only. Leave at default to avoid conflicts with base label color.

### typebased

| Style Key | Text | Border | Background | Notes |
|---|---|---|---|---|
| `typebased_quest` | `#C9A84C` | `#8B6914` | `#2A1A00` | Quest items |
| `typebased_gems1` | `#C77DFF` | `#9B4FCC` | `#0E0018` | Gems tier 1 (style fallback — see Section 3) |
| `typebased_gems2` | `#8B3A62` | `#6B2040` | `#120008` | Gems tier 2 (style fallback) |
| `typebased_gems3` | `#3A6BBF` | `#2A4F9A` | transparent | Gems tier 3 (style fallback) |
| `typebased_flaskcharms` | `#2A8B6A` | `#1A5A44` | transparent | Flasks and charms |
| `typebased_flaskcharms1high` | `#2A8B6A` | `#1A5A44` | transparent | High quality flasks/charms |

### gear

| Style Key | Text | Border | Background | Notes |
|---|---|---|---|---|
| `gear_jewelrare` | `#8B3A62` | `#6B2040` | `#120008` | Rare jewels |
| `gear_jewelmagic` | `#3A6BBF` | `#2A4F9A` | `#000A18` | Magic jewels |
| `gear_jewelmagiclow` | `#3A6BBF` | `#2A4F9A` | transparent | Low magic jewels |
| `gear_jewellery1` | `#A0522D` | `#7A3B1E` | `#1A0A00` | Jewellery T1 |
| `gear_jewellery2` | `#8B3A62` | `#6B2040` | `#120008` | Jewellery T2 |
| `gear_tieredjewellery` | `#A0522D` | `#7A3B1E` | `#1A0A00` | Tiered jewellery |
| `gear_decojewellery` | `#A0522D` | `#7A3B1E` | transparent | Deco jewellery border only |
| `gear_highlightdrop2` | `#8B3A62` | `#6B2040` | `#120008` | Highlight drop tier 2 |
| `gear_highlightdrop3` | `#A0522D` | `#7A3B1E` | `#1A0A00` | Highlight drop tier 3 |
| `gear_highlightedsize` | `#A0522D` | `#7A3B1E` | transparent | Highlighted size gear |
| `gear_weakrare1` | `#7A7060` | `#5A5048` | transparent | Weak rare gear T1 |
| `gear_weakrare2` | `#7A7060` | `#5A5048` | transparent | Weak rare gear T2 |
| `gear_weakrareleveling1` | `#7A7060` | `#5A5048` | transparent | Weak rare leveling gear |
| `gear_vendor` | `#3A3530` | `#252220` | transparent | Vendor gear |
| `gear_unstyled` | — | — | — | No style change |

### xeno

| Style Key | Text | Border | Background | Notes |
|---|---|---|---|---|
| `xeno_a` | `#C0243C` | `#8B0000` | `#1A0008` | Xeno A-tier |
| `xeno_b` | `#2A8B6A` | `#1A5A44` | transparent | Xeno B-tier |
| `xeno_c` | `#2A8B6A` | `#1A5A44` | transparent | Xeno C-tier |
| `xeno_d` | `#7A7060` | `#5A5048` | transparent | Xeno D-tier |
| `xeno_e` | `#7A7060` | `#5A5048` | transparent | Xeno E-tier |

### itemproperty

| Style Key | Text | Border | Background | Notes |
|---|---|---|---|---|
| `itemproperty_achancing` | `#A0522D` | `#7A3B1E` | `#1A0A00` | Chancing bases S-tier |
| `itemproperty_bchancing` | `#2A8B6A` | `#1A5A44` | transparent | Chancing bases A-tier |
| `itemproperty_aecocraft` | `#A0522D` | `#7A3B1E` | `#1A0A00` | Eco-craft bases high |
| `itemproperty_becocraft` | `#2A8B6A` | `#1A5A44` | transparent | Eco-craft bases low |
| `itemproperty_salvage1` | `#7A7060` | `#5A5048` | transparent | Salvageable quality T1 |
| `itemproperty_salvage2` | `#7A7060` | `#5A5048` | transparent | Salvageable socket T2 |
| `itemproperty_salvagelvl1` | `#7A7060` | `#5A5048` | transparent | Salvageable leveling |
| `itemproperty_level82` | `#7A7060` | `#5A5048` | transparent | ilvl 82 bases |
| `itemproperty_toplevelbased1` | `#7A7060` | `#5A5048` | transparent | Top level bases |

### utility

| Style Key | Text | Border | Background | Notes |
|---|---|---|---|---|
| `utility_unknownitem` | `#3A6BBF` | `#2A4F9A` | `#000A18` | Unknown/unrecognized items |
| `utility_unremarkabledrop` | `#3A3530` | `#252220` | transparent | Invisible filler |
| `utility_minimize` | — | — | transparent | Do not change |
| `utility_basicraredecorator` | — | — | — | Border overlay — do not change |
| `utility_decoremovermagic` | — | — | — | Decorator remover — do not change |
| `utility_decoremovernormal` | — | — | — | Decorator remover — do not change |
| `utility_highlight3` | — | — | — | No color assigned |
| `utility_highlight4` | — | — | — | No color assigned |

---

## Section 3 — Gem Icon Overrides (Per-Rule)

These cannot be set via the GFT style key system. They require individual rule changes targeting specific `itemTag` entries. The change object format is:

```json
{
  "identifier": {
    "identifier": "MinimapIcon",
    "mode": "normal",
    "index": 1,
    "version": 3,
    "isReal": true
  },
  "newValue": ["<size>", "<color>", "<shape>"]
}
```

Where size is `"0"` (large), `"1"` (medium), `"2"` (small).

### Skill gems — Diamond · Purple

| itemTag | Display name | Size | Color | Shape |
|---|---|---|---|---|
| `gems->uncut;skill20` | Skill Gem Level 20 | `0` | `Purple` | `Diamond` |
| `gems->uncut;skill19` | Skill Gem Level 19 | `1` | `Purple` | `Diamond` |
| `gems->uncut;skillgemprogression18` | Skill Gem Level 18 | `1` | `Purple` | `Diamond` |
| `gems->uncut;skillgemprogression17` | Skill Gem Level 17 | `2` | `Purple` | `Diamond` |
| `gems->uncut;skillgemprogression16` | Skill Gem Level 16 | `2` | `Purple` | `Diamond` |
| `gems->uncut;skillgemprogression15` | Skill Gem Level 15 | `2` | `Purple` | `Diamond` |
| `gems->uncut;skillgemprogression14` | Skill Gem Level 14 | `2` | `Purple` | `Diamond` |
| `gems->uncut;otherskilleg` | Skill Gem Endgame | none | — | — |
| `gems->uncut;skillcampaign` | Skill Gem Campaign | none | — | — |

### Spirit gems — Kite · Purple

| itemTag | Display name | Size | Color | Shape |
|---|---|---|---|---|
| `gems->uncut;spirit20` | Spirit Gem Level 20 | `0` | `Purple` | `Kite` |
| `gems->uncut;spirit19` | Spirit Gem Level 19 | `1` | `Purple` | `Kite` |
| `gems->uncut;spiritgemprogression18` | Spirit Gem Level 18 | `1` | `Purple` | `Kite` |
| `gems->uncut;spiritgemprogression17` | Spirit Gem Level 17 | `2` | `Purple` | `Kite` |
| `gems->uncut;spiritgemprogression16` | Spirit Gem Level 16 | `2` | `Purple` | `Kite` |
| `gems->uncut;spiritgemprogression15` | Spirit Gem Level 15 | `2` | `Purple` | `Kite` |
| `gems->uncut;spiritgemprogression14` | Spirit Gem Level 14 | `2` | `Purple` | `Kite` |
| `gems->uncut;otherspiriteg` | Spirit Gem Endgame | none | — | — |
| `gems->uncut;spiritcampaign` | Spirit Gem Campaign | none | — | — |

### Support gems — Cross · Purple

| itemTag | Display name | Size | Color | Shape |
|---|---|---|---|---|
| `gems->uncut;supportearlymaps` | Support Gem Endgame Early | `1` | `Purple` | `Cross` |
| `gems->uncut;othersupporteg` | Support Gem Endgame | `2` | `Purple` | `Cross` |
| `gems->uncut;supportcampaign` | Support Gem Campaign | none | — | — |

### Lineage gems — Diamond · Pink

| itemTag | Display name | Size | Color | Shape |
|---|---|---|---|---|
| `gems->lineage;s` | Lineage Gem S-tier | `0` | `Pink` | `Diamond` |
| `gems->lineage;a` | Lineage Gem A-tier | `1` | `Pink` | `Diamond` |
| `gems->lineage;b` | Lineage Gem B-tier | `2` | `Pink` | `Diamond` |
| `gems->lineage;c` | Lineage Gem C-tier | none | — | — |

### Cut gems (corrupted) — Diamond · Grey

| itemTag | Display name | Size | Color | Shape |
|---|---|---|---|---|
| `gems;upgradedgemstwice` | Twice Corrupted Gem 21/23 | `2` | `Grey` | `Diamond` |
| `gems;upgradedgemslevel` | Twice Corrupted Gem | `2` | `Grey` | `Diamond` |
| `gems;any` | Cut Gem (any) | none | — | — |

---

## Section 4 — Map Icon Assignments

| Category | Shape | Color | Large | Medium | Small |
|---|---|---|---|---|---|
| S-tier / apex | Star | Purple | apex_stier, fragments_a, splinter1/2 | maps_specialb | — |
| Currency T1–T2 | Circle | Yellow | currency_a, gold_pilehuge, fragments_a | currency_b/c/d, fragments_b/c | — |
| Currency T5–T6 | — | — | — | — | no icon |
| Uniques | Star | Orange | uniques_a | uniques_x/xbossdrop/exceptional | uniques_b |
| Exotics | Diamond | Orange/Pink/Cyan | — | exotics_btier(O) / ctier(P) / dtier(C) | — |
| Waystones | Square | Orange/Pink/Cyan | — | maps_regularhighest(O) / high(P) / mid(C) | — |
| Jewellery | Square | Orange/Pink | gear_jewellery1 | gear_jewellery2 | — |
| Rare jewels | Star | Pink | gear_jewelrare | — | — |
| Magic jewels | Circle | Cyan | gear_jewelmagic | — | gear_jewelmagiclow |
| Artifacts/corrupted | Circle | Red | — | exotics_artifacthigh / corrupt | — |
| Xeno A | Circle | Red | xeno_a | — | — |
| Xeno B–C | Circle | Green | — | xeno_b | xeno_c |
| Crafting bases | Diamond | White | itemproperty_aecocraft | itemproperty_becocraft | — |
| Chancing bases | Diamond | White | itemproperty_achancing | — | — |

---

## Section 5 — Re-apply Script

Paste in browser console on filterblade.xyz to reapply all GFT color changes.

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
    } else {
      // transparent — disable background if line exists
      const bgLine = lineList.find(l => l.ident === 'SetBackgroundColor');
      if (bgLine) { bgLine.param[3] = 0; bgLine.isEverModified = true; }
    }
  }
  style.updateAllConnectedEntries();
  return `OK: ${styleId}`;
}

// [styleId, textHex, borderHex, bgHex or null for transparent]
const colors = [
  ['apex_stier',               '#C77DFF', '#E0AAFF', '#1A0030'],
  ['currency_a',               '#C9A84C', '#8B6914', '#2A1A00'],
  ['currency_b',               '#C9A84C', '#8B6914', '#2A1A00'],
  ['currency_c',               '#A08030', '#6B5010', '#1E1200'],
  ['currency_d',               '#A08030', '#6B5010', '#1E1200'],
  ['currency_e',               '#7A6020', '#4A3A10', null],
  ['currency_supply2',         '#7A6020', '#4A3A10', null],
  ['currency_supply4',         '#7A6020', '#4A3A10', null],
  ['currency_specialartifact', '#A08030', '#6B5010', '#1E1200'],
  ['gold_pilehuge',            '#C9A84C', '#8B6914', '#2A1A00'],
  ['gold_pilelarge',           '#C9A84C', '#8B6914', '#1E1200'],
  ['gold_pilemedium',          '#A08030', '#6B5010', null],
  ['gold_pilesmall',           '#7A7060', '#5A5048', null],
  ['uniques_a',                '#A0522D', '#7A3B1E', '#1A0A00'],
  ['uniques_exceptional',      '#A0522D', '#7A3B1E', '#1A0A00'],
  ['uniques_x',                '#A0522D', '#7A3B1E', '#1A0A00'],
  ['uniques_xbossdrop',        '#A0522D', '#7A3B1E', '#1A0A00'],
  ['uniques_b',                '#A0522D', '#7A3B1E', '#120800'],
  ['uniques_c',                '#A0522D', '#7A3B1E', null],
  ['exotics_btier',            '#A0522D', '#7A3B1E', '#1A0A00'],
  ['exotics_ctier',            '#8B3A62', '#6B2040', '#120008'],
  ['exotics_identifiedmod',    '#8B3A62', '#6B2040', '#120008'],
  ['exotics_dtier',            '#3A6BBF', '#2A4F9A', '#000A18'],
  ['exotics_artifact',         '#C0243C', '#8B0000', '#1A0008'],
  ['exotics_artifacthigh',     '#C0243C', '#8B0000', '#1A0008'],
  ['exotics_corrupt',          '#C0243C', '#8B0000', '#1A0008'],
  ['exotics_corrupthigh',      '#C0243C', '#8B0000', '#1A0008'],
  ['fragments_a',              '#C77DFF', '#E0AAFF', '#1A0030'],
  ['fragments_b',              '#C9A84C', '#8B6914', '#2A1A00'],
  ['fragments_c',              '#C9A84C', '#8B6914', '#1E1200'],
  ['fragments_d',              '#8B3A62', '#6B2040', '#120008'],
  ['fragments_e',              '#7A7060', '#5A5048', null],
  ['fragments_splinter1',      '#C77DFF', '#E0AAFF', '#1A0030'],
  ['fragments_splinter2',      '#C77DFF', '#E0AAFF', '#1A0030'],
  ['fragments_splinter3',      '#C9A84C', '#8B6914', '#2A1A00'],
  ['fragments_splinter4',      '#8B3A62', '#6B2040', '#120008'],
  ['fragments_splinter5',      '#7A7060', '#5A5048', null],
  ['fragments_fragdmuted',     '#7A7060', '#5A5048', null],
  ['maps_specialb',            '#C77DFF', '#E0AAFF', '#1A0030'],
  ['maps_specialc',            '#C9A84C', '#8B6914', '#2A1A00'],
  ['maps_regularhighest',      '#A0522D', '#7A3B1E', '#1A1000'],
  ['maps_regularhigh',         '#8B3A62', '#6B2040', '#0E0008'],
  ['maps_regularmid',          '#3A6BBF', '#2A4F9A', '#000A18'],
  ['maps_regularlow',          '#7A7060', '#5A5048', null],
  ['typebased_quest',          '#C9A84C', '#8B6914', '#2A1A00'],
  ['typebased_gems1',          '#C77DFF', '#9B4FCC', '#0E0018'],
  ['typebased_gems2',          '#8B3A62', '#6B2040', '#120008'],
  ['typebased_gems3',          '#3A6BBF', '#2A4F9A', null],
  ['typebased_flaskcharms',    '#2A8B6A', '#1A5A44', null],
  ['typebased_flaskcharms1high','#2A8B6A','#1A5A44', null],
  ['gear_jewelrare',           '#8B3A62', '#6B2040', '#120008'],
  ['gear_jewelmagic',          '#3A6BBF', '#2A4F9A', '#000A18'],
  ['gear_jewelmagiclow',       '#3A6BBF', '#2A4F9A', null],
  ['gear_jewellery1',          '#A0522D', '#7A3B1E', '#1A0A00'],
  ['gear_jewellery2',          '#8B3A62', '#6B2040', '#120008'],
  ['gear_tieredjewellery',     '#A0522D', '#7A3B1E', '#1A0A00'],
  ['gear_decojewellery',       '#A0522D', '#7A3B1E', null],
  ['gear_highlightdrop2',      '#8B3A62', '#6B2040', '#120008'],
  ['gear_highlightdrop3',      '#A0522D', '#7A3B1E', '#1A0A00'],
  ['gear_highlightedsize',     '#A0522D', '#7A3B1E', null],
  ['gear_weakrare1',           '#7A7060', '#5A5048', null],
  ['gear_weakrare2',           '#7A7060', '#5A5048', null],
  ['gear_weakrareleveling1',   '#7A7060', '#5A5048', null],
  ['gear_vendor',              '#3A3530', '#252220', null],
  ['xeno_a',                   '#C0243C', '#8B0000', '#1A0008'],
  ['xeno_b',                   '#2A8B6A', '#1A5A44', null],
  ['xeno_c',                   '#2A8B6A', '#1A5A44', null],
  ['xeno_d',                   '#7A7060', '#5A5048', null],
  ['xeno_e',                   '#7A7060', '#5A5048', null],
  ['itemproperty_achancing',   '#A0522D', '#7A3B1E', '#1A0A00'],
  ['itemproperty_bchancing',   '#2A8B6A', '#1A5A44', null],
  ['itemproperty_aecocraft',   '#A0522D', '#7A3B1E', '#1A0A00'],
  ['itemproperty_becocraft',   '#2A8B6A', '#1A5A44', null],
  ['itemproperty_salvage1',    '#7A7060', '#5A5048', null],
  ['itemproperty_salvage2',    '#7A7060', '#5A5048', null],
  ['itemproperty_salvagelvl1', '#7A7060', '#5A5048', null],
  ['itemproperty_level82',     '#7A7060', '#5A5048', null],
  ['itemproperty_toplevelbased1','#7A7060','#5A5048', null],
  ['utility_unknownitem',      '#3A6BBF', '#2A4F9A', '#000A18'],
  ['utility_unremarkabledrop', '#3A3530', '#252220', null],
];

colors.forEach(([id, text, border, bg]) => console.log(setColor(id, text, border, bg)));
```



---

## Section 6 — Sound Assignments

All sounds use the `PlayAlertSound` identifier with `CustomAlertSound` format:

```json
{
  "identifier": {
    "identifier": "PlayAlertSound",
    "mode": "normal",
    "index": 1,
    "version": 3,
    "isReal": true
  },
  "newValue": ["CustomAlertSound", ["filename.mp3", 300]]
}
```

Volume is `300` throughout. Sounds target individual rules by `itemTag`.

### Sound tier assignments

| Tier | Sound File | Categories |
|---|---|---|
| S-tier | `Stefan Gold_6veryvaluable.mp3` | apex_stier, fragments_a, splinter1, maps_specialb |
| Top currency | `Stefan Gold_6veryvaluable.mp3` | currency;s (T1 currency) |
| High currency | `Stefan Gold_2currency.mp3` | currency;a, currency;b |
| Uniques T1 | `Stefan Gold_1maybevaluable.mp3` | uniques;t1, uniques;sekhemaring |
| Uniques T2 | `Stefan Gold_1maybevaluable.mp3` | uniques;t2, uniques;multispecialhigh, uniques;exceptional |
| High exotics | `Stefan Gold_1maybevaluable.mp3` | exotics_btier, exotics_identifiedmod |
| High fragments | `Stefan Gold_4maps.mp3` | fragments_b, fragments_splinter2/3 |
| Waystones T13–T16 | `map1.mp3` | waystones;waystone_t13 through waystone_t16 |
| Waystones T8–T12 | `map2.mp3` | waystones;waystone_t8 through waystone_t12 |
| Waystones T4–T7 | `map3.mp3` | waystones;waystone_t4 through waystone_t7 |
| Special maps | `GhazzyTV_5highmaps.mp3` | maps_specialb, maps_specialc |
| Gems L17–L20 | `gem.mp3` | gems->uncut;skill20, skill19, spirit20, spirit19, skillgemprogression18/17, spiritgemprogression18/17 |
| Gems L14–L16 | `gem.mp3` | gems->uncut;skillgemprogression16/15/14, spiritgemprogression16/15/14 |
| Lineage gems S/A | `gem.mp3` | gems->lineage;s, gems->lineage;a |
| Rare jewels | `gem.mp3` | gear_jewelrare (jewels->generic;anyrare, anytimelost, any5modded) |
| Mid currency | `chime1.mp3` | currency;c, currency;d |
| Magic jewels | `jewel.mp3` | gear_jewelmagic (jewels->generic;anymagic) |
| Flasks / charms | `chime2.mp3` | endgame->flasks;toplevelflasks, endgame->charms;hight1charms |
| Salvageables / crafting | `transmute.mp3` | itemproperty_aecocraft, itemproperty_achancing, endgame->salvagable entries |
| Xeno B–C | `pong.mp3` | xenotiering;a, xenotiering;b, xenotiering;c |
| Chancing bases | `chime1.mp3` | chancing;chances, chancing;chancea |
| Low value / filler | no sound | currency;e, supply2/4, maps_regularlow, gear_weakrare*, xeno_d/e |

### Full itemTag → sound mapping

```javascript
const sounds = [
  // S-tier / apex
  ['currency;s',                        'Stefan Gold_6veryvaluable.mp3'],
  ['apex_stier',                        'Stefan Gold_6veryvaluable.mp3'],  // via style — handled separately
  ['fragments->generic;s',              'Stefan Gold_6veryvaluable.mp3'],
  ['currency->splinter;t1',             'Stefan Gold_6veryvaluable.mp3'],
  ['maplike->special;superkeys',        'Stefan Gold_6veryvaluable.mp3'],

  // Top currency
  ['currency;a',                        'Stefan Gold_2currency.mp3'],
  ['currency;b',                        'Stefan Gold_2currency.mp3'],
  ['currency->splinter;t2',            'Stefan Gold_2currency.mp3'],
  ['fragments->generic;a',             'Stefan Gold_4maps.mp3'],
  ['currency->splinter;t3',            'Stefan Gold_4maps.mp3'],

  // Uniques
  ['uniques;t1',                        'Stefan Gold_1maybevaluable.mp3'],
  ['uniques;sekhemaring',               'Stefan Gold_1maybevaluable.mp3'],
  ['uniques;multispecialhigh',          'Stefan Gold_1maybevaluable.mp3'],
  ['uniques;overqualityuniques',        'Stefan Gold_1maybevaluable.mp3'],
  ['uniques;oversocketuniques1',        'Stefan Gold_1maybevaluable.mp3'],
  ['uniques;oversocketuniques2',        'Stefan Gold_1maybevaluable.mp3'],
  ['uniques;twicecorrupteduniques',     'Stefan Gold_1maybevaluable.mp3'],
  ['uniques;t2',                        'Stefan Gold_1maybevaluable.mp3'],
  ['uniques;t3boss',                    'Stefan Gold_1maybevaluable.mp3'],
  ['uniques;multispecial',              'Stefan Gold_1maybevaluable.mp3'],

  // High exotics / special
  ['exoticbases;superexoticbases',      'Stefan Gold_1maybevaluable.mp3'],
  ['exoticbases;kalandrabases',         'Stefan Gold_1maybevaluable.mp3'],
  ['exotic->exceptional;overqual1q1',   'Stefan Gold_1maybevaluable.mp3'],
  ['exotic->exceptional;oversockt1s3',  'Stefan Gold_1maybevaluable.mp3'],
  ['exotic->exceptional;oversockt1s2',  'Stefan Gold_1maybevaluable.mp3'],

  // Maps — waystones T13–T16
  ['waystones;waystone_t16',            'map1.mp3'],
  ['waystones;waystone_t15',            'map1.mp3'],
  ['waystones;waystone_t14',            'map1.mp3'],
  ['waystones;waystone_t13',            'map1.mp3'],
  ['waystones;corrupted8high',          'map1.mp3'],
  ['waystones;corrupted8',              'map1.mp3'],
  ['maplike->special;vaultkeysrare',    'GhazzyTV_5highmaps.mp3'],
  ['maplike->special;vaultkeys',        'GhazzyTV_5highmaps.mp3'],
  ['maplike->special;logbookshigh',     'GhazzyTV_5highmaps.mp3'],

  // Maps — waystones T8–T12
  ['waystones;waystone_t12',            'map2.mp3'],
  ['waystones;waystone_t11',            'map2.mp3'],
  ['waystones;waystone_t10',            'map2.mp3'],
  ['waystones;waystone_t9',             'map2.mp3'],
  ['waystones;waystone_t8',             'map2.mp3'],
  ['waystones;enchanted34',             'map2.mp3'],
  ['waystones;enchanted2',              'map2.mp3'],
  ['fragments->generic;b',              'GhazzyTV_4maps.mp3'],
  ['currency->splinter;t3',            'GhazzyTV_4maps.mp3'],

  // Maps — waystones T4–T7
  ['waystones;waystone_t7',             'map3.mp3'],
  ['waystones;waystone_t6',             'map3.mp3'],
  ['waystones;waystone_t5',             'map3.mp3'],
  ['waystones;waystone_t4',             'map3.mp3'],
  ['waystones;enchanted1',              'map3.mp3'],
  ['fragments->generic;c',              'map3.mp3'],
  ['currency->splinter;t4',            'map3.mp3'],

  // Gems
  ['gems->uncut;skill20',               'gem.mp3'],
  ['gems->uncut;skill19',               'gem.mp3'],
  ['gems->uncut;skillgemprogression18', 'gem.mp3'],
  ['gems->uncut;skillgemprogression17', 'gem.mp3'],
  ['gems->uncut;skillgemprogression16', 'gem.mp3'],
  ['gems->uncut;skillgemprogression15', 'gem.mp3'],
  ['gems->uncut;skillgemprogression14', 'gem.mp3'],
  ['gems->uncut;spirit20',              'gem.mp3'],
  ['gems->uncut;spirit19',              'gem.mp3'],
  ['gems->uncut;spiritgemprogression18','gem.mp3'],
  ['gems->uncut;spiritgemprogression17','gem.mp3'],
  ['gems->uncut;spiritgemprogression16','gem.mp3'],
  ['gems->uncut;spiritgemprogression15','gem.mp3'],
  ['gems->uncut;spiritgemprogression14','gem.mp3'],
  ['gems->uncut;supportearlymaps',      'gem.mp3'],
  ['gems->lineage;s',                   'gem.mp3'],
  ['gems->lineage;a',                   'gem.mp3'],
  ['gems->lineage;b',                   'gem.mp3'],
  ['jewels->generic;anytimelost',       'gem.mp3'],
  ['jewels->generic;any5modded',        'gem.mp3'],
  ['jewels->generic;anycorruptedmod',   'gem.mp3'],
  ['jewels->generic;anyrare',           'gem.mp3'],

  // Mid currency
  ['currency;c',                        'chime1.mp3'],
  ['currency;d',                        'chime1.mp3'],
  ['chancing;chances',                  'chime1.mp3'],
  ['chancing;chancea',                  'chime1.mp3'],

  // Magic jewels
  ['jewels->generic;anymagic',          'jewel.mp3'],

  // Flasks / charms
  ['endgame->flasks;toplevelqualityflasks', 'chime2.mp3'],
  ['endgame->flasks;toplevelflasks',    'chime2.mp3'],
  ['endgame->charms;topqualitycharms',  'chime2.mp3'],
  ['endgame->charms;hight1charms',      'chime2.mp3'],
  ['endgame->charms;highothercharms',   'chime2.mp3'],

  // Salvageables / crafting bases
  ['endgame->normalcraft->economy;group1t1', 'transmute.mp3'],
  ['endgame->normalcraft->economy;group1t2', 'transmute.mp3'],
  ['endgame->normalcraft->any;t1ideallevel', 'transmute.mp3'],
  ['endgame->normalcraft->any;t1',           'transmute.mp3'],
  ['chancing;chanceany',                'transmute.mp3'],

  // Xeno B–C
  ['xenotiering;s',                     'pong.mp3'],
  ['xenotiering;a',                     'pong.mp3'],
  ['xenotiering;b',                     'pong.mp3'],
  ['xenotiering;c',                     'pong.mp3'],

  // No sound — low value / filler
  // currency;e, currency;supplieslow, waystones T1–T3,
  // gear_weakrare*, xeno_d/e, fragments d/e, utility_minimize
];

function setSound(itemTag, filename, volume = 300) {
  const cs = gFilterBlade.changeStorage;
  const result = cs.addChange('dynamic', {
    identifier: {
      identifier: 'PlayAlertSound',
      mode: 'normal',
      index: 1,
      version: 3,
      isReal: true
    },
    newValue: ['CustomAlertSound', [filename, volume]],
    logicName: 'editFilterEntry',
    version: 1,
    itemTag: itemTag
  }, true);
  return result ? `OK: ${itemTag}` : `SKIP: ${itemTag}`;
}

sounds.forEach(([tag, file]) => console.log(setSound(tag, file)));
cs.updateLocalStorage();
```

---

## Version History

| Date | Changes | Notes |
|---|---|---|
| 2026-06-19 | Initial Dark Moody Amethyst scheme | Full redesign from Cosmic Gold. 93 style keys, background colors, gem icon overrides, sound assignments documented. |
