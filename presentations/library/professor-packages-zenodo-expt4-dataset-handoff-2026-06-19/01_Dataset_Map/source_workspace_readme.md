# LG M50T 21700 Expt 4 drive-cycle aging

This folder groups the LG M50T 21700 degradation study, Expt 4 drive-cycle aging work products.

## Folders

- [local converted data not published]: converted BioLogic `.mpt` and `.mpr` files, conversion manifests, logs, and raw-data visualization outputs.
- `02_Time_Series_DRT_Pipeline`: section reports, graphs, notebooks, and summary files for the time-series DRT pipeline.

## Code

Zenodo-specific scripts now live in:

```text
scripts/experiments/zenodo_expt4/
```

Shared time-domain DRT helpers remain in:

```text
scripts/experiments/
```

Use the DRT Python environment for reruns:

```powershell
& "[local path redacted]" scripts\experiments\zenodo_expt4\zenodo_expt4_raw_to_csv.py --dry-run
& "[local path redacted]" scripts\experiments\zenodo_expt4\zenodo_expt4_time_series_drt_pipeline.py --max-batch-files 2
```
