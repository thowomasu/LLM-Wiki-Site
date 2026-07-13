# Time-Series To DRT Pipeline Package

Prepared: 2026-06-15

## Short Version

This package contains a research prototype for estimating a DRT-like relaxation
spectrum from current-voltage-time pulse/rest data, then comparing that result
against EIS-derived DRT.

Current status:

- Engineering scaffold: viable for research iteration.
- Scientific method: not validated.
- Current rule-selected median EIS correlation: about 0.141.

Plainly: the pipeline runs, produces auditable outputs, and is now structured
well enough to discuss. It is not yet strong enough to use as a ground-truth
label generator.

## What To Read First

1. `00_Read_First/PLAIN_ENGLISH_OVERVIEW.md`
2. `00_Read_First/DRIVE_CYCLE_DATASET_RECOMMENDATION.md`
3. `00_Read_First/VIABILITY_REPORT.md`
4. `00_Read_First/MEETING_WALKTHROUGH.md`
5. `01_Method_And_Math/CODE_WALKTHROUGH_FOR_PROFESSOR.md`
6. `03_Key_Plots/PLOT_GUIDE.md`
7. `02_Key_Results/Model Rule/model_rule_report.md`

Use the `.html` files for easier reading. The Markdown files are included so the
source text remains editable and inspectable.

## Main Claim

The prototype can:

- load DIB-style battery time-series CSV files
- find pulse/rest windows
- fit a time-domain DRT-like tau/gamma curve
- compare the time-domain curve against EIS-derived DRT
- test SOC mapping assumptions
- test baseline and regularization assumptions
- apply a pre-declared model-selection rule before looking at EIS metrics

The prototype cannot yet claim:

- time-domain DRT is validated against EIS
- the selected pulse windows are exact SOC matches
- the fitted DRT curves are safe training labels
- good voltage reconstruction proves correct gamma shape
- the DIB dataset is a proper drive-cycle dataset

## What I Need Feedback On

The biggest open questions are experimental, not just coding:

- Does the project require a real drive-cycle dataset, such as FUDS, US06, UDDS,
  HWFET, LA92, or WLTP?
- Which exact pulse windows correspond to the EIS SOC labels?
- What is the current sign convention in the time-series files?
- What nominal or measured capacity should be used for SOC reconstruction?
- Are the low-current capacity-check pulses intended to be comparable to EIS?
- Which EIS preprocessing and DRT method should be treated as the reference?
- Can you provide one cell/SOC/temp/SOH example that should be considered a
  trusted matched validation case?

## Reproduction

The code is included in `04_Code/`.

The commands below assume the full project repo layout. The copied code in this
package is mainly for review.

The plotting layer uses Matplotlib with a headless backend. Use a Python
environment with `numpy`, `pandas`, `matplotlib`, and `openpyxl` installed.

The main runner is:

```powershell
python scripts/experiments/run_time_domain_rough_prototype.py
```

For machines without the DIB dataset:

```powershell
python scripts/experiments/run_time_domain_rough_prototype.py --synthetic-only
```

The pre-declared rule can also be applied to the included saved model-sensitivity
summary:

```powershell
python scripts/experiments/time_domain_model_rule.py --from-existing-sensitivity
```

The real-data run expects these environment variables when the DIB dataset is
not in the default location:

```powershell
$env:DIB_DATA_ROOT = "path\to\Rashid and Faraji-Niri DIB battery SOH estimation dataset"
$env:DIB_CAPACITY_ROOT = "path\to\Rashid and Faraji-Niri DIB battery SOH estimation dataset\.csvfiles\Capacity_Check"
$env:DIB_EIS_WORKBOOK = "path\to\Rashid and Faraji-Niri DIB battery SOH estimation dataset\WholeDataRealSOH.xlsx"
```

## What Is Not Included

This package does not include the raw DIB dataset or the full set of large
selected-window CSVs. That is deliberate. The goal is a reviewable handoff, not
a raw data dump.

## Blunt Warning

Do not use these time-domain DRT outputs as labels for model training yet. The
current results are useful for research iteration, but the EIS agreement is too
weak and the SOC/window matching still needs protocol confirmation.

Also: if the professor's requirement is drive-cycle loading, do not defend DIB
as the main dataset. Use DIB for the EIS/pulse prototype only, then switch the
drive-cycle part to a dataset such as CALCE dynamic profiles.
