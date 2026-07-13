# Reproducibility

## Interpreter

Use the DRT conda environment for this project:

```powershell
& "[local path redacted]" -c "import sys; print(sys.executable)"
```

## Regenerate The Package

```powershell
& "[local path redacted]" scripts\experiments\zenodo_expt4\zenodo_expt4_time_series_drt_pipeline.py
```

Optional smaller smoke run:

```powershell
& "[local path redacted]" scripts\experiments\zenodo_expt4\zenodo_expt4_time_series_drt_pipeline.py --max-batch-files 2
```

## Inputs Expected

- Converted raw CSV root: `[local path redacted]`
- Raw LG M50T 21700 Expt 4 drive-cycle aging root: `[local path redacted]`

## Outputs To Check

- `../index.html`: browser entry point.
- `../README.html`: package overview.
- `../02_Section_Results/**/*.html`: HTML copies of section reports.
- `../02_Section_Results/**/*.csv`: normalized data, windows, DRT vectors, and batch tables.
- `../02_Section_Results/**/*.json`: run summaries.

## Quality Gate

After regenerating the package, run the vault checks before committing:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/wiki.ps1 build
powershell -ExecutionPolicy Bypass -File scripts/wiki.ps1 lint
powershell -ExecutionPolicy Bypass -File scripts/wiki.ps1 source-lint
```
