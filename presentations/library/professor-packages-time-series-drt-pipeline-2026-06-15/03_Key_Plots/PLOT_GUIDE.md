# Plot Guide

Prepared: 2026-06-15

All plots in this folder were regenerated with Matplotlib from saved CSV and JSON outputs. The raw DIB dataset was not present in this workspace, so plots that need raw DIB files were rebuilt from exported result tables, not from original raw measurements.

Each PNG also has a matching `*_EXPLANATION.md` file. Read that sidecar file when you want the plain-language interpretation of the figure, the main takeaway, and the limitation that should not be overclaimed.

## Existing Key Plots

| Plot | What It Shows | Units |
|---|---|---|
| `synthetic_section_1_plots.png` | Synthetic current input, voltage fit, recovered DRT, and residuals. | Current A, voltage V, residual mV, tau s, gamma mOhm |
| `section_2_window_plot.png` | Accepted pulse/rest windows on synthetic current and voltage. | Time s, current A, voltage V |
| `section_3_candidate_fit_plot.png` | Selected-window fit and recovered DRT. | Local time s, current A, voltage V, residual mV, tau s, gamma mOhm |
| `section_8_cell28_soc_sweep_summary.png` | Cell28 comparison across SOC labels. | SOC %, RMSE mV, DRT area Ohm |
| `section_9_validation_diagnostics.png` | Scale and lambda diagnostics. | SOC %, lambda, correlation, normalized RMSE |
| `section_10_soc_alignment.png` | SOC label versus coulomb-counted SOC. | SOC %, voltage V, error percentage points |
| `dib_batch_summary.png` | Generalized DIB batch validation across cells. | SOC %, RMSE mV, correlation, normalized RMSE, area ratio |

## Added Summary Plots

| Plot | What It Shows | Why It Matters |
|---|---|---|
| `soc_mapping_sensitivity_summary.png` | Whether different SOC mapping assumptions change metrics. | They did not explain the weak EIS match in this small run. |
| `model_sensitivity_summary.png` | How baseline and lambda choices affect metrics. | This is a major weak point. |
| `model_rule_summary.png` | Result after the pre-declared model rule. | The honest rule still gives weak EIS agreement. |

## Blunt Reading

The plots are now readable, but the scientific result did not become prettier. That is good. The figures should not hide the problem.

The story is:

1. The pipeline reconstructs voltage well.
2. The DRT-like shape does not match EIS strongly.
3. SOC uncertainty exists.
4. Model assumptions matter.
5. A drive-cycle dataset is needed if the project claim is about drive-cycle behavior.
