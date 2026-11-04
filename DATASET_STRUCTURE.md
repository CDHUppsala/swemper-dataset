# Swemper Dataset Structure, Contents and Naming Conventions

This document outlines the structure and contents of the Swemper dataset located on the host `beast` at `/zpool/beast-mirror/swemper/curated`.

## Project Information

**Communicating Medicine: Digitalisation of Swedish Medical Periodicals 1781–2011 (SweMPer)**

The dataset is part of the SweMPer project, which aims to digitize and analyze Swedish medical periodicals. The curated folder contains:
- OCR text (fulltext)
- XML and AltoXML (structure and layout)
- Pipeline metadata
- scanned images (JPG) and compressed images (AVIF)

## Dataset Statistics

- **Total Periodicals:** 22 medical periodicals
- **Total Pages:** 633,082 digitized pages (893 periodical-years, 1781–2014)
- **Total Size:** ~2.0 TB
- **Composition:**
    - **Images:** ~1.9 TB (The vast majority of data)
        - **JPG (Originals):** ~1.65 TB (633,082 master scans)
        - **AVIF (Compressed):** ~275 GB
        - Largest: `svenska_lakartidningen` (~916 GB, 216,271 pp), `socialmedicinsk_tidskrift` (~365 GB, 45,831 pp), `hygiea` (~166 GB, 122,868 pp).
    - **Texts:** < 10 GB (e.g., `hygiea` texts are ~1.1 GB, `svenska_lakartidningen` texts are significant but text files are small).
    - **Metadata/XML:** Remaining capacity.

## Changelog Insights & Curation Status

Based on `CHANGELOG.md`:
- **Folder Structure:** A major migration to the `uub-per-year` folder structure for texts was completed in late 2025.
- **Status & Diabetes:** These collections were imported from `actdisease` and re-indexed (starting at 0001). Old text and yaml files may be deprecated.
- **Eira:** Scraped files for `Eira` are known to be incomplete and require partial rescraping.
- **Socialmedicinsk Tidskrift:** 1955 filenames were manually fixed from an incorrect 1954 naming pattern.
- **Sequencing:** Several journals (`hygiea`, `sigyn`, `homeopatiens_seger`) had image sequencing issues (starting at 0000 or 0002) which have been addressed.

## Overview

The dataset contains digitized Swedish medical periodicals. Each periodical has its own directory containing subdirectories for different file types (images, metadata, OCR text, etc.).

> [!NOTE]
> Curation is ongoing. Metadata and specific file types might not be available for all periodicals or every year/volume.

## Periodicals

The curated dataset contains **22 medical periodicals** comprising **633,082 pages** across **893 periodical-years** (1781–2014):

| SweMPer ID (Folder) | Full Bibliographic Title / Organization | Curated Years | Active Span Details | Pages |
| :--- | :--- | :--- | :--- | :--- |
| `allergia` | *Allergia* (Astma- och Allergiförbundet) | 1957–1990 | 34 years (continuous) | 4,055 |
| `diabetes` | *Diabetes* (Svenska Diabetesförbundet) | 1949–1990 | 40 years (continuous) | 8,891 |
| `helsovannen` | *Helsowännen* (1885–1899) / *Hälsovännen: tidskrift för allmän och enskild helsovård* (1900–1961) | 1885–1961 | 70 years (continuous) | 28,367 |
| `homeopatiens_seger` | *Homeopatiens seger: tidskrift för vetenskaplig homeopati* (Svenska föreningen för vetenskaplig homeopati) | 1907–1947 | 35 years (continuous; continuation of *Sigyn*) | 4,089 |
| `hygiea` | *Hygiea: medicinsk och farmaceutisk månadsskrift* (Svenska Läkaresällskapet) | 1839–1938 | 104 years (continuous) | 122,868 |
| `jordemodern` | *Jordemodern: tidskrift för barnmorskor* (Svenska Barnmorskeförbundet) | 1888–2011 | 123 years (continuous) | 52,067 |
| `lakare_och_fältskärer` | *Vetenskapshandlingar för läkare och fältskärer* (utg. Sven Hedin) | 1793–1803 | 6 years (1793, 1794, 1796, 1797, 1799, 1803) | 2,436 |
| `lakare_pharmaceuter` | *Tidskrift för läkare och pharmaceuter* | 1832–1838 | 7 years (1832–1838 continuous) | 3,294 |
| `mft_motpol` | *MFT: Medicinska föreningarnas tidskrift* / *Motpol: tidskrift för sjukvårdsdebatt* | 1960–1996 | 34 years (1960–1972, 1974–1994, 1996) | 8,961 |
| `ms-brevet` | *MS-brevet* (Riksförbundet för multipel skleros / NHR) | 1954–1978 | 25 years (continuous) | 4,332 |
| `reuma` | *Reuma* / *Reumatikertidningen* (Riksförbundet mot reumatism) | 1949–1964 | 15 years (continuous) | 1,667 |
| `samlingar_blandade` | *Samlingar i blandade ämnen för läkare-vetenskapen och naturforskningen* | 1810–1812 | 3 years (continuous) | 522 |
| `sigyn` | *Sigyn: tidskrift för vetenskaplig homeopati* (föregångare till *Homeopatiens seger*) | 1916–1919 | 4 years (continuous) | 186 |
| `sjukskotersketidningen` | *Svensk sjukskötersketidning* (Svensk sjuksköterskeförening) | 1908–1976 | 68 years (continuous) | 56,012 |
| `sls_förhandlingar` | *Svenska Läkaresällskapets förhandlingar* | 1841–1938 | 95 year/volume folders (1841–1864 multi-year spans, 1865–1938 annual) | 38,909 |
| `sls_handlingar` | *Svenska Läkaresällskapets handlingar* | 1813–1835 | 15 years (periodic volumes) | 6,498 |
| `sls_årsberättelse` | *Svenska Läkaresällskapets årsberättelse* | 1810–1841 | 30 years | 3,642 |
| `socialmedicinsk_tidskrift` | *Socialmedicinsk tidskrift* | 1924–2014 | 91 years (continuous) | 45,831 |
| `status` | *Status* (Riksförbundet för hjärt- och lungsjuka) | 1938–1991 | 54 years (continuous) | 16,959 |
| `svensk_sanatorietidning` | *Svensk sanatorietidning: organ för Svenska sanatorieföreningen* | 1946–1964 | 17 years (1946–1947, 1950–1964) | 448 |
| `svenska_lakartidningen` | *Svenska Läkartidningen* (Sveriges läkarförbund) | 1904–1976 | 73 years (continuous) | 216,271 |
| `veckoskrift_för_läkare` | *Veckoskrift för läkare och naturforskare* | 1781–1807 | 15 years (1781–1788, 1791, 1794, 1797–1798, 1804–1807) | 6,777 |
| **TOTAL** | **22 Periodicals** | **1781–2014** | **893 Periodical-Years** | **633,082 pages** |

> [!NOTE]
> - `logs/` in `/curated/` is an operational directory and not part of the periodical corpus.
> - Several early periodicals use multi-year directory names (e.g. `sls_förhandlingar/images/jpg/1841-1843/`).
> - Folder naming adheres to the SweMPer ID format (`[periodical_name]`). Note that `mft_motpol` was previously mislabeled as `mtf_motpol` in older notes.

## Directory Structure

The general structure for a periodical (e.g., `hygiea`) is as follows:

```
./swemper/curated/[periodical_name]/
├── altoxml/
│   └── [year]/             # Layout-heavy XML from library sources
├── images/
│   ├── avif/
│   │   └── [year]/         # Compressed delivery images
│   └── jpg/
│       └── [year]/         # Original source master scans
├── metadata/
│   ├── v1/
│   │   └── [year]/         # Legacy pipeline metadata (preserved)
│   ├── v2/, v3/
│   │   └── [year]/         # Historical/active YAML pipeline metadata 
│   └── v4/
│       └── [year]/         # Current YAML page layout & issue metadata 
├── outputs/
│   └── [year]/             # Pipeline JSON bounding box extractions
├── pdf/                    # FLAT: Archive-only full volume PDFs from UUB
├── texts/
│   ├── ra-ocr/
│   │   └── [year]/         # Page-level OCR delivered by Riksarkivet
│   ├── tesseract-v1/
│   │   └── [year]/         # In-house page-level OCR pipeline 
│   └── uub-per-year/       # Concatenated full-volume text from UUB
└── xml/
    └── [year]/             # Standard structural XML from libraries
```

## Filename Conventions

Files generally follow the convention:
`[periodical]_[year]_[vol]_[issue]_[description]_[page].[extension]`

However, many fields are optional. The most common patterns are:

1.  **Standard (with volume):** `[periodical]_[year]_vol[volume]_[page].[extension]`
    *   Example: `hygiea_1839_vol001_0001.jpg`

2.  **No Volume:** `[periodical]_[year]_[page].[extension]`
    *   Example: `allergia_1957_0000.jpg`
    *   Example: `socialmedicinsk_tidskrift_1924_0001.jpg`

3.  **With Issue (and optional description):** `[periodical]_[year]_vol[volume]_[issue]_[description]_[page].[extension]`
    *   Example: `diabetes_1984_vol034_nr001_0017.jpg` (With issue number)
    *   Example: `status_1955_vol018_nr012julen1955glimtar_0012.jpg` (With issue and description "julen1955glimtar")

**Important Notes:**
*   **Ignore `advertisements/` and `outputs/`:** Files within these subdirectories may rely on older naming conventions and should be ignored when determining the standard pattern.
*   `_vol` is typically present (`_vol001`) even if there is only one volume. However, when it is missing (e.g., `allergia`, `socialmedicinsk_tidskrift`), it indicates there is only one volume for that year.
*   **Zero-Padding Conventions:** Indices are generally zero-padded to facilitate sorting:
    *   **Volume (`vol`):** 3 digits (e.g., `vol001`, `vol123`).
    *   **Issue (`nr`):** 3 digits (e.g., `nr001`, `nr012`).
    *   **Page:** 4 digits (e.g., `0001`, `0485`, `1234`).
*   The page number is usually the last segment before the extension.

## Metadata Structure

Metadata is stored in YAML format (currently `v2`). A typical metadata file contains the following fields:

- `Swemper-page-descriptor`: Root element
    - `ContainerVolumeFile`: Reference to the YAML file itself
    - `CreationDate`: Date of processing
    - `DocumentTopic`: Topic tag (e.g., "hygiea-journal")
    - `FileSize`: Size of the original image
    - `FileType`: Type of the original image (e.g., "JPEG")
    - `IdentifiedLayoutElements`: Detected page elements
        - `Advertisements`: List of ads with bounding box, score, content, etc.
        - `AuthorNames`, `HeaderOrFooters`, `Images`, `Lists`, `Pagination`, `Tables`, `TextBlocks`, `Titles`: Lists of other elements
    - `JournalName`: Name of the journal
    - `Language`: Language of the content
    - `NumberIndex`: Issue number index (often "NA" for bound volumes)
    - `PageFilename`: Name of the source image file
    - `PageIndex`: Page number (zero-padded)
    - `Source`: Source of the scan
    - `SourceFileResolution`: Image resolution
    - `Timestamp`: Processing timestamp
    - `TotalPages`: Total pages in the volume
    - `VolumeIndex`: Volume identifier
    - `Year`: Year of publication
    - `md5_checksum`: Checksum of the source file

```yaml
Swemper-page-descriptor:
  ContainerVolumeFile: "hygiea_1920_vol001_0001.yaml"
  CreationDate: "2025-12-04"
  DocumentTopic: "hygiea-journal"
  ...
```
