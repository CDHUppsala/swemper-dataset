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

- **Total Size:** ~2.0 TB
- **Composition:**
    - **Images:** ~1.9 TB (The vast majority of data)
        - **JPG (Originals):** ~1.65 TB
        - **AVIF (Compressed):** ~275 GB
        - Largest: `svenska_lakartidningen` (~916 GB), `socialmedicinsk_tidskrift` (~365 GB), `hygiea` (~166 GB).
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

The following periodicals are currently included:

- `allergia`
- `diabetes`
- `helsovannen`
- `homeopatiens_seger`
- `hygiea`
- `jordemodern`
- `lakare_och_fältskärer`
- `lakare_pharmaceuter`
- `ms-brevet`
- `mtf_motpol`
- `reuma`
- `samlingar_blandade`
- `sigyn`
- `sjukskotersketidningen`
- `sls_förhandlingar`
- `sls_handlingar`
- `sls_årsberättelse`
- `socialmedicinsk_tidskrift`
- `status`
- `svenska_lakartidningen`
- `svensk_sanatorietidning`
- `veckoskrift_för_läkare`

## Directory Structure

The general structure for a periodical (e.g., `hygiea`) is as follows:

```
[periodical_name]/
├── altoxml/             # AltoXML files (from library sources like UUB)
│   └── [year]/          # Organized by year
├── images/              # Scanned images
│   ├── avif/            # Compressed AVIF images (for deployment)
│   └── jpg/             # Original scanned JPG images
│       └── [year]/      # Organized by year
├── metadata/            # Metadata files
│   └── v2/              # Version 2 of the pipeline metadata
│       └── [year]/      # Organized by year
├── texts/               # OCR text outputs
│   ├── ra-ocr/          # OCR from Riksarkivet
│   ├── tesseract-v1/    # In-house Tesseract v1 OCR output
│   │   └── [year]/      # Organized by year
│   └── uub-per-year/    # OCR from Uppsala University Library (UUB)
├── xml/                 # Standard XML files (from library sources)
│   └── [year]/          # Organized by year
├── outputs/             # Pipeline outputs
└── pdf/                 # PDF files
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
