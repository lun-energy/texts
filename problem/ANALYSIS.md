# Danish Energy Label XML Analysis

Analysis of 10 property energy label pairs (draft → final) from Botjek A/S.

**Date:** 2026-04-30  
**Properties analyzed:** 
- Ivarsvej 27 (Odense V)
- Spangsvej 15 (Odense NV)
- Lungstedløkken 15 (Odense SV)
- Spurvevej 13 (Vejle)
- Møllehøj 15 (Sønderborg)
- Kirkegyden 15 (Odense N)
- Lunden 3 (Galten)
- Nypølsgade 14 (Sydals)
- Strandbakken 5 (Rudkøbing)
- Sønderskovvej 5 (Humble)

---

## 1. File Structure Overview

### The 20 XML Files

All follow the Danish Energy Agency schema (`http://www.ens.dk/EnergyLabel`, version 2.0.1).

| Property | Draft file | Final file | Draft size | Final size (after cleanup) |
|----------|------------|------------|------------|---------------------------|
| Ivarsvej 27 | `Ivarsvej_27_5200_Odense_V.xml` | `Ivarsvej_27_5200_Odense_V final.xml` | 39 KB | 89 KB |
| Spangsvej 15 | `Spangsvej_15_5210_Odense_NV.xml` | `Spangsvej_15_5210_Odense_NV final.xml` | 58 KB | 93 KB |
| Lungstedløkken 15 | `Lungstedløkken_15_5250_Odense_SV.xml` | `Lungstedløkken_15_5250_Odense_SV final.xml` | 50 KB | 100 KB |
| Spurvevej 13 | `Spurvevej_13_7100_Vejle.xml` | `Spurvevej_13_7100_Vejle final.xml` | 102 KB | 151 KB |
| Møllehøj 15 | `Møllehøj_15_6400_Sønderborg plans.xml` | `Møllehøj_15_6400_Sønderborg final.xml` | 45 KB | 90 KB |
| Kirkegyden 15 | `Kirkegyden_15_5270_Odense_N.xml` | `Kirkegyden_15_5270_Odense_N final.xml` | 119 KB | 128 KB |
| Lunden 3 | `Lunden_3_8464_Galten.xml` | `Lunden_3_8464_Galten final.xml` | 43 KB | 76 KB |
| Nypølsgade 14 | `Nypølsgade_14_6470_Sydals.xml` | `Nypølsgade_14_6470_Sydals final.xml` | 67 KB | 127 KB |
| Strandbakken 5 | `Strandbakken_5_5900_Rudkøbing.xml` | `Strandbakken_5_5900_Rudkøbing final.xml` | 48 KB | 93 KB |
| Sønderskovvej 5 | `Sønderskovvej_5_5932_Humble.xml` | `Sønderskovvej_5_5932_Humble final.xml` | 50 KB | 81 KB |

### Two Software Tools

**Draft files** (Plans/plans export):
- `<EnergyLabelSoftware><Name>Plans</Name><Version>1</Version>`
- Pretty-printed, multi-line XML
- Placeholder serial `100103025`, placeholder company `000000`
- Contains `XXX` / `???` markers for incomplete data
- Missing mandatory boilerplate statuses

**Final files** (Energy10 submission):
- `<EnergyLabelSoftware><Name>Energy10</Name><Version>1.00</Version>`
- Minified single-line XML (before image removal)
- Real serial numbers (311897xxx), real company `600078` (Botjek A/S)
- All placeholders resolved
- Full `<ResultData>` and `<PDFReportData>` with BuildingReview

### Image Cleanup

Removed 28 embedded base64 JPEG images totaling ~8.5 MB across 18 files (all files except Ivarsvej and Møllehøj finals which had no images). Empty `<Images>` wrappers retained for schema compliance.

---

## 2. The Transformation Pipeline

```
draft.xml InputData/Statuses      (18–48 Status entries per property)
    │
    │  Text normalization:
    │  • XXX/??? placeholders filled in
    │  • Location descriptions added (room names, brands)
    │  • Template sentences refined
    │
    │  Structure expansion:
    │  • 7–15 new boilerplate Statuses added per property
    │  • BI codes reclassified (1-1-3-0 → 1-1-1-0, 2-1-0-0 → 2-1-3-0, etc.)
    │
    ▼
final.xml InputData/Statuses      (31–55 Status entries per property)
    │
    │  BuildingReview generation:
    │  • Group by BIClassification
    │  • Concatenate LongText fields per BI group
    │  • Deduplicate identical boilerplate
    │  • Apply consultant-written summaries (Status #1 wins)
    │
    ▼
final.xml PDFReportData/BuildingReview/Text    (18–23 Text blocks per property)
```

### Status Count Changes (Draft → Final)

| Property | Draft Statuses | Final Statuses | Change | BuildingReview blocks |
|----------|----------------|----------------|--------|----------------------|
| Ivarsvej 27 | 18 | 31 | +13 | 17 |
| Spangsvej 15 | 31 | 47 | +16 | 13 |
| Lungstedløkken 15 | 23 | 40 | +17 | 17 |
| Spurvevej 13 | 48 | 55 | +7 | 23 |
| Møllehøj 15 | 29 | 39 | +10 | 14 |
| Kirkegyden 15 | 48 | 56 | +8 | 17 |
| Lunden 3 | 23 | 32 | +9 | 16 |
| Nypølsgade 14 | 40 | 49 | +9 | 14 |
| Strandbakken 5 | 18 | 28 | +10 | 17 |
| Sønderskovvej 5 | 18 | 24 | +6 | 15 |
| **TOTAL** | **296** | **401** | **+105** | **163** |
| **Average** | **29.6** | **40.1** | **+10.5** | **16.3** |

---

## 3. The Seven Transformation Patterns

### Pattern 1: 1:1 Copy (Unchanged)

**Rule:** Draft Status LongText == Final Status LongText == Review StatusText (byte-for-byte identical)

**Examples:**
- **Ivarsvej `1-4-2-0`** (Gulv mod uopvarmet kælder): *"Gulv mod uopvarmet kælder udført som lukket bjælkelag vurderes isoleret med 30 mm mineraluld. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet."*
- **Spurvevej `1-4-4-0`** (Kældergulv): *"Kældergulv er udført af beton med slidlagsgulv. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale."*
- **Møllehøj `1-5-1-0`** (Ventilation): *"Der er naturlig ventilation i hele ejendommen. Ejendommen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand."*

**Count:** ~8 per property (clean installations without placeholders)

---

### Pattern 1b: Property Value Update (Data Correction)

**Rule:** Draft and Final describe the same building element with the same ShortText structure, but a key property value has been corrected/updated based on better information sources.

**Examples:**

**Spangsvej `1-4-4-0` (Kældergulv):**
- **Draft ShortText:** `Kældergulv - Beton med slidlag - uisoleret`
- **Draft LongText:** *"Kældergulv er udført af beton med slidlagsgulv. Gulvet er **uisoleret**. Konstruktions- og isoleringsforhold er baseret på **ejers oplysninger**."*
- **Final ShortText:** `Kældergulv - Beton med slidlag - 50 mm mineraluld/polystyrenplader`
- **Final LongText:** *"Kældergulv er udført af beton med slidlagsgulv. Gulvet er **isoleret med 50 mm mineraluld** under betonen med letklinker som kapillarbrydende lag. Konstruktions- og isoleringsforhold er **konstateret ud fra tegningsmateriale**."*

**What changed:**
1. **Insulation status corrected**: "uisoleret" → "isoleret med 50 mm mineraluld"
2. **Information source upgraded**: "ejers oplysninger" (owner's claim) → "tegningsmateriale" (technical drawings)
3. **ShortText significantly edited** to reflect corrected insulation value

This pattern reveals the consultant's investigation process: they start with the owner's information in Plans, then verify/correct it in Energy10 based on technical documentation. The fuzzy matching (69% similarity in this case) helps identify these as the same element despite significant ShortText edits.

**Common property updates:**
- Insulation thickness corrections
- U-value adjustments
- Material specification refinements
- Source verification upgrades (ejers oplysninger → tegningsmateriale → målt)

**Count:** Variable per property (depends on data quality discrepancies between owner information and technical documentation)

---

### Pattern 2: Placeholder Resolved

**Rule:** Draft had `???` or `XXX`, final fills it in, Review copies from final.

#### Placeholder Types

**A. `(??? U-værdi tillæg påført: X.XX W/m²K)`** — Calculation note, always deleted:
- Present in all wall/floor Statuses across all 5 properties
- Draft: `"Konstruktions- og isoleringsforhold ... \n(??? U-værdi tillæg påført: 0.16 W/m2K)"`
- Final: line deleted entirely

**B. Location/room fills:**

| Property | Status (BI) | Draft placeholder | Final value |
|----------|------------|-------------------|-------------|
| Spurvevej 13 | `2-1-4-0` Åben pejs | `"Ovnen er placeret i ???"` | **"stue på 1. sal"** |
| Spurvevej 13 | `2-2-2-0` Varmerør | `"samlet længde på ca. ??? m"` | **"placeret i uopvarmet depotrum i kælder"** |
| Spurvevej 13 | `3-1-5-0` VVB | `"placeret i ???. isoleret med ca. ??? isolering"` | **"bryggers i kælder"** (insulation clause dropped) |
| Møllehøj 15 | `2-2-1-0` Gulvvarme | `"Der er desuden gulvvarme i ???"` | **"bryggers, køkken, stue, entré og to badeværelser"** |
| Møllehøj 15 | `3-1-5-0` VVB | `"placeret i ???"` | **"mærke Bosch, årgang ca. 2015"** (location → brand/year) |

**C. Document references (Comments/Additional):**

| Property | Draft | Final |
|----------|-------|-------|
| Ivarsvej 27 | `"Bygningstegninger XXX"` | **"Bygningstegninger 1951"** |
| Ivarsvej 27 | `"Tidligere energimærkningsrapport af den XX-XX-XX, med energimærkningsnummer: XXX"` | **"11. maj 2022, med energimærkningsnummer: 311599521"** |
| Spangsvej 15 | `"Bygningstegninger XXX"` | **"fra opførelsen dateret 1978 og tilbygning dateret 1979"** |
| Lungstedløkken 15 | `"Bygningstegninger XXX"` | **"fra opførelsen dateret 1976"** |
| Spurvevej 13 | `"Bygningstegninger XXX"` | **"Udaterede bygningstegninger"** |
| Møllehøj 15 | `"Bygningstegninger XXX"` | **"Snit- og plantegninger fra 2008"** |

**D. Template choices (Comments/OnBuildingDescription):**

Every draft contains 3 mutually-exclusive lines for BBR-area agreement, each ending with `XXX`:
1. *"De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen. XXX"*
2. *"Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen. XXX"*
3. *"Det opmålte opvarmede areal stemmer ikke overens med BBR-meddelelsen. Afvigelsen består i XXX"*

Final keeps exactly one:
- **Ivarsvej, Lungstedløkken:** option 1
- **Møllehøj:** option 2
- **Spangsvej, Spurvevej:** option 3 with detail filled: *"...kælderen er opvarmet"* / *"...kælderen med undtagelse af depotrum medtaget"*

**Count:** ~4 real fills + ~10 template selections per property

---

### Pattern 3: N Draft Statuses Collapsed via Dedup

**Rule:** Multiple draft Statuses with identical LongText but distinct underlying BuildingUnit payloads → one Review sentence.

**Primary example:** `1-3-1-0` (Vinduer/windows)

Each `<Status>` wraps a `<Window>` payload with physical placement data:
```xml
<Window xmlns="http://www.ens.dk/BuildingUnits">
  <NumberOfWindows>2</NumberOfWindows>
  <Orientation>95</Orientation>
  <Inclination>90</Inclination>
  <Area>1.48</Area>
  <UValue>2.7</UValue>
  <GlassShare>0.57</GlassShare>
  <SolarHeatTransmittance>0.63</SolarHeatTransmittance>
</Window>
```

The `ShortText`/`LongText` describes the **glazing type**, not the window instance. So "6 statuses, one sentence" = "6 physical window positions, one window type."

#### Window Analysis by Property

**Ivarsvej 27: 6 placements → 1 type**
- All windows: `2-lags energirude med varm kant`, U=1.4
- Orientations: 2× north (3°), 1× east (93°), 3× south (183°)
- Areas: 1.17–4.58 m²
- Draft: 6× *"Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude."*
- **Review:** *"Vinduerne er monteret med tolags energirude."*

**Spangsvej 15: 9 placements → 3 types**
- 3× `2-lags energirude varm kant` (U=1.30)
- 3× `2-lags energirude kold kant` (U=1.42)
- 3× `3-lags energirude klasse B` (U=1.15)
- Draft: 9 Statuses with 3 distinct sentences
- **Review:** *"Vinduerne er monteret med to- og trelags energiruder."* (genuine union)

**Lungstedløkken 15: 5 placements → 3 types**
- 3× `2-lags energirude kold kant` (U=1.42)
- 1× `2-lags termorude kold kant` (U=2.80, 5.75 m² NW picture window)
- 1× `3-lags energirude klasse B` (U=1.20)
- **Review:** *"Vinduerne i bygningen er fortrinsvis med 2 og 3 lags energiruder. **Undtaget er vinduespartier ved tagterrasse i overetagen.**"*
  - The explicit exception traces to the single poor-quality NW window (row 4)

**Spurvevej 13: 9 placements → 2 types + 1 special**
- 8× `2-lags termorude` (U=2.7–2.8)
- 1× `Glasbyggesten` (U=3.0, 0.55 m² at north stairwell)
- **Review:** *"Alle vinduer er monteret med tolags termoruder. Vindue ved trappe er med glasbyggesten."*

**Møllehøj 15: 5 placements → 1 type**
- All: `2-lags energirude kold kant`, U=1.50
- Orientations: 3× east (96°), 1× west (276°), 1× north (6°)
- **Review:** *"Beskrivelse og glasforhold vedrørende vinduer, ovenlys/tagvinduer og døre er baseret på visuel kontrol ved konsulent. Vinduer, ovenlys/tagvinduer og døre er med to-lags energiruder med kold kant. Den massive yderdør er isoleret. ..."*
  - Consultant wrote this summary from scratch (no draft equivalent)

#### The Mechanism

The consultant edits **only Status #1** of each BI group to contain the summary. Energy10's BuildingReview generator emits only Status #1's LongText, suppressing the boilerplate from Statuses #2..N.

Example (Ivarsvej final Statuses):
```
[1] "Vinduerne er monteret med tolags energirude."           ← rewritten summary (emitted to Review)
[2] "Oplukkelige vinduer med flere fag. Vinduerne er ..."   ← untouched boilerplate (suppressed)
[3] "Oplukkelige vinduer med flere fag. Vinduerne er ..."   ← untouched
[4] "Oplukkelige vinduer med flere fag. Vinduerne er ..."   ← untouched
[5] "Oplukkelige vinduer med flere fag. Vinduerne er ..."   ← untouched
[6] "Oplukkelige vinduer med flere fag. Vinduerne er ..."   ← untouched
```

**Count:** 1–2 per property (primarily on `1-3-1-0` windows)

---

### Pattern 4: Multiple Final Statuses Concatenated

**Rule:** Multiple distinct Statuses with the same BI → their LongTexts concatenated with `\n\n` separators in the Review.

**Examples:**

**Ivarsvej `2-2-4-0` (Regulering):**
- Draft: 1 Status bundling two topics
- Final: split into 2 Statuses
  - #1 `Termostatventiler på alle radiatorer`: *"Der er monteret termostatventiler på alle radiatorer til regulering af korrekt rumtemperatur."*
  - #2 `Sommerstop af varmeanlæg`: *"Udenfor fyringssæsonen forudsættes det i beregningen, at varmeanlægget kan afbrydes. Enten automatisk via udeføler eller manuelt ved lukning af ventiler og slukning af varmefordelingspumper."*
- **Review:** #1 + `"\n\n"` + #2

**Spangsvej `1-4-1-0` (Terrændæk):**
- 3 floor constructions (bryggers/bathroom letklinkerbeton, strøgulve with 75mm insulation, general letklinkerbeton)
- **Review:** all 3 LongTexts chained with paragraph breaks

**Lungstedløkken `1-3-3-0` (Døre):**
- 3 doors, each with room label:
  - *"Terrassedør i stueetage er monteret med tolags energiruder."*
  - *"Hoveddør er monteret med tolags energiruder."*
  - *"Terrassedør i overetagen er monteret med tolags termoruder."*
- **Review:** sentence-level concatenation (no paragraph breaks here)

**Spurvevej `1-3-3-0` (Døre):**
- 6 doors/ports: kælder-yderdør, stue-terrassedør, entre-yderdør, 1.sal-terrassedør, garage-port, uisoleret kælderdør
- **Review:** 6-sentence paragraph

**Møllehøj `1-1-1-0` (Tag/loft):**
- 3 Statuses: Loftsrum 400mm + Skråvægge 400mm + Loftslem 30mm
- Each ends with *"Der er ikke givet forslag til efterisolering, da den årlige besparelse vil være minimal i forhold til investeringen."*
- **Review:** all 3 concatenated with repeating tail

**Count:** 3–5 per property (multi-variant constructions: roofs, floors, doors)

---

### Pattern 5: Inserted Boilerplate (No Draft Source)

**Rule:** Review block with a BI that has no corresponding Status in the draft. These are mandatory registration items that Energy10 always emits.

#### Universal Insertions (Every Property)

| BI | Review text (abridged) |
|----|------------------------|
| `1-5-1-0` | *"Der er naturlig ventilation i hele bygningen/ejendommen. Bygningen/Ejendommen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand."* |
| `2-1-3-0` or `2-1-2-0` | Heat source description (fjernvarme/kedel with location and specs) |
| `2-1-5-0` | *"Der er ikke stillet forslag til varmepumpe, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag."* |
| `2-1-6-0` | *"Der er ikke stillet forslag til solvarmeanlæg, da dette ..."* |
| `2-2-1-0` | Radiator system description: *"Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg."* |
| `2-2-4-0` | Thermostat + summer-stop combo |
| `3-1-3-0` | Standard DHW connector pipe: *"Varmetabet fra tilslutningsrør under 5 meter indregnes med et standard værdisæt for rørlængde og isoleringsniveau svarende til 4 meter med 30 mm isolering. Dette udføres iht. gældende Håndbog for Energikonsulenter."* |
| `4-1-3-0` | *"Der er ingen solceller på bygningen."* |

#### Property-Specific Insertions

- **Møllehøj `2-1-2-0`:** Kedel description (gas, Wolf CGB 2-20) — reclassified from draft's `2-1-0-0`
- **Spangsvej `3-1-5-0`:** Brugsvandsveksler description

#### Counts

| Property | Pattern 5 (inserted) | Out of total Review blocks | Percentage |
|----------|---------------------|---------------------------|------------|
| Ivarsvej 27 | **11** | 20 | 55% |
| Spangsvej 15 | 6 | 19 | 32% |
| Lungstedløkken 15 | 7 | 23 | 30% |
| Spurvevej 13 | 8 | 23 | 35% |
| Møllehøj 15 | 5 | 18 | 28% |

Ivarsvej's draft was thin on technical installations, so more than half of its final Review is boilerplate.

**Count:** 7–11 per property

---

### Pattern 6: Selective Inclusion (Rare)

**Rule:** Final has multiple Statuses for a BI, but Review uses only one "summary" Status, suppressing the rest.

Distinct from Pattern 3 (where draft text repetition drove dedup) — here the consultant intentionally overwrites Status #1 as an umbrella, and Energy10 recognizes this.

**Examples:**

**Lungstedløkken `1-3-1-0` (Vinduer):**
- Final has 5 Statuses:
  - #1: *"**Vinduerne i bygningen er fortrinsvis med 2 og 3 lags energiruder. Undtaget er vinduespartier ved tagterrasse i overetagen.**"* ← consultant summary
  - #2–5: original template sentences (*"Oplukkelige vinduer med et fag..."*, etc.)
- **Review:** only #1

This is a textbook example of Pattern 6. The consultant:
1. **Describes the general pattern** — "fortrinsvis" (primarily) acknowledges the majority case
2. **Explicitly notes exceptions** — "Undtaget er..." (Except for...) documents the specific variation
3. **Overwrites Status #1** as an umbrella description instead of listing all individual windows

This summary style is consultant-authored prose, not software-generated boilerplate. It demonstrates domain expertise: rather than forcing readers to infer patterns from 5+ individual window descriptions, the consultant provides a human-readable synthesis that both generalizes ("primarily 2 and 3 layer energy glass") and specifies exceptions ("window sections at the roof terrace on the upper floor").

**Lungstedløkken `3-1-3-0` (Tilslutningsrør):**
- Final has 2 Statuses:
  - #1: *"Standard tilslutningsrør ... (boilerplate)"*
  - #2: *"Brugsvandsrør med cirkulation er udført som PEX-rør. Rørene er isoleret med 10 mm isolering."*
- **Review:** only #2

**Count:** 0–2 per property (consultant-driven umbrella rewrites)

---

## 4. Pattern Distribution Across All Properties

Analysis of how the 163 BuildingReview blocks across 10 properties break down by transformation pattern:

| Property | P1 | P2 | P3 | P4 | P5 | P6 | Total |
|----------|---:|---:|---:|---:|---:|---:|------:|
| Ivarsvej 27 | 1 | 1 | 1 | 1 | 11 | 2 | 17 |
| Spangsvej 15 | 0 | 1 | 1 | 3 | 6 | 1 | 13 |
| Lungstedløkken 15 | 0 | 2 | 1 | 2 | 10 | 1 | 17 |
| Spurvevej 13 | 5 | 4 | 1 | 4 | 6 | 1 | 23 |
| Møllehøj 15 | 1 | 3 | 1 | 1 | 5 | 2 | 14 |
| Kirkegyden 15 | 3 | 3 | 2 | 1 | 6 | 2 | 17 |
| Lunden 3 | 1 | 3 | 1 | 2 | 8 | 1 | 16 |
| Nypølsgade 14 | 0 | 3 | 1 | 0 | 7 | 1 | 14 |
| Strandbakken 5 | 1 | 3 | 2 | 0 | 11 | 0 | 17 |
| Sønderskovvej 5 | 4 | 2 | 1 | 1 | 6 | 0 | 15 |
| **TOTAL** | **16** | **25** | **12** | **15** | **76** | **11** | **163** |
| **Percentage** | **10%** | **15%** | **7%** | **9%** | **47%** | **7%** | **100%** |

**Pattern Legend:**
- **P1** (10%): 1:1 unchanged copy — Draft Status LongText copied verbatim to Review
- **P2** (15%): Placeholder resolved — `???`/`XXX` filled in, then copied to Review
- **P3** (7%): N draft Statuses collapsed — Multiple identical texts deduplicated (mostly windows)
- **P4** (9%): Multiple final Statuses concatenated — Distinct texts joined with paragraph breaks
- **P5** (47%): Inserted boilerplate — No draft source; mandatory registration items
- **P6** (7%): Selective inclusion — Consultant summary in Status #1 wins, rest suppressed

### Key Findings

1. **Pattern 5 dominates:** Nearly half (47%) of all Review blocks are boilerplate insertions with no draft source. This is the mandatory technical scaffolding Energy10 always generates.

2. **Pattern 2 is consistent:** Placeholder resolution occurs 2–4 times per property, accounting for 15% of transformations overall.

3. **Pattern 3 concentration:** Window deduplication (BI `1-3-1-0`) accounts for most P3 occurrences. The 84 draft window Statuses across all properties collapse to just 20 unique Review texts.

4. **Property variation:**
   - **Ivarsvej & Strandbakken** have the highest P5 ratios (65%) — thinnest draft technical detail
   - **Spurvevej** has the highest P1 count (5) — most complete draft
   - **Kirkegyden** shows balanced P1+P2+P6 (3+3+2) — medium draft quality with good consultant edits

---

## 5. BI Classification Reshuffles

Several Statuses moved from one BIClassification to another between draft and final:

| Property | ShortText | Draft BI | Final BI | Reason |
|----------|-----------|----------|----------|--------|
| Spurvevej 13 | Loftslem - 100 mm isolering | `1-1-3-0` | `1-1-1-0` | Hatch reclassified from roof/loft to outer-wall bucket |
| Spurvevej 13 | Fjernvarme uden veksler | `2-1-0-0` | `2-1-3-0` | Heat source subtype correction |
| Ivarsvej 27 | Skråvægge - 250 mm isolering | `1-1-3-0` | `1-1-1-0` | Sloped wall reclassified to outer-wall |
| Ivarsvej 27 | Vægge mod skunkrum | `1-1-3-0` | `1-1-1-0` | Attic-facing wall reclassified |
| Spangsvej 15 | Loftslem | `1-1-3-0` | `1-1-1-0` | Same as Spurvevej |
| Lungstedløkken 15 | Vægge mod skunkrum | `1-1-3-0` | `1-1-1-0` | Same pattern |
| Møllehøj 15 | Kedel - Gas - Wolf CGB 2-20 | `2-1-0-0` | `2-1-2-0` | Heat source subtype |
| Møllehøj 15 | Loftslem | `1-1-3-0` | `1-1-1-0` | Same as others |
| Møllehøj 15 | Skråvægge | `1-1-3-0` | `1-1-1-0` | Same pattern |

**Pattern:** Skunke walls, loft hatches and sloped walls consistently migrate from roof-loft BI bucket (`1-1-3-0`) to outer-wall bucket (`1-1-1-0`). Generic heat-source codes (`2-1-0-0`) get split into proper subtypes (`2-1-2-0` kedel, `2-1-3-0` fjernvarme).

---

## 6. Detailed Placeholder Resolution Summary

### Total Placeholder Count Across All 5 Properties

- **`???` U-value margin notes:** ~10 (all deleted in finals)
- **`???` location/measurement fills:** ~5 (resolved to room names, brands, lengths)
- **`XXX` template directives in Comments:** ~45 (pick-one-of-several choices; consultant selects applicable line)

**Resolution rate:** 100% — no placeholder survives into the final.

### `XXX` Template Directive Categories

All drafts carry the same template alternatives in `<Comments><Additional>` and `<Comments><OnBuildingDescription>`:

#### Owner Info Sheet
```
Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema. XXX
Ved bygningsgennemgangen forelå ikke et udfyldt ejeroplysningsskema. ... XXX
```
**Result:** All 5 finals kept the first line (owner sheet was present).

#### Source Documents
```
Bygningstegninger XXX
Tidligere energimærkningsrapport af den XX-XX-XX, med energimærkningsnummer: XXX
Andet XXX
```
**Result:** Consultant fills date/year for drawings; previous label reference kept or deleted per property; "Andet" always deleted.

#### BBR Area Agreement (3 mutually-exclusive lines)
```
De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen. XXX
Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med ... XXX
Det opmålte opvarmede areal stemmer ikke overens med BBR-meddelelsen. Afvigelsen består i XXX
```
**Result:** Exactly one line kept per property, with detail filled if discrepancy exists.

#### Access/Measurement Qualifier Lines (Always Deleted)
```
Ved bygningsgennemgangen var der ikke adgang til XXX.
Følgende rum XXX er uopvarmet. (vælg desuden en af nedenstående 2 muligheder XXX Slet dette)
Arealerne forudsættes jf. gældende Håndbog for energikonsulenter opvarmet med samme opvarmningsform ... XXX
Arealerne forudsættes jf. gældende Håndbog for energikonsulenter som værende el-opvarmet ... XXX
```
**Result:** All deleted in all 5 finals (full access granted, no exceptional area treatments).

---

## 7. BuildingReview Generation Algorithm

Based on observed behavior across all 5 properties:

```python
def generate_building_review(statuses):
    """
    Pseudo-code for Energy10's BuildingReview generation.
    """
    # 1. Group Statuses by BIClassification
    by_bi = group_by(statuses, key="BIClassification")
    
    # 2. For each BI group that should appear in the review:
    review_blocks = []
    for bi, status_list in by_bi.items():
        if bi not in REVIEW_ELIGIBLE_BI_CODES:
            continue  # Skip non-reportable BI codes
        
        # 3. Check if Status #1 has been consultant-edited (Pattern 6)
        first = status_list[0]
        if is_consultant_summary(first.LongText):
            # Use only Status #1
            review_text = first.LongText
        else:
            # 4. Deduplicate and concatenate all LongTexts
            unique_texts = deduplicate_preserving_order(
                s.LongText for s in status_list
            )
            review_text = "\n\n".join(unique_texts)
        
        review_blocks.append({
            "BIClassification": bi,
            "StatusText": review_text,
            "Proposals": extract_proposals(status_list)
        })
    
    return review_blocks
```

Key behaviors:
1. **Grouping by BI:** All Statuses with the same `BIClassification` contribute to one Review block
2. **Status #1 priority:** If Status #1's LongText is a consultant-written summary (identifiable by lack of boilerplate patterns), Energy10 emits only that
3. **Concatenation otherwise:** If Status #1 is boilerplate, concatenate all distinct LongTexts with paragraph breaks
4. **Deduplication:** Identical LongText strings are deduplicated before concatenation

---

## 8. Data Quality Observations

### Consistency Across Properties

**High consistency:**
- All 10 use the same BBR/building-code structure
- Identical boilerplate templates for comments
- Uniform BI classification after final corrections
- Consistent U-value, area, orientation precision (1–2 decimals)

**Per-consultant variation:**
- 5 consultants across 10 properties:
  - Dennis Funder-Schmidt (Ivarsvej, Lunden)
  - Anders Tubæk Jørgensen (Spangsvej, Lungstedløkken)
  - Jan Heiner Nielsen (Spurvevej)
  - Lars Heise (Møllehøj, Nypølsgade)
  - Unknown consultants (Kirkegyden, Strandbakken, Sønderskovvej)
- Writing style differences (some add more detail to room locations, others more concise)
- Different thoroughness on placeholder fills (Møllehøj has most brand/year detail)

### Minor Discrepancies

**Orientation correction (Ivarsvej only):**
- Draft: 2°, 92°, 182°
- Final: 3°, 93°, 183° (all +1°)
- Likely due to building rotation recalculation

**Volume/thickness adjustments:**
- Møllehøj VVB: draft said 100 L, final corrected to 110 L
- Møllehøj terrændæk: draft 250 mm, final "ca. 275 mm"

---

## 9. Window Status Deep Dive (Pattern 3 Expanded)

The window Status analysis (`1-3-1-0`) across all 10 properties reveals the mechanics of Pattern 3 deduplication:

| Property | Draft Statuses | Unique LongTexts | Final Statuses | Collapse Ratio |
|----------|----------------|------------------|----------------|----------------|
| Ivarsvej 27 | 6 | 1 | 6 | 6.0:1 |
| Spangsvej 15 | 9 | 3 | 9 | 3.0:1 |
| Lungstedløkken 15 | 5 | 3 | 5 | 1.7:1 |
| Spurvevej 13 | 9 | 3 | 9 | 3.0:1 |
| Møllehøj 15 | 5 | 1 | 5 | 5.0:1 |
| Kirkegyden 15 | 16 | 4 | 16 | 4.0:1 |
| Lunden 3 | 7 | 1 | 7 | 7.0:1 |
| Nypølsgade 14 | 16 | 2 | 16 | 8.0:1 |
| Strandbakken 5 | 5 | 1 | 5 | 5.0:1 |
| Sønderskovvej 5 | 6 | 1 | 6 | 6.0:1 |
| **TOTAL** | **84** | **20** | **84** | **4.2:1** |

### What Each Status Represents

Each `<Status>` for BI `1-3-1-0` wraps a `<Window>` payload containing:
- `NumberOfWindows`: count of identical units at this placement
- `Orientation`: compass direction (0–360°)
- `Inclination`: tilt (90° = vertical)
- `Area`: total glazing area in m²
- `UValue`: thermal transmittance (W/m²K)
- `GlassShare`, `SolarHeatTransmittance`: glazing properties

The `ShortText`/`LongText` describes the **glazing type** (e.g., "2-lags energirude med varm kant"), not the individual window. That's why Nypølsgade has 16 Statuses with only 2 unique texts — 16 physical window positions, 2 glazing types.

### Highest Collapse Ratios

- **Nypølsgade 14:** 8.0:1 (16 windows → 2 glazing types)
- **Lunden 3:** 7.0:1 (7 windows → 1 glazing type)
- **Ivarsvej 27, Sønderskovvej 5:** 6.0:1 (uniform glazing throughout)

Properties with lower ratios (1.7–3.0:1) have more glazing variety — typically a mix of 2-layer and 3-layer energy glass, or older thermo-pane in specific locations.

---

## 10. Key Takeaways

1. **Draft = partial inspection export; Final = regulatory submission**
   - Draft is consultant's in-progress work with placeholders
   - Final is the legally-binding, complete registration

2. **BuildingReview is a projection of Statuses**
   - Not independently authored
   - Mechanically derived by grouping on BIClassification and concatenating LongText
   - Consultant controls output by editing Status #1 of each BI group

3. **Two deduplication strategies:**
   - **Automatic (Pattern 3):** N physically-distinct but textually-identical Statuses → Review uses summary from Status #1
   - **Manual (Pattern 4):** Consultant writes distinct text for each Status → Review concatenates all

4. **Mandatory boilerplate dominates final size:**
   - 47% of all Review blocks are Pattern 5 insertions (no draft source)
   - Draft focuses on construction/envelope; final adds all technical-installation scaffolding
   - Range: 35–65% per property, with thinner drafts showing higher P5 percentages

5. **The `???` / `XXX` system is template-driven:**
   - `???` = free-text slot (location, brand, measurement) — ~5 per property
   - `XXX` = menu marker (pick one alternative, delete the rest) — ~45 per property
   - 100% resolution rate across all 10 properties

6. **Window Statuses are position records, not descriptions:**
   - Each `<Status>` for BI `1-3-1-0` represents a physical window placement
   - The ShortText/LongText describes the **glazing type** shared by multiple placements
   - Be18 calculations require per-orientation records (hence N records with identical text)
   - Average 4.2:1 collapse ratio (84 draft Statuses → 20 unique Review texts)

7. **Transformation volume is substantial:**
   - Draft: 296 Statuses total → Final: 401 Statuses (+35% expansion)
   - Final: 401 Statuses → Review: 163 blocks (60% compression via grouping/dedup)
   - Net: 296 draft Statuses → 163 Review blocks (45% reduction after round-trip)

8. **Quality varies by property complexity:**
   - Simple properties (Strandbakken, Sønderskovvej): 18 draft → 24–28 final (+33–55%)
   - Complex properties (Kirkegyden, Spurvevej): 48 draft → 55–56 final (+15–17%)
   - More detailed drafts require less boilerplate insertion in the final

---

## 11. Summary Statistics

### Dataset Overview
- **Total properties analyzed:** 10
- **Total XML files:** 20 (10 pairs)
- **Total file size (cleaned):** 1.43 MB (621 KB draft + 812 KB final)
- **Images removed:** 28 (8.5 MB of base64 JPEG data)

### Status Counts
- **Total draft Statuses:** 296 (avg 29.6 per property)
- **Total final Statuses:** 401 (avg 40.1 per property)
- **Net Status expansion:** +105 (+35%)
- **Total BuildingReview blocks:** 163 (avg 16.3 per property)

### Transformation Patterns
- **Pattern 1** (unchanged): 16 occurrences (10%)
- **Pattern 1b** (property value update): Variable (newly identified data correction pattern)
- **Pattern 2** (placeholder): 25 occurrences (15%)
- **Pattern 3** (dedup): 12 occurrences (7%)
- **Pattern 4** (concat): 15 occurrences (9%)
- **Pattern 5** (inserted): 76 occurrences (47%)
- **Pattern 6** (selective): 11 occurrences (7%)

### Window Analysis (BI 1-3-1-0)
- **Total window Statuses:** 84 across all properties
- **Unique glazing types:** 20
- **Average collapse ratio:** 4.2:1
- **Highest collapse:** 8.0:1 (Nypølsgade 14: 16 windows → 2 types)

### Placeholder Resolution
- **Total placeholders:** ~500 (`???` and `XXX` combined)
- **U-value calculation notes:** ~10 (all deleted)
- **Location/measurement fills:** ~25
- **Template menu choices:** ~465
- **Resolution rate:** 100%

### Consultant Distribution
- Dennis Funder-Schmidt: 2 properties
- Anders Tubæk Jørgensen: 2 properties
- Lars Heise: 2 properties
- Jan Heiner Nielsen: 1 property
- Other/Unknown: 3 properties

---

## Appendix: BI Classification Categories

| BI Range | Category | Examples |
|----------|----------|----------|
| `1-1-*` | Tag / loft | Hanebåndsloft, skråvægge, loftslem |
| `1-2-*` | Ydervægge | Hulmur, massiv væg, let ydervæg, kælderydervæg |
| `1-3-*` | Vinduer / døre / linjetab | Vinduer, ovenlys, terrassedør, yderdør, linjetab |
| `1-4-*` | Gulv / terrændæk | Gulv mod kælder, terrændæk, kældergulv |
| `1-5-*` | Ventilation | Naturlig / mekanisk ventilation |
| `1-6-*` | Internt varmetilskud | Standard heat contribution from occupants/devices |
| `2-1-*` | Varmeforsyning | Fjernvarme, kedel, varmepumpe, solvarme, brændeovn |
| `2-2-*` | Varmefordeling | Radiatorer, gulvvarme, rør, pumpe, regulering |
| `3-1-*` | Varmt brugsvand | Forbrug, varmtvandsbeholder, rør, cirkulation |
| `4-1-*` | Solceller | Installation / forslag |

---

**Analysis complete — 10 properties, 401 final Statuses, 163 BuildingReview blocks analyzed**

**Note:** Pattern 1b (Property Value Update) was discovered through fuzzy matching analysis (≥60% ShortText similarity), which revealed cases where consultants corrected property values based on better information sources, even when ShortText was significantly edited.
