# Danish Energy Label XML Analysis — Landevejen 70, 5683 Haarby

Analysis of a single property energy label pair (draft → final) from Botjek A/S.

**Date:** 2026-05-08
**Property:** Landevejen 70, 5683 Haarby
**Consultant:** Jacob Reimer Madsen (ID 402535), jrm@botjek.dk
**Serial:** 311898812 (final) / 100103025 (draft placeholder)

---

## 1. File Structure Overview

| | Draft | Final |
|--|-------|-------|
| Filename | `Landevejen_70_5683_Haarby.xml` | `Landevejen_70_5683_Haarby final.xml` |
| Size | 435 KB | 2.06 MB (includes embedded PDF/images) |
| Lines | 1 516 (pretty-printed) | 137 (minified) |
| Software | Plans v1 | Energy10 v1.00 |
| Company | `000000` Botjek | `600078` Botjek A/S |
| Consultant ID | `000000` / name `"jrm "` | `402535` / Jacob Reimer Madsen |
| ReviewDate | 2024-10-11 | 2026-05-04 |
| ValidFrom | 2026-05-08 | 2026-05-04 |

**Notable:** ReviewDate in draft is 2024-10-11 — the site inspection took place in October 2024, but the final submission did not happen until May 2026, approximately 18 months later.

### Building Facts

| Field | Value |
|-------|-------|
| Address | Landevejen 70, 5683 Haarby |
| BFE | 3056121 |
| BBR code | 120 (fritliggende enfamilieshus) |
| Year of construction | 1939 |
| BBR dwelling area | 130 m² |
| Total heated area | 126 m² |
| Top floor heated | 39 m² |
| Unheated basement | 12 m² |
| Primary heat source | Pille-kedel, NBE Woody/Scotte/BlackStar, 16 kW |
| Secondary | Luft/luft varmepumpe (stue, 2010–2015) |
| Energy label (current) | **F** |
| After profitable proposals | **B** |
| After all proposals | **A2010** |

---

## 2. Status Count Changes

| | Draft | Final | Change |
|--|------:|------:|-------:|
| `<Status>` elements | 43 | 51 | +8 |
| BuildingReview Text blocks | — | 22 | — |

### Draft BI distribution

| BI | Count | Component |
|----|------:|-----------|
| `1-3-1-0` | 9 | Vinduer |
| `1-1-3-0` | 5 | Tag/loft (hanebåndsloft, skråvægge, skunkrum, loftslem, vægge mod skunkrum) |
| `1-3-4-0` | 5 | Linjetab (vinduer/døre) |
| `1-3-3-0` | 4 | Yderdøre |
| `1-2-2-0` | 3 | Massive ydervægge (letbeton) |
| `1-4-5-0` | 3 | Linjetab (fundament) |
| `1-2-1-0` | 2 | Hulmur tegl/tegl |
| `1-1-1-0` | 1 | Loftsrum |
| `1-4-3-0` | 1 | Gulv mod krybekælder |
| `1-4-2-0` | 1 | Etageadskillelse mod det fri |
| `1-4-1-0` | 1 | Terrændæk |
| `2-2-4-0` | 1 | Regulering (termostat) |
| `2-2-2-0` | 1 | Varmerør |
| `2-2-3-0` | 1 | Varmefordelingspumpe |
| `2-2-1-0` | 1 | Radiator |
| `2-1-5-0` | 1 | Varmepumpe (luft/luft) |
| `2-1-0-0` | 1 | Kedel (generic) |
| `3-1-3-0` | 1 | Tilslutningsrør VVB |
| `3-1-5-0` | 1 | Varmtvandsbeholder |

### Final BI distribution (changes highlighted)

Added in final: `1-5-1-0`, `1-6-1-0`, `2-1-6-0`, `3-1-1-0`, `3-1-4-0`, `4-1-3-0` (all Pattern 5 boilerplate insertions).  
`2-1-0-0` → `2-1-2-0` (BI reclassification).  
`1-1-3-0` count 5 → 1 (four elements reclassified to `1-1-1-0`).  
`2-2-4-0` count 1 → 2 (Sommerstop split out as separate Status).

---

## 3. Transformation Patterns (all 22 BuildingReview blocks)

### Pattern 1 — 1:1 Copy (Unchanged)

Draft Status LongText copied verbatim to final Status and to BuildingReview.

| BI | ShortText | Text |
|----|-----------|------|
| `1-1-3-0` | Skråvægge - 150 mm isolering | *"Skråvægge vurderes isoleret med 150 mm mineraluld. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet."* |
| `2-1-5-0` | Luft/luft varmepumpe | *"Der er registreret en luft til luft-varmepumpe. Varmepumpen er placeret stue. Varmepumpen anvendes alene til rumopvarmning."* |
| `2-2-1-0` | Radiator - 2-streng | *"Varmeanlægget er udført som et 2-strengs radiatorsystem, hvor radiatorerne er tilsluttet separate frem- og returløb."* |
| `2-2-3-0` | Automatisk modulerende | *"Varmeanlægget er forsynet med en varmefordelingspumpe. Pumpens effekt er vurderet til ca. 45 W. Pumpen er placeret i udhus..."* |
| `3-1-5-0` | 94 l - Metro model 110 | *"Der er registreret en varmtvandsbeholder... fabrikat Metro, model 110 (rør ned). Beholderen har et volumen på ca. 91 liter og er placeret i gang..."* |

**Note on `2-1-2-0`:** The kedel Status LongText is unchanged, but its BI code was reclassified from `2-1-0-0` → `2-1-2-0` (generic heat source → specific boiler subtype). See Section 5.

**Count: 6** (P1 count includes `2-1-2-0` after BI correction)

---

### Pattern 1b — Location Qualifier Added

Draft has a generic component description; final adds a room name or building qualifier without changing the rest of the sentence.

| BI | Draft LongText | Final LongText |
|----|----------------|----------------|
| `1-1-1-0` | *"Loftsrum vurderes isoleret med 50 mm mineraluld..."* | *"Loftsrum **i tilbygning** vurderes isoleret med 50 mm mineraluld..."* |
| `1-1-1-0` | *"Hanebåndsloft vurderes isoleret med 200 mm mineraluld..."* | *"Hanebåndsloft **på 1 sal** vurderes isoleret med 200 mm mineraluld..."* |
| `1-4-1-0` | *"Terrændæk er udført af beton med letklinkerbeton..."* | *"Terrændæk **i tilbygning** er udført af beton med letklinkerbeton..."* |
| `1-4-2-0` | *"Etageadskillelse **mod det fri** udført som lukket bjælkelag..."* | *"Etageadskillelse **mod kælder** udført som lukket bjælkelag..."* |
| `1-4-3-0` | *"Gulv mod krybekælder af træ/bjælker er uisoleret..."* | *"Gulve **i oprindelig hus** mod krybekælder af træ/bjælker er uisoleret..."* |
| `1-2-1-0` | *"Ydervægge er udført som 30 cm hulmur..."* | *"Ydervægge **oprindelig hus** er udført som 30 cm hulmur..."* |

The `1-4-2-0` case is also a factual correction: the floor is above an unheated basement/crawl space, not above the open air — "mod det fri" was wrong.

The `1-2-2-0` group receives even heavier treatment: the three wall Statuses go from generic to room-labelled (*"i tilbygning i værelse"*, *"i tilbygning i gangen mod vej"*) plus a "not rentable" explanation appended to two of them. These appear in BuildingReview via Pattern 4 (concatenation).

**Count: 4**

---

### Pattern 2 — Placeholder Resolved

`???` location/measurement fills and `XXX` template menu choices.

#### Free-text `???` fills

| BI | Draft | Final |
|----|-------|-------|
| `2-2-2-0` | *"Rørene er placeret i **???** og har en samlet længde på ca. **??? m**."* | *"Rørene er placeret i **garage** og har en samlet længde på ca. **10 m**."* |
| `3-1-3-0` | *"Rørene er placeret i **???** og har en samlet længde på ca. **??? m**."* | *"Rørene er placeret i **udhus** og har en samlet længde på ca. **5 m**."* |
| `1-2-1-0` ×2 | *(??? U-værdi tillæg påført: 0.16 / 0.27 W/m²K)* | Deleted entirely |

#### `XXX` template menu choices (Comments section)

| Template line | Draft | Final |
|---------------|-------|-------|
| Ejeroplysningsskema | Both options present | *"forelå **ikke** et udfyldt ejeroplysningsskema..."* (second option kept) |
| Bygningstegninger | `Bygningstegninger XXX` | *"Bygningstegninger: **Ingen**"* |
| Energimærke reference | `af den XX-XX-XX, med nr.: XXX` | *"**10-06-2019**, med energimærkningsnummer: **311388269**"* |
| Andet | `Andet XXX` | Deleted |
| BBR area agreement (3 options) | All three present | Option 3 kept: *"...stemmer ikke overens... Afvigelsen består i **1 sal og stueplan**"* |
| Adgang til | `ikke adgang til XXX` | *"ikke adgang til **krybekælder**"* |
| Uopvarmede rum template | Present | Deleted |
| Area assumption templates ×2 | Present | Deleted |
| `XXX bygningstegninger` in OnBuildingDescription | `stikprøver og XXX bygningstegninger` | *"stikprøver og **skøn**"* |

**New paragraph added to OnBuildingDescription (no draft source):**  
*"Klimaskærmen ved udestuen er uisoleret, og den permanente opvarmningskilde vurderes ikke at kunne opvarme udestuen til mindst 15°. Udestuen er derfor ikke medregnet i det opvarmede areal jf. 'Håndbog for energikonsulenter'."*  
This explains the area discrepancy: BBR 130 m² vs heated 126 m² (udestue excluded).

**Count: 2** (in BuildingReview terms; ~10 template resolutions in Comments)

---

### Pattern 4 — Multiple Statuses Concatenated

Multiple distinct Statuses with the same BI → LongTexts joined with `\n\n` in BuildingReview.

**`1-1-1-0` (Tag/loft) — 5 Statuses → 1 Review block:**

| Status | Text |
|--------|------|
| Hanebåndsloft | *"Hanebåndsloft på 1 sal vurderes isoleret med 200 mm mineraluld..."* |
| Loftsrum | *"Loftsrum i tilbygning vurderes isoleret med 50 mm mineraluld..."* |
| Loft mod skunkrum | *"Loft mod skunkrum vurderes isoleret med 100 mm mineraluld..."* |
| Vægge mod skunkrum | *"Vægge mod skunkrum vurderes isoleret med 200 mm isolering..."* |
| Loftslem | *"Loftslem vurderes isoleret med 100 mm mineraluld. Konstruktionstykkelse er målt ved loftlem..."* |

**`1-2-2-0` (Massive ydervægge) — 3 Statuses → 1 Review block:**

| Status | Text (abridged) |
|--------|-----------------|
| 23 cm + 100 mm | *"Ydervægge i tilbygning i værelse består af 23 cm massiv letbetonvæg med indvendig pladebeklædning og 100 mm isolering..."* |
| 19 cm uisoleret | *"Ydervægge i tilbyning i værelse består af 19 cm massiv og uisoleret letbetonvæg..."* + "ikke rentabelt" footnote |
| 29 cm uisoleret | *"Ydervægge i tilbygning i gangen mod vej består af 29 cm massiv og uisoleret letbetonvæg..."* + "ikke rentabelt" footnote |

**`2-2-4-0` (Regulering) — 2 Statuses → 1 Review block:**

| Status | Text |
|--------|------|
| Termostatventiler | *"Der er monteret termostatventiler på alle radiatorer til regulering af korrekt rumtemperatur."* |
| Sommerstop | *"Udenfor fyringssæsonen forudsættes det i beregningen, at varmeanlægget kan afbrydes. Enten automatisk via udeføler eller manuelt ved lukning af ventiler og slukning af varmefordelingspumper."* |

Note: In draft only one `2-2-4-0` Status existed (Termostatventiler). The Sommerstop Status was **added** in the final, then both are concatenated.

**Count: 3**

---

### Pattern 5 — Inserted Boilerplate (No Draft Source)

New Statuses and Review blocks with no corresponding draft Status.

| BI | BuildingReview text (abridged) |
|----|-------------------------------|
| `1-5-1-0` | *"Der er naturlig ventilation i hele bygningen. Bygningen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand."* |
| `2-1-6-0` | *"Der er ikke stillet forslag til solvarmeanlæg, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag."* |
| `3-1-1-0` | *"I beregningen er der indregnet et varmtvandsforbrug på 250 liter pr. m² opvarmet etageareal pr. år."* |
| `3-1-4-0` | *"Der er ingen ladekredspumpe i bygningen."* |
| `4-1-3-0` | *"Der er ingen solceller på bygningen."* |

`1-6-1-0` (internal heat gain) appears as a Status in the final InputData but has no BuildingReview Text block (internal calculation input only).

**Count: 5** (in BuildingReview)

---

### Pattern 6 — Selective Inclusion (Consultant Summary Wins)

Consultant rewrites Status #1 of a BI group as a prose umbrella; Energy10 emits only that text, suppressing the remaining boilerplate Statuses.

**`1-3-1-0` — Windows: 9 Statuses → 3-sentence Review**

Draft had 9 window Statuses with 3 unique boilerplate sentences:
- *"Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude."* (×5)
- *"Oplukkelige vinduer med et fag. Vinduerne er monteret med trelags termorude."* (×1)
- *"Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags energirude."* (×3)

Final Status #1 (entre/gang), #2 (stue), #4 (øvrige) are rewritten with location context. Energy10 emits those 3 distinct texts as a concatenated Review (Patterns 4+6 combined):

> *"Vinduer i entre og gang er monteret med tolags termoruder.*
> *Vindue i stue er monteret med trelags termoruder.*
> *Øvrige vinduer er monteret med tolags energiruder."*

Window breakdown by type:

| Glazing type | U-value | Placements |
|-------------|---------|------------|
| 2-lags termorude kold kant (U=2.8) | 2.80 | 5 (entre, gang, bathroom?, east, east) |
| 3-lags termorude kold kant | (lower) | 1 (stue) |
| 2-lags energirude kold kant (U=1.42) | 1.42 | 3 (west ×2, north) |

Collapse ratio: 9:3 (3.0:1)

**`1-3-3-0` — Doors: 4 Statuses → 1-sentence Review**

Draft had 4 identical Statuses:
> *"Yderdør med enkeltfagsvindue, monteret med tolags termoruder."*

Final Status #1 rewritten as umbrella:
> *"Alle yderdøre er monteret med tolags termoruder."*

Energy10 emits only the umbrella. Statuses #2–4 retain the original boilerplate (suppressed).

Collapse ratio: 4:1

**Count: 2**

---

## 4. Pattern Distribution Summary

| BI | Review Text | Pattern | Notes |
|----|------------|---------|-------|
| `1-1-1-0` | Text 0 | **P4** | 5 Statuses concatenated |
| `1-1-3-0` | Text 1 | **P1** | Skråvægge, unchanged |
| `1-2-1-0` | Text 2 | **P1b** | "oprindelig hus" qualifier + BI from `2-1-0-0`... wait that's kedel. Hulmur stays 1-2-1-0, but location qualifier added |
| `1-2-2-0` | Text 3 | **P4** | 3 Statuses with room identifiers concatenated |
| `1-3-1-0` | Text 4 | **P6** | 9 → 3 consultant summaries |
| `1-3-3-0` | Text 5 | **P6** | 4 → 1 umbrella |
| `1-4-1-0` | Text 6 | **P1b** | "i tilbygning" added |
| `1-4-2-0` | Text 7 | **P1b** | "mod det fri" corrected to "mod kælder" |
| `1-4-3-0` | Text 8 | **P1b** | "i oprindelig hus" added |
| `1-5-1-0` | Text 9 | **P5** | No draft source |
| `2-1-2-0` | Text 10 | **P1** | Text unchanged, BI reclassified from `2-1-0-0` |
| `2-1-5-0` | Text 11 | **P1** | Luft/luft varmepumpe, unchanged |
| `2-1-6-0` | Text 12 | **P5** | No draft source |
| `2-2-1-0` | Text 13 | **P1** | Radiator, unchanged |
| `2-2-2-0` | Text 14 | **P2** | Location + length filled in |
| `2-2-3-0` | Text 15 | **P1** | Pump, unchanged |
| `2-2-4-0` | Text 16 | **P4** | Termostat + new Sommerstop Status |
| `3-1-1-0` | Text 17 | **P5** | No draft source |
| `3-1-3-0` | Text 18 | **P2** | Location + length filled in |
| `3-1-4-0` | Text 19 | **P5** | No draft source |
| `3-1-5-0` | Text 20 | **P1** | VVB, unchanged |
| `4-1-3-0` | Text 21 | **P5** | No draft source |

| Pattern | Count | % |
|---------|------:|--:|
| P1 (unchanged) | 6 | 27% |
| P1b (location qualifier) | 4 | 18% |
| P2 (placeholder) | 2 | 9% |
| P4 (concatenated) | 3 | 14% |
| P5 (inserted boilerplate) | 5 | 23% |
| P6 (consultant umbrella) | 2 | 9% |
| **Total** | **22** | **100%** |

**Key observation:** Pattern 5 is lower than average (23% vs 47% across the 10-property dataset) because this draft is unusually complete — it already contained `2-2-2-0`, `2-2-3-0`, `2-2-1-0`, `2-1-5-0`, `3-1-3-0`, and `3-1-5-0`, which are often absent from thinner drafts.

---

## 5. BI Classification Reshuffles

| ShortText | Draft BI | Final BI | Reason |
|-----------|----------|----------|--------|
| Hanebåndsloft - 200 mm isolering | `1-1-3-0` | `1-1-1-0` | Same pattern as all other properties |
| Vægge mod skunkrum - 200 mm isolering | `1-1-3-0` | `1-1-1-0` | Same pattern |
| Loft mod skunkrum - 100 mm isolering | `1-1-3-0` | `1-1-1-0` | Same pattern |
| Loftslem - 100 mm isolering | `1-1-3-0` | `1-1-1-0` | Same pattern as Spurvevej, Spangsvej, Møllehøj |
| Kedel - Pille - NBE Woody/Scotte/BlackStar | `2-1-0-0` | `2-1-2-0` | Generic → specific boiler subtype (same as Spurvevej fjernvarme, Møllehøj gas) |

**Not reclassified:** Skråvægge stays `1-1-3-0` — consistent with all 10 previous properties.

---

## 6. Investment Rounding

Draft Proposal investments and their final equivalents (from ProposalGroup matching):

| Component | Draft | Final | Δ |
|-----------|------:|------:|--:|
| Massiv ydervæg 50 mm (large) | 24 612 | 24 792 | +180 |
| Massiv ydervæg 50 mm (small) | 13 620 | 13 800 | +180 |
| Vægge mod skunkrum | 6 774 | 6 903 | +129 |
| Krybekælder → terrændæk | 95 120 | 95 100 | −20 |
| Loftsrum 300 mm | 14 073 | 14 294 | +221 |
| Hanebåndsloft 150 mm | 8 432 | 8 432 | 0 |
| Skråvægge 200 mm | 33 865 | 33 865 | 0 |
| Loft mod skunkrum 250 mm | 5 697 | 5 697 | 0 |

Minor recalculations across the board — likely due to area or cost-rate updates between the Plans export and final Energy10 entry. No major price changes.

---

## 7. Notable Unique Features

### 1. No owner information sheet
Unlike all 10 properties in the main analysis where the owner sheet was present, this draft was filed without one. The consultant selected the second template option: *"forelå ikke et udfyldt ejeroplysningsskema. Det forudsættes hermed, at der ikke er givet tilladelse til destruktive undersøgelser."*

### 2. No drawings available
*"Bygningstegninger: Ingen"* — the consultant had no technical drawings. All construction data (insulation, dimensions) is based on estimates from the build year and direct measurements at the loft hatch. This is why multiple Statuses use *"skønnet ud fra renoveringstidspunktet"* rather than *"tegningsmateriale"*.

### 3. BBR area discrepancy — udestue
Area does not match BBR (130 m² vs 126 m² heated). The consultant added a non-template paragraph explaining an unheated conservatory (udestue) was excluded: *"Klimaskærmen ved udestuen er uisoleret, og den permanente opvarmningskilde vurderes ikke at kunne opvarme udestuen til mindst 15°..."*

### 4. Prior energy label referenced
The previous label (number 311388269, dated 10-06-2019) was referenced in the final. Draft had `XX-XX-XX`/`XXX` placeholders. Two construction assessments explicitly rely on it: *"Konstruktions- og isoleringsforhold er baseret på et tidligere energimærke"* (cavity wall, crawl space floor, terraced floor).

### 5. 18-month gap between inspection and submission
ReviewDate 2024-10-11 → submission 2026-05-04. This is the longest draft-to-final gap in the dataset and may explain why Plans used a placeholder ValidFrom of 2026-05-08 (the actual submission day), while Energy10 backdated to 2026-05-04.

### 6. Crawl space — no access
*"Ved bygningsgennemgangen var der ikke adgang til krybekælder."* The floor above it is described as unisolated based on the prior energy label, not direct inspection. The most profitable proposal (kroner 95 100, DKK 2 800/year saving) is to fill in and seal the crawl space.

---

## 8. Summary Statistics

| Metric | Value |
|--------|-------|
| Draft Statuses | 43 |
| Final Statuses | 51 (+8, +19%) |
| BuildingReview blocks | 22 |
| Placeholders resolved (`???`) | 4 (2 location fills, 2 U-value notes deleted) |
| Template choices (`XXX`) | ~10 (across Comments sections) |
| BI reshuffles | 5 |
| Investment adjustments | 8 proposals, minor rounding |
| Window placements | 9 → 3 unique glazing types → 3-sentence Review |
| Door placements | 4 → 1 umbrella sentence |
| Pattern 5 (boilerplate %) | 23% (below 47% dataset average — draft was well-filled) |

---

**Analysis complete — 1 property, 43 draft Statuses, 51 final Statuses, 22 BuildingReview blocks**
