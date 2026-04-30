# Danish Energy Label Analysis — By Component Type

This analysis organizes the XML transformations by building component type rather than by transformation pattern.

**Properties analyzed:** 10
**Component types:** Walls, Windows, Doors, Floors, Ceilings/Roofs, Technical systems

---

## Table of Contents

1. [Walls](#walls)
2. [Windows](#windows)
3. [Doors](#doors)
4. [Floors](#floors)
5. [Ceilings/Roofs](#ceilingsroofs)
6. [Technical Systems](#technical-systems)
   - [Heat Source](#heat-source)
   - [Heat Distribution](#heat-distribution)
   - [Domestic Hot Water](#domestic-hot-water)
   - [Ventilation](#ventilation)
   - [Solar Cells](#solar-cells)

---

## Walls

**BI Classification:** `1-2-*` (External walls, basement walls, cavity walls, etc.)

### Overview

- **Properties with wall statuses:** 10/10
- **Total draft statuses:** 29
- **Total final statuses:** 29
- **Change:** +0 (stable)
- **BuildingReview entries:** 18

### Typical Transformations

**Common Pattern:** 1:1 mapping with placeholder resolution

**Example (Ivarsvej 27 — 1-2-1-0):**

**Draft ShortText:**
```
Hul ydervæg - 30 cm tegl/tegl - mineraluldsgranulat
```

**Draft LongText:**
```
Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet vurderes efterisoleret med mineraluldsgranulat. Konstruktions- og isoleringsforhold er baseret på et tidligere energimærke.
(??? U-værdi tillæg påført: 0.16 W/m2K)
```

**Final ShortText:**
```
Hul ydervæg - 30 cm tegl/tegl - mineraluldsgranulat
```

**Final LongText:**
```
Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet vurderes efterisoleret med mineraluldsgranulat. Konstruktions- og isoleringsforhold er baseret på et tidligere energimærke.
```

### Common BI Classifications for Walls

- `1-2-1-0`: 10 statuses across properties
- `1-2-4-0`: 6 statuses across properties
- `1-2-2-1`: 5 statuses across properties
- `1-2-2-0`: 5 statuses across properties
- `1-2-3-0`: 3 statuses across properties

### Key Observations

- Wall statuses remain stable (draft count = final count)
- Most transformations are 1:1 with `???` placeholders resolved to actual U-values, thicknesses
- Consultants rarely add or remove wall entries
- Wall descriptions in BuildingReview typically consolidate multiple similar walls

---

## Windows

**BI Classification:** `1-3-1-0` (Windows)

### Overview

- **Properties with window statuses:** 10/10
- **Total draft statuses:** 84
- **Total final statuses:** 84
- **Change:** +0 (stable)
- **BuildingReview entries:** 10

### Typical Transformations

**Common Pattern:** N-to-1 deduplication (Pattern 3)

Windows show the most dramatic transformation:
- **Draft:** One `<Status>` per physical window (with unique `<Window>` payload: area, orientation, U-value)
- **Final:** Multiple draft statuses with identical boilerplate text are collapsed
- **BuildingReview:** Consultant writes a single summary describing the window types

**Example — Pattern 6 (Selective Inclusion with Summary):**

From Lungstedløkken 15:

```
Vinduerne i bygningen er fortrinsvis med 2 og 3 lags energiruder.
Undtaget er vinduespartier ved tagterrasse i overetagen.
```

This is a **consultant-written summary** that:
- Describes the general pattern ("primarily 2 and 3 layer energy glass")
- Explicitly notes exceptions ("Except for window sections at the roof terrace")
- Appears in the final BuildingReview instead of listing all individual windows

### Key Observations

- Windows have the highest Status count (84 in both draft and final)
- Each physical window gets its own Status in the draft
- Draft statuses have identical LongText but unique Window payloads (area, orientation, U-value)
- Consultants edit only the *first* Status in each BI group for the summary
- The BuildingReview algorithm selects this first Status for the PDF report
- This is why Pattern 3 (N-to-1 deduplication) is so common for windows

---

## Doors

**BI Classification:** `1-3-3-0` (Exterior doors)

### Overview

- **Properties with door statuses:** 10/10
- **Total draft statuses:** 35
- **Total final statuses:** 35
- **Change:** +0 (stable)
- **BuildingReview entries:** 8

### Typical Transformations

**Common Pattern:** Similar to windows — N-to-1 deduplication

Like windows, doors often have:
- Multiple draft Statuses with identical boilerplate
- Each referring to a distinct physical door (with unique Door payload)
- Consultant edits the first Status for the summary
- BuildingReview shows this consolidated description

**Example — Spurvevej 13:**

**Draft:** 6 door Statuses (various types: terrace doors, entrance doors, garage doors)

**Final:** 6 door Statuses (same count, but texts updated)

**BuildingReview (Pattern 4 — Concatenation):**

```
Yderdør i kælder er monteret med tolags termoruder.

Terrassedør i stue er monteret med tolags termorude.

Yderdør med sideparti i entre er monteret med tolags termoruder.

Terrassedør på første sal er monteret med tolags energirude.

Portpanelet i garage er udført som et sandwichmodul som dobbelt lag.
```

All individual door descriptions are concatenated (separated by blank lines) in the BuildingReview, preserving location-specific details rather than using a generic summary.

### Key Observations

- Doors behave similarly to windows in transformation patterns
- Count remains stable (35 draft = 35 final)
- Each door gets individual tracking in draft, consolidated in review
- Common door types: sliding door sets, entrance doors with side panels, terrace doors

---

## Floors

**BI Classification:** `1-4-*` (Floors, ground slabs, basement ceilings)

### Overview

- **Properties with floor statuses:** 10/10
- **Total draft statuses:** 44
- **Total final statuses:** 44
- **Change:** +0 (stable)
- **BuildingReview entries:** 12

### Common BI Classifications

- `1-4-5-0`: 22 statuses
- `1-4-1-0`: 17 statuses
- `1-4-2-0`: 3 statuses
- `1-4-4-0`: 2 statuses

### Typical Transformations

**Common Pattern:** 1:1 with placeholder resolution and property value updates

Floors tend to have:
- Stable status counts
- Minimal boilerplate insertion
- Direct transformation of `???` values to actual measurements
- **Property value corrections** when better data sources are available

**Example — Spangsvej 15 (1-4-1-0 - Ground slab):**

**Draft LongText:**
```
Terrændæk er udført af beton med letklinkerbeton. Gulvet er uisoleret. 
Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.
```

**Final LongText:**
```
Terrændæk i bryggers og badeværelse er udført af beton med letklinkerbeton. 
Gulvet er uisoleret. Konstruktions- og isoleringsforhold er konstateret ud 
fra tegningsmateriale.
```

**Change:** Location detail added ("i bryggers og badeværelse"), transforming a generic description into a location-specific one. This is Pattern 1a (near-identical with minor wording modifications).

**Example — Spangsvej 15 (1-4-4-0 - Basement floor, Pattern 1b - Property Value Update):**

**Draft:**
- ShortText: `Kældergulv - Beton med slidlag - uisoleret`
- LongText: `Gulvet er uisoleret. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.`

**Final:**
- ShortText: `Kældergulv - Beton med slidlag - 50 mm mineraluld/polystyrenplader`
- LongText: `Gulvet er isoleret med 50 mm mineraluld under betonen... Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.`

**Change:** This demonstrates **Pattern 1b (Property Value Update)** - the consultant corrected the insulation status from "uisoleret" to "isoleret med 50 mm mineraluld" after reviewing technical drawings. The information source upgraded from "ejers oplysninger" (owner's claim) to "tegningsmateriale" (technical documentation). This reveals the consultant's verification process: starting with owner information, then confirming/correcting with actual building documentation.

### Key Observations

- `1-4-5-0` (Linear loss: Foundation) is most common (23 statuses)
- `1-4-1-0` (Ground slab / terrændæk) second most common (17 statuses)
- Floors show stable, predictable transformations
- Less consultant intervention compared to windows/doors
- **Pattern 1b (Property Value Update)** occasionally appears when owner information differs from technical documentation (e.g., insulation status corrections)

---

## Ceilings/Roofs

**BI Classification:** `1-1-*` (Roofs, attic ceilings, walls to unheated spaces)

### Overview

- **Properties with ceiling/roof statuses:** 10/10
- **Total draft statuses:** 28
- **Total final statuses:** 30
- **Change:** +2
- **BuildingReview entries:** 14

### Common BI Classifications

- `1-1-1-0`: 20 statuses
- `1-1-3-0`: 10 statuses

### Typical Transformations

**Notable:** BI code reshuffling observed

In some properties, draft entries under `1-1-3-0` (walls to unheated spaces) are re-classified to `1-1-1-0` (attic ceilings) in the final version.

**Example — Lungstedløkken 15:**

**Draft (BI 1-1-3-0 — "Walls to unheated spaces"):**
```
ShortText: Vægge mod skunkrum - 150 mm isolering

LongText: Vægge mod skunkrum vurderes isoleret med 150 mm isolering. 
Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet.
```

**Final (BI 1-1-1-0 — "Attic ceilings", reclassified):**
```
ShortText: Vægge mod skunkrum - 150 mm isolering

LongText: Vægge mod skunkrum vurderes isoleret med 150 mm isolering.
Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet.
```

**Change:** 
1. BI code changed from `1-1-3-0` → `1-1-1-0`
2. Minor text edit: "renoveringstidspunktet" (renovation time) → "opførelsestidspunktet" (construction time)

This demonstrates consultant review of building element categorization. "Skunkrum" (unheated attic/crawl space) walls are better classified under attic ceilings than as walls to unheated spaces.

### Key Observations

- Modest increase (+2 statuses across all properties)
- BI reshuffling indicates consultant review of building element categorization
- Mixture of direct 1:1 transformations and slight reclassifications

---

## Technical Systems

Technical systems show the **most dramatic increases** from draft to final.

| System Type | Draft | Final | Change |
|-------------|-------|-------|--------|
| Heat Source | 12 | 35 | +23 |
| Heat Distribution | 11 | 38 | +27 |
| Domestic Hot Water | 10 | 32 | +22 |
| Ventilation | 4 | 10 | +6 |
| Solar Cells | 0 | 10 | +10 |

### Heat Source

**BI Classification:** `2-1-*`

- Draft: 12 | Final: 35 | Change: +23

**Common Pattern:** Massive boilerplate insertion (Pattern 5)

Heat source shows:
- Very few draft statuses (often just 2-3 per property)
- Final includes many "Ingen [X] - Intet forslag" (No [X] - No proposal) entries
- These are auto-generated boilerplate confirming absence of solar thermal, heat pumps, etc.

**Example — Spurvevej 13:**

**Draft heat source statuses:** 2  
**Final heat source statuses:** 4

**Boilerplate entry added (BI 2-1-5-0):**
```
ShortText: Ingen varmepumpe - Intet forslag

LongText: Der er ikke stillet forslag til varmepumpe, da dette, med bygningens 
eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre 
en reduktion af energiomkostningerne.
```

This entry was **not present in the draft** — Energy10 software auto-generated it to document the evaluation and explain why a heat pump was not recommended. This is pure Pattern 5 (inserted boilerplate).

### Heat Distribution

**BI Classification:** `2-2-*`

- Draft: 11 | Final: 38 | Change: +27

**Common Pattern:** Boilerplate insertion for radiators, thermostats, summer shutoff

Distribution systems gain many standard compliance statuses:
- Radiator configurations (2-pipe system per HB2023)
- Thermostat valves on all radiators
- Summer shutoff of heating system

### Domestic Hot Water

**BI Classification:** `3-1-*`

- Draft: 10 | Final: 32 | Change: +22

**Common Pattern:** Extensive boilerplate insertion

DHW shows the highest increase ratio:
- Draft has only basic entries (often 1-2 per property)
- Final includes standard consumption profiles, pipe lengths, tank insulation specs
- All per HB2023 (Håndbog for Energikonsulenter 2023)

**Example — Spurvevej 13:**

**Draft DHW statuses:** 2  
**Final DHW statuses:** 3

**Standard entry added (BI 3-1-1-0):**
```
ShortText: Bolig - standard varmtvandforbrug iht. HB2023

LongText: I beregningen er der indregnet et varmtvandsforbrug på 250 liter 
pr. m² opvarmet etageareal pr. år.
```

This HB2023 compliance entry was **not in the draft**. Energy10 automatically inserted the standard domestic hot water consumption profile to ensure calculations follow the 2023 Handbook for Energy Consultants (Håndbog for Energikonsulenter). Classic Pattern 5.

### Ventilation

**BI Classification:** `1-5-*`

- Draft: 4 | Final: 10 | Change: +6

**Common Pattern:** Natural ventilation specs added

Ventilation gains:
- Infiltration rates (0.3-0.4 l/s m²)
- Tightness classifications

### Solar Cells

**BI Classification:** `4-1-*`

- Draft: 0 | Final: 10 | Change: +10

**Common Pattern:** Absence confirmation boilerplate

Solar cells:
- Absent from all drafts (0 entries)
- Final includes "Ingen solcelle" (No solar cells) for each property
- Pure boilerplate to confirm field was evaluated

### Key Observations on Technical Systems

Technical systems are where **Pattern 5 (Inserted boilerplate) dominates**:

1. **Drafts are minimal** — consultants only record what exists (e.g., "district heating")
2. **Finals are comprehensive** — Energy10 software auto-generates:
   - Standard compliance entries (HB2023 defaults)
   - Absence confirmations ("No heat pump", "No solar thermal")
   - System specifications (radiator types, pipe insulation, etc.)
3. **BuildingReview is sparse** — technical details don't all appear in the PDF summary

This is fundamentally different from building envelope components (walls, windows) where:
- Drafts and finals have similar counts
- Transformations are mostly 1:1 with placeholder resolution
- Consultants actively edit descriptions

---

## Summary

### Component Type Transformation Profiles

| Component | Draft→Final Stability | Dominant Pattern | Consultant Activity |
|-----------|----------------------|------------------|---------------------|
| **Walls** | Stable (29→29) | 1:1 placeholder resolution | Low |
| **Windows** | Stable (84→84) | N-to-1 deduplication | Medium (summary writing) |
| **Doors** | Stable (35→35) | N-to-1 deduplication | Medium |
| **Floors** | Stable (44→44) | 1:1 placeholder resolution | Low |
| **Ceilings** | Modest growth (28→30) | 1:1 + BI reshuffling | Low |
| **Heat Source** | High growth (12→35) | Massive boilerplate insertion | Low |
| **Heat Dist** | High growth (11→38) | Boilerplate insertion | Low |
| **DHW** | Very high growth (10→32) | Extensive boilerplate | Low |
| **Ventilation** | Growth (4→10) | Standard spec insertion | Low |
| **Solar Cells** | Complete addition (0→10) | Absence boilerplate | None |

### Key Takeaways by Component Type

#### Building Envelope (Walls, Windows, Doors, Floors, Ceilings)
- **Stable counts** — draft and final have similar numbers of Status entries
- **Active consultant editing** — especially for windows and doors where summary descriptions are crafted
- **Physical detail preserved** — each window/door tracked individually with unique payload data
- **Pattern 3 dominates** — multiple identical draft texts refer to distinct physical elements
- **Pattern 1b (Property Value Update)** — consultants correct property values (insulation, U-values) when better information sources become available, upgrading from "ejers oplysninger" (owner info) to "tegningsmateriale" (technical drawings)

#### Technical Systems (Heat, DHW, Ventilation, Solar)
- **Explosive growth** — finals have 2-3x more Status entries than drafts
- **Software-generated compliance** — Energy10 auto-inserts HB2023 standard specifications
- **Absence documentation** — systems not present get explicit "No [X]" entries
- **Pattern 5 dominates** — inserted boilerplate is the primary transformation
- **Minimal consultant editing** — technical specs are standardized, not customized
