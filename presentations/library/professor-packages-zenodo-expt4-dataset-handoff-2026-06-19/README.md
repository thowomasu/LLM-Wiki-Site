# LG M50T 21700 degradation dataset, Expt 4 handoff

Prepared: 2026-06-19

This is a curated handoff package for the LG M50T 21700 degradation study, Expt 4 drive-cycle aging battery ageing dataset.
It does not include the full raw dataset because that is large and already has a stable DOI.
It includes the analysis reports, plots, validation audit, and code needed to understand what was done.

## Read This First

Start here:

1. `00_Read_First/README.md`
2. `00_Read_First/Executive_Summary.md`
3. `00_Read_First/Limits_And_Caveats.md`
4. `01_Dataset_Map/Dataset_Map.md`
5. `04_Validation_Audit/README.md`

## Folder Map

| Folder | What it contains | Why it matters |
|---|---|---|
| `00_Read_First/` | Plain-language overview, verdict, caveats, and source notes. | Use this before opening any CSV or report. |
| `01_Dataset_Map/` | Dataset structure, source DOI, checksum note, and column guide. | Explains what Expt4 is and how the files relate. |
| `02_Pipeline_Report/` | Main pipeline report, section reports, CSVs, JSON summaries, and browser report. | Shows the actual analysis workflow and outputs. |
| `03_Key_Plots/` | Curated plots plus sidecar explanations. | Fast visual review without hunting through folders. |
| `04_Validation_Audit/` | Leakage audit and stricter validation results. | Most important folder if judging scientific strength. |
| `05_Code/` | Scripts used for conversion, pipeline generation, visualization, and validation. | Lets someone inspect or rerun the work. |
| `06_Reproduction/` | Reproduction commands and environment notes. | Explains what must exist locally to rerun. |

## Source Dataset

- Zenodo record: https://zenodo.org/records/10637534
- DOI: https://doi.org/10.5281/zenodo.10637534
- Related paper DOI: https://doi.org/10.1016/j.jpowsour.2024.234185
- Expt4 zip listed by Zenodo: `Expt 4 - Drive Cycle Aging (Control).zip`
- Published MD5 for Expt4 zip: `99083707bc7a24e72d9865abac19ce50`

## Honest One-Sentence Verdict

This package shows a working internal health-feature pipeline for LG M50T 21700 Expt 4 drive-cycle aging, but it does not prove DRT physics or EIS validation.
