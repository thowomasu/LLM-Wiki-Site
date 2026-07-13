# Code

This folder contains the scripts relevant to LG M50T 21700 Expt 4 drive-cycle aging.

## Scripts

| Script | Purpose |
|---|---|
| `scripts/zenodo_expt4/zenodo_expt4_raw_to_csv.py` | Converts raw Expt4 files where possible. |
| `scripts/zenodo_expt4/zenodo_expt4_degradation_mpr_to_csv.py` | Converts degradation `.mpr` files using the local converter stack. |
| `scripts/zenodo_expt4/zenodo_expt4_time_series_drt_pipeline.py` | Main Expt4 time-series DRT and health-feature pipeline. |
| `scripts/zenodo_expt4/zenodo_expt4_validation_audit.py` | Leakage and grouped-validation audit. |
| `scripts/zenodo_expt4/zenodo_expt4_run_sx_visualization_all_cell_rig.py` | Visualization helper for cell and rig groups. |
| `scripts/zenodo_expt4/time_domain_zenodo_expt4_manifest.py` | Manifest builder for Expt4 files. |
| `scripts/zenodo_expt4/time_domain_zenodo_expt4_gitt_batch.py` | GITT batch runner. |
| `scripts/time_series_drt_consolidated_pipeline.py` | Shared consolidated pipeline script. |

## Python Environment

The local project used:

```powershell
[local path redacted]
```

The scripts assume access to the original Expt4 dataset path.
They will not fully rerun from this package alone unless that raw dataset exists locally.

## Commenting Note

The code is included for inspection and rerun.
The clearest explanation is in the pipeline docs and validation audit, not buried in code comments.
