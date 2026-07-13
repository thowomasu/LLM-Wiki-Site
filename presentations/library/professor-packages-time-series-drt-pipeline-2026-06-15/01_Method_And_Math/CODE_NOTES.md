# Prototype Code Notes

For a more detailed professor-facing walkthrough, read
`CODE_WALKTHROUGH_FOR_PROFESSOR.md`. That file explains the main scripts by line
range, units, assumptions, and why each block exists.

## Why These Packages

- `numpy`: core numerical arrays, least-squares solving, interpolation, tau integration, and correlations.
- `pandas`: CSV and Excel tables. The DIB data is table-shaped and has messy headers, so pandas is the practical choice.
- `matplotlib`: report-quality PNG plots using the headless `Agg` backend, so the scripts can render readable analysis figures without opening a GUI.
- `argparse`: command-line flags for repeatable runs.
- `csv`, `json`, and `pathlib`: standard-library output files, metadata, and paths.

## Main Scripts

- `scripts/experiments/time_domain_drt_pilot.py`: synthetic sanity check and core time-domain DRT solver.
- `scripts/experiments/time_domain_window_finder.py`: loads messy battery CSVs and finds pulse/rest windows.
- `scripts/experiments/time_domain_candidate_fit.py`: fits one selected pulse window into a DRT-like tau/gamma curve.
- `scripts/experiments/time_domain_eis_compare.py`: derives an EIS DRT and compares it against a time-domain DRT.
- `scripts/experiments/time_domain_dib_batch.py`: discovers multiple DIB cells, runs the pipeline, and writes batch summaries.
- `scripts/experiments/time_domain_soc_mapping_sensitivity.py`: reruns the same cases under multiple SOC mapping assumptions.
- `scripts/experiments/time_domain_model_sensitivity.py`: reruns matched cases across baseline modes and lambda values.
- `scripts/experiments/time_domain_model_rule.py`: applies the pre-declared model-selection rule before EIS scoring.
- `scripts/experiments/time_domain_viability_report.py`: reads the latest outputs and writes a blunt viability report.
- `scripts/experiments/time_domain_export_html.py`: writes HTML viewing copies of the main Markdown reports.

## Important Variables

- `time_s`: elapsed time in seconds. For DIB files, this must be `Prog Time`, not `Step Time`, because `Step Time` resets.
- `current_a`: applied current in amps. The first batch pass uses low-current discharge pulses because they are closer to small-signal behavior.
- `voltage_v`: measured terminal voltage in volts. The fitter reconstructs this signal.
- `temperature_c`: measured cell temperature. Large drift means the pulse is less comparable to EIS.
- `tau_s`: relaxation time constants in seconds.
- `gamma_ohm`: DRT-like resistance weight at each tau.
- `R0`: instantaneous ohmic resistance.
- `lambda_value`: smoothness strength. Higher values make gamma smoother, but too much smoothing can hide real structure.
- `estimated_soc`: SOC estimate from anchored coulomb counting.
- `soc_error_percent`: `estimated_soc` minus the target EIS SOC label.
- `capacity_ah_used`: capacity estimate read from DIB `AhPrev` or `AhAccu`.
- `cumulative_ah_start`: integrated current at the selected pulse start.
- `quality_pass`: rough engineering triage. It is not scientific validation.
- `quality_flags`: why a row failed triage, such as high voltage RMSE or temperature drift.
- `baseline_mode`: free voltage-baseline model used by the fitter. Options are `offset`, `time`, `charge`, and `time_charge`.
- `time_drift_v_per_s`: linear voltage drift term when a time baseline is enabled.
- `charge_drift_v_per_as`: voltage drift per amp-second, used as a local OCV-change proxy.
- `normalized_rmse`: shape error after normalizing DRT areas, useful when raw EIS and time-domain gamma scales differ.
- `gamma_roughness`: normalized second-difference curvature of the gamma curve. Lower is smoother, not automatically better.
- `band_stability`: how much fast/mid/slow band areas change near a lambda value.
- `selection_score`: internal score used by the model rule. It must not include EIS metrics.
- `model_selection_rule`: explanation of the lambda/baseline rule used after the candidate window is already selected.
- `candidate_selection_rule`: explanation of how the pulse window was selected.

## Current Weak Point

The code can fit and compare curves now. That is not the same as proving the method. The weak point is still experimental alignment: SOC labels, baseline/OCV handling, and whether the selected pulses really excite the same processes as EIS.

The batch runner now uses anchored coulomb counting by default. This is better than pure pre-rest voltage sorting, but it still assumes the highest-voltage selected pulse is the high-SOC anchor and that the raw capacity column is the right scale. Treat it as a useful prototype rule, not ground truth.

The sensitivity runner tests four SOC modes: `voltage`, `coulomb`, `endpoint`, and `linear`. On the first three DIB cases, all four modes selected the same pulse windows, so SOC mapping did not explain the weak EIS agreement.

The model sensitivity runner tests baseline and lambda assumptions. On the first two DIB cases, every target changed correlation by more than 0.1 across model settings. That means baseline/regularization is now the main engineering weak point.

The model-rule runner fixes `time_charge` baseline and chooses lambda from voltage RMSE, gamma roughness, and broad-band stability before EIS metrics are read. On the saved run, it selected 10 rows with 0 errors and 10 quality-pass rows, but median EIS correlation stayed weak at about 0.141.

The viability report currently says `research_scaffold_viable` and `not_validated`. That is the right level of confidence. Use the code to test assumptions. Do not use it yet to generate final training labels.

## Commenting Rule For Future Code

When adding pipeline variables, explain them at the point where they are created:

- unit
- source
- whether it is a measured value, fitted value, assumption, or diagnostic
- whether downstream code treats it as evidence or only as a triage flag

Do not make the next reader reverse-engineer a variable from a CSV column name.
