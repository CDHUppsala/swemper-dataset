# Swemper data changelog

All notable changes to Swemper data will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.24+added_metadata-v2_large_dec_batch] – 2025-12-08
### Changed
- ADDED Various 1920s – ca. 36k pages
    - helsovannen: 1920-1929
    - hygiea: 1920-1929
    - jordemodern: 1920-1929
- ADDED svlt:
    - svlt: 1920-1929 (61335 pp)
    - svlt: 1941-1959
- ADDED 1800s (10662):
    - samlingar_blandade: 1810-1812 (everything)
    - sls_handlingar: 1810-1841
    - sls_årsberättelse: 1810-1841
- ADDED patienttidskrifter (31572)
    - allergia: 1938-1991
    - diabetes: 1938-1991
    - reuma: 1938-1991
    - status: 1938-1991
- NOTE: some journals within the ranges above were not in print (thus not missing from dataset).

## [0.1.23+added_tesseract-v1_remaining] – 2025-12-06
### Changed
- ADDED: Tesseract OCR for all pages missing the edition, including in year-range folders. Very few pages should be missing from the edition now.

## [0.1.22+added_transcoded_year-range_avifs] – 2025-11-28
### Changed
- ADDED: Transcoded AVIFs for all pages including in year-ranges. Every page should now have an AVIF file, though some exceptions/edge cases might still exist.

## [0.1.21+merge_step02_metadata-v2] – 2025-11-03
### Changed
- ADDED: Generated metadata-v2 for the following selection: sjukskotersketidningen, 1908-1933 (full); homeopatiens_seger, 1907-1947 (full); sigyn, 1916-1919 (full); lakare_och_fältskärer 1793-1803 (full); lakare_pharmaceuter, 1832-1838 (full); ms-brevet, 1954-1978 (full); mtf_motpol (full); svensk_sanatorietidning, 1946-1964 (full); veckoskrift_för_läkare 1781-1807 (full); helsovannen, 1930-1961; hygiea 1930-1938; jordmodern, 1930-1970; socialmedicinsk_tidskrift, 1930-1970; svenska_lakartidningen, 1930-1940.

## [0.1.20+merge_step01_avif_and_tess-v1] – 2025-11-03
### Changed
- ADDED: newly transcoded and correctly named AVIFs for (all years present): sjukskotersketidningen, homeopatiens_seger, sigyn, lakare_och_fältskärer, lakare_pharmaceuter, ms-brevet, mtf_motpol, svensk_sanatorietidning, veckoskrift_för_läkare, svenska_lakartidningen, helsovannen, jordmodern, socialmedicinsk_tidskrift, hygiea
- Partially ADDED tesseract-v1/ for the above journals

- Also added tesseract-v1 for many years of many journals.

## [0.1.19+added_sjukskotersketidningen_tesseract_v1] – 2025-10-17
### Changed
- ADDED: all (1908–1938) `tesseract-v1/` ocr text-files to `sjukskotersketidningen/`

## [0.1.18+corrected_mistake_ms-brevet] – 2025-10-09
### Changed
- discovered and corrected mistake in `ms-brevet` 1968 where uub `per-year_volume` txts
had been treated (renamed, organised) as per-page. Renamed to `*-DEPRECATED.txt`

## [0.1.17+migrate_to_edition_structure_005] – 2025-10-09
### Changed
- `clean_empty_dirs.py`: Removed 7 empty tesseract-v1/ directories.
    - `/zpool/beast-mirror/swemper/curated/helsovannen/texts/tesseract-v1,
/zpool/beast-mirror/swemper/curated/homeopatiens_seger/texts/tesseract-v1,
/zpool/beast-mirror/swemper/curated/jordemodern/texts/tesseract-v1, /zpool/beast-mirror/swemper/curated/reuma/texts/tesseract-v1, /zpool/beast-mirror/swemper/curated/sls_förhandlingar/texts/tesseract-v1, /zpool/beast-mirror/swemper/curated/sls_årsberättelse/texts/tesseract-v1, /zpool/beast-mirror/swemper/curated/svensk_sanatorietidning/texts/tesseract-v1`

## [0.1.16+migrate_to_edition_structure_004] – 2025-10-07
### Changed
- `move_ra-edition_ocr.py`: separated riksarkivet/Fränsta textfiles currently in `tesseract-v1/` and moved them into their own edition subfolder: `ra-ocr/`. Script was run with this csv as input: `swemper_ra-scanned_volumes.csv`

## [0.1.15+migrate_to_edition_structure_003] – 2025-10-07
### Changed
- `migrate_to_edition_structure.py` (updated): Updated script to find and migrate concatenated per-year files to correct edition subfolder: `uub-per-year/`.


## [0.1.14+migrate_to_edition_structure_002] – 2025-10-07
### Changed
- `migrate_to_edition_structure.py`: Completed migration to new folder structure for *all remaining journals*. Also manually discovered and fixed ms-brevet/txt/1968 that had the wrong path. Confirmed with updated validation script(`validate_and_rename_sep2025.py`) NOTE: where {journal}/{avifimages|avifimages75|advertisements|outputs} exists -- these are unchanged/unmoved!

## [0.1.13+migrate_to_edition_structure_001] – 2025-10-07
### Changed
- `migrate_to_edition_structure.py`: Completed migration to new folder structure for `sigyn/` and `allergia/`. Confirmed with manual checks and updated validation script(`validate_and_rename_sep2025.py`) NOTE: where `{journal}/{avifimages|avifimages75|advertisements|outputs}` exists -- these are unchanged/unmoved!

## [0.1.12+initial_import_sjukskotersketidningen] – 2025-10-07
### Changed
- Initial import using new folder structure: `images/jpg` and `texts/uub-per-year`
edition.

## [0.1.11+validation_after_changes] – 2025-09-30
### Changed
- Ran `jpg-txt_integrity_check.py` and examined logs to make sure they align with validation results from `validate_and_rename_all_sep2025.py` which they did.
- no snapshot made.

## [0.1.10+corrected_some_hygiea_image_sequencing] – 2025-09-30
### Changed
- Used `resequence_filenames.py` to reindex `hygiea/images/1902-1904/` and
`hygiea/images/1908-1911`. Now starts at 0001. Corresponding xmls were already correctly indexed.

## [0.1.9+corrected_all_svlt_xml_yaml_and_alto] – 2025-09-30
### Changed
- Used `validate_and_rename_all_sep2025.py` to identify and rename incorrect xml (57465), yaml (2999) and alto.xml (57465) filenames across svenska_lakartidningen.

## [0.1.8+socialmedicinsk_fix_1955-txt_and_yaml-final] – 2025-09-30
### Changed
- used neovim oil filemanager to batch rename all incorrect `*_1954_*` to `*_1955_*` in
- used neovim oil filemanager to batch rename all incorrect `*_1954_*` to `*_1955_*` in
`socialmedicinsk_tidskrift/metadata/v1/1955`

## [0.1.8+socialmedicinsk_fix_1955-txt_and_yaml] – 2025-09-30
### Changed
- used neovim oil filemanager to batch rename all incorrect `*_1954_*` to `*_1955_*` in
- used neovim oil filemanager to batch rename all incorrect `*_1954_*` to `*_1955_*` in
`socialmedicinsk_tidskrift/texts/1955`

## [0.1.7+corrected_57k_svlt_txts] – 2025-09-30
### Changed
- Used `validate_and_rename_all_sep2025.py` to identify and rename 57492 incorrect txt filenames across svenska_lakartidningen.

## [0.1.7+corrected_60k_svlt_jpgs] – 2025-09-30
### Changed
- Used new script (`validate_and_rename_all_sep2025.py`) to identify and rename 60464 incorrect txt filenames across svenska_lakartidningen.

## [0.1.6+socialmedicinsk_fix_1955-DONE] – 2025-09-29

### Changed
- used neovim oil filemanager to batch rename all incorrect `*_1954_*` to `*_1955_*` in
`socialmedicinsk_tidskrift/images/1955`


## [0.1.5+status_and_diabetes_ocr_add] – 2025-05-14
### Changed
- `transcribe_concurrent.py`: ran script to generate tesseract OCR for `curated/status`
and `curated/diabetes`.

## [0.1.4+status_and_diabetes_reimport] – 2025-05-09
### Changed
- `reimport_status_diabetes.py`: curated filenames, copied from `actdisease/` (jpgs only); manually moved old jpgs, txts and metadata to `DEPRECATED_DATA/` before run. pdfs were kept. Status and Diabetes should now be complete, except need for re-ocr. 
- Previous jpg filecount, both folders: 16826+7150. New file count: 16959+8891. 
- NOTE: jpgs were reindexed starting at 0001, i.e. old txt and yaml files are deprecated and will not match.

## [0.1.3+uub_007_add] – 2025-04-15
### Changed
- Curated and added all data in `UUB_leverans_007/`: UUB delivered `MS-brevet` 1968 (no. 01-06). 
- NOTE: 1968 has been given anomalous volume-identifier compared to the rest of the series (`_vol015_nr*`). We keep it for now. 
- NOTE: All UUB and Fränsta delivered files should now have been incorporated!

## [0.1.2+uub_005_add] – 2025-04-15
### Changed
- Curated and added UUB in `uub_leverans_005/` UUB delivered "Samlingar i blandade ämnen för läkare och naturforskare" (`samlingar_blandade`) and `Sigyn`. `Sigyn` (1916) and `homeopatiens_seger` (1910-1923) also had their `jpg-indices` fixed. 
- NOTE: `hygiea` `1905-*/`, `1902-*/` are not fixed yet.

## [0.1.1+changelog_add] – 2025-04-15
### Changed
- Added `CHANGELOG.md`, retroactively updated
- Includes all curated data except: unfixed Status and Diabetes; Eira; final UUB imports

## [0.1.0+accumulated_imports] – 2025-04-15
### Changed
- The bulk of data has been moved to `curated/`. Start of versioning and changelog. 
- Summary of changes:
    - Curated and added remaining UUB-files in: `uub_leverans_001/` see `swemper-code/uub_leverans001_rename.py`
    - Curated and added remaining UUB-files in: `uub_leverans_002/`. See `swemper-code/uub_leverans002_rename.py`
    - Merged, curated and added socialmedicinsk_tidskrift 
    - Curated and added allergia and diabetes
    - Curated and added jordemodern, incl. previously merged scraped files
    - Merged, curated and added helsovannen and status
    - Merged, curated and added svenska_lakartidningen; NOTE: excluded broken 1960 vol. 2.
    - Curated and added files in `uub_leverans_00[2-4]`: hygiea, jordemodern, homeopatiens_seger (Fränsta), ms-brevet (Fränsta), mtf_motpol, reuma, sls_*, svensk_sanatorietidning, svenska_lakartidningen. See `swemper-code/rename_fransta_v2.py`

# Swemper data notes and todo-list

## TODO
- INVESTIGATE: Sequencing problem: `'/zpool/beast-mirror/swemper/curated/homeopatiens_seger/images/1907'... Context: Journal='homeopatiens_seger', Year(s)='1907' ... Page sequence starts at '0002', not 0000 or 0001.`
- Scraping. We are missing some data in the scraped sources that have been imported (See `skrapade_tidskrifter_lovisa.docx`):
    - helsovannen: 1895 Nr. 24 (40 pages scraped but 58 @ kb, delar av ett register ), 1903 no. 20 (?)
    - Jordemodern: 1893 no. 12 (40 scraped but 44 at kb, namnregister saknas), 1897 no. 12 (40, 72 @ kb, register saknas), 1901 no 6 is missing, 1902 no. 10 missing
- Import/rename scraped files (Eira). NOTE: scraped files are known to be incomplete and need partial rescrape. Cursory check indicates page indices > 40 have been left out (example: Eira 1884 no. 2 has 40 pages, but kb has 44)
- Double check scraped data in Eira that has not been investigated.
- NOTE Found missing svenska_lakartidningen 1960 vol 2 scans on the external HDD. They are now copied and kept on backup-SSD. Could potentially reimport, but condition of scans/files are bad.
- ==DONE== ~~Sequencing problem: Hygiea 1902-1904*, 1908-1911* has zero-indexed jpgs. Should be fixed.~~
-  ==DONE== <del>Socialmedicinsk tidskrift has incongrous filenames in 1955/ socialmedicinsk_tidskrift_1954_*. Needs to be looked at/fixed</del>
-  ==DONE== <del>Diabetes and Status is missing pages. Need to swap in and curate filenames from `/zpool/beast-mirror/actdisease/ocr_output/merged/`</del>
-  ==DONE== <del>Sigyn and homeopatiens image indexes start at 0 and needs fix</del>
-  ==DONE== <del>svenska_lakartidningen multiple years are named "*svenska_läkartidningen" not "svenska_lakartidningen"</del>
-  ==DONE== <del>Import/rename final UUB-files with irregular non-alvin names</del> 
-  ==DONE== <del>Redo incomplete Status and Diabetes with complete actdisease</del>
sources</del>
-  ==DONE== <del><del>Check missing ocr-pages from Fränsta.</del>~~
-  ==DONE== <del>Import/rename all Fränsta-scanned files in: `uub_leverans_002/`, `uub_leverans_003/`, `uub_leverans_004/`</del>
-  ==DONE== <del>Import/rename first batches of UUB-scanned files in: `uub_leverans_001`, `uub_leverans_002`</del>
