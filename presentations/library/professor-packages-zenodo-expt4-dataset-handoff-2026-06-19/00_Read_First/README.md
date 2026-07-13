# Read First

This folder is the short version.
Read it before opening the reports.

## What This Package Is

This package explains work done on LG M50T 21700 degradation study, Expt 4 drive-cycle aging from the dataset "Lithium-ion battery degradation: comprehensive cycle ageing data and analysis for commercial 21700 cells."

The original dataset contains raw battery cycler files, processed time-series files, and summary health labels.
The analysis here focuses on Experiment 4, the drive-cycle ageing control experiment.

## What Was Done

- Converted and audited the available Expt4 files.
- Parsed processed GITT, discharge-curve, and hybrid-pulse time series.
- Extracted voltage, pulse, resistance, and DRT-like features.
- Joined those features to health labels from the dataset summary files.
- Ran internal validation checks.
- Ran a leakage audit to catch features that accidentally encode the target.

## What To Open

| Need | Open |
|---|---|
| Short result | `Executive_Summary.md` |
| Scientific warnings | `Limits_And_Caveats.md` |
| Dataset structure | `../01_Dataset_Map/Dataset_Map.md` |
| Column meanings | `../01_Dataset_Map/Column_Guide.md` |
| Pipeline details | `../02_Pipeline_Report/pipeline_readme.md` |
| Browser report | `../02_Pipeline_Report/index.html` |
| Validation audit | `../04_Validation_Audit/README.md` |
| Rerun commands | `../06_Reproduction/REPRODUCIBILITY.md` |

## Bottom Line

The dataset is real and the local Expt4 zip checksum matches Zenodo.
The pipeline works.
The headline modeling claim must stay modest.

Do not present this as proof that DRT peaks are physically validated.
That would be overstating the evidence.
