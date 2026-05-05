# Plans XML vs Final XML — Comments Section Analysis

This report compares the four `<Comments>` sub-fields between each project's **Plans XML** (boilerplate template the consultant starts from) and its **Final XML** (after the consultant has filled it in). For every consultant-added line we look at whether its facts (years, areas, building type, heat source, room/story features) are already present in **upstream structured data** and could therefore be auto-populated.

**Valid auto-populate sources** (upstream of the consultant):
- **Plans XML** — `BBR.YearOfConstruction`, `BBR.YearOfRenovation`,   `BBR.DwellingArea`, `BBR.CommercialArea`, `Zone.BuildingType`,   `Zone.FloorCount`, `Zone.HousingUnits`
- **JSON room-by-room model** — `heating.sources[].sourceType`,   `stories[].storyType`, `stories[].rooms[].roomType` / `roomName`

Final XML is **not** used as a source: it is the consultant's output, so any field present only in Final cannot count as auto-populatable.

**Comment fields analysed:**
- `Additional` — general legal/explanatory text
- `OnEnergyPrices` — text about energy price assumptions
- `OnBuildingDescription` — building summary, areas, year, accessed rooms
- `OnDestructiveInspections` — destructive inspection text

**Legend for hits inside added lines:**
- ✅ value present in Plans XML or JSON (auto-populatable today)
- ❌ value detected but not found in upstream data (would need extra source or consultant input)

---

## Aggregate scoreboard (10 projects)

- Consultant-added lines analysed: **71**
- Lines with at least one auto-populatable token: **26**
- Tokens detected: **52**
- Tokens already covered by structured data: **35** (67%)

### Hits by category

| Category | Detected | Auto-populatable | Coverage |
|---|---|---|---|
| Year | 15 | 9 | 60% |
| Heat source | 7 | 7 | 100% |
| Room/story feature | 12 | 8 | 67% |
| Area (m²) | 14 | 7 | 50% |
| Building type | 4 | 4 | 100% |

### Activity by Comments sub-field

| Field | Projects with edits | Lines added | Lines removed | Tokens detected | Auto-populatable | Coverage |
|---|---|---|---|---|---|---|
| `Additional` | 10/10 | 29 | 51 | 10 | 5 | 50% |
| `OnEnergyPrices` | 8/10 | 11 | 10 | 7 | 7 | 100% |
| `OnBuildingDescription` | 10/10 | 31 | 82 | 35 | 23 | 66% |
| `OnDestructiveInspections` | 0/10 | 0 | 0 | 0 | 0 | — |

### Takeaways

- `OnBuildingDescription` is where the consultant cites the most facts. The JSON `home.latestSnapshot.building` block already contains **everything** that goes into the typical opening sentence — `constructedYear`, `renovatedYear`, `dwellingAreaSquareMeters`, `heatedAreaSquareMeters`, `roofStoriesAreaSquareMeters` ("udnyttet tagetage"), `regularStoriesAreaSquareMeters`, `basementAreaSquareMeters`, `buildingType`, `numberOfStories`, `storyTypes`. So the entire phrase *"Bygningen er et fritliggende enfamilieshus med X m² udnyttet tagetage, opført i Y, med et opvarmet areal på Z m²"* is **fully auto-populatable from JSON**.
- `OnEnergyPrices` is dominated by heat-source mentions (`fjernvarme`, `træpiller`, …) which are derivable from `JSON.heating.primarySource.sourceType`. The specific supplier name (e.g. *"Fjernvarme Fyn"*) is NOT in our data and would need an external address-based lookup.
- `Additional` edits are mostly **boilerplate placeholder removals** (`XXX`-cleanup) plus small free-text references to previous energy reports. Reference numbers and dates are not in upstream data, but the placeholder cleanup itself is deterministic.
- `OnDestructiveInspections` is empty in every project.
- Free-text room features (e.g. `tagterrasse`, `udestue`, `udhus`) are NOT consistently in the JSON model. JSON would need richer room-type metadata to cover those.
- Several **standard phrases** are pasted verbatim across many projects (see _Repeated standard phrases_ section below). Promoting them to the Plans XML template — or at least to a pick-list — would remove the bulk of the consultant's manual editing in `Additional` and `OnBuildingDescription`.

---

## Repeated standard phrases

**9 distinct phrases** are reused across ≥2 projects, accounting for **32 of 71** consultant-added lines (45%). These are strong candidates for direct inclusion in the Plans XML boilerplate or a pick-list — the consultant is effectively copy-pasting them today.

Numbers/years/dates are masked as `<NUM>`, `<YEAR>`, `<DATE>`, `<ID>` so that lines differing only in those values group together. Click each phrase to see the per-project raw text.

### `Additional`

| # projects | Total occurrences | Auto-populatable | Normalized phrase |
|---|---|---|---|
| **8/10** | 8 | — | ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema. |
| **2/10** | 2 | — | udfyldt ejeroplysningsskema. |
| **2/10** | 2 | — | ved bygningsgennemgangen forelå der ingen tegningsmateriale eller bygningsbeskrivelser. |

<details><summary><code>ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema.</code> — 8 projects (Ivarsvej_27_5200_Odense_V, Kirkegyden_15_5270_Odense_N, Lunden_3_8464_Galten, Lungstedløkken_15_5250_Odense_SV, Spangsvej_15_5210_Odense_NV, Spurvevej_13_7100_Vejle, Strandbakken_5_5900_Rudkøbing, Sønderskovvej_5_5932_Humble)</summary>

- _Ivarsvej_27_5200_Odense_V_: Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema.

</details>

<details><summary><code>udfyldt ejeroplysningsskema.</code> — 2 projects (Møllehøj_15_6400_Sønderborg, Nypølsgade_14_6470_Sydals)</summary>

- _Møllehøj_15_6400_Sønderborg_: Udfyldt ejeroplysningsskema.

</details>

<details><summary><code>ved bygningsgennemgangen forelå der ingen tegningsmateriale eller bygningsbeskrivelser.</code> — 2 projects (Møllehøj_15_6400_Sønderborg, Nypølsgade_14_6470_Sydals)</summary>

- _Møllehøj_15_6400_Sønderborg_: Ved bygningsgennemgangen forelå der ingen tegningsmateriale eller bygningsbeskrivelser.

</details>

---

### `OnEnergyPrices`

| # projects | Total occurrences | Auto-populatable | Normalized phrase |
|---|---|---|---|
| **3/10** | 3 | ✅ all | fjernvarmeprisen er i denne rapport fastsat ud fra de tariffer, der var gældende ved energimærkningsrapportens officielle indberetningsdato. fjernvarmeprisen stammer fra det konkrete fjernvarmeværk… |

<details><summary><code>fjernvarmeprisen er i denne rapport fastsat ud fra de tariffer, der var gældende ved energimærkni…</code> — 3 projects (Ivarsvej_27_5200_Odense_V, Lungstedløkken_15_5250_Odense_SV, Spangsvej_15_5210_Odense_NV)</summary>

- _Ivarsvej_27_5200_Odense_V_: Fjernvarmeprisen er i denne rapport fastsat ud fra de tariffer, der var gældende ved energimærkningsrapportens officielle indberetningsdato. Fjernvarmeprisen stammer fra det konkrete fjernvarmeværk: Fjernvarme Fyn.

</details>

---

### `OnBuildingDescription`

| # projects | Total occurrences | Auto-populatable | Normalized phrase |
|---|---|---|---|
| **7/10** | 7 | — | ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og bygningstegninger. |
| **4/10** | 4 | — | de opmålte opvarmede arealer stemmer overens med bbr-meddelelsen. |
| **2/10** | 2 | — | ejendommen er kontrolopmålt af energikonsulenten. |
| **2/10** | 2 | — | det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med bbr-meddelelsen. |
| **2/10** | 2 | — | arealerne forudsættes jf. gældende håndbog for energikonsulenter opvarmet med samme opvarmningsform som resten af bygningen, uanset at der ingen varmekilde er, da det vurderes at eksisterende varme… |

<details><summary><code>ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og bygningstegninger.</code> — 7 projects (Ivarsvej_27_5200_Odense_V, Lunden_3_8464_Galten, Lungstedløkken_15_5250_Odense_SV, Spangsvej_15_5210_Odense_NV, Spurvevej_13_7100_Vejle, Strandbakken_5_5900_Rudkøbing, Sønderskovvej_5_5932_Humble)</summary>

- _Ivarsvej_27_5200_Odense_V_: Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og bygningstegninger.

</details>

<details><summary><code>de opmålte opvarmede arealer stemmer overens med bbr-meddelelsen.</code> — 4 projects (Ivarsvej_27_5200_Odense_V, Kirkegyden_15_5270_Odense_N, Strandbakken_5_5900_Rudkøbing, Sønderskovvej_5_5932_Humble)</summary>

- _Ivarsvej_27_5200_Odense_V_: De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen.

</details>

<details><summary><code>ejendommen er kontrolopmålt af energikonsulenten.</code> — 2 projects (Kirkegyden_15_5270_Odense_N, Nypølsgade_14_6470_Sydals)</summary>

- _Kirkegyden_15_5270_Odense_N_: Ejendommen er kontrolopmålt af energikonsulenten.

</details>

<details><summary><code>det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med bbr-meddelelsen.</code> — 2 projects (Møllehøj_15_6400_Sønderborg, Nypølsgade_14_6470_Sydals)</summary>

- _Møllehøj_15_6400_Sønderborg_: Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen.

</details>

<details><summary><code>arealerne forudsættes jf. gældende håndbog for energikonsulenter opvarmet med samme opvarmningsfo…</code> — 2 projects (Strandbakken_5_5900_Rudkøbing, Sønderskovvej_5_5932_Humble)</summary>

- _Strandbakken_5_5900_Rudkøbing_: Arealerne forudsættes jf. gældende Håndbog for energikonsulenter opvarmet med samme opvarmningsform som resten af bygningen, uanset at der ingen varmekilde er, da det vurderes at eksisterende varmeanlæg er tilstrækkelig til at kunne opvarme hele boligen

</details>

---

## Ivarsvej_27_5200_Odense_V

- Plans XML: `Ivarsvej_27_5200_Odense_V.xml`
- Final XML: `Ivarsvej_27_5200_Odense_V final.xml`
- JSON model: `Ivarsvej_27_5200_Odense_V.json`

### Structured facts

| Fact | Value | Source |
|---|---|---|
| Year of construction (Plans BBR) | 1952 | Plans XML BBR.YearOfConstruction |
| Year of construction (JSON) | 1952 | JSON building.constructedYear |
| Year of renovation (Plans BBR) | _(missing)_ | Plans XML BBR.YearOfRenovation |
| Year of renovation (JSON) | _(missing)_ | JSON building.renovatedYear |
| Dwelling area (Plans BBR) | 144 | Plans XML BBR.DwellingArea |
| Dwelling area (JSON) | 144 | JSON building.dwellingAreaSquareMeters |
| Heated area (JSON) | 144 | JSON building.heatedAreaSquareMeters |
| Roof stories area (JSON) | 67 | JSON building.roofStoriesAreaSquareMeters |
| Regular stories area (JSON) | 77 | JSON building.regularStoriesAreaSquareMeters |
| Basement area (JSON) | 77 | JSON building.basementAreaSquareMeters |
| Number of stories (JSON) | 1 | JSON building.numberOfStories |
| Floor count (Plans Zone) | 1 | Plans XML Zone.FloorCount |
| Building type (Plans Zone) | fritliggende enfamilieshus | Mapped from Plans Zone.BuildingType |
| Building type (JSON) | fritliggende enfamilieshus | Mapped from JSON building.buildingType |
| Heat source (JSON) | Fjernvarme | Mapped from JSON heat source |
| Story types (JSON building) | ground, basement | JSON building.storyTypes |
| Stories localised (JSON walk) | _(missing)_ | JSON model.stories[].storyType |
| # rooms (JSON walk) | _(missing)_ | JSON model.stories[].rooms[] |
| Has loft (JSON) | _(missing)_ | JSON building.storyTypes (loft/attic) |
| Has basement (JSON) | True | JSON building.storyTypes (basement) |
| Has workshop (JSON) | _(missing)_ | JSON rooms with workshop/værksted |
| Has garage (JSON) | _(missing)_ | JSON rooms with garage |

### `Additional` (Plans: 2648 chars → Final: 2485 chars · +3/-5 lines)

**Consultant-added lines & auto-populate analysis:**

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema.
  - _no auto-populatable values detected_
- Bygningstegninger 1951
  - ❌ **Year**: `1951` (source: `?`)
- Tidligere energimærkningsrapport af den 11. maj 2022, med energimærkningsnummer: 311599521
  - ❌ **Year**: `2022` (source: `?`)

<details><summary>Lines removed from boilerplate (5)</summary>

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema. XXX
- Ved bygningsgennemgangen forelå ikke et udfyldt ejeroplysningsskema. Det forudsættes hermed, at der ikke er givet tilladelse til destruktive undersøgelser. XXX
- Bygningstegninger XXX
- Tidligere energimærkningsrapport af den XX-XX-XX, med energimærkningsnummer: XXX
- _(…1 more…)_

</details>

### `OnEnergyPrices` (Plans: 705 chars → Final: 935 chars · +4/-3 lines)

**Consultant-added lines & auto-populate analysis:**

- Der er i energimærket anvendt aktuelle energipriser for alle brændselstyper fx fjernvarme, olie, naturgas, brænde og træpiller.
  - ✅ **Heat source**: `fjernvarme` (source: `JSON.heating.primarySource.sourceType`)
- Rapportens elpris er anvendt ud fra en gennemsnits vurdering, da energipriserne varierer dagligt og i forhold til valg af leverandør.
  - _no auto-populatable values detected_
- I forbindelse med rapportens forslag om energiforbedringer, bør man altid søge sparring med en professionel rådgiver eller leverandør.
  - _no auto-populatable values detected_
- Fjernvarmeprisen er i denne rapport fastsat ud fra de tariffer, der var gældende ved energimærkningsrapportens officielle indberetningsdato. Fjernvarmeprisen stammer fra det konkrete fjernvarmeværk: Fjernvarme Fyn.
  - ✅ **Heat source**: `fjernvarme` (source: `JSON.heating.primarySource.sourceType`)

<details><summary>Lines removed from boilerplate (3)</summary>

- Der er i energimærket anvendt aktuelle energipriser for alle brændselstyper fx olie, naturgas, brænde og træpiller.
- Rapportens elpris er anvendt ud fra en gennemsnitsvurdering, da energipriserne varierer dagligt og i forhold til valg af leverandør.
- I forbindelse med rapportens forslag om energiforbedringer, bør man altid søge  sparring med en professionel rådgiver eller leverandør.

</details>

### `OnBuildingDescription` (Plans: 1377 chars → Final: 577 chars · +2/-8 lines)

**Consultant-added lines & auto-populate analysis:**

- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og bygningstegninger.
  - _no auto-populatable values detected_
- De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen.
  - _no auto-populatable values detected_

<details><summary>Lines removed from boilerplate (8)</summary>

- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og XXX bygningstegninger.
- De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer ikke overens med BBR-meddelelsen. Afvigelsen består i XXX
- _(…4 more…)_

</details>

### `OnDestructiveInspections` (Plans: 0 chars → Final: 0 chars · +0/-0 lines)

**Consultant-added lines & auto-populate analysis:**

_(no consultant-added lines)_

---

## Kirkegyden_15_5270_Odense_N

- Plans XML: `Kirkegyden_15_5270_Odense_N.xml`
- Final XML: `Kirkegyden_15_5270_Odense_N final.xml`
- JSON model: `Kirkegyden_15_5270_Odense_N.json`

### Structured facts

| Fact | Value | Source |
|---|---|---|
| Year of construction (Plans BBR) | 1900 | Plans XML BBR.YearOfConstruction |
| Year of construction (JSON) | 1900 | JSON building.constructedYear |
| Year of renovation (Plans BBR) | _(missing)_ | Plans XML BBR.YearOfRenovation |
| Year of renovation (JSON) | _(missing)_ | JSON building.renovatedYear |
| Dwelling area (Plans BBR) | 284 | Plans XML BBR.DwellingArea |
| Dwelling area (JSON) | 284 | JSON building.dwellingAreaSquareMeters |
| Heated area (JSON) | 284 | JSON building.heatedAreaSquareMeters |
| Roof stories area (JSON) | 0 | JSON building.roofStoriesAreaSquareMeters |
| Regular stories area (JSON) | 483 | JSON building.regularStoriesAreaSquareMeters |
| Basement area (JSON) | 7 | JSON building.basementAreaSquareMeters |
| Number of stories (JSON) | 1 | JSON building.numberOfStories |
| Floor count (Plans Zone) | 1 | Plans XML Zone.FloorCount |
| Building type (Plans Zone) | fritliggende enfamilieshus | Mapped from Plans Zone.BuildingType |
| Building type (JSON) | fritliggende enfamilieshus | Mapped from JSON building.buildingType |
| Heat source (JSON) | Fjernvarme | Mapped from JSON heat source |
| Story types (JSON building) | basement, ground | JSON building.storyTypes |
| Stories localised (JSON walk) | _(missing)_ | JSON model.stories[].storyType |
| # rooms (JSON walk) | _(missing)_ | JSON model.stories[].rooms[] |
| Has loft (JSON) | _(missing)_ | JSON building.storyTypes (loft/attic) |
| Has basement (JSON) | True | JSON building.storyTypes (basement) |
| Has workshop (JSON) | _(missing)_ | JSON rooms with workshop/værksted |
| Has garage (JSON) | _(missing)_ | JSON rooms with garage |

### `Additional` (Plans: 2648 chars → Final: 2462 chars · +2/-5 lines)

**Consultant-added lines & auto-populate analysis:**

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema.
  - _no auto-populatable values detected_
- Tidligere energimærkningsrapport af den 18-10-2007, med energimærkningsnummer: 100051936
  - ❌ **Year**: `2007` (source: `?`)

<details><summary>Lines removed from boilerplate (5)</summary>

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema. XXX
- Ved bygningsgennemgangen forelå ikke et udfyldt ejeroplysningsskema. Det forudsættes hermed, at der ikke er givet tilladelse til destruktive undersøgelser. XXX
- Bygningstegninger XXX
- Tidligere energimærkningsrapport af den XX-XX-XX, med energimærkningsnummer: XXX
- _(…1 more…)_

</details>

### `OnEnergyPrices` (Plans: 705 chars → Final: 705 chars · +0/-0 lines)

**Consultant-added lines & auto-populate analysis:**

_(no consultant-added lines)_

### `OnBuildingDescription` (Plans: 1377 chars → Final: 537 chars · +2/-8 lines)

**Consultant-added lines & auto-populate analysis:**

- Ejendommen er kontrolopmålt af energikonsulenten.
  - _no auto-populatable values detected_
- De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen.
  - _no auto-populatable values detected_

<details><summary>Lines removed from boilerplate (8)</summary>

- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og XXX bygningstegninger.
- De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer ikke overens med BBR-meddelelsen. Afvigelsen består i XXX
- _(…4 more…)_

</details>

### `OnDestructiveInspections` (Plans: 0 chars → Final: 0 chars · +0/-0 lines)

**Consultant-added lines & auto-populate analysis:**

_(no consultant-added lines)_

---

## Lunden_3_8464_Galten

- Plans XML: `Lunden_3_8464_Galten.xml`
- Final XML: `Lunden_3_8464_Galten final.xml`
- JSON model: `Lunden_3_8464_Galten.json`

### Structured facts

| Fact | Value | Source |
|---|---|---|
| Year of construction (Plans BBR) | 1969 | Plans XML BBR.YearOfConstruction |
| Year of construction (JSON) | 1969 | JSON building.constructedYear |
| Year of renovation (Plans BBR) | 1976 | Plans XML BBR.YearOfRenovation |
| Year of renovation (JSON) | 1976 | JSON building.renovatedYear |
| Dwelling area (Plans BBR) | 146 | Plans XML BBR.DwellingArea |
| Dwelling area (JSON) | 146 | JSON building.dwellingAreaSquareMeters |
| Heated area (JSON) | 146 | JSON building.heatedAreaSquareMeters |
| Roof stories area (JSON) | 0 | JSON building.roofStoriesAreaSquareMeters |
| Regular stories area (JSON) | 146 | JSON building.regularStoriesAreaSquareMeters |
| Basement area (JSON) | 0 | JSON building.basementAreaSquareMeters |
| Number of stories (JSON) | 1 | JSON building.numberOfStories |
| Floor count (Plans Zone) | 1 | Plans XML Zone.FloorCount |
| Building type (Plans Zone) | fritliggende enfamilieshus | Mapped from Plans Zone.BuildingType |
| Building type (JSON) | fritliggende enfamilieshus | Mapped from JSON building.buildingType |
| Heat source (JSON) | Fjernvarme | Mapped from JSON heat source |
| Story types (JSON building) | ground | JSON building.storyTypes |
| Stories localised (JSON walk) | _(missing)_ | JSON model.stories[].storyType |
| # rooms (JSON walk) | _(missing)_ | JSON model.stories[].rooms[] |
| Has loft (JSON) | _(missing)_ | JSON building.storyTypes (loft/attic) |
| Has basement (JSON) | _(missing)_ | JSON building.storyTypes (basement) |
| Has workshop (JSON) | _(missing)_ | JSON rooms with workshop/værksted |
| Has garage (JSON) | _(missing)_ | JSON rooms with garage |

### `Additional` (Plans: 2648 chars → Final: 2794 chars · +4/-5 lines)

**Consultant-added lines & auto-populate analysis:**

- Ejendommen er oprindeligt fra 1969, med en tilbygning i 1976. Størstedelen af klimaskærmen, herunder gulve og ydervægge, står som ved opførelsen. Loftrummet er blevet efterisoleret og der er skiftet vinduer i hele ejendommen.
  - ✅ **Year**: `1969` (source: `Plans BBR.YearOfConstruction / JSON building.constructedYear`)
  - ✅ **Year**: `1976` (source: `Plans BBR.YearOfRenovation / JSON building.renovatedYear`)
  - ❌ **Room/story feature**: `loft` (source: `?`)
- Der kunne ved besigtigelsen ikke lokaliseres styring af gulvvarme i badeværelse. Men da gulvet var varmt er der ingen tvivl om der er gulvvarme.
  - _no auto-populatable values detected_
- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema.
  - _no auto-populatable values detected_
- Bygningstegninger fra opførelsen og tilbygningen.
  - _no auto-populatable values detected_

<details><summary>Lines removed from boilerplate (5)</summary>

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema. XXX
- Ved bygningsgennemgangen forelå ikke et udfyldt ejeroplysningsskema. Det forudsættes hermed, at der ikke er givet tilladelse til destruktive undersøgelser. XXX
- Bygningstegninger XXX
- Tidligere energimærkningsrapport af den XX-XX-XX, med energimærkningsnummer: XXX
- _(…1 more…)_

</details>

### `OnEnergyPrices` (Plans: 705 chars → Final: 815 chars · +1/-1 lines)

**Consultant-added lines & auto-populate analysis:**

- Fjernvarmeprisen er i denne rapport fastsat ud fra de tariffer, der var gældende ved energimærkningsrapportens officielle indberetningsdato. Fjernvarmeprisen stammer fra det konkrete fjernvarmeværk: Galten Varmeværk A.m.b.a.
  - ✅ **Heat source**: `fjernvarme` (source: `JSON.heating.primarySource.sourceType`)

<details><summary>Lines removed from boilerplate (1)</summary>

- Der er i energimærket anvendt aktuelle energipriser for alle brændselstyper fx olie, naturgas, brænde og træpiller.

</details>

### `OnBuildingDescription` (Plans: 1377 chars → Final: 700 chars · +2/-8 lines)

**Consultant-added lines & auto-populate analysis:**

- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og bygningstegninger.
  - _no auto-populatable values detected_
- Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen, hvilket skønnes den oprindelige del er både lidt kortere og smallere end oplyst i tegningsmateriale.
  - _no auto-populatable values detected_

<details><summary>Lines removed from boilerplate (8)</summary>

- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og XXX bygningstegninger.
- De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer ikke overens med BBR-meddelelsen. Afvigelsen består i XXX
- _(…4 more…)_

</details>

### `OnDestructiveInspections` (Plans: 0 chars → Final: 0 chars · +0/-0 lines)

**Consultant-added lines & auto-populate analysis:**

_(no consultant-added lines)_

---

## Lungstedløkken_15_5250_Odense_SV

- Plans XML: `Lungstedløkken_15_5250_Odense_SV.xml`
- Final XML: `Lungstedløkken_15_5250_Odense_SV final.xml`
- JSON model: `Lungstedløkken_15_5250_Odense_SV.json`

### Structured facts

| Fact | Value | Source |
|---|---|---|
| Year of construction (Plans BBR) | 1976 | Plans XML BBR.YearOfConstruction |
| Year of construction (JSON) | 1976 | JSON building.constructedYear |
| Year of renovation (Plans BBR) | 1984 | Plans XML BBR.YearOfRenovation |
| Year of renovation (JSON) | 1984 | JSON building.renovatedYear |
| Dwelling area (Plans BBR) | 177 | Plans XML BBR.DwellingArea |
| Dwelling area (JSON) | 177 | JSON building.dwellingAreaSquareMeters |
| Heated area (JSON) | 177 | JSON building.heatedAreaSquareMeters |
| Roof stories area (JSON) | 77 | JSON building.roofStoriesAreaSquareMeters |
| Regular stories area (JSON) | 100 | JSON building.regularStoriesAreaSquareMeters |
| Basement area (JSON) | 0 | JSON building.basementAreaSquareMeters |
| Number of stories (JSON) | 1 | JSON building.numberOfStories |
| Floor count (Plans Zone) | 1 | Plans XML Zone.FloorCount |
| Building type (Plans Zone) | fritliggende enfamilieshus | Mapped from Plans Zone.BuildingType |
| Building type (JSON) | fritliggende enfamilieshus | Mapped from JSON building.buildingType |
| Heat source (JSON) | Fjernvarme | Mapped from JSON heat source |
| Story types (JSON building) | first, ground | JSON building.storyTypes |
| Stories localised (JSON walk) | _(missing)_ | JSON model.stories[].storyType |
| # rooms (JSON walk) | _(missing)_ | JSON model.stories[].rooms[] |
| Has loft (JSON) | _(missing)_ | JSON building.storyTypes (loft/attic) |
| Has basement (JSON) | _(missing)_ | JSON building.storyTypes (basement) |
| Has workshop (JSON) | _(missing)_ | JSON rooms with workshop/værksted |
| Has garage (JSON) | _(missing)_ | JSON rooms with garage |

### `Additional` (Plans: 2648 chars → Final: 2506 chars · +3/-5 lines)

**Consultant-added lines & auto-populate analysis:**

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema.
  - _no auto-populatable values detected_
- Bygningstegninger fra opførelsen dateret 1976.
  - ✅ **Year**: `1976` (source: `Plans BBR.YearOfConstruction / JSON building.constructedYear`)
- Tidligere energimærkningsrapport af den 22-03-16, med energimærkningsnummer: 311166410
  - _no auto-populatable values detected_

<details><summary>Lines removed from boilerplate (5)</summary>

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema. XXX
- Ved bygningsgennemgangen forelå ikke et udfyldt ejeroplysningsskema. Det forudsættes hermed, at der ikke er givet tilladelse til destruktive undersøgelser. XXX
- Bygningstegninger XXX
- Tidligere energimærkningsrapport af den XX-XX-XX, med energimærkningsnummer: XXX
- _(…1 more…)_

</details>

### `OnEnergyPrices` (Plans: 705 chars → Final: 804 chars · +1/-1 lines)

**Consultant-added lines & auto-populate analysis:**

- Fjernvarmeprisen er i denne rapport fastsat ud fra de tariffer, der var gældende ved energimærkningsrapportens officielle indberetningsdato. Fjernvarmeprisen stammer fra det konkrete fjernvarmeværk: Fjernvarme Fyn.
  - ✅ **Heat source**: `fjernvarme` (source: `JSON.heating.primarySource.sourceType`)

<details><summary>Lines removed from boilerplate (1)</summary>

- Der er i energimærket anvendt aktuelle energipriser for alle brændselstyper fx olie, naturgas, brænde og træpiller.

</details>

### `OnBuildingDescription` (Plans: 1377 chars → Final: 882 chars · +3/-8 lines)

**Consultant-added lines & auto-populate analysis:**

- Bygningen er et fritliggende enfamilieshus med 77 m² udnyttet tagetage, opført i 1976, med et opvarmet areal på 177 m².  Ejendommen har gennemgået diverse isoleringsarbejde gennem tiden.
  - ✅ **Year**: `1976` (source: `Plans BBR.YearOfConstruction / JSON building.constructedYear`)
  - ✅ **Area (m²)**: `77 m²` (source: `JSON building.roofStoriesAreaSquareMeters`)
  - ✅ **Area (m²)**: `177 m²` (source: `Plans BBR.DwellingArea`)
  - ✅ **Building type**: `fritliggende enfamilieshus` (source: `Plans Zone.BuildingType`)
  - ✅ **Room/story feature**: `tagetage` (source: `JSON building.roofStoriesAreaSquareMeters&gt;0`)
- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og bygningstegninger.
  - _no auto-populatable values detected_
- Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen. Overetagen er opmålt lidt mindre. Skønnes at være grundet tagterrasse er medregnet i beboelse.
  - ❌ **Room/story feature**: `tagterrasse` (source: `?`)

<details><summary>Lines removed from boilerplate (8)</summary>

- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og XXX bygningstegninger.
- De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer ikke overens med BBR-meddelelsen. Afvigelsen består i XXX
- _(…4 more…)_

</details>

### `OnDestructiveInspections` (Plans: 0 chars → Final: 0 chars · +0/-0 lines)

**Consultant-added lines & auto-populate analysis:**

_(no consultant-added lines)_

---

## Møllehøj_15_6400_Sønderborg

- Plans XML: `Møllehøj_15_6400_Sønderborg plans.xml`
- Final XML: `Møllehøj_15_6400_Sønderborg final.xml`
- JSON model: `Møllehøj_15_6400_Sønderborg.json`

### Structured facts

| Fact | Value | Source |
|---|---|---|
| Year of construction (Plans BBR) | 2008 | Plans XML BBR.YearOfConstruction |
| Year of construction (JSON) | 2008 | JSON building.constructedYear |
| Year of renovation (Plans BBR) | _(missing)_ | Plans XML BBR.YearOfRenovation |
| Year of renovation (JSON) | _(missing)_ | JSON building.renovatedYear |
| Dwelling area (Plans BBR) | 135 | Plans XML BBR.DwellingArea |
| Dwelling area (JSON) | 135 | JSON building.dwellingAreaSquareMeters |
| Heated area (JSON) | 135 | JSON building.heatedAreaSquareMeters |
| Roof stories area (JSON) | 0 | JSON building.roofStoriesAreaSquareMeters |
| Regular stories area (JSON) | 135 | JSON building.regularStoriesAreaSquareMeters |
| Basement area (JSON) | 0 | JSON building.basementAreaSquareMeters |
| Number of stories (JSON) | 1 | JSON building.numberOfStories |
| Floor count (Plans Zone) | 1 | Plans XML Zone.FloorCount |
| Building type (Plans Zone) | fritliggende enfamilieshus | Mapped from Plans Zone.BuildingType |
| Building type (JSON) | fritliggende enfamilieshus | Mapped from JSON building.buildingType |
| Heat source (JSON) | naturalGasBoiler | Mapped from JSON heat source |
| Story types (JSON building) | ground | JSON building.storyTypes |
| Stories localised (JSON walk) | _(missing)_ | JSON model.stories[].storyType |
| # rooms (JSON walk) | _(missing)_ | JSON model.stories[].rooms[] |
| Has loft (JSON) | _(missing)_ | JSON building.storyTypes (loft/attic) |
| Has basement (JSON) | _(missing)_ | JSON building.storyTypes (basement) |
| Has workshop (JSON) | _(missing)_ | JSON rooms with workshop/værksted |
| Has garage (JSON) | _(missing)_ | JSON rooms with garage |

### `Additional` (Plans: 2648 chars → Final: 2720 chars · +5/-5 lines)

**Consultant-added lines & auto-populate analysis:**

- Udfyldt ejeroplysningsskema.
  - _no auto-populatable values detected_
- Snit- og plantegninger fra 2008.
  - ✅ **Year**: `2008` (source: `Plans BBR.YearOfConstruction / JSON building.constructedYear`)
- Ved bygningsgennemgangen forelå der ingen tegningsmateriale eller bygningsbeskrivelser.
  - _no auto-populatable values detected_
- Det oplyste varmeforbrug stammer fra ejer, og er udelukkende oplyst i kr., hvorfor der ved enheder fremgår 0.
  - _no auto-populatable values detected_
- Udgifter til oplyst varmeforbrug er registeret som variable udgifter, da der ikke foreligger en opgørelse, hvor de faste udgifter er udspecificeret.
  - _no auto-populatable values detected_

<details><summary>Lines removed from boilerplate (5)</summary>

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema. XXX
- Ved bygningsgennemgangen forelå ikke et udfyldt ejeroplysningsskema. Det forudsættes hermed, at der ikke er givet tilladelse til destruktive undersøgelser. XXX
- Bygningstegninger XXX
- Tidligere energimærkningsrapport af den XX-XX-XX, med energimærkningsnummer: XXX
- _(…1 more…)_

</details>

### `OnEnergyPrices` (Plans: 705 chars → Final: 705 chars · +0/-0 lines)

**Consultant-added lines & auto-populate analysis:**

_(no consultant-added lines)_

### `OnBuildingDescription` (Plans: 1377 chars → Final: 641 chars · +4/-9 lines)

**Consultant-added lines & auto-populate analysis:**

- Bygningen er et fritliggende enfamilieshus, opført i 2008 med et opvarmet areal på 133 m². Ejendommen er traditionelt isoleret udfra det gældende bygningsreglement på opførelsestidspunktet.
  - ✅ **Year**: `2008` (source: `Plans BBR.YearOfConstruction / JSON building.constructedYear`)
  - ❌ **Area (m²)**: `133 m²` (source: `?`)
  - ✅ **Building type**: `fritliggende enfamilieshus` (source: `Plans Zone.BuildingType`)
- Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen.
  - _no auto-populatable values detected_
- Det samlede boligareal i BBR-Oversigt er angivet til 135 m². I henhold til vor opmåling er opvarmet areal 133 m².
  - ✅ **Area (m²)**: `135 m²` (source: `Plans BBR.DwellingArea`)
  - ❌ **Area (m²)**: `133 m²` (source: `?`)
- Udestuen er ikke medregnet i det opvarmede areal jf. ”Håndbog for energikonsulenter”, da den er uopvarmet.
  - ❌ **Room/story feature**: `udestue` (source: `?`)

<details><summary>Lines removed from boilerplate (9)</summary>

- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og XXX bygningstegninger.
- De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer ikke overens med BBR-meddelelsen. Afvigelsen består i XXX
- _(…5 more…)_

</details>

### `OnDestructiveInspections` (Plans: 0 chars → Final: 0 chars · +0/-0 lines)

**Consultant-added lines & auto-populate analysis:**

_(no consultant-added lines)_

---

## Nypølsgade_14_6470_Sydals

- Plans XML: `Nypølsgade_14_6470_Sydals.xml`
- Final XML: `Nypølsgade_14_6470_Sydals final.xml`
- JSON model: `Nypølsgade_14_6470_Sydals.json`

### Structured facts

| Fact | Value | Source |
|---|---|---|
| Year of construction (Plans BBR) | 1800 | Plans XML BBR.YearOfConstruction |
| Year of construction (JSON) | 1800 | JSON building.constructedYear |
| Year of renovation (Plans BBR) | _(missing)_ | Plans XML BBR.YearOfRenovation |
| Year of renovation (JSON) | _(missing)_ | JSON building.renovatedYear |
| Dwelling area (Plans BBR) | 190 | Plans XML BBR.DwellingArea |
| Dwelling area (JSON) | 190 | JSON building.dwellingAreaSquareMeters |
| Heated area (JSON) | 190 | JSON building.heatedAreaSquareMeters |
| Roof stories area (JSON) | 52 | JSON building.roofStoriesAreaSquareMeters |
| Regular stories area (JSON) | 138 | JSON building.regularStoriesAreaSquareMeters |
| Basement area (JSON) | 0 | JSON building.basementAreaSquareMeters |
| Number of stories (JSON) | 1 | JSON building.numberOfStories |
| Floor count (Plans Zone) | 1 | Plans XML Zone.FloorCount |
| Building type (Plans Zone) | fritliggende enfamilieshus | Mapped from Plans Zone.BuildingType |
| Building type (JSON) | fritliggende enfamilieshus | Mapped from JSON building.buildingType |
| Heat source (JSON) | electricHeating | Mapped from JSON heat source |
| Story types (JSON building) | ground | JSON building.storyTypes |
| Stories localised (JSON walk) | _(missing)_ | JSON model.stories[].storyType |
| # rooms (JSON walk) | _(missing)_ | JSON model.stories[].rooms[] |
| Has loft (JSON) | _(missing)_ | JSON building.storyTypes (loft/attic) |
| Has basement (JSON) | _(missing)_ | JSON building.storyTypes (basement) |
| Has workshop (JSON) | _(missing)_ | JSON rooms with workshop/værksted |
| Has garage (JSON) | _(missing)_ | JSON rooms with garage |

### `Additional` (Plans: 2648 chars → Final: 3070 chars · +5/-5 lines)

**Consultant-added lines & auto-populate analysis:**

- Udfyldt ejeroplysningsskema.
  - _no auto-populatable values detected_
- Ved bygningsgennemgangen forelå der ingen tegningsmateriale eller bygningsbeskrivelser.
  - _no auto-populatable values detected_
- Det oplyste varmeforbrug stammer fra ejer, og er udelukkende oplyst i kr. (for el-forbrug), hvorfor der ved enheder fremgår 0.
  - _no auto-populatable values detected_
- I den oplyste udgift til elforbrug indgår tillige elforbrug til husholdning, belysning mv.  Det beregnede forbrug er uden elforbrug til husholdningen, belysning mv, hvilket svarer til ca. 4.000-4.500 kWh for en almindelig husstand.
  - _no auto-populatable values detected_
- Ved beregningen af det samlede energiforbrug indgår el-forbrug iflg. Bygningsreglementet med en faktor på 1,9 p.g.a. den større CO2-belastning ved elproduktion, hvilket ved el-opvarmede huse medfører at energimærket ofte befinder sig i den nederste ende af energimærkningsskalaen.
  - _no auto-populatable values detected_

<details><summary>Lines removed from boilerplate (5)</summary>

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema. XXX
- Ved bygningsgennemgangen forelå ikke et udfyldt ejeroplysningsskema. Det forudsættes hermed, at der ikke er givet tilladelse til destruktive undersøgelser. XXX
- Bygningstegninger XXX
- Tidligere energimærkningsrapport af den XX-XX-XX, med energimærkningsnummer: XXX
- _(…1 more…)_

</details>

### `OnEnergyPrices` (Plans: 705 chars → Final: 664 chars · +1/-1 lines)

**Consultant-added lines & auto-populate analysis:**

- Rapportens pris på rummeter træ er anvendt ud fra en gennemsnitsvurdering.
  - _no auto-populatable values detected_

<details><summary>Lines removed from boilerplate (1)</summary>

- Der er i energimærket anvendt aktuelle energipriser for alle brændselstyper fx olie, naturgas, brænde og træpiller.

</details>

### `OnBuildingDescription` (Plans: 1377 chars → Final: 880 chars · +7/-9 lines)

**Consultant-added lines & auto-populate analysis:**

- Bygningen er et fritliggende enfamilieshus med udnyttet tagetage, opført i 1800 med et opvarmet areal på 190,3 m². I henhold til ejer er der foretaget væsentlig ombygning/tilbygning i 2011-2019. Ejendommen har gennemgået diverse isoleringsarbejde gennem tiden på loft og ved vinduer, døre, vægge og gulv.
  - ✅ **Year**: `1800` (source: `Plans BBR.YearOfConstruction / JSON building.constructedYear`)
  - ❌ **Year**: `2011` (source: `?`)
  - ❌ **Year**: `2019` (source: `?`)
  - ❌ **Area (m²)**: `3 m²` (source: `?`)
  - ✅ **Building type**: `fritliggende enfamilieshus` (source: `Plans Zone.BuildingType`)
  - ✅ **Room/story feature**: `tagetage` (source: `JSON building.roofStoriesAreaSquareMeters&gt;0`)
  - ✅ **Room/story feature**: `loft` (source: `JSON building.roofStoriesAreaSquareMeters&gt;0`)
- Ejendommen er kontrolopmålt af energikonsulenten.
  - _no auto-populatable values detected_
- Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen.
  - _no auto-populatable values detected_
- Arealer jfr. BBR: Bebyggede areal: 138 m², opvarmede areal 190 m² heraf 52 m² tagetage.
  - ✅ **Area (m²)**: `138 m²` (source: `JSON building.regularStoriesAreaSquareMeters`)
  - ✅ **Area (m²)**: `190 m²` (source: `Plans BBR.DwellingArea`)
  - ✅ **Area (m²)**: `52 m²` (source: `JSON building.roofStoriesAreaSquareMeters`)
  - ✅ **Room/story feature**: `tagetage` (source: `JSON building.roofStoriesAreaSquareMeters&gt;0`)
- Arealer jfr. vores opmåling: Bebyggede areal: 128,7 m², opvarmede areal 190,3 m² heraf 61,6 m² tagetage.
  - ❌ **Area (m²)**: `7 m²` (source: `?`)
  - ❌ **Area (m²)**: `3 m²` (source: `?`)
  - ❌ **Area (m²)**: `6 m²` (source: `?`)
  - ✅ **Room/story feature**: `tagetage` (source: `JSON building.roofStoriesAreaSquareMeters&gt;0`)
- Ved bygningsgennemgangen var der ikke adgang til skunk.
  - _no auto-populatable values detected_
- Værksted medregnes til det opvarmede areal.
  - ❌ **Room/story feature**: `værksted` (source: `?`)

<details><summary>Lines removed from boilerplate (9)</summary>

- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og XXX bygningstegninger.
- De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer ikke overens med BBR-meddelelsen. Afvigelsen består i XXX
- _(…5 more…)_

</details>

### `OnDestructiveInspections` (Plans: 0 chars → Final: 0 chars · +0/-0 lines)

**Consultant-added lines & auto-populate analysis:**

_(no consultant-added lines)_

---

## Spangsvej_15_5210_Odense_NV

- Plans XML: `Spangsvej_15_5210_Odense_NV.xml`
- Final XML: `Spangsvej_15_5210_Odense_NV final.xml`
- JSON model: `Spangsvej_15_5210_Odense_NV.json`

### Structured facts

| Fact | Value | Source |
|---|---|---|
| Year of construction (Plans BBR) | 1970 | Plans XML BBR.YearOfConstruction |
| Year of construction (JSON) | 1970 | JSON building.constructedYear |
| Year of renovation (Plans BBR) | 1979 | Plans XML BBR.YearOfRenovation |
| Year of renovation (JSON) | 1979 | JSON building.renovatedYear |
| Dwelling area (Plans BBR) | 141 | Plans XML BBR.DwellingArea |
| Dwelling area (JSON) | 141 | JSON building.dwellingAreaSquareMeters |
| Heated area (JSON) | 141 | JSON building.heatedAreaSquareMeters |
| Roof stories area (JSON) | 0 | JSON building.roofStoriesAreaSquareMeters |
| Regular stories area (JSON) | 141 | JSON building.regularStoriesAreaSquareMeters |
| Basement area (JSON) | 34 | JSON building.basementAreaSquareMeters |
| Number of stories (JSON) | 1 | JSON building.numberOfStories |
| Floor count (Plans Zone) | 1 | Plans XML Zone.FloorCount |
| Building type (Plans Zone) | fritliggende enfamilieshus | Mapped from Plans Zone.BuildingType |
| Building type (JSON) | fritliggende enfamilieshus | Mapped from JSON building.buildingType |
| Heat source (JSON) | Fjernvarme | Mapped from JSON heat source |
| Story types (JSON building) | basement, ground | JSON building.storyTypes |
| Stories localised (JSON walk) | _(missing)_ | JSON model.stories[].storyType |
| # rooms (JSON walk) | _(missing)_ | JSON model.stories[].rooms[] |
| Has loft (JSON) | _(missing)_ | JSON building.storyTypes (loft/attic) |
| Has basement (JSON) | True | JSON building.storyTypes (basement) |
| Has workshop (JSON) | _(missing)_ | JSON rooms with workshop/værksted |
| Has garage (JSON) | _(missing)_ | JSON rooms with garage |

### `Additional` (Plans: 2648 chars → Final: 2446 chars · +2/-5 lines)

**Consultant-added lines & auto-populate analysis:**

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema.
  - _no auto-populatable values detected_
- Bygningstegninger fra opførelsen dateret 1978 og tilbygning dateret 1979.
  - ❌ **Year**: `1978` (source: `?`)
  - ✅ **Year**: `1979` (source: `Plans BBR.YearOfRenovation / JSON building.renovatedYear`)

<details><summary>Lines removed from boilerplate (5)</summary>

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema. XXX
- Ved bygningsgennemgangen forelå ikke et udfyldt ejeroplysningsskema. Det forudsættes hermed, at der ikke er givet tilladelse til destruktive undersøgelser. XXX
- Bygningstegninger XXX
- Tidligere energimærkningsrapport af den XX-XX-XX, med energimærkningsnummer: XXX
- _(…1 more…)_

</details>

### `OnEnergyPrices` (Plans: 705 chars → Final: 804 chars · +1/-1 lines)

**Consultant-added lines & auto-populate analysis:**

- Fjernvarmeprisen er i denne rapport fastsat ud fra de tariffer, der var gældende ved energimærkningsrapportens officielle indberetningsdato. Fjernvarmeprisen stammer fra det konkrete fjernvarmeværk: Fjernvarme Fyn.
  - ✅ **Heat source**: `fjernvarme` (source: `JSON.heating.primarySource.sourceType`)

<details><summary>Lines removed from boilerplate (1)</summary>

- Der er i energimærket anvendt aktuelle energipriser for alle brændselstyper fx olie, naturgas, brænde og træpiller.

</details>

### `OnBuildingDescription` (Plans: 1377 chars → Final: 803 chars · +3/-8 lines)

**Consultant-added lines & auto-populate analysis:**

- Bygningen er et fritliggende enfamilieshus, med 34 m² kælder, opført i 1970 med et opvarmet areal på 175 m². Ejendommen har gennemgået diverse isoleringsarbejde gennem tiden.
  - ✅ **Year**: `1970` (source: `Plans BBR.YearOfConstruction / JSON building.constructedYear`)
  - ✅ **Area (m²)**: `34 m²` (source: `JSON building.basementAreaSquareMeters`)
  - ❌ **Area (m²)**: `175 m²` (source: `?`)
  - ✅ **Building type**: `fritliggende enfamilieshus` (source: `Plans Zone.BuildingType`)
  - ✅ **Room/story feature**: `kælder` (source: `JSON building.storyTypes (basement)`)
- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og bygningstegninger.
  - _no auto-populatable values detected_
- Det opmålte opvarmede areal stemmer ikke overens med BBR-meddelelsen. Afvigelsen består i at kælderen er opvarmet.
  - ✅ **Room/story feature**: `kælder` (source: `JSON building.storyTypes (basement)`)

<details><summary>Lines removed from boilerplate (8)</summary>

- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og XXX bygningstegninger.
- De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer ikke overens med BBR-meddelelsen. Afvigelsen består i XXX
- _(…4 more…)_

</details>

### `OnDestructiveInspections` (Plans: 0 chars → Final: 0 chars · +0/-0 lines)

**Consultant-added lines & auto-populate analysis:**

_(no consultant-added lines)_

---

## Spurvevej_13_7100_Vejle

- Plans XML: `Spurvevej_13_7100_Vejle.xml`
- Final XML: `Spurvevej_13_7100_Vejle final.xml`
- JSON model: `Spurvevej_13_7100_Vejle.json`

### Structured facts

| Fact | Value | Source |
|---|---|---|
| Year of construction (Plans BBR) | 1969 | Plans XML BBR.YearOfConstruction |
| Year of construction (JSON) | 1969 | JSON building.constructedYear |
| Year of renovation (Plans BBR) | _(missing)_ | Plans XML BBR.YearOfRenovation |
| Year of renovation (JSON) | _(missing)_ | JSON building.renovatedYear |
| Dwelling area (Plans BBR) | 180 | Plans XML BBR.DwellingArea |
| Dwelling area (JSON) | 180 | JSON building.dwellingAreaSquareMeters |
| Heated area (JSON) | 180 | JSON building.heatedAreaSquareMeters |
| Roof stories area (JSON) | 74 | JSON building.roofStoriesAreaSquareMeters |
| Regular stories area (JSON) | 106 | JSON building.regularStoriesAreaSquareMeters |
| Basement area (JSON) | 106 | JSON building.basementAreaSquareMeters |
| Number of stories (JSON) | 1 | JSON building.numberOfStories |
| Floor count (Plans Zone) | 1 | Plans XML Zone.FloorCount |
| Building type (Plans Zone) | fritliggende enfamilieshus | Mapped from Plans Zone.BuildingType |
| Building type (JSON) | fritliggende enfamilieshus | Mapped from JSON building.buildingType |
| Heat source (JSON) | Fjernvarme | Mapped from JSON heat source |
| Story types (JSON building) | ground, basement | JSON building.storyTypes |
| Stories localised (JSON walk) | _(missing)_ | JSON model.stories[].storyType |
| # rooms (JSON walk) | _(missing)_ | JSON model.stories[].rooms[] |
| Has loft (JSON) | _(missing)_ | JSON building.storyTypes (loft/attic) |
| Has basement (JSON) | True | JSON building.storyTypes (basement) |
| Has workshop (JSON) | _(missing)_ | JSON rooms with workshop/værksted |
| Has garage (JSON) | _(missing)_ | JSON rooms with garage |

### `Additional` (Plans: 2648 chars → Final: 2401 chars · +2/-5 lines)

**Consultant-added lines & auto-populate analysis:**

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema.
  - _no auto-populatable values detected_
- Udateret bygningstegninger.
  - _no auto-populatable values detected_

<details><summary>Lines removed from boilerplate (5)</summary>

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema. XXX
- Ved bygningsgennemgangen forelå ikke et udfyldt ejeroplysningsskema. Det forudsættes hermed, at der ikke er givet tilladelse til destruktive undersøgelser. XXX
- Bygningstegninger XXX
- Tidligere energimærkningsrapport af den XX-XX-XX, med energimærkningsnummer: XXX
- _(…1 more…)_

</details>

### `OnEnergyPrices` (Plans: 705 chars → Final: 806 chars · +1/-1 lines)

**Consultant-added lines & auto-populate analysis:**

- Fjernvarmeprisen er i denne rapport fastsat ud fra de tariffer, der var gældende ved energimærkningsrapportens officielle indberetningsdato. Fjernvarmeprisen stammer fra det konkrete fjernvarmeværk: Vejle Fjernvarme
  - ✅ **Heat source**: `fjernvarme` (source: `JSON.heating.primarySource.sourceType`)

<details><summary>Lines removed from boilerplate (1)</summary>

- Der er i energimærket anvendt aktuelle energipriser for alle brændselstyper fx olie, naturgas, brænde og træpiller.

</details>

### `OnBuildingDescription` (Plans: 1377 chars → Final: 651 chars · +2/-8 lines)

**Consultant-added lines & auto-populate analysis:**

- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og bygningstegninger.
  - _no auto-populatable values detected_
- De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen. Dog er kælderen med undtagelse af depotrum medtaget i det opvarmede areal.
  - ✅ **Room/story feature**: `kælder` (source: `JSON building.storyTypes (basement)`)

<details><summary>Lines removed from boilerplate (8)</summary>

- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og XXX bygningstegninger.
- De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer ikke overens med BBR-meddelelsen. Afvigelsen består i XXX
- _(…4 more…)_

</details>

### `OnDestructiveInspections` (Plans: 0 chars → Final: 0 chars · +0/-0 lines)

**Consultant-added lines & auto-populate analysis:**

_(no consultant-added lines)_

---

## Strandbakken_5_5900_Rudkøbing

- Plans XML: `Strandbakken_5_5900_Rudkøbing.xml`
- Final XML: `Strandbakken_5_5900_Rudkøbing final.xml`
- JSON model: `Strandbakken_5_5900_Rudkøbing.json`

### Structured facts

| Fact | Value | Source |
|---|---|---|
| Year of construction (Plans BBR) | 1937 | Plans XML BBR.YearOfConstruction |
| Year of construction (JSON) | 1937 | JSON building.constructedYear |
| Year of renovation (Plans BBR) | _(missing)_ | Plans XML BBR.YearOfRenovation |
| Year of renovation (JSON) | _(missing)_ | JSON building.renovatedYear |
| Dwelling area (Plans BBR) | 107 | Plans XML BBR.DwellingArea |
| Dwelling area (JSON) | 107 | JSON building.dwellingAreaSquareMeters |
| Heated area (JSON) | 107 | JSON building.heatedAreaSquareMeters |
| Roof stories area (JSON) | 45 | JSON building.roofStoriesAreaSquareMeters |
| Regular stories area (JSON) | 62 | JSON building.regularStoriesAreaSquareMeters |
| Basement area (JSON) | 62 | JSON building.basementAreaSquareMeters |
| Number of stories (JSON) | 1 | JSON building.numberOfStories |
| Floor count (Plans Zone) | 1 | Plans XML Zone.FloorCount |
| Building type (Plans Zone) | fritliggende enfamilieshus | Mapped from Plans Zone.BuildingType |
| Building type (JSON) | fritliggende enfamilieshus | Mapped from JSON building.buildingType |
| Heat source (JSON) | Fjernvarme | Mapped from JSON heat source |
| Story types (JSON building) | ground, basement, first | JSON building.storyTypes |
| Stories localised (JSON walk) | _(missing)_ | JSON model.stories[].storyType |
| # rooms (JSON walk) | _(missing)_ | JSON model.stories[].rooms[] |
| Has loft (JSON) | _(missing)_ | JSON building.storyTypes (loft/attic) |
| Has basement (JSON) | True | JSON building.storyTypes (basement) |
| Has workshop (JSON) | _(missing)_ | JSON rooms with workshop/værksted |
| Has garage (JSON) | _(missing)_ | JSON rooms with garage |

### `Additional` (Plans: 2648 chars → Final: 2390 chars · +2/-5 lines)

**Consultant-added lines & auto-populate analysis:**

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema.
  - _no auto-populatable values detected_
- Bygningstegninger
  - _no auto-populatable values detected_

<details><summary>Lines removed from boilerplate (5)</summary>

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema. XXX
- Ved bygningsgennemgangen forelå ikke et udfyldt ejeroplysningsskema. Det forudsættes hermed, at der ikke er givet tilladelse til destruktive undersøgelser. XXX
- Bygningstegninger XXX
- Tidligere energimærkningsrapport af den XX-XX-XX, med energimærkningsnummer: XXX
- _(…1 more…)_

</details>

### `OnEnergyPrices` (Plans: 705 chars → Final: 656 chars · +1/-1 lines)

**Consultant-added lines & auto-populate analysis:**

- Der er i energimærket anvendt aktuelle energipriser for fjernvarme
  - ✅ **Heat source**: `fjernvarme` (source: `JSON.heating.primarySource.sourceType`)

<details><summary>Lines removed from boilerplate (1)</summary>

- Der er i energimærket anvendt aktuelle energipriser for alle brændselstyper fx olie, naturgas, brænde og træpiller.

</details>

### `OnBuildingDescription` (Plans: 1377 chars → Final: 832 chars · +3/-8 lines)

**Consultant-added lines & auto-populate analysis:**

- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og bygningstegninger.
  - _no auto-populatable values detected_
- De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen.
  - _no auto-populatable values detected_
- Arealerne forudsættes jf. gældende Håndbog for energikonsulenter opvarmet med samme opvarmningsform som resten af bygningen, uanset at der ingen varmekilde er, da det vurderes at eksisterende varmeanlæg er tilstrækkelig til at kunne opvarme hele boligen
  - _no auto-populatable values detected_

<details><summary>Lines removed from boilerplate (8)</summary>

- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og XXX bygningstegninger.
- De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer ikke overens med BBR-meddelelsen. Afvigelsen består i XXX
- _(…4 more…)_

</details>

### `OnDestructiveInspections` (Plans: 0 chars → Final: 0 chars · +0/-0 lines)

**Consultant-added lines & auto-populate analysis:**

_(no consultant-added lines)_

---

## Sønderskovvej_5_5932_Humble

- Plans XML: `Sønderskovvej_5_5932_Humble.xml`
- Final XML: `Sønderskovvej_5_5932_Humble final.xml`
- JSON model: `Sønderskovvej_5_5932_Humble.json`

### Structured facts

| Fact | Value | Source |
|---|---|---|
| Year of construction (Plans BBR) | 1850 | Plans XML BBR.YearOfConstruction |
| Year of construction (JSON) | 1850 | JSON building.constructedYear |
| Year of renovation (Plans BBR) | 1963 | Plans XML BBR.YearOfRenovation |
| Year of renovation (JSON) | 1963 | JSON building.renovatedYear |
| Dwelling area (Plans BBR) | 100 | Plans XML BBR.DwellingArea |
| Dwelling area (JSON) | 100 | JSON building.dwellingAreaSquareMeters |
| Heated area (JSON) | 100 | JSON building.heatedAreaSquareMeters |
| Roof stories area (JSON) | 64 | JSON building.roofStoriesAreaSquareMeters |
| Regular stories area (JSON) | 100 | JSON building.regularStoriesAreaSquareMeters |
| Basement area (JSON) | 0 | JSON building.basementAreaSquareMeters |
| Number of stories (JSON) | 1 | JSON building.numberOfStories |
| Floor count (Plans Zone) | 1 | Plans XML Zone.FloorCount |
| Building type (Plans Zone) | fritliggende enfamilieshus | Mapped from Plans Zone.BuildingType |
| Building type (JSON) | fritliggende enfamilieshus | Mapped from JSON building.buildingType |
| Heat source (JSON) | oilBoiler | Mapped from JSON heat source |
| Story types (JSON building) | ground | JSON building.storyTypes |
| Stories localised (JSON walk) | _(missing)_ | JSON model.stories[].storyType |
| # rooms (JSON walk) | _(missing)_ | JSON model.stories[].rooms[] |
| Has loft (JSON) | _(missing)_ | JSON building.storyTypes (loft/attic) |
| Has basement (JSON) | _(missing)_ | JSON building.storyTypes (basement) |
| Has workshop (JSON) | _(missing)_ | JSON rooms with workshop/værksted |
| Has garage (JSON) | _(missing)_ | JSON rooms with garage |

### `Additional` (Plans: 2648 chars → Final: 2299 chars · +1/-6 lines)

**Consultant-added lines & auto-populate analysis:**

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema.
  - _no auto-populatable values detected_

<details><summary>Lines removed from boilerplate (6)</summary>

- Ved bygningsgennemgangen forelå udfyldt ejeroplysningsskema. XXX
- Ved bygningsgennemgangen forelå ikke et udfyldt ejeroplysningsskema. Det forudsættes hermed, at der ikke er givet tilladelse til destruktive undersøgelser. XXX
- Følgende materiale var til rådighed for udarbejdelsen af energimærket:
- Bygningstegninger XXX
- _(…2 more…)_

</details>

### `OnEnergyPrices` (Plans: 705 chars → Final: 649 chars · +1/-1 lines)

**Consultant-added lines & auto-populate analysis:**

- Der er i energimærket anvendt aktuelle energipriser for el.
  - _no auto-populatable values detected_

<details><summary>Lines removed from boilerplate (1)</summary>

- Der er i energimærket anvendt aktuelle energipriser for alle brændselstyper fx olie, naturgas, brænde og træpiller.

</details>

### `OnBuildingDescription` (Plans: 1377 chars → Final: 833 chars · +3/-8 lines)

**Consultant-added lines & auto-populate analysis:**

- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og bygningstegninger.
  - _no auto-populatable values detected_
- De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen.
  - _no auto-populatable values detected_
- Arealerne forudsættes jf. gældende Håndbog for energikonsulenter opvarmet med samme opvarmningsform som resten af bygningen, uanset at der ingen varmekilde er, da det vurderes at eksisterende varmeanlæg er tilstrækkelig til at kunne opvarme hele boligen
  - _no auto-populatable values detected_

<details><summary>Lines removed from boilerplate (8)</summary>

- Ejendommen er kontrolopmålt af energikonsulenten ud fra stikprøver og XXX bygningstegninger.
- De opmålte opvarmede arealer stemmer overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer, med mindre afvigelser, overens med BBR-meddelelsen. XXX
- Det opmålte opvarmede areal stemmer ikke overens med BBR-meddelelsen. Afvigelsen består i XXX
- _(…4 more…)_

</details>

### `OnDestructiveInspections` (Plans: 0 chars → Final: 0 chars · +0/-0 lines)

**Consultant-added lines & auto-populate analysis:**

_(no consultant-added lines)_

---
