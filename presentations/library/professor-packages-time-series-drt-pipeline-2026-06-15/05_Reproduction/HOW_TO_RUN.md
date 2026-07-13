# How To Run

## Python

Use Python 3 with at least:

- `numpy`
- `pandas`
- `matplotlib`
- `openpyxl`

The EIS comparison path also expects the local pyDRTtools dependency used in
the project environment.

Plots are rendered with Matplotlib's headless `Agg` backend, so a display or GUI
backend is not required.

## Environment Variables

If the DIB dataset is not in the default project path, set:

```powershell
$env:DIB_DATA_ROOT = "path\to\Rashid and Faraji-Niri DIB battery SOH estimation dataset"
$env:DIB_CAPACITY_ROOT = "path\to\Rashid and Faraji-Niri DIB battery SOH estimation dataset\.csvfiles\Capacity_Check"
$env:DIB_EIS_WORKBOOK = "path\to\Rashid and Faraji-Niri DIB battery SOH estimation dataset\WholeDataRealSOH.xlsx"
```

## Synthetic Smoke Test

These commands assume the full project repo layout, with scripts under
`scripts/experiments/`. The copied scripts in this package are mainly for review.

This smoke test does not require raw DIB data:

```powershell
python scripts/experiments/run_time_domain_rough_prototype.py --synthetic-only
```

## Full Pipeline

This requires the DIB capacity CSVs and EIS workbook:

```powershell
python scripts/experiments/run_time_domain_rough_prototype.py
```

## Pre-Declared Model Rule

From saved model-sensitivity output:

```powershell
python scripts/experiments/time_domain_model_rule.py --from-existing-sensitivity
```

From raw DIB data:

```powershell
python scripts/experiments/time_domain_model_rule.py --max-cases 2
```

## Rebuild HTML Reports

```powershell
python scripts/experiments/time_domain_export_html.py
```

## Expected Current Verdict

The current saved outputs should say:

- engineering scaffold: `research_scaffold_viable`
- scientific method: `not_validated`
- rule-selected median EIS correlation: about `0.141`

If a run reports a much stronger result, check whether lambda or baseline was
chosen after looking at EIS. That would be leakage.
