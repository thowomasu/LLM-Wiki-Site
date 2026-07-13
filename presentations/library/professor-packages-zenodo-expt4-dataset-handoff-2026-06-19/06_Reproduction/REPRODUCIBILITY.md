# Reproducibility

## What You Need

To rerun the full analysis, you need:

1. The original LG M50T 21700 Expt 4 drive-cycle aging dataset zip.
2. The extracted local dataset folder.
3. The DRT Python environment.
4. The scripts in `../05_Code/scripts/`.

## Expected Dataset Location

The current scripts were run against:

```text
[local path redacted]
```

If the dataset is somewhere else, update the paths in the scripts or pass equivalent arguments if available.

## Environment

Use:

```powershell
& "[local path redacted]" -c "import sys; print(sys.executable)"
```

Expected output:

```text
[local path redacted]
```

## Example Commands

Dry-run conversion:

```powershell
& "[local path redacted]" ..\05_Code\scripts\zenodo_expt4\zenodo_expt4_raw_to_csv.py --dry-run
```

Run the Expt4 pipeline on a small batch:

```powershell
& "[local path redacted]" ..\05_Code\scripts\zenodo_expt4\zenodo_expt4_time_series_drt_pipeline.py --max-batch-files 2
```

Run the validation audit:

```powershell
& "[local path redacted]" ..\05_Code\scripts\zenodo_expt4\zenodo_expt4_validation_audit.py
```

## Reproduction Limits

This package is not a standalone copy of the raw dataset.
That is intentional.
The raw dataset is large and should be pulled from Zenodo using the DOI.

The package is meant for review, explanation, and rerun support.
It is not meant to replace the source dataset.
