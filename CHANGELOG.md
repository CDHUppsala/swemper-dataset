# SweMPer Data Changelog

All notable changes to SweMPer data will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.38+metadata_v4_visual_ocr_and_reindex_homeopatiens_seger] – 2026-11-03
### Added
- Promoted visual OCR metadata tier `metadata/v4` (171,803 YAML files, 13 GB) into curated storage (`/zpool/beast-mirror/swemper/curated/`) across all 22 periodicals via zero-block intra-dataset moves.
- Applied 312,995 GPT-cleaned visual elements across 26 finalized Excel workbooks into `metadata/v4` descriptors using [`curation_fixes/apply_visual_ocr_sheets_to_v4.py`](curation_fixes/apply_visual_ocr_sheets_to_v4.py), with 31,515 intentional blanks written as `Content: ""` (never raw OCR).
- Successfully passed corpus-wide pre-flight validation gate across all 22 periodicals (633,526 pages) via [`validate_dataset.py`](validate_dataset.py) verifying zero schema or checksum errors.

### Changed
- Re-indexed *Homeopatiens Seger* (1907–1909) across all 7 curated tiers (`images/jpg`, `images/avif`, `texts/tesseract-v1`, `outputs/v2`, `metadata/v2`, `metadata/v3`, `metadata/v4`) using [`curation_fixes/reindex_homeopatiens_seger_1907_1909.py`](curation_fixes/reindex_homeopatiens_seger_1907_1909.py) with `--skip-staging`:
  - 1907 (`vol001`): 100 pages shifted from `0002..0101` to canonical `0001..0100`.
  - 1908 (`vol002`): 150 pages shifted from `0002..0151` to canonical `0001..0150`.
  - 1909 (`vol003`): 124 pages shifted from `0002..0125` to canonical `0001..0124`.
  - Verified 1:1 parity against FineReader XML (`xml/`), which was already 0001-indexed.
  - Resolves GitHub issue [CDHUppsala/swemper#80](https://github.com/CDHUppsala/swemper/issues/80).
- Re-indexed *Svenska Läkartidningen* 1964 `vol001` staging `metadata/v4` to match curated milestone `0.1.35` (+2 shift, purging duplicate scans `2231`/`2232`), and sanitized 811 `CropPath:` lines via [`curation_fixes/sanitize_svlt_1964_v4_croppaths.py`](curation_fixes/sanitize_svlt_1964_v4_croppaths.py).

## [0.1.37+ingest_sjukskotersketidningen_1912] – 2026-10-12
### Added
- Ingested missing year 1912 (`vol001`, 364 pages) for *Svensk sjukskötersketidning* from UUB delivery 008 (Alvin ID `658455`) using [`curation_fixes/ingest_sjukskotersketidningen_1912.py`](curation_fixes/ingest_sjukskotersketidningen_1912.py).
- Moved delivered master scans (`images/jpg`), ALTO XML layout files (`xml`), full-volume archive PDF (`pdf`), and volume text (`texts/uub-per-year`) via zero-duplication intra-dataset moves within `beast-mirror/swemper`.
- Transcoded 364 derivative AVIF images (`images/avif`, Quality 75, 0.75x Lanczos scale) and transcribed 364 Swedish OCR text files (`texts/tesseract-v1`).
- Verified 100% parity across all active tiers (364 pages each).
- Resolves and closes GitHub issue [CDHUppsala/swemper#9](https://github.com/CDHUppsala/swemper/issues/9).

## [0.1.36+remediate_jordemodern_1901_1902_missing_issues] – 2026-10-10
### Added
- Remediated missing issues in *Jordemodern* for year 1901 (Issue nr 6, 24 pages) and year 1902 (Issue nr 10, 24 pages) across `images/jpg`, `images/avif`, and `texts/tesseract-v1` (48 pages / 144 files total) using [`curation_fixes/remediate_jordemodern_1901_1902_missing_issues.py`](curation_fixes/remediate_jordemodern_1901_1902_missing_issues.py).
- Converted original `.jp2` scans from `SCRAPED_FILES/jordemodern_images/` to master JPEG scans (Quality 92), derivative AVIF images (Quality 75, 0.75x Lanczos scale), and Swedish Tesseract OCR (`texts/tesseract-v1`).
- Verified 1:1 page parity across JPG, AVIF, and TXT for 1901 (302 pages) and 1902 (296 pages).
- Addresses GitHub issue [CDHUppsala/swemper#82](https://github.com/CDHUppsala/swemper/issues/82) (core image & text tiers complete; downstream YAML metadata generation pending).

## [0.1.35+fix_svlt_1964_vol001_misplaced_pages] – 2026-10-09
### Changed
- Re-indexed *Svenska Läkartidningen* 1964 Volume 1 (`vol001`) across all 7 curated tiers (`images/jpg`, `images/avif`, `texts/tesseract-v1`, `outputs/v1`, `outputs/v3`, `metadata/v1`, `metadata/v3`) using [`curation_fixes/reindex_svlt_1964_vol001.py`](curation_fixes/reindex_svlt_1964_vol001.py).
- Shifted 1,624 files covering indices `_0607`..`_2230` up by 2 to `_0609`..`_2232` to resolve an original scanning gap where journal pages 317 and 318 had been skipped during continuous scanning.
- Reinserted missing journal pages 317 and 318 at indices `_0607` and `_0608` (formerly scanned at the end of volume 1 as `2231_0607` and `2232_0608`).
- Sanitized internal YAML metadata headers (`Year: "1964"`, `VolumeIndex: "vol001"`, `PageIndex`, `PageFilename`, `ContainerVolumeFile`) eliminating corrupted `Year: "2231"` and `Year: "2232"` values caused by legacy filename parsing errors.
- Resolves GitHub issues [CDHUppsala/swemper#53](https://github.com/CDHUppsala/swemper/issues/53) and [CDHUppsala/swemper#75](https://github.com/CDHUppsala/swemper/issues/75).

### Removed
- Purged 2 redundant duplicate scans `svenska_lakartidningen_1964_vol001_2231.*` and `svenska_lakartidningen_1964_vol001_2232.*` across all tiers.
- Total pages for `vol001` corrected to 2,232 continuous pages (`0001` through `2232`), bringing total 1964 page count to 9,000 pages (and curated master dataset total to 633,079 pages).

## [0.1.34+remove_allergia_1967_0152_duplicate] – 2026-10-09
### Removed
- Removed extraneous scan `allergia_1967_0152` across all curated tiers (`images/jpg`, `images/avif`, `texts/tesseract-v1`, `metadata/v1`, `metadata/v2`, `metadata/v3`, `outputs/v1`, `outputs/v2`, `avifimages`, `avifimages75`). File was an accidental duplicate scan of the front cover of issue nr 1, 1968 (`allergia_1968_0000`).
- Verified 1:1 page correspondence across all active tiers for `allergia` (152 pages in 1967; 4,054 total pages across 1957–1990). Resolves GitHub issue [CDHUppsala/swemper#8](https://github.com/CDHUppsala/swemper/issues/8).

## [0.1.33+relocate_svlt_scanning_notes] – 2026-10-08
### Changed
- Relocated 6 historical scanning notes files (`svenska_lakartidningen_<year>_comments.txt` for years 1971–1976) from `svenska_lakartidningen/texts/tesseract-v1/<year>/` to dedicated documentation folder `svenska_lakartidningen/documentation/scanning_notes/`.
- Verified 1:1 page correspondence across original JPGs and `tesseract-v1` OCR text files for all 216,271 pages of `svenska_lakartidningen` (1904–1976).
- Achieved 100.0% exact parity (633,082 / 633,082 pages) across all 22 periodicals in the curated dataset between `images/jpg` and `texts/tesseract-v1`.

## [0.1.32+remove_stray_socialmedicinsk_ocr] – 2026-10-08
### Removed
- Removed 556 empty (0-byte) phantom files (`socialmedicinsk_tidskrift_1990_*.txt`) mistakenly placed in `socialmedicinsk_tidskrift/texts/tesseract-v1/1989/`.
- Removed stray operator note `1974.txt` in `socialmedicinsk_tidskrift/texts/tesseract-v1/1974/`.
- Removed stray terminal command artifacts `-l.txt` and `out.txt.txt` in `socialmedicinsk_tidskrift/texts/tesseract-v1/1990/`.
- Verified 1:1 page correspondence across original JPGs and `tesseract-v1` OCR text files for all 45,831 pages of `socialmedicinsk_tidskrift` (1924–2014).

## [0.1.31+added_sjukskotersketidningen_avif_and_tess_v1_1934-1973] – 2026-10-04
### Added
- Transferred transcoded AVIF images for `sjukskotersketidningen` across years 1934–1973 (40 volumes, 43,054 pages).
- Generated and added `tesseract-v1` OCR text files for `sjukskotersketidningen` across years 1934–1973 (40 volumes, 43,054 pages).
- Verified 1:1 page correspondence across original JPGs, AVIFs, and OCR text files for the entire 1934–1973 range.

## [0.1.30_fix_v3_years_sls_forhandlingar] – 2026-08-25
### Fixed
- Fixed incorrect v3 metadata in `sls_förhandlingar`.

## [0.1.29+added_all_missing_jsonoutputs_sls_förhandlingar] – 2026-04-08
### Added
- Added missing `outputs/**/*.json`.
- Added missing `sls_förhandlingar` metadata (YAML).
- Note: Corresponding ZFS snapshot on dataset is `beast-mirror/swemper@0.1.29_remap_year_fields` (created 2026-04-21).

## [0.1.28+fixed_incorrect_mft_filenames_and_references] – 2026-04-08
### Fixed
- Fixed incorrect filenames and references in metadata from `mtf_` to `mft_motpol`.

## [0.1.27+added_more_v3_data] – 2026-04-01
### Added
- Added missing year ranges (newly processed YAML) for most journals in the dataset.

## [0.1.26+remove_stray_allergia_files] – 2026-04-01
### Removed
- Removed stray files in `allergia/metadata/v3/*.yaml`.

## [0.1.25+postprocessed_boxes] – 2026-02-04
### Fixed
- Fixed overlapping boxes in YAML files (75% overlap) to improve layout detection results (`fix_overlap_v3.py`).

## [0.1.24+added_metadata-v2_large_dec_batch] – 2025-12-08
### Added
- Added Various 1920s – ca. 36k pages:
  - `helsovannen`: 1920–1929
  - `hygiea`: 1920–1929
  - `jordemodern`: 1920–1929
- Added `svlt`:
  - `svlt`: 1920–1929 (61,335 pp)
  - `svlt`: 1941–1959
- Added 1800s (10,662 pp):
  - `samlingar_blandade`: 1810–1812 (everything)
  - `sls_handlingar`: 1810–1841
  - `sls_årsberättelse`: 1810–1841
- Added patienttidskrifter (31,572 pp):
  - `allergia`: 1938–1991
  - `diabetes`: 1938–1991
  - `reuma`: 1938–1991
  - `status`: 1938–1991
- Note: Some journals within the ranges above were not in print (thus not missing from dataset).

## [0.1.23+added_tesseract-v1_remaining] – 2025-12-06
### Added
- Tesseract OCR for all pages missing the edition, including in year-range folders. Very few pages should be missing from the edition now.

## [0.1.22+added_transcoded_year-range_avifs] – 2025-11-28
### Added
- Transcoded AVIFs for all pages including in year-ranges. Every page should now have an AVIF file, though some exceptions/edge cases might still exist.

## [0.1.21+merge_step02_metadata-v2] – 2025-11-03
### Added
- Generated `metadata-v2` for the following selection:
  - Full runs: `sjukskotersketidningen` (1908–1933), `homeopatiens_seger` (1907–1947), `sigyn` (1916–1919), `lakare_och_fältskärer` (1793–1803), `lakare_pharmaceuter` (1832–1838), `ms-brevet` (1954–1978), `mft_motpol` (full), `svensk_sanatorietidning` (1946–1964), `veckoskrift_för_läkare` (1781–1807).
  - Partial runs: `helsovannen` (1930–1961), `hygiea` (1930–1938), `jordemodern` (1930–1970), `socialmedicinsk_tidskrift` (1930–1970), `svenska_lakartidningen` (1930–1940).

## [0.1.20+merge_step01_avif_and_tess-v1] – 2025-11-03
### Added
- Newly transcoded and correctly named AVIFs for (all years present): `sjukskotersketidningen`, `homeopatiens_seger`, `sigyn`, `lakare_och_fältskärer`, `lakare_pharmaceuter`, `ms-brevet`, `mft_motpol`, `svensk_sanatorietidning`, `veckoskrift_för_läkare`, `svenska_lakartidningen`, `helsovannen`, `jordemodern`, `socialmedicinsk_tidskrift`, `hygiea`.
- Partially added `tesseract-v1/` for the above journals.
- Also added `tesseract-v1` for many years across multiple journals.

## [0.1.19+added_sjukskotersketidningen_tesseract_v1] – 2025-10-17
### Added
- All (1908–1933) `tesseract-v1/` OCR text files to `sjukskotersketidningen/`.

## [0.1.18+corrected_mistake_ms-brevet] – 2025-10-09
### Fixed
- Discovered and corrected mistake in `ms-brevet` 1968 where UUB `per-year_volume` txts had been treated (renamed, organised) as per-page. Renamed to `*-DEPRECATED.txt`.

## [0.1.17+migrate_to_edition_structure_005] – 2025-10-09
### Removed
- `clean_empty_dirs.py`: Removed 7 empty `tesseract-v1/` directories:
  - `helsovannen/texts/tesseract-v1`
  - `homeopatiens_seger/texts/tesseract-v1`
  - `jordemodern/texts/tesseract-v1`
  - `reuma/texts/tesseract-v1`
  - `sls_förhandlingar/texts/tesseract-v1`
  - `sls_årsberättelse/texts/tesseract-v1`
  - `svensk_sanatorietidning/texts/tesseract-v1`

## [0.1.16+migrate_to_edition_structure_004] – 2025-10-07
### Changed
- `move_ra-edition_ocr.py`: Separated Riksarkivet/Fränsta text files currently in `tesseract-v1/` and moved them into their own edition subfolder: `ra-ocr/`. Script was run with input CSV: `swemper_ra-scanned_volumes.csv`.

## [0.1.15+migrate_to_edition_structure_003] – 2025-10-07
### Changed
- `migrate_to_edition_structure.py` (updated): Updated script to find and migrate concatenated per-year files to correct edition subfolder: `uub-per-year/`.

## [0.1.14+migrate_to_edition_structure_002] – 2025-10-07
### Changed
- `migrate_to_edition_structure.py`: Completed migration to new folder structure for *all remaining journals*.
- Manually discovered and fixed `ms-brevet/txt/1968` that had the wrong path.
- Confirmed with updated validation script (`validate_and_rename_sep2025.py`).
- Note: Where `{journal}/{avifimages|avifimages75|advertisements|outputs}` exists, these remain unchanged/unmoved.

## [0.1.13+migrate_to_edition_structure_001] – 2025-10-07
### Changed
- `migrate_to_edition_structure.py`: Completed migration to new folder structure for `sigyn/` and `allergia/`.
- Confirmed with manual checks and updated validation script (`validate_and_rename_sep2025.py`).
- Note: Where `{journal}/{avifimages|avifimages75|advertisements|outputs}` exists, these remain unchanged/unmoved.

## [0.1.12+initial_import_sjukskotersketidningen] – 2025-10-07
### Added
- Initial import using new folder structure: `images/jpg` and `texts/uub-per-year` edition.

## [0.1.11+validation_after_changes] – 2025-09-30
### Changed
- Ran `jpg-txt_integrity_check.py` and examined logs to verify alignment with validation results from `validate_and_rename_all_sep2025.py`.
- Note: No ZFS snapshot made for this step.

## [0.1.10+corrected_some_hygiea_image_sequencing] – 2025-09-30
### Fixed
- Used `resequence_filenames.py` to reindex `hygiea/images/1902-1904/` and `hygiea/images/1908-1911/`. Filenames now start at 0001. Corresponding XML files were already correctly indexed.

## [0.1.9+corrected_all_svlt_xml_yaml_and_alto] – 2025-09-30
### Fixed
- Used `validate_and_rename_all_sep2025.py` to identify and rename incorrect XML (57,465), YAML (2,999), and ALTO XML (57,465) filenames across `svenska_lakartidningen`.

## [0.1.8+socialmedicinsk_fix_1955-txt_and_yaml-final] – 2025-09-30
### Fixed
- Used Neovim Oil file manager to batch rename all incorrect `*_1954_*` to `*_1955_*` in `socialmedicinsk_tidskrift/metadata/v1/1955`.

## [0.1.8+socialmedicinsk_fix_1955-txt_and_yaml] – 2025-09-30
### Fixed
- Used Neovim Oil file manager to batch rename all incorrect `*_1954_*` to `*_1955_*` in `socialmedicinsk_tidskrift/texts/1955`.

## [0.1.7+corrected_57k_svlt_txts] – 2025-09-30
### Fixed
- Used `validate_and_rename_all_sep2025.py` to identify and rename 57,492 incorrect TXT filenames across `svenska_lakartidningen`.

## [0.1.7+corrected_60k_svlt_jpgs] – 2025-09-30
### Fixed
- Used `validate_and_rename_all_sep2025.py` to identify and rename 60,464 incorrect JPG filenames across `svenska_lakartidningen`.

## [0.1.6+socialmedicinsk_fix_1955-DONE] – 2025-09-29
### Fixed
- Used Neovim Oil file manager to batch rename all incorrect `*_1954_*` to `*_1955_*` in `socialmedicinsk_tidskrift/images/1955`.

## [0.1.5+status_and_diabetes_ocr_add] – 2025-05-14
### Added
- `transcribe_concurrent.py`: Ran script to generate Tesseract OCR for `curated/status` and `curated/diabetes`.

## [0.1.4+status_and_diabetes_reimport] – 2025-05-09
### Changed
- `reimport_status_diabetes.py`: Curated filenames, copied from `actdisease/` (JPGs only); manually moved old JPGs, TXTs, and metadata to `DEPRECATED_DATA/` prior to run. Full-volume PDFs were kept. `status` and `diabetes` should now be complete, except for re-OCR requirement.
- Previous JPG file count (both folders): 16,826 + 7,150. New file count: 16,959 + 8,891.
- Note: JPGs were reindexed starting at 0001 (old TXT and YAML files are deprecated and will not match).

## [0.1.3+uub_007_add] – 2025-04-15
### Added
- Curated and added all data in `UUB_leverans_007/`: UUB delivered `ms-brevet` 1968 (no. 01–06).
- Note: 1968 has an anomalous volume-identifier compared to the rest of the series (`_vol015_nr*`). Kept for now.
- Note: All UUB and Fränsta delivered files should now be incorporated.

## [0.1.2+uub_005_add] – 2025-04-15
### Added
- Curated and added UUB delivery `uub_leverans_005/`: "Samlingar i blandade ämnen för läkare och naturforskare" (`samlingar_blandade`) and `sigyn`.
- `sigyn` (1916) and `homeopatiens_seger` (1910–1923) also had their JPG indices fixed.
- Note: `hygiea` `1902-*/` and `1905-*/` are not fixed yet.

## [0.1.1+changelog_add] – 2025-04-15
### Added
- Added `CHANGELOG.md`, retroactively updated.
- Includes all curated data except: unfixed `status` and `diabetes`; `eira`; final UUB imports.

## [0.1.0+accumulated_imports] – 2025-04-15
### Added
- The bulk of data has been moved to `curated/`. Start of versioning and changelog.
- Summary of changes:
  - Curated and added remaining UUB files in `uub_leverans_001/` (see `swemper-code/uub_leverans001_rename.py`).
  - Curated and added remaining UUB files in `uub_leverans_002/` (see `swemper-code/uub_leverans002_rename.py`).
  - Merged, curated, and added `socialmedicinsk_tidskrift`.
  - Curated and added `allergia` and `diabetes`.
  - Curated and added `jordemodern`, including previously merged scraped files.
  - Merged, curated, and added `helsovannen` and `status`.
  - Merged, curated, and added `svenska_lakartidningen` (excluded broken 1960 vol. 2).
  - Curated and added files in `uub_leverans_00[2-4]`: `hygiea`, `jordemodern`, `homeopatiens_seger` (Fränsta), `ms-brevet` (Fränsta), `mft_motpol`, `reuma`, `sls_*`, `svensk_sanatorietidning`, `svenska_lakartidningen` (see `swemper-code/rename_fransta_v2.py`).

# SweMPer Data Notes and Todo List

## TODO
- INVESTIGATE: Sequencing problem: `'/zpool/beast-mirror/swemper/curated/homeopatiens_seger/images/1907'... Context: Journal='homeopatiens_seger', Year(s)='1907' ... Page sequence starts at '0002', not 0000 or 0001.`
- Scraping. We are missing some data in the scraped sources that have been imported (see `skrapade_tidskrifter_lovisa.docx`):
  - `helsovannen`: 1895 Nr. 24 (40 pages scraped but 58 at KB, parts of an index), 1903 no. 20 (?)
  - `jordemodern`: 1893 no. 12 (40 scraped but 44 at KB, name index missing), 1897 no. 12 (40 scraped but 72 at KB, index missing), 1901 no. 6 is missing, 1902 no. 10 is missing.
- Import/rename scraped files (`eira`). NOTE: Scraped files are known to be incomplete and need partial rescrape. Cursory check indicates page indices > 40 have been left out (example: `eira` 1884 no. 2 has 40 pages, but KB has 44).
- Double check scraped data in `eira` that has not been investigated.
- NOTE: Found missing `svenska_lakartidningen` 1960 vol. 2 scans on external HDD. Copied and kept on backup SSD. Could potentially reimport, but scan/file condition is poor.
- [x] ~~Allergia 1967 includes front cover from nr001 1968 (removed `allergia_1967_0152` in 0.1.34; resolves issue #8).~~
- [x] ~~Sequencing problem: Hygiea 1902–1904, 1908–1911 has zero-indexed JPGs. Fixed.~~
- [x] ~~Socialmedicinsk tidskrift has incongruous filenames in 1955 (`socialmedicinsk_tidskrift_1954_*`). Fixed.~~
- [x] ~~Diabetes and Status missing pages. Swapped in and curated filenames from `/zpool/beast-mirror/actdisease/ocr_output/merged/`.~~
- [x] ~~Sigyn and Homeopatiens Seger image indices start at 0. Fixed.~~
- [x] ~~`svenska_lakartidningen`: multiple years named "*svenska_läkartidningen" instead of "svenska_lakartidningen". Fixed.~~
- [x] ~~Import/rename final UUB files with irregular non-Alvin names.~~
- [x] ~~Redo incomplete Status and Diabetes with complete actdisease sources.~~
- [x] ~~Check missing OCR pages from Fränsta.~~
- [x] ~~Import/rename all Fränsta-scanned files in `uub_leverans_002/`, `uub_leverans_003/`, `uub_leverans_004/`.~~
- [x] ~~Import/rename first batches of UUB-scanned files in `uub_leverans_001/`, `uub_leverans_002/`.~~
