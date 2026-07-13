# Time Domain DRT Pilot

## Purpose

This folder tracks the time-series-to-DRT prototype section by section.

The current goal is not to train a model. The current goal is to prove that the data pipeline can estimate a DRT-like relaxation spectrum from current-voltage-time data in a controlled setting, then compare it against EIS-derived DRT when real matched data is available.

If you only read three files, read these first:

1. `PLAIN_ENGLISH_OVERVIEW.md`
2. `DRIVE_CYCLE_DATASET_RECOMMENDATION.md`
3. `../01_Method_And_Math/CODE_WALKTHROUGH_FOR_PROFESSOR.md`

The professor's drive-cycle criticism is valid. DIB is useful for pulse/rest and EIS comparison, but it should not be presented as the main drive-cycle dataset.

## One-Command Rough Prototype

Status: complete for first pass.

## Local Data Configuration

The DIB dataset is not stored in this repo. Set these environment variables before running the DIB-dependent sections:

```powershell
$env:DIB_DATA_ROOT = "path\to\Rashid and Faraji-Niri DIB battery SOH estimation dataset"
$env:DIB_CAPACITY_ROOT = "path\to\Rashid and Faraji-Niri DIB battery SOH estimation dataset\.csvfiles\Capacity_Check"
$env:DIB_EIS_WORKBOOK = "path\to\Rashid and Faraji-Niri DIB battery SOH estimation dataset\WholeDataRealSOH.xlsx"
```

`DIB_DATA_ROOT` is enough when the extracted dataset keeps the original DIB folder structure. Use the narrower variables only when your files live somewhere else.

Runner:

`scripts/experiments/run_time_domain_rough_prototype.py`

Command:

```powershell
& "python" "scripts\experiments\run_time_domain_rough_prototype.py"
```

Plotting scripts now use Matplotlib with the headless `Agg` backend. Use a Python environment with `numpy`, `pandas`, and `matplotlib` installed. On this Windows machine, the tested interpreter is:

```powershell
& "[local path redacted]" "scripts\experiments\run_time_domain_rough_prototype.py" --synthetic-only
```

Use `--synthetic-only` if the local DIB folder is not available.

Main handoff:

- `ROUGH_PROTOTYPE_HANDOFF.md`
- `rough_prototype_runner_log.md`

The runner rebuilds the synthetic checks and DIB-format smoke test everywhere. When local DIB data is available, it also rebuilds Cell28 time-domain DRT fits, EIS comparisons, regularization diagnostics, SOC-alignment diagnostics, generalized batch checks, SOC-mapping sensitivity, model sensitivity, the pre-declared model rule, viability reporting, HTML doc mirrors, and the final handoff summary.

Key orientation docs:

- `ASSUMPTIONS.md`
- `CODE_NOTES.md`
- `TIME_DOMAIN_DRT_MATH.md`
- `VIABILITY_REPORT.md`
- `Model Rule/model_rule_report.md`

## Section Status

### first-slice protocol inventory: Synthetic inverse sanity check

Status: complete for first pass.

Script:

`scripts/experiments/time_domain_drt_pilot.py`

Command:

```powershell
& "python" "scripts\experiments\time_domain_drt_pilot.py"
```

Outputs:

- `section_1_synthetic_report.md`
- `synthetic_section_1_timeseries.csv`
- `synthetic_section_1_drt.csv`
- `synthetic_section_1_summary.json`
- `synthetic_section_1_plots.png`

Result:

- Synthetic truth: R0 = 0.002 ohm, RC branches at 8 s, 45 s, and 180 s.
- Recovered R0: about 0.00181 ohm.
- Voltage reconstruction RMSE: about 0.801 mV, close to the injected 0.8 mV noise.
- Fast and mid relaxation bands are recovered reasonably.
- The slow branch is smeared and shifted, which is a warning that exact DRT peak location is fragile in pulse-based time-domain fitting.

Interpretation:

first-slice protocol inventory passes the basic math sanity check. It does not prove the method works on real data.

### file and protocol screen: Real-data input contract and window finder

Status: complete for first pass using the synthetic first-slice protocol inventory CSV.

Script:

`scripts/experiments/time_domain_window_finder.py`

Command:

```powershell
& "python" "scripts\experiments\time_domain_window_finder.py"
```

Outputs:

- `section_2_window_finder_report.md`
- `section_2_window_candidates.csv`
- `section_2_summary.json`
- `section_2_window_plot.png`

Result:

- Loaded 1401 finite rows from `synthetic_section_1_timeseries.csv`.
- Detected 5 pulse/rest candidate windows.
- Accepted all 5 synthetic pulse windows.
- Estimated usable tau ranges per window based on sampling interval and pulse/rest duration.

Interpretation:

file and protocol screen passes the mechanics check. It correctly finds pulse/rest regions on clean synthetic data and exports candidate windows for downstream DRT fitting.

Limits:

- The detector currently assumes step-like current pulses and rests.
- It reports temperature drift but does not reject windows based on it yet.
- Real battery data may need protocol-specific rules and current sign checks.

## Next Section

### HPPC window finder: Candidate-window DRT fit

Status: complete for first pass using the best synthetic file and protocol screen candidate.

Script:

`scripts/experiments/time_domain_candidate_fit.py`

Command:

```powershell
& "python" "scripts\experiments\time_domain_candidate_fit.py"
```

Outputs:

- `section_3_candidate_fit_report.md`
- `section_3_selected_window.csv`
- `section_3_window_drt.csv`
- `section_3_summary.json`
- `section_3_candidate_fit_plot.png`

Result:

- Selected candidate id 5, the highest excitation-score synthetic pulse.
- Fit rows: 245 after including 30 seconds before the pulse and 180 seconds after it.
- Estimated tau range: 2 s to about 81.33 s.
- Recovered R0: about 0.00175 ohm.
- Voltage reconstruction RMSE: about 0.803 mV, close to the injected 0.8 mV noise.
- Recovered fast-band resistance around 10 s and mid-band resistance around 60 s.
- Did not recover the true 180 s branch because this selected window cannot support tau above about 81 s. That is the correct limitation, not a bug.

Interpretation:

HPPC window finder passes the synthetic integration test. The window finder and DRT solver work together on one accepted window.

The important lesson is tau visibility. A single pulse/rest window only supports a bounded tau range. If the window is too short, slow processes are invisible no matter how good the solver is.

### HPPC candidate fit: Real CSV pilot

Status: blocked on real professor/dataset CSV, but complete for DIB-style format smoke test.

Smoke-test script:

`scripts/experiments/time_domain_real_csv_smoke_test.py`

Command:

```powershell
& "python" "scripts\experiments\time_domain_real_csv_smoke_test.py"
```

Smoke-test outputs:

- `section_4_real_csv_smoke_test_report.md`
- `section_4_synthetic_dib_like_timeseries.csv`
- `section_4_window_candidates.csv`
- `section_4_window_summary.json`
- `section_4_window_plot.png`
- `section_4_selected_window.csv`
- `section_4_window_drt.csv`
- `section_4_fit_summary.json`
- `section_4_candidate_fit_plot.png`

Smoke-test result:

- Rewrote the synthetic first-slice protocol inventory signal with DIB-style columns: `Step Time`, `Current`, `Voltage`, `LogTemp001`.
- Loader correctly mapped those columns to `time_s`, `current_a`, `voltage_v`, and `temperature_c`.
- Window finder detected 5 candidates and accepted all 5.
- Candidate-window fit produced the same result family as HPPC window finder: R0 about 0.00175 ohm and voltage RMSE about 0.803 mV.

Interpretation:

HPPC candidate fit proves column compatibility and end-to-end mechanics for a realistic CSV layout. It does not prove real-data performance.

Real CSV pilot:

Use the same file and protocol screen and HPPC window finder scripts on one real battery time-series CSV.

Expected command pattern:

```powershell
& "python" "scripts\experiments\time_domain_window_finder.py" --input "path\to\real_timeseries.csv"
& "python" "scripts\experiments\time_domain_candidate_fit.py" --input "path\to\real_timeseries.csv"
```

Expected checks:

- Does the loader map the real columns correctly?
- Are pulse/rest windows detected?
- Are temperature drift and sampling interval acceptable?
- Does voltage reconstruction look physically sane?
- Is the tau range compatible with the EIS-derived DRT comparison target?

Minimum professor/dataset handoff:

- exact time-series file path or dataset download link
- exact column meanings and units
- current sign convention
- time format and sampling rate
- cell id and cycle/test id
- SOC, SOH, and temperature metadata if available
- matching EIS file or table for the same cell/SOC/temp/SOH condition

### EIS DRT baseline: Real DIB capacity-file pilot

Status: complete for first pass on local DIB time-series data.

Input:

`$DIB_CAPACITY_ROOT\100per_Cells_Capacity_Check_09112021_000cycle\Cell27_100SOH_Capacity_Check_25degC_000cycle.csv`

Key fix:

The DIB CSV has metadata rows before the data table, and both `Step Time` and `Prog Time`. `Step Time` resets at each protocol step, so the loader must use `Prog Time` as the continuous time axis.

Commands:

```powershell
& "python" "scripts\experiments\time_domain_window_finder.py" --input "$DIB_CAPACITY_ROOT\100per_Cells_Capacity_Check_09112021_000cycle\Cell27_100SOH_Capacity_Check_25degC_000cycle.csv" --output-prefix section_5_dib
& "python" "scripts\experiments\time_domain_candidate_fit.py" --input "$DIB_CAPACITY_ROOT\100per_Cells_Capacity_Check_09112021_000cycle\Cell27_100SOH_Capacity_Check_25degC_000cycle.csv" --candidates "40 Outputs\Experiments\Time Domain DRT Pilot\section_5_dib_window_candidates.csv" --candidate-id 12 --include-pre-s 120 --include-post-s 1200 --output-prefix section_5_dib
```

Window finder result:

- Loaded 112531 finite rows.
- Continuous duration: about 103879 s.
- Median sample interval: about 0.998 s.
- Found 27 active-current candidates.
- Accepted 26 candidates.

Candidate fit result:

- Selected candidate id 12, a roughly 30 s, -10 A pulse with long rest before and after.
- Fit rows: 2163.
- Candidate tau range from window finder: about 2 s to 410 s.
- Fit tau range: about 1.95 s to 449 s.
- R0 estimate: about 0.02697 ohm.
- Voltage reconstruction RMSE: about 5.77 mV.
- Main recovered DRT peak: about 113 s.
- Temperature drift inside the pulse candidate: about 0.9 C.

Interpretation:

The local DIB data is usable now. The real-data pipeline runs end to end on one capacity-check file.

But this is not yet matched-pair validation. The selected pulse has noticeable temperature drift, and we have not compared the time-domain DRT against the matching EIS-derived DRT. This is a real-data smoke test, not proof.

Follow-up:

Cell27 is useful as a real-data smoke test, but it is a bad matched-validation target in the local DIB folder because the matching Cell27 EIS files are not present. Do not spend time forcing Cell27 into the validation story.

### time-domain versus EIS bridge comparison: Cell28 matched-data target

Status: complete for first pass.

Reason for switching from Cell27 to Cell28:

Cell28 has both capacity-check time-series data and matching EIS conditions in the local DIB folder. That makes it a real matched-pair candidate instead of just a pulse-fitting example.

Inputs:

- Capacity time series: `$DIB_CAPACITY_ROOT\100per_Cells_Capacity_Check_09112021_000cycle\Cell28_100SOH_Capacity_Check_25degC_000cycle.csv`
- EIS workbook: `$DIB_EIS_WORKBOOK`
- Matching EIS conditions found for Cell28: 100 SOH, 25 C, SOC 5, 20, 50, 70, and 95 percent.

Window-finder command:

```powershell
& "python" "scripts\experiments\time_domain_window_finder.py" --input "$DIB_CAPACITY_ROOT\100per_Cells_Capacity_Check_09112021_000cycle\Cell28_100SOH_Capacity_Check_25degC_000cycle.csv" --output-prefix section_6_cell28
```

Result:

- Loaded 112932 finite rows.
- Continuous duration: about 104275 s.
- Median sample interval: about 0.998 s.
- Found 27 active-current candidates.
- Accepted 26 candidates.

Best first matched candidate:

Candidate id 10 is the cleaner first target because it has a roughly 30 s, -2.5 A pulse, no measured temperature drift in the pulse, and pre-pulse voltage near 4.01 V, which lines up with the 70 percent SOC EIS condition better than the colder-smoke-test Cell27 window.

Candidate-fit command:

```powershell
& "python" "scripts\experiments\time_domain_candidate_fit.py" --input "$DIB_CAPACITY_ROOT\100per_Cells_Capacity_Check_09112021_000cycle\Cell28_100SOH_Capacity_Check_25degC_000cycle.csv" --candidates "40 Outputs\Experiments\Time Domain DRT Pilot\section_6_cell28_window_candidates.csv" --candidate-id 10 --include-pre-s 120 --include-post-s 1200 --output-prefix section_6_cell28_70soc_lowtempdrift
```

Fit result:

- Fit rows: 2163.
- R0 estimate: about 0.02726 ohm.
- Voltage reconstruction RMSE: about 1.44 mV.
- Fit tau range: about 1.94 s to 449 s.
- Main recovered structures: about 45 s, 90 s, and a boundary peak near 449 s.

Interpretation:

This is the strongest real-data time-domain DRT result so far. It reconstructs voltage well and uses a lower-drift pulse near a known EIS SOC point. But the slow boundary peak is not automatically trustworthy. Boundary peaks often mean the selected window is not long enough to resolve the slow process cleanly.

### lambda sensitivity check: Matched Cell28 time-domain DRT versus EIS-derived DRT

Status: complete for first pass, not validated yet.

Script:

`scripts/experiments/time_domain_eis_compare.py`

Comparison target:

- Cell: 28
- SOH: 100
- Temperature: 25 C
- SOC: 70 percent
- Time-domain DRT: `section_6_cell28_70soc_lowtempdrift_window_drt.csv`
- EIS source: `WholeDataRealSOH.xlsx`

pyDRTtools comparison command:

```powershell
& "python" "scripts\experiments\time_domain_eis_compare.py" --time-drt "40 Outputs\Experiments\Time Domain DRT Pilot\section_6_cell28_70soc_lowtempdrift_window_drt.csv" --cell 28 --soh 100 --temp 25 --soc 70 --eis-method pydrttools --output-prefix section_7_cell28_70soc_compare_pydrttools
```

Outputs:

- `section_7_cell28_70soc_compare_pydrttools_comparison_report.md`
- `section_7_cell28_70soc_compare_pydrttools_comparison_summary.json`
- `section_7_cell28_70soc_compare_pydrttools_comparison_plot.png`
- `section_7_cell28_70soc_compare_pydrttools_eis_drt.csv`
- `section_7_cell28_70soc_compare_pydrttools_overlap_comparison.csv`

Result:

- EIS points used: 46 out of 61.
- EIS tau range: about 0.001 s to 316 s.
- Overlap tau range: about 1.94 s to 316 s.
- Overlap correlation: about 0.12.
- Time-domain overlap area: about 0.00191.
- EIS overlap area: about 0.01705.

Interpretation:

This does not validate the time-domain DRT yet. The two DRTs have weak shape agreement and very different area. That could mean the time-domain inverse is underestimating polarization resistance, the EIS DRT settings are not comparable, the selected pulse does not excite the same processes, or the SOC match is approximate.

The next serious step is repeatability:

- run the same comparison for Cell28 at SOC 95, 50, 20, and 5 percent where suitable pulse windows exist
- compare band areas instead of exact peak positions
- tune the time-domain regularization and EIS DRT regularization as a pair
- check whether repeated pulses at the same approximate SOC give similar band areas

Blunt takeaway:

One matched-pair plot is not evidence. A small table across SOC points is evidence. If the trend is not repeatable, the pipeline is still a curve generator, not a measurement pipeline.

### combined EIS and time-domain DRT prototype: Cell28 SOC sweep

Status: complete for first pass, not validated yet.

Script:

`scripts/experiments/time_domain_cell28_soc_sweep.py`

Command:

```powershell
& "python" "scripts\experiments\time_domain_cell28_soc_sweep.py"
```

Purpose:

combined EIS and time-domain DRT prototype repeats the Cell28 matched comparison across SOC points using the lower-current pulse windows. This is the first useful validation table.

Cases:

| SOC percent | Candidate | Pre-rest V | Temp drift C | Time RMSE mV | Corr | Time overlap area | EIS overlap area |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 95 | 6 | 4.16472 | 0.0 | 1.492 | -0.0417 | 0.00139 | 0.01220 |
| 70 | 10 | 4.01062 | 0.0 | 1.437 | 0.1209 | 0.00191 | 0.01705 |
| 50 | 14 | 3.70286 | 0.0 | 1.427 | 0.0848 | 0.00128 | 0.01233 |
| 20 | 20 | 3.46115 | 0.1 | 1.493 | 0.1907 | 0.00105 | 0.04803 |
| 5 | 24 | 3.18030 | 0.2 | 2.277 | 0.1092 | 0.00185 | 0.07002 |

Outputs:

- `section_8_cell28_soc_sweep_report.md`
- `section_8_cell28_soc_sweep_summary.csv`
- `section_8_cell28_soc_sweep_summary.json`
- `section_8_cell28_soc_sweep_summary.png`
- per-SOC time-domain fit files: `section_8_cell28_*soc_*`
- per-SOC EIS comparison files: `section_8_cell28_*soc_compare_pydrttools_*`

Interpretation:

The time-domain voltage fits are good across SOC, roughly 1.4 mV to 2.3 mV RMSE. That means the model can explain the local voltage window.

But the matched EIS comparison is weak. Correlations stay low, and the EIS overlap area grows strongly at low SOC while the time-domain overlap area stays small. That means the present time-domain DRT pipeline is not yet a validated substitute for EIS-derived DRT.

This is still progress. We now have a repeatable validation harness instead of one cherry-picked plot.

Next technical questions:

- Is the time-domain solver underestimating gamma because of scaling, regularization, or baseline drift handling?
- Does a 30 s pulse with 1200 s post-rest actually excite the same tau content as the EIS spectrum?
- Should validation compare broad band areas after normalization instead of raw gamma magnitude?
- Should SOC be assigned by integrated capacity rather than pre-rest voltage?

Blunt takeaway:

The pipeline is mechanically real now. Scientifically, it is not proven. The next job is to find out whether the mismatch is a bug, a modeling assumption, or a real limitation of pulse-only time-domain data.

### time-series 2D DRT surface: Validation diagnostics

Status: complete for first pass.

Script:

`scripts/experiments/time_domain_validation_diagnostics.py`

Command:

```powershell
& "python" "scripts\experiments\time_domain_validation_diagnostics.py"
```

Purpose:

time-series 2D DRT surface checks whether the combined EIS and time-domain DRT prototype mismatch is mostly a scale problem or a shape problem. This matters because a constant scale problem could be fixed by units or normalization. A shape problem means the time-domain inverse is not measuring the same thing as EIS under the current assumptions.

Outputs:

- `section_9_validation_diagnostics_report.md`
- `section_9_scale_diagnostics.csv`
- `section_9_lambda_sweep_70soc.csv`
- `section_9_validation_diagnostics.json`
- `section_9_validation_diagnostics.png`

Scale diagnostic result:

| SOC percent | Corr | EIS/time area ratio | Best scale time to EIS | Normalized RMSE |
|---:|---:|---:|---:|---:|
| 95 | -0.0417 | 8.79 | 0.412 | 0.861 |
| 70 | 0.1209 | 8.91 | 0.626 | 0.875 |
| 50 | 0.0848 | 9.63 | 0.608 | 0.891 |
| 20 | 0.1907 | 45.66 | 3.598 | 0.904 |
| 5 | 0.1092 | 37.79 | 1.978 | 1.091 |

Interpretation:

This is not just a constant unit-conversion problem. The best scale factor varies by SOC, and the low-SOC EIS/time area ratio is much larger than the high-SOC ratio.

70 percent SOC lambda sweep result:

- Default lambda 0.001 gives correlation about 0.121 and normalized RMSE about 0.875.
- Lambda 0.3 gives the best correlation in the tested range, about 0.353.
- Lambda 3.0 gives the best normalized RMSE in the tested range, about 0.259, but correlation drops to about 0.281.
- Voltage RMSE barely changes across the sweep, staying around 1.437 mV.

Interpretation:

The default time-domain regularization was probably too weak for EIS comparison. Stronger smoothing makes the time-domain curve less spiky and more EIS-like.

But this does not validate the method. Heavier smoothing can make curves look more similar while destroying interpretability. If the regularization has to be tuned against EIS, then it must be selected by a transparent rule, not by eyeballing the best plot.

Next serious target:

Validate the metadata and baseline before changing the model:

- compute SOC from capacity integration in the capacity-check file
- verify that candidate windows actually correspond to the EIS SOC labels
- estimate and subtract OCV/baseline from rest periods more carefully
- compare discharge and charge pulses separately
- rerun combined EIS and time-domain DRT prototype with a pre-declared lambda rule

Blunt takeaway:

The mismatch survived scale diagnostics. Regularization helps one case, but it is not a clean fix. The weak point is now experimental alignment and baseline modeling, not whether Python can draw a DRT curve.

### EIS 2D DRT surface: SOC alignment diagnostic

Status: complete for first pass.

Script:

`scripts/experiments/time_domain_soc_alignment.py`

Command:

```powershell
& "python" "scripts\experiments\time_domain_soc_alignment.py"
```

Purpose:

EIS 2D DRT surface checks whether the pulse windows used for matched EIS validation line up with the intended EIS SOC labels. Earlier matching mostly used pre-rest voltage. This section adds coulomb counting from the measured current.

Capacity clues from the raw Cell28 CSV:

- `AhAccu` max absolute value: about 4.956 Ah
- `AhPrev` max absolute value: about 4.962 Ah
- endpoint capacity implied by the 95 to 5 percent matched cases: about 5.112 Ah

Matched-case result using candidate 6 as the 95 percent SOC anchor and 4.962 Ah capacity:

| EIS SOC label | Candidate | Pre-rest V | Coulomb-count SOC | Error |
|---:|---:|---:|---:|---:|
| 95 | 6 | 4.16472 | 95.00 | 0.00 |
| 70 | 10 | 4.01062 | 76.07 | +6.07 |
| 50 | 14 | 3.70286 | 46.55 | -3.45 |
| 20 | 20 | 3.46115 | 17.03 | -2.97 |
| 5 | 24 | 3.18030 | 2.28 | -2.72 |

Outputs:

- `section_10_soc_alignment_report.md`
- `section_10_matched_soc_alignment.csv`
- `section_10_all_candidate_soc_alignment.csv`
- `section_10_soc_alignment_summary.json`
- `section_10_soc_alignment.png`

Interpretation:

The SOC labels are plausible but not exact under simple coulomb counting. The 70 percent case is the biggest problem: it looks closer to 75 to 77 percent SOC depending on the capacity rule.

This weakens the clean "matched-pair validation" story. It does not prove the time-domain DRT is wrong, and it does not prove EIS comparison is wrong. It proves the matching metadata is not tight enough yet.

Next serious target:

- ask for exact protocol annotations that say which pulse windows correspond to which SOC targets
- compute SOC by protocol-aware capacity integration, not just a single anchor
- rerun combined EIS and time-domain DRT prototype using windows whose integrated SOC is closest to the EIS SOC label
- compare candidate 10 against interpolated EIS DRT between 70 and 95 SOC if exact SOC is unavailable

Blunt takeaway:

The current validation is contaminated by SOC uncertainty. Do not present the 70 percent comparison as exact. Present it as an approximate matched case and say the next task is protocol-aware SOC reconstruction.

### time-series versus EIS 2D comparison: Generalized DIB batch runner

Status: complete for first pass.

Script:

`scripts/experiments/time_domain_dib_batch.py`

Command:

```powershell
& "python" "scripts\experiments\time_domain_dib_batch.py" --max-cases 3 --soc-selection coulomb
```

Purpose:

time-series versus EIS 2D comparison tests whether the prototype can run on multiple DIB cells instead of only the hand-picked Cell28 case.

What it does:

- discovers DIB capacity-check CSV files
- discovers matching EIS rows from `WholeDataRealSOH.xlsx`
- restricts the first generalized comparison to 25 C, because DIB capacity CSVs are 25 C
- selects the earliest cycle per cell/SOH/temp by default, because those files have the pulse-rich RPT pattern
- chooses likely SOC pulse windows with anchored coulomb counting by default
- also supports `--soc-selection voltage`, `--soc-selection endpoint`, and `--soc-selection linear` for assumption testing
- fits time-domain DRT for each selected pulse window
- compares each fitted time-domain DRT against pyDRTtools-derived EIS DRT

Outputs:

- `DIB Batch/dib_batch_results.csv`
- `DIB Batch/dib_batch_errors.csv`
- `DIB Batch/dib_batch_selected_cases.csv`
- `DIB Batch/dib_batch_case_summaries.json`
- `DIB Batch/dib_batch_summary.png`
- `DIB Batch/dib_batch_report.md`

First generalized run:

- Selected capacity cases: 3
- Cells processed: 15, 18, and 20
- SOH labels processed: 80 and 85
- SOC comparisons produced: 15
- Errors: 0
- Median voltage RMSE: about 1.586 mV
- Median EIS correlation: about 0.105
- Quality-pass comparisons: 15 of 15
- Quality flag counts: none in this small run
- Median absolute SOC selection error: about 3.004 percentage points
- Max absolute SOC selection error: about 6.069 percentage points

New batch result columns:

- `soc_selection_method`: whether the row came from anchored coulomb counting or voltage sorting.
- `estimated_soc`: SOC estimated from integrated current and the raw capacity column.
- `soc_error_percent`: `estimated_soc` minus the target EIS SOC label.
- `capacity_ah_used`: capacity estimate pulled from `AhPrev` or `AhAccu`.
- `soc_anchor_candidate_id`: high-voltage pulse used as the high-SOC anchor.
- `cumulative_ah_start`: integrated current at the start of the selected pulse.
- `shape_corr`: same value family as overlap correlation, included with the other shape metrics.
- `area_ratio_eis_over_time`: EIS DRT overlap area divided by time-domain DRT overlap area.
- `best_scale_time_to_eis`: least-squares scale factor that best maps time-domain gamma onto EIS gamma over the shared tau grid.
- `scaled_rmse`: RMSE after applying the best scale factor.
- `normalized_rmse`: scaled RMSE divided by the EIS gamma norm, useful for comparing cases with different absolute DRT size.
- `quality_pass`: basic engineering triage result.
- `quality_flags`: comma-separated reasons when a row fails triage, for example high voltage RMSE, high temperature drift, weak current excitation, or too few shared tau points.

Interpretation:

The generalized DIB pipeline works mechanically across multiple cells. It can discover files, load DIB CSVs, find pulse windows, select SOC-like windows, fit time-domain DRT, and compare against matched 25 C EIS rows.

But the validation remains weak. EIS correlations are still low. The new quality gates only say the selected windows are not obviously broken under simple engineering checks. They do not say the time-domain DRT agrees with EIS in a scientifically strong way.

The SOC assignment is now better than pure voltage sorting, but it is still anchored coulomb counting. It assumes the highest-voltage selected pulse is the high-SOC anchor and that `AhPrev` or `AhAccu` is the right capacity scale. That is defensible for a prototype. It is not enough for a thesis claim without protocol confirmation.

Important correction:

Do not use the latest aged-cycle capacity files by default for this prototype. Many latest-cycle files contain only two long charge/discharge segments, which are poor DRT excitation windows. The earliest-cycle files contain the pulse-rich protocol needed by the current solver.

Blunt takeaway:

The prototype is now generalized enough to test DIB cells. It is not yet smart enough to choose scientifically perfect windows. The next fix is professor/protocol-confirmed SOC reconstruction and stronger quality gates tied to the experiment protocol, not more plotting.

### multi-cell 2D batch check: SOC mapping sensitivity

Status: complete for first pass.

Script:

`scripts/experiments/time_domain_soc_mapping_sensitivity.py`

Command:

```powershell
& "python" "scripts\experiments\time_domain_soc_mapping_sensitivity.py" --max-cases 3
```

Purpose:

multi-cell 2D batch check treats SOC matching as an assumption layer instead of pretending it is known ground truth. It reruns the same three DIB cases under four SOC mapping modes:

- `voltage`: assign SOC by pre-rest voltage order.
- `coulomb`: anchor the highest-voltage pulse at 95 percent SOC, then use integrated current and raw capacity.
- `endpoint`: force the highest-voltage pulse to 95 percent and the lowest-voltage pulse to 5 percent.
- `linear`: fit SOC labels against integrated Ah from voltage-ranked candidates.

Outputs:

- `SOC Mapping Sensitivity/soc_mapping_sensitivity_results.csv`
- `SOC Mapping Sensitivity/soc_mapping_sensitivity_mode_summary.csv`
- `SOC Mapping Sensitivity/soc_mapping_sensitivity_by_target.csv`
- `SOC Mapping Sensitivity/soc_mapping_sensitivity_case_summaries.json`
- `SOC Mapping Sensitivity/soc_mapping_sensitivity_errors.csv`
- `SOC Mapping Sensitivity/soc_mapping_sensitivity_report.md`

Result:

- Total comparisons: 60
- Errors: 0
- Unique time-domain fits needed after caching: 15
- Targets with different candidate IDs across modes: 0
- Targets with correlation range above 0.1 across modes: 0
- Median EIS correlation under every mode: about 0.105
- Median normalized RMSE under every mode: about 0.866

Interpretation:

For these first three DIB cases, SOC mapping assumptions do not change the selected pulse windows. The weak EIS agreement survives all four mapping assumptions.

That is not proof that the method fails. It means the current mismatch is probably not just an artifact of voltage sorting versus coulomb counting. The next weak points are time-domain model assumptions, EIS/time-domain comparability, baseline handling, and regularization.

Blunt takeaway:

Good news: the prototype is less fragile to SOC mapping than expected on this small run. Bad news: the EIS mismatch is still there, so SOC mapping was not the easy excuse.

### multi-temperature 2D batch check: Model sensitivity

Status: complete for first pass.

Script:

`scripts/experiments/time_domain_model_sensitivity.py`

Command:

```powershell
& "python" "scripts\experiments\time_domain_model_sensitivity.py" --max-cases 2
```

Purpose:

multi-temperature 2D batch check tests whether EIS agreement changes when the time-domain model assumptions change. It varies:

- baseline mode: `offset`, `charge`, and `time_charge`
- DRT smoothness strength: lambda values `0.001`, `0.1`, `1.0`, and `3.0`
- SOC selection fixed at `coulomb`

Outputs:

- `Model Sensitivity/model_sensitivity_results.csv`
- `Model Sensitivity/model_sensitivity_setting_summary.csv`
- `Model Sensitivity/model_sensitivity_by_target.csv`
- `Model Sensitivity/model_sensitivity_case_summaries.json`
- `Model Sensitivity/model_sensitivity_errors.csv`
- `Model Sensitivity/model_sensitivity_report.md`

Result:

- Total comparisons: 120
- Errors: 0
- EIS cache entries: 10
- Quality-pass comparisons: 112 of 120
- Main quality flag: 8 high-voltage-RMSE rows
- Best median normalized RMSE: `time_charge`, lambda `3.0`, about `0.301`
- Best median correlation: `offset`, lambda `3.0`, about `0.374`
- Targets with correlation range above 0.1 across model settings: 10 of 10

Interpretation:

The EIS comparison is highly sensitive to baseline and regularization choices. That is the biggest weak point right now.

Stronger smoothing often improves normalized shape metrics while barely changing voltage RMSE. That does not automatically mean the smoother DRT is more correct. It may just mean the curve became easier to match after removing structure.

Blunt takeaway:

SOC mapping was not the easy excuse. Model assumptions are now the main suspect. Do not pick the prettiest baseline/lambda after seeing EIS. Define the rule first, then test it.

### combined DRT mirror check: Viability report

Status: complete for first pass.

Script:

`scripts/experiments/time_domain_viability_report.py`

Command:

```powershell
& "python" "scripts\experiments\time_domain_viability_report.py"
```

Outputs:

- `VIABILITY_REPORT.md`
- `viability_summary.json`

Current verdict:

- Engineering scaffold: `research_scaffold_viable`
- Scientific method: `not_validated`
- Synthetic inverse check: pass, RMSE about `0.801` mV
- DIB batch runner: pass, 15 rows, 0 errors, 15 quality-pass rows
- SOC mapping sensitivity: pass, 4 modes, 0 errors
- Model sensitivity: pass, 120 rows, 0 errors, 112 quality-pass rows
- Pre-declared model rule: pass, 10 selected rows, 0 errors, 10 quality-pass rows
- Batch median EIS correlation: about `0.105`
- Rule-selected median EIS correlation: about `0.141`
- Model-sensitive targets: 10

Interpretation:

The code is viable enough to use for research iteration. It is not viable as a training-label generator yet.

The next required move is to run the pre-declared model rule on more cells after protocol metadata is confirmed. If rule-selected outputs still disagree with EIS, the method is not validated.

Blunt takeaway:

The prototype is now useful. It is still not scientifically proven. Training a model now would train on unresolved preprocessing assumptions.

### failure-mode audit: Pre-declared model rule

Status: complete for first pass.

Script:

`scripts/experiments/time_domain_model_rule.py`

Command using existing model-sensitivity outputs:

```powershell
& "python" "scripts\experiments\time_domain_model_rule.py" --from-existing-sensitivity
```

Command from raw DIB files when available:

```powershell
& "python" "scripts\experiments\time_domain_model_rule.py" --max-cases 2
```

Outputs:

- `Model Rule/model_rule_report.md`
- `Model Rule/model_rule_results.csv`
- `Model Rule/model_rule_lambda_candidates.csv`
- `Model Rule/model_rule_errors.csv`
- `Model Rule/model_rule_case_summaries.json`

Current result:

- Selected comparisons: 10
- Lambda candidates scored: 40
- Errors: 0
- Quality-pass comparisons: 10 of 10
- Median voltage RMSE: about `1.711` mV
- Median EIS correlation after rule selection: about `0.141`
- Median normalized RMSE after rule selection: about `0.978`
- Selected lambda: `0.001` for every saved target in this first rule run

Interpretation:

This makes the pipeline more honest because lambda is selected without using EIS agreement. It also makes the bad news harder to dodge: the rule-selected EIS comparison is still weak.

Blunt takeaway:

The pipeline is now viable as a research scaffold. It is still not validated as a measurement method.

### weighting probe: HTML documentation export

Status: complete for first pass.

Script:

`scripts/experiments/time_domain_export_html.py`

Command:

```powershell
& "python" "scripts\experiments\time_domain_export_html.py"
```

Purpose:

The Markdown files remain the source of truth because this is an Obsidian vault. The HTML files are viewing copies with better spacing, tables, and typography.

The math HTML uses MathJax to render LaTeX equations. If the browser is offline, the raw TeX will still be visible but may not render prettily.

Current HTML mirrors:

- `README.html`
- `ROUGH_PROTOTYPE_HANDOFF.html`
- `ASSUMPTIONS.html`
- `CODE_NOTES.html`
- `TIME_DOMAIN_DRT_MATH.html`
- `VIABILITY_REPORT.html`
- `Model Rule/model_rule_report.html`

## Earlier HPPC window finder Implementation Target

Use the accepted candidate windows from file and protocol screen and fit time-domain DRT on one selected pulse/rest window.

Expected inputs:

- `section_2_window_candidates.csv`
- real or synthetic time-series CSV

Expected outputs:

- selected window CSV
- measured versus reconstructed voltage plot
- DRT curve for that window
- residual plot
- fit quality summary

The first version should run on the synthetic data. After the professor gives the real dataset, the same script should run on a real pulse/rest window.

## file and protocol screen Implementation Target

Build a loader that accepts real battery time-series files with:

- time
- current
- voltage
- temperature
- optional cell, cycle, SOC, SOH metadata

Then identify pulse/rest windows and compute quality flags:

- median sampling interval
- current step size
- rest duration
- temperature drift
- voltage missingness
- current excitation score
- usable tau range

This section should not fit DRT yet. Its job is to stop bad windows from entering the solver.

## Blunt Warning

The solver will always return a curve. A curve is not evidence. The evidence comes from reconstruction error, excitation quality, repeatability, and matched EIS comparison.
