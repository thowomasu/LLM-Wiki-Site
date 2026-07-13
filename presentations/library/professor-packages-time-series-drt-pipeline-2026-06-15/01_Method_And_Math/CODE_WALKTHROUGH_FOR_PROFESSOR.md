# Code Walkthrough For Professor

Prepared: 2026-06-15

## How To Read This

This is a line-by-line style map of the main scripts. It uses line ranges instead of repeating every source line in full. That is intentional. Explaining every import, blank line, and closing parenthesis separately would add bulk without adding understanding.

The useful question is: what does each block do, what units does it use, and what assumption does it make?

## Execution Order

Use this order when reviewing the package:

1. `run_time_domain_rough_prototype.py`
2. `time_domain_drt_pilot.py`
3. `time_domain_window_finder.py`
4. `time_domain_candidate_fit.py`
5. `time_domain_eis_compare.py`
6. `time_domain_cell28_soc_sweep.py`
7. `time_domain_soc_alignment.py`
8. `time_domain_dib_batch.py`
9. `time_domain_soc_mapping_sensitivity.py`
10. `time_domain_model_sensitivity.py`
11. `time_domain_model_rule.py`
12. `time_domain_viability_report.py`
13. `time_domain_package_plots.py`

## Shared Vocabulary

| Name | Unit | Meaning |
|---|---:|---|
| `time_s` | s | Continuous elapsed time. For DIB files this must be `Prog Time`, not `Step Time`, because `Step Time` resets at each protocol step. |
| `current_a` | A | Applied current. Sign convention still needs protocol confirmation. |
| `voltage_v` | V | Measured terminal voltage. This is the signal the model reconstructs. |
| `temperature_c` | C | Measured cell temperature. High drift weakens the comparison to EIS. |
| `tau_s` | s | Relaxation time constant. Plotted on a log scale. |
| `gamma_ohm` | Ohm | DRT-like resistance weight at each tau. |
| `R0` | Ohm | Instantaneous ohmic resistance term. |
| `lambda_value` | none | Smoothness strength. Larger values make gamma smoother. |
| `rmse_mv` | mV | Voltage reconstruction error. Good RMSE does not prove the DRT shape is correct. |
| `overlap_corr_gamma` | none | Shape correlation between time-domain gamma and EIS gamma on the shared tau range. |
| `normalized_rmse` | none | Shape error after scaling the time-domain gamma to EIS. |

## Main Runner

File: `scripts/experiments/run_time_domain_rough_prototype.py`

| Lines | What The Code Does | Why It Matters |
|---:|---|---|
| 1-24 | Imports standard libraries and shared path helpers. | Keeps the runner portable inside the repo. |
| 27-28 | Defines `PROJECT_ROOT` and `OUTPUT_DIR`. | Every output is written under the experiment folder. |
| 31-66 | `run_step` runs one script as a subprocess, captures output, records exit code, and writes a log entry. | This is the audit trail. If one step fails, the log says which one. |
| 68-77 | `scrub_log_text` removes local absolute paths from logs. | Prevents private local folder paths from leaking into the professor package. |
| 79-97 | Loads JSON and CSV result files. | Used later to build a readable final summary. |
| 99-126 | Converts values to floats, computes medians, counts boolean values, and formats numbers. | Keeps the summary stable even when files contain missing values. |
| 128-393 | `write_final_summary` reads all output summaries and writes the handoff report. | This is where results become a readable narrative. |
| 396-512 | `main` parses flags, decides whether raw DIB data is available, runs each pipeline section, and writes logs. | This is the full workflow controller. |
| 514 | Calls `main` when the script is run directly. | Standard Python entry point. |

## Synthetic Solver

File: `scripts/experiments/time_domain_drt_pilot.py`

| Lines | What The Code Does | Why It Matters |
|---:|---|---|
| 52-60 | Defines `SyntheticCell`, including R0 and true RC branches. | This creates a known answer. Without a known answer, the first validation would be circular. |
| 63-80 | Builds the synthetic pulse-current pattern. | Creates step-like current excitation in amps. |
| 83-97 | Computes exact RC voltage response for a tau value. | This simulates physical relaxation after current changes. |
| 100-138 | Builds voltage from baseline, R0, RC branches, and noise. | Produces the synthetic current-voltage-time dataset. |
| 141-197 | Builds integration utilities, tau grid, and kernel matrix. | Converts current history into candidate relaxation responses. |
| 199-267 | Builds smoothness penalty and nonnegative least-squares solver. | Enforces gamma to be physically nonnegative and not absurdly jagged. |
| 269-363 | Handles baseline terms and free coefficients. | Separates slow voltage drift from relaxation behavior. |
| 365-414 | Fits the time-domain DRT. | Main inverse step: current and voltage in, tau/gamma curve out. |
| 416-447 | Summarizes peaks and broad tau bands. | Makes the DRT result readable without inspecting every tau point. |
| 449-594 | Writes CSVs and Matplotlib plots. | Saves evidence, not just terminal output. |
| 597-656 | Writes the first-slice protocol inventory report. | Explains whether the synthetic sanity check passed. |
| 659-726 | Main workflow for first-slice protocol inventory. | Runs simulation, fit, plots, and report. |

## Window Finder

File: `scripts/experiments/time_domain_window_finder.py`

| Lines | What The Code Does | Why It Matters |
|---:|---|---|
| 48-62 | Sets project paths and acceptable column names. | Allows messy CSVs to be mapped into a standard schema. |
| 68-82 | Finds the first matching column for each logical name. | Example: `Prog Time` can become `time_s`. |
| 84-102 | Detects where the real CSV header starts. | DIB files have metadata rows before the table. |
| 104-126 | Converts time columns into seconds. | Required because time can appear as numeric seconds or clock-like strings. |
| 128-159 | Loads a time-series CSV and returns standardized columns. | Produces `time_s`, `current_a`, `voltage_v`, and optional `temperature_c`. |
| 161-173 | Removes rows with missing core values and estimates sample interval. | Prevents bad rows from entering the detector. |
| 175-185 | Defines rest and step thresholds from the current signal. | Avoids hard-coding one current threshold for every dataset. |
| 187-217 | Finds contiguous active-current regions and rest durations before and after them. | This is how pulse/rest windows are discovered. |
| 219-228 | Scores a window by current step size, pulse length, and rest length. | Better windows should have stronger excitation and enough relaxation time. |
| 230-326 | Builds the candidate window table and quality summary. | This is the core detector. |
| 328-391 | Writes CSV and Matplotlib window plot. | Makes the detector auditable. |
| 394-458 | Writes a plain report explaining accepted and rejected windows. | The professor can see why a window was chosen. |
| 460-478 | Parses command-line arguments and runs the finder. | Lets the same script run on synthetic, DIB, or future drive-cycle CSVs. |

## Candidate Fit

File: `scripts/experiments/time_domain_candidate_fit.py`

| Lines | What The Code Does | Why It Matters |
|---:|---|---|
| 54-62 | Sets paths for default input and candidate files. | Default mode uses the synthetic outputs from first-slice protocol inventory and file and protocol screen. |
| 65-90 | Loads accepted candidates and chooses one candidate by ID or score. | Prevents fitting rejected windows. |
| 92-108 | Slices the time-series data around the chosen pulse. | Adds pre-rest and post-rest context around the pulse. |
| 110-128 | Estimates a simple voltage trend. | Helps separate baseline drift from relaxation. |
| 130-161 | Calls the DRT fitter and attaches metadata. | This is the actual selected-window inverse fit. |
| 163-171 | Writes CSV rows. | Saves selected window data and DRT curve. |
| 173-242 | Writes the candidate-fit plot. | Shows current, measured voltage, fitted voltage, DRT weights, and residuals. |
| 245-312 | Writes the candidate-fit report. | Explains fit quality and tau limits. |
| 314-328 | Converts numpy values into JSON-safe values. | Prevents broken JSON files. |
| 330-409 | Parses command-line options and writes all outputs. | Makes the fit reproducible from the terminal. |

## EIS Comparison

File: `scripts/experiments/time_domain_eis_compare.py`

| Lines | What The Code Does | Why It Matters |
|---:|---|---|
| 25-38 | Loads the matching EIS row for cell, SOH, temperature, and SOC. | This defines the comparison target. |
| 40-50 | Loads the time-domain DRT CSV. | Brings in the fitted tau/gamma curve. |
| 52-76 | Computes an EIS-derived DRT using the selected method. | Creates the reference curve. |
| 78-122 | Interpolates both curves on shared log-tau points and computes shape metrics. | Comparison is only fair over the overlap range. |
| 124-177 | Writes comparison CSV and plot. | Saves the evidence behind the correlation number. |
| 180-230 | Writes the comparison report. | Makes clear whether the match is strong or weak. |
| 232-269 | Parses command-line inputs and runs the comparison. | Allows repeated comparisons across SOC. |

## DIB Batch Runner

File: `scripts/experiments/time_domain_dib_batch.py`

| Lines | What The Code Does | Why It Matters |
|---:|---|---|
| 54-70 | Defines paths for raw DIB data, capacity CSVs, EIS workbook, and batch outputs. | These are not stored in the repo, so paths must be configurable. |
| 74-88 | Defines target SOC values and quality thresholds. | These thresholds decide what is a rough engineering pass. |
| 91-119 | Writes CSV/JSON-safe values. | Keeps batch outputs machine-readable. |
| 121-160 | Discovers capacity files and EIS metadata. | Finds possible matched cases. |
| 162-187 | Matches capacity files to EIS rows by cell, SOH, temperature, and cycle rule. | Prevents comparing unrelated files. |
| 189-250 | Computes pre-rest voltage, capacity clues, and cumulative Ah. | Needed for SOC assignment. |
| 252-302 | Builds the eligible pulse-window pool. | Filters out windows that are wrong current direction or too weak. |
| 304-543 | Implements four SOC selection modes: voltage, coulomb, endpoint, and linear. | SOC matching is treated as an assumption, not as guaranteed truth. |
| 545-561 | Dispatches to the requested SOC selection mode. | Makes sensitivity testing possible. |
| 563-624 | Computes shape metrics and compares a fitted result to EIS. | Produces correlation, area ratio, scale, and normalized error. |
| 626-661 | Computes broad-band values and quality flags. | Makes triage explicit. |
| 663-765 | Processes one matched case end to end. | Loads CSV, finds windows, selects SOC candidates, fits, compares, and records results. |
| 767-806 | Writes the batch plot. | Summarizes many cell/SOC comparisons. |
| 809-900 | Writes the batch report. | Explains batch counts, errors, and interpretation. |
| 902-981 | Parses command-line flags and runs all selected cases. | Lets the user limit cells, cases, and SOC selection method. |

## Model Rule

File: `scripts/experiments/time_domain_model_rule.py`

| Lines | What The Code Does | Why It Matters |
|---:|---|---|
| 39-54 | Sets output path, lambda candidates, baseline mode, RMSE slack, and band labels. | This defines the rule before EIS scoring. |
| 61-105 | Writes CSVs, parses cell filters, ranks values, and cleans numbers. | Utility layer for robust reports. |
| 107-137 | Computes gamma roughness and band-area changes. | Measures whether a DRT curve is too jagged or unstable. |
| 139-157 | Attaches band-stability metrics to lambda candidates. | Helps the rule avoid unstable curves. |
| 159-217 | Selects lambda using voltage RMSE, roughness, band stability, and penalties. | This is the pre-declared model-selection rule. It must not use EIS agreement. |
| 219-257 | Fits all lambda candidates for one case. | Builds the candidate set the rule will choose from. |
| 259-288 | Adds EIS comparison only after the rule has selected a candidate. | This is the honesty guardrail. |
| 290-397 | Selects cases and processes raw DIB files. | Full-data mode. |
| 399-430 | Runs from raw DIB files. | Requires local DIB data. |
| 432-544 | Runs from existing sensitivity outputs. | Allows review when raw DIB data is missing. |
| 546-640 | Writes the model-rule report. | States whether the pre-declared rule actually improved validation. |
| 642-681 | Parses arguments and chooses raw mode or existing-output mode. | Makes the script usable in both environments. |

## Package Plot Regenerator

File: `scripts/experiments/time_domain_package_plots.py`

| Lines | What The Code Does | Why It Matters |
|---:|---|---|
| 1-21 | Imports plotting, data, and path libraries, then forces Matplotlib `Agg`. | Plots can render without opening a GUI. |
| 23-32 | Defines experiment, package-result, and package-plot folders. | The script knows where to read tables and where to save PNGs. |
| 35-68 | Defines colors and plot style. | Keeps all graphs readable and consistent. |
| 70-100 | Reads JSON/CSV, cleans axes, saves plots to both experiment and package folders. | Prevents manual copying mistakes. |
| 104-181 | Redraws the synthetic sanity-check plot. | Shows current, voltage, DRT, and residuals with units. |
| 183-218 | Redraws the window-finder plot. | Shows accepted windows clearly. |
| 220-279 | Redraws the candidate-fit plot. | Shows the selected pulse fit and DRT curve. |
| 281-314 | Redraws the Cell28 SOC sweep summary. | Makes the weak EIS agreement obvious. |
| 316-378 | Redraws the validation diagnostics. | Shows why scale and lambda do not magically solve the mismatch. |
| 380-434 | Redraws the SOC-alignment diagnostic. | Shows the 70 percent SOC uncertainty plainly. |
| 436-471 | Redraws the generalized DIB batch plot. | Shows spread across cells instead of one cherry-picked case. |
| 473-547 | Adds SOC mapping and model sensitivity plots. | Turns important CSV-only evidence into figures. |
| 549-584 | Adds the pre-declared model-rule plot. | Shows that the honest rule still has weak agreement. |
| 586-596 | Runs every plot function. | One command refreshes the whole package plot set. |

## What To Say Out Loud

The code is not the problem anymore. The weak point is the experiment design and dataset match.

If the project requires a battery under drive-cycle loading, then the DIB dataset should not be the main dataset. It can still be useful for EIS and pulse/rest experiments, but it does not carry the main drive-cycle claim.
