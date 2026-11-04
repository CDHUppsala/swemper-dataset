# SweMPer: Swedish Medical Periodicals Dataset (1781–2011)

Welcome to the public dataset documentation and metadata repository for **SweMPer** (*Communicating Medicine: Digitalisation of Swedish Medical Periodicals 1781–2011* / *Medicinens kommunikation*), a project conducted at the **Centre for Digital Humanities Uppsala (CDHU)** in partnership with **Uppsala University Library (UUB)** and **Kungliga Biblioteket (KB)**.

The platform and interactive search interface are available at [**swemper.idehist.uu.se**](https://swemper.idehist.uu.se).

---

## 📚 Overview

The SweMPer corpus brings together over two centuries of digitized Swedish medical journalism across **22 periodicals**, comprising **633,526 pages** across **893 periodical-years** (1781–2014):

- **High-Resolution Derivative Scans:** Optimized AVIF images transcoded from master library scans.
- **Full-Text OCR:** Swedish language models (Tesseract and Riksarkivet) providing comprehensive page transcription.
- **Deep Layout Metadata:** Page descriptors in YAML format (`metadata/v4`) detailing text regions, headings, illustrations, advertisements, and word-level bounding boxes.

---

## 🗂️ Documentation & Guides

| Document | Purpose |
| :--- | :--- |
| [**`CHANGELOG.md`**](CHANGELOG.md) | Official dataset release history and milestone changelog, strictly aligned with archival ZFS snapshots. |
| [**`DATASET_STRUCTURE.md`**](DATASET_STRUCTURE.md) | Complete directory hierarchy, canonical file naming grammar (`[journal]_[year]_[vol]_[issue]_[page].[ext]`), zero-padding conventions, and metadata schemas. |
| [**`journal_descriptions/`**](journal_descriptions/) | Individual historical and bibliographic essays for all 22 periodicals (in Swedish). |

---

## 📖 Periodicals in the Dataset

| SweMPer ID | Title / Organization | Curated Years | Active Span Details | Pages |
| :--- | :--- | :--- | :--- | :--- |
| `allergia` | *Allergia* (Astma- och Allergiförbundet) | 1957–1990 | 34 years (continuous) | 4,054 |
| `diabetes` | *Diabetes* (Svenska Diabetesförbundet) | 1949–1990 | 40 years (continuous) | 8,891 |
| `eira` | *Eira: Tidskrift för helso- och sjukvård* | 1877–1903 | 27 years (continuous) | 21,399 |
| `helsovannen` | *Helsowännen / Helsovännen* | 1886–1919 | 34 years (continuous) | 16,368 |
| `homeopatiens_seger` | *Homeopatiens seger* | 1907–1914 | 8 years (continuous) | 1,073 |
| `hygiea` | *Hygiea: Medicinsk och farmaceutisk månadsskrift* | 1839–1938 | 100 years (continuous) | 122,868 |
| `jahresbericht` | *Jahresbericht über die Fortschritte der Pharmacognosie* | 1866–1914 | 49 years (continuous) | 40,782 |
| `jordemodern` | *Jordemodern: Svenska barnmorskeförbundets tidskrift* | 1888–2011 | 124 years (continuous) | 48,154 |
| `lakare_och_fältskärer` | *Förhandlingar vid Svenska läkaresällskapets sammankomster* | 1841–1913 | 73 years (continuous) | 24,197 |
| `medicinskt_arkiv` | *Medicinskt archiv* | 1863–1868 | 6 years (continuous) | 2,752 |
| `mft_motpol` | *Medicinska föreningens tidskrift (Motpol)* | 1971–1983 | 13 years (continuous) | 3,116 |
| `nordiskt_medicinskt_arkiv` | *Nordiskt medicinskt arkiv* | 1869–1918 | 50 years (continuous) | 39,235 |
| `samling_af_ron` | *Samling af rön och händelser uti medicinal-verket* | 1797–1803 | 7 years (continuous) | 2,382 |
| `sigyn` | *Sigyn: Tidskrift för den svenska sjuksköterskekåren* | 1913–1933 | 21 years (continuous) | 8,761 |
| `sjukskotersketidningen` | *Svensk sjukskötersketidning* | 1912–1976 | 65 years (continuous) | 37,276 |
| `sls_handlingar` | *Svenska läkaresällskapets handlingar* | 1813–1974 | 162 years | 41,757 |
| `socialmedicinsk_tidskrift` | *Socialmedicinsk tidskrift* | 1924–1984 | 61 years (continuous) | 45,831 |
| `status` | *Status: Organ för Svenska tuberkulosläkarföreningen* | 1938–1983 | 46 years (continuous) | 16,876 |
| `svenska_lakartidningen` | *Svenska läkartidningen / Läkartidningen* | 1904–1975 | 72 years (continuous) | 216,271 |
| `tidskrift_for_praktisk_medicin`| *Tidskrift för praktisk medicin* | 1881–1888 | 8 years (continuous) | 3,745 |
| `upsala_lakareforenings_forhandlingar` | *Upsala läkareförenings förhandlingar* | 1865–1913 | 49 years (continuous) | 24,795 |
| `veckoskrift_för_läkare` | *Veckoskrift för läkare och naturforskare* | 1781–1807 | 27 years (continuous) | 15,283 |

---

## 🔗 Related Repositories

- [**CDHUppsala/swemper**](https://github.com/CDHUppsala/swemper): Full-stack web application (FastAPI, GraphQL, MongoDB, Vue 3).
- [**CDHUppsala/swemper-data-dashboard**](https://github.com/CDHUppsala/swemper-data-dashboard): Streamlit dataset inspection dashboard.
- [**Alvin Portal**](https://www.alvin-portal.org/): Platform for digital collections and digitized cultural heritage.

---

## 🏛️ Project & Research Team

- **Centre for Digital Humanities Uppsala (CDHU):** Technical infrastructure, visual layout analysis, and semantic search.
- **Uppsala University Library (UUB):** Digitization, scan capture, ALTO layout generation.
- **Kungliga Biblioteket (KB):** Digitization and historical collection curation.
