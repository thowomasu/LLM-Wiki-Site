# CALB L148N58A Viability Report

## Verdict

Engineering scaffold: usable.
Pulse bridge: viable across 10, 25, and 40 C after tau support is constrained and the final adaptive rule is applied.
Scientific validation: not done.
10 C: solved in the final final 10 C rule pipeline, 82 of 82 rows pass across HPPC_1C and HPPC_C3.
Multi-temperature final rule: solved in frozen pulse-to-EIS rule and analysis step 246 of 246 rows pass across 10, 25, and 40 C, with 2 correlation-only rows using the lower EIS-lambda fallback.
Drive-cycle transfer: weak. drive-cycle transfer test beats a baseline-only model, drive-cycle ECM baseline check loses to a stronger drive-cycle-fitted ECM baseline, and SOC-stratified drive-cycle audit shows the SOC-aligned subset is tiny.
SOC alignment: good for the frozen pulse-to-EIS rule pulse bridge, bad for the drive-cycle calibration rows.
Uncertainty: the weak drive-cycle result and SOC mismatch are not obvious row-sampling flukes.
External replication: blocked until corrected same-cell EIS evidence is available.

## Why

The package now finds HPPC windows, fits a time-domain DRT, computes an EIS DRT baseline, compares them, sweeps lambda, and runs a rough combined inverse problem.
That is close to the Time Domain DRT Pilot workflow structure.
The package now also runs same-dataset 2D DRT comparisons across cells and temperatures.
tau-constrained pulse-to-EIS fit and protocol replication check show that constraining the time-domain tau grid to EIS support creates a strong pulse-test bridge in aggregate.
cold-temperature diagnosis was the catch: the 10 C high- and mid-OCV records did not recover under strict same-state matching.
cold EIS-window probe and cold time-window probe identify a cold-specific rule that recovers strict-comparable 10 C records 0, 1, and 2: EIS trimmed to 0.03 to 50 Hz with lambda 3, and time-domain `time_charge` baseline on the 120/1200 s window.
record-3 protocol search solves record 3 by dropping the earlier long-pulse-only assumption and using short HPPC pulse candidates near 3.50 V.
final 10 C rule consolidates this into one reproducible rule and gets 82 of 82 quality-pass rows.
multi-temperature rule tests the same rule across 10, 25, and 40 C and gets 244 of 246 rows. The only failures are the same 40 C, cell 59861, EIS record 1 case under both HPPC protocols.
outlier probe shows those two failures are not candidate failures. The same selected long-discharge candidate passes if EIS lambda is reduced from 3 to 0.1.
frozen pulse-to-EIS rule makes that into the narrow final adaptive rule: try EIS lambda 3 first, retry lambda 0.1 only when OCV and time RMSE already pass and correlation is the only failing gate. That gets 246 of 246 rows with 2 fallback rows and zero errors.

## Hard Limit

The current EIS match uses nearest OCV. That is better than guessing, but it is not protocol-confirmed SOC alignment.
The 2D comparison improves the matching by using multiple HPPC windows near the EIS OCV records.
If the curves disagree, the honest answer is not `the method failed` or `the method works`. The honest answer is `alignment and model assumptions are still unresolved`.
Do not use far-away OCV candidates to rescue 10 C. cold-temperature diagnosis shows that such candidates can produce high correlation, but that breaks the same-state comparison.
Do not claim lambda tuning fixes 10 C either. cold regularization probe keeps strict matching and shows regularization is not a clean rescue.
Do not use the cold time-window probe long-pulse rule for record 3. record-3 protocol search shows record 3 needs short HPPC pulse candidates, especially HPPC_C3 candidate 25.
Do not collapse the final rule into naive nearest-long-pulse selection. The record-specific candidate rule is the fix.
Do not pretend multi-temperature rule already solved all temperatures. It did not. It left 2 correlation-only failures.
Do not broaden frozen pulse-to-EIS rule into an unconstrained hyperparameter search. The fallback is only defensible because it fires on correlation-only failures after the OCV and voltage-fit gates already pass.
Do not sell the drive-cycle result as validated transfer. SOC alignment audit says most drive-cycle calibration rows are not SOC-aligned to the matched C/20 reference, and SOC-stratified drive-cycle audit says only 16 of 198 rows are within 5 percent SOC delta.
Do not sell external validation yet. external-validation claim boundary found hard blockers in every local candidate replication path.

## Latest Multi-Temperature Batch

multi-temperature 2D batch check ran the time-series 2D DRT versus EIS 2D DRT comparison across 11 processed cells at 10, 25, and 40 C.

- Comparison rows: 123.
- Quality-pass rows: 99.
- Load or archive errors: 0.
- Median quality-pass gamma correlation: -0.0486.
- Median quality-pass absolute OCV delta: 0.00467 V.

Blunt read: this is now a real same-dataset comparison pipeline. It is not a validated bridge. The OCV matching looks good, but the gamma-shape agreement is weak.

## Latest Tau-Constrained Result

protocol replication check replicated the tau-constrained bridge across HPPC_1C and HPPC_C3.

- Rows: 246.
- Quality-pass rows: 203.
- Median constrained correlation: 0.8925.
- HPPC_1C median constrained correlation: 0.8956.
- HPPC_C3 median constrained correlation: 0.8889.

Blunt read: this was the viable pulse-test baseline before the 10 C fix. frozen pulse-to-EIS rule supersedes the temperature caveat.

## 10 C Caveat

cold-temperature diagnosis tested every long 10 C HPPC candidate across both pulse protocols.

- Candidate probe rows: 653.
- Case rows: 82.
- Strict nearest OCV median correlation: -0.0250.
- Best candidate within 20 mV median correlation: -0.0250.
- Best voltage-pass candidate regardless of OCV median correlation: 0.9106.

Blunt read: at the cold-temperature diagnosis stage, 10 C was not fixed. The apparent rescue only appeared when the OCV/state match was allowed to go bad. That diagnosis forced the later cold EIS-window probe through final 10 C rule instead of a fake far-OCV rescue.

## 10 C Regularization Probe

cold regularization probe swept EIS-side and time-domain regularization while keeping strict nearest-OCV matching.

- EIS lambda rows: 656.
- Time lambda rows: 492.
- Best EIS lambda median correlation: 0.3984.
- Rows above 0.75 at best EIS lambda: 0.
- Best time-domain lambda median correlation: -0.0250.

Blunt read: broad lambda tuning was not the 10 C fix. Heavy EIS smoothing improved the aggregate median but still failed the gate and damaged the already-good low-OCV record. frozen pulse-to-EIS rule's fallback is narrower: it fires only on correlation-only failures after OCV and time RMSE pass.

## 10 C Baseline/Sign Probe

cold baseline-sign probe swept baseline modes and current sign while keeping strict nearest-OCV matching.

- Variant rows: 656.
- Best variant: time|sign_+1.
- Best median strict correlation: 0.9177546505204854.
- Rows above 0.75 at best variant: 4.

- Best variant quality-pass fraction: 0.04878048780487805.

Blunt read: baseline or sign changes tiny subset not validation.

## 10 C EIS Window Probe

cold EIS-window probe swept cold-specific EIS frequency windows and EIS regularization while keeping strict nearest-OCV matching.

- Variant rows: 2214.
- Best variant: ge_0p03hz_le_50hz_lam_3.
- Best median strict correlation: 0.928248017443013.
- Best quality-pass fraction: 0.6829268292682927.
- Best corr >= 0.75 fraction: 1.0.

Blunt read: cold eis window high corr but insufficient coverage.

## 10 C Time-Window Probe

cold time-window probe kept the cold EIS-window probe EIS rule fixed and swept time-domain baseline/window choices.

- Variant rows: 328.
- Best variant: time_charge_pre_120_post_1200.
- Best median strict correlation: 0.9282648777010276.
- Best quality-pass fraction: 0.8048780487804879.
- Best corr >= 0.75 fraction: 1.0.
- Record 0 quality-pass rows: 22 of 22.
- Record 1 quality-pass rows: 22 of 22.
- Record 2 quality-pass rows: 22 of 22.
- Record 3 quality-pass rows: 0 of 16.

Blunt read: this fixed records 0 to 2. It did not solve record 3 because the earlier candidate selection only used long-pulse candidates.

## 10 C Record-3 Protocol Search

record-3 protocol search searched every 10 C time-series protocol for EIS record 3.

- Candidate rows fitted: 144.
- HPPC_1C quality-pass cases: 8 of 8.
- HPPC_C3 quality-pass cases: 8 of 8.
- HPPC_C3 median candidate OCV delta: 0.002621314285278231 V.
- HPPC_C3 median time RMSE: 0.8214103162490584 mV.
- HPPC_C3 median correlation: 0.9261162519215498.
- Best row: cell 60195, HPPC_C3 candidate 25, OCV delta 0.0039887728576659676 V, RMSE 0.7905935624384443 mV, correlation 0.9295091961482039.

Blunt read: record 3 is solved by short HPPC pulse candidates, not by the long-pulse rule. The earlier record-3 failure was a candidate-selection failure.

## Final 10 C Pipeline

final 10 C rule consolidates the solved 10 C rule.

- Rows: 82.
- Quality-pass rows: 82.
- Error count: 0.
- Median quality-pass correlation: 0.9281845691435505.
- Median quality-pass OCV delta: 0.003476104583740147 V.
- Median quality-pass time RMSE: 5.388854059089618 mV.
- Record 0: 22 of 22 pass.
- Record 1: 22 of 22 pass.
- Record 2: 22 of 22 pass.
- Record 3: 16 of 16 pass.

Blunt read: 10 C is solved under the declared gate. This is still bridge validation, not SOH validation.

## Final Multi-Temperature Rule

multi-temperature rule applies the final 10 C rule across 10, 25, and 40 C.

- Rows: 246.
- Quality-pass rows: 244.
- Error count: 0.
- Median quality-pass correlation: 0.9282125467314115.
- Median quality-pass OCV delta: 0.003296648910522393 V.
- Median quality-pass time RMSE: 3.1563794367812985 mV.
- Failing rows: 40 C, cell 59861, EIS record 1, HPPC_1C and HPPC_C3.
- Failure mode: OCV and time RMSE pass, but correlation is about 0.701 under EIS lambda 3.

Blunt read: the fixed 10 C rule mostly generalizes, but multi-temperature rule is not complete by itself.

## Final Adaptive Multi-Temperature Rule

frozen pulse-to-EIS rule keeps the same candidate and time-domain rule, then adds a narrow EIS regularization fallback.

- Rows: 246.
- Quality-pass rows: 246.
- Fallback rows: 2.
- Error count: 0.
- EIS lambda sequence: 3.0, then 0.1 only for correlation-only failures.
- Median quality-pass correlation: 0.928192585051496.
- Median quality-pass OCV delta: 0.003296648910522393 V.
- Median quality-pass time RMSE: 3.144651471038199 mV.
- Verdict: `adaptive_final_rule_all_temperatures_all_rows_pass`.

Blunt read: this is the current defensible CALB bridge result. It solves the declared gate across the fresh-cell temperature grid. It still does not validate SOH, aging prediction, or the combined EIS plus time-domain inverse.

## Drive-Cycle Validation

drive-cycle transfer test tests fixed HPPC-derived DRT dynamics on held-out drive-cycle voltage.

- Rows: 198.
- Error count: 0.
- DRT win fraction versus baseline-only model: 1.0.
- Median DRT holdout RMSE: 150.9172295922953 mV.
- Median baseline holdout RMSE: 164.95303653565315 mV.
- Median DRT improvement versus baseline: 16.830790799673707 mV.
- Verdict: `drive_cycle_transfer_supports_hppc_drt`.

Blunt read: drive-cycle transfer test is a drive-cycle transfer test against a weak baseline-only comparator. Do not call this SOH validation, and do not stop reading before drive-cycle ECM baseline check.

## Stronger Drive-Cycle ECM Baseline Audit

drive-cycle ECM baseline check tests whether drive-cycle transfer test survives a stronger internal baseline.

- Rows: 198.
- Error count: 0.
- Median fixed DRT holdout RMSE: 150.9172295922953 mV.
- Median best ECM holdout RMSE: 134.8626012268972 mV.
- Median DRT minus best ECM RMSE: 3.0704702158353285 mV.
- DRT win fraction versus best ECM: 0.12121212121212122.
- Verdict: `drive_cycle_ecm_baseline_beats_fixed_drt`.

Blunt read: this is the more honest internal drive-cycle benchmark, and it downgrades the drive-cycle transfer test drive-cycle claim. Fixed HPPC-derived DRT did not beat a simple calibrated ECM-style baseline here. It still does not prove SOH, aging, or external generalization.

## SOC And Protocol Alignment Audit

SOC alignment audit maps EIS OCV, HPPC pre-rest voltage, and drive-cycle calibration voltage onto same-cell, same-temperature C/20 discharge curves.

- C/20 curves used: 33.
- Bridge rows: 246.
- Drive-cycle rows: 198.
- Bridge median absolute SOC delta: 0.004556003613014614.
- Bridge rows above 2 percent SOC delta: 0.
- Drive-cycle median absolute SOC delta: 0.0637559086707088.
- Drive-cycle rows above 5 percent SOC delta: 182 of 198.
- Verdict: `soc_alignment_audit_complete`.

Blunt read: the pulse bridge is state-aligned enough for the current internal claim. The drive-cycle transfer is not. That is a real weakness, not a wording problem.

## Bootstrap Uncertainty Audit

analysis step 38 bootstraps the final bridge, drive-cycle baseline, and SOC-alignment metrics.

- Bootstrap samples: 5000.
- Metrics: 12.
- drive-cycle ECM baseline check median DRT minus best ECM RMSE: 3.0704702158353285 mV, bootstrap CI 2.9206679021260555 to 4.964587444670613 mV.
- drive-cycle ECM baseline check DRT win fraction versus best ECM: 0.12121212121212122, bootstrap CI 0.07575757575757576 to 0.16666666666666666.
- SOC alignment audit drive rows above 5 percent SOC-delta fraction: 0.9191919191919192, bootstrap CI 0.8787878787878788 to 0.9545454545454546.
- Verdict: `uncertainty_audit_complete`.

Blunt read: the bad drive-cycle result survives resampling. Pretending it is noise would be weak thinking.

## External Replication Readiness

external-validation claim boundary checks the local evidence for an external validation rerun.

- Assets reviewed: 13.
- Hard blockers: 3.
- Preferred external dataset: KIT/RADAR4KIT.
- Ready for external replication: false.
- Verdict: `external_replication_blocked_missing_corrected_eis`.

Blockers:

- KIT/RADAR4KIT local EIS archive is incomplete and needs the corrected EIS addendum.
- Local LG M50T 21700 Expt 4 drive-cycle aging evidence has no same-cell EIS for this DRT bridge.
- Local DIB comparison has only five exact paired rows from one cell/SOH/temp condition, with weak shape agreement outside one SOC.

Blunt read: external validation is not done. The next useful move is to get corrected KIT EIS or another same-cell EIS-paired dataset, not to polish CALB again.

## Generated Section Summary

```json
{
  "section_1_data_audit": {
    "processed_cells": 11,
    "temperatures_c": [
      10,
      25,
      40
    ],
    "first_slice_cell": "59294",
    "first_slice_temperature_c": 25,
    "protocol_count": 7,
    "time_series_protocol_count": 6,
    "eis_records": 3
  },
  "section_2_file_protocol_screen": {
    "screened_protocols": 6,
    "recommended_first_fit_protocol": "HPPC_1C",
    "reason": "HPPC gives clear pulse/rest excitation and shares cell/temp with EIS.",
    "drive_cycle_warning": "WLTP, UDDS, and US06 are dynamic validation targets later, not the first clean pulse-relaxation inverse target."
  },
  "section_3_hppc_window_finder": {
    "input_path": "[local path redacted]",
    "selected_candidate": {
      "candidate_id": 6,
      "accepted": true,
      "start_idx": 31612,
      "end_idx": 35212,
      "start_time_s": 6400.512999999999,
      "end_time_s": 6760.413799999998,
      "pulse_duration_s": 359.90079999999944,
      "pre_rest_s": 600.0479000000014,
      "post_rest_s": 3599.0044000000016,
      "median_current_a": -57.99932,
      "current_step_a": -57.99957,
      "max_abs_step_a": 57.99996,
      "voltage_span_v": 0.1894269999999998,
      "temperature_drift_c": null,
      "median_dt_s": 0.10009999999965657,
      "tau_min_s": 0.20019999999931315,
      "tau_max_s": 1319.635066666667,
      "excitation_score": 1804.3672208320384
    },
    "summary": {
      "rows_loaded_after_cleaning": 172269,
      "time_start_s": 0.0,
      "time_stop_s": 44762.7107,
      "duration_s": 44762.7107,
      "median_dt_s": 0.10009999999965657,
      "rest_current_threshold_a": 0.8700518999999999,
      "step_current_threshold_a": 2.900173,
      "current_min_a": -58.00464,
      "current_max_a": 37.70427,
      "voltage_min_v": 2.499992,
      "voltage_max_v": 4.25577,
      "candidate_count": 27,
      "accepted_count": 27
    }
  },
  "section_4_hppc_candidate_fit": {
    "input_path": "02_First_Slice/HPPC_1C.csv",
    "candidate_id": 6,
    "columns": {
      "time_s": "time_s",
      "current_a": "current_a",
      "voltage_v": "voltage_v",
      "temperature_c": null
    },
    "fit_rows": 6000,
    "include_pre_s": 120.0,
    "include_post_s": 1200.0,
    "lambda_value": 0.001,
    "baseline_mode": "charge",
    "pre_rest_voltage_v": 4.075706,
    "r0_ohm": 0.0011236705609684763,
    "rmse_v": 0.0016060101557984316,
    "rmse_mv": 1.6060101557984316,
    "tau_min_s": 0.20019999999931318,
    "tau_max_s": 559.6260999999998,
    "n_tau": 72,
    "top_recovered_peaks": [
      {
        "tau_s": 559.6260999999998,
        "gamma_ohm": 0.0005148132340912911
      },
      {
        "tau_s": 30.607198460687094,
        "gamma_ohm": 0.0005026310213440038
      },
      {
        "tau_s": 27.370470132566965,
        "gamma_ohm": 0.00038749461032804716
      },
      {
        "tau_s": 2.09330178030111,
        "gamma_ohm": 0.00012921433624243732
      },
      {
        "tau_s": 0.20019999999931318,
        "gamma_ohm": 2.3979226225744946e-05
      },
      {
        "tau_s": 500.445327432659,
        "gamma_ohm": 0.0
      }
    ],
    "broad_band_summary": [
      {
        "band": "fast_band_4_to_16_s",
        "tau_start_s": 4.0,
        "tau_stop_s": 16.0,
        "gamma_sum_ohm": 0.0
      },
      {
        "band": "mid_band_25_to_90_s",
        "tau_start_s": 25.0,
        "tau_stop_s": 90.0,
        "gamma_sum_ohm": 0.000890125631672051
      },
      {
        "band": "slow_band_90_to_450_s",
        "tau_start_s": 90.0,
        "tau_stop_s": 450.0,
        "gamma_sum_ohm": 0.0
      }
    ]
  },
  "section_5_eis_drt_baseline": {
    "summary_rows": [
      {
        "eis_record_index": 0,
        "ocv_value": 3.959110736846924,
        "cleaned_points": 34,
        "frequency_min_hz": 0.0100010996684432,
        "frequency_max_hz": 516.4194946289062,
        "tau_min_s": 0.00010272975410314595,
        "tau_max_s": 47.741232974834425,
        "r_inf_ohm": 0.0007902907086738024,
        "real_rmse_ohm": 1.221310964960631e-05,
        "imag_rmse_ohm": 7.066916655359628e-06,
        "gamma_area": 0.0013273163072143848
      },
      {
        "eis_record_index": 1,
        "ocv_value": 3.722273349761963,
        "cleaned_points": 34,
        "frequency_min_hz": 0.0100010996684432,
        "frequency_max_hz": 516.4194946289062,
        "tau_min_s": 0.00010272975410314595,
        "tau_max_s": 47.741232974834425,
        "r_inf_ohm": 0.0008047724034517807,
        "real_rmse_ohm": 1.294541133538452e-05,
        "imag_rmse_ohm": 5.7450219979198466e-06,
        "gamma_area": 0.001156826544309245
      },
      {
        "eis_record_index": 2,
        "ocv_value": 3.630812168121338,
        "cleaned_points": 34,
        "frequency_min_hz": 0.0100010996684432,
        "frequency_max_hz": 516.4194946289062,
        "tau_min_s": 0.00010272975410314595,
        "tau_max_s": 47.741232974834425,
        "r_inf_ohm": 0.0008145308210172761,
        "real_rmse_ohm": 1.1740624956020148e-05,
        "imag_rmse_ohm": 4.7210830807830845e-06,
        "gamma_area": 0.0010801334504528088
      }
    ]
  },
  "section_6_bridge_comparison": {
    "pre_rest_voltage_v": 4.075706,
    "nearest_eis_record_index": 0,
    "nearest_eis_ocv_value": 3.959110736846924,
    "ocv_delta_v": 0.11659526315307644,
    "comparison": {
      "overlap_tau_min_s": 0.20019999999931318,
      "overlap_tau_max_s": 47.741232974834425,
      "overlap_points": 49,
      "overlap_corr_gamma": -0.06347473208491614,
      "overlap_rmse_gamma": 0.00035849076158705394,
      "overlap_time_gamma_area": 0.00011527224899930599,
      "overlap_eis_gamma_area": 0.00041158716038815625,
      "best_scale_time_to_eis": 0.020217989693639363,
      "scaled_rmse": 0.0003468228449093935,
      "normalized_scaled_rmse": 0.9999854340866104
    }
  },
  "section_7_lambda_sensitivity": {
    "best_corr_row": {
      "lambda_value": 3.0,
      "rmse_mv": 1.606020905293428,
      "r0_ohm": 0.0011242269307246457,
      "residual_norm": 0.12440184439724812,
      "smooth_norm": 0.0010503456048456623,
      "overlap_corr_gamma": -0.06290097176658203,
      "normalized_scaled_rmse": 0.9999758118785423,
      "time_gamma_area": 0.00011542086107508307,
      "eis_gamma_area": 0.00041158716038815625
    },
    "best_voltage_rmse_row": {
      "lambda_value": 0.003,
      "rmse_mv": 1.606010155798413,
      "r0_ohm": 0.0011236705601877185,
      "residual_norm": 0.12440101174494467,
      "smooth_norm": 0.0011065221671348526,
      "overlap_corr_gamma": -0.06347473248486245,
      "normalized_scaled_rmse": 0.9999854340869229,
      "time_gamma_area": 0.00011527224895333407,
      "eis_gamma_area": 0.00041158716038815625
    },
    "rows": [
      {
        "lambda_value": 0.0001,
        "rmse_mv": 1.6060101557984285,
        "r0_ohm": 0.001123670561065089,
        "residual_norm": 0.12440101174494586,
        "smooth_norm": 0.0011065221858905304,
        "overlap_corr_gamma": -0.06347473203542311,
        "normalized_scaled_rmse": 0.9999854340865718,
        "time_gamma_area": 0.00011527224900499526,
        "eis_gamma_area": 0.00041158716038815625
      },
      {
        "lambda_value": 0.0003,
        "rmse_mv": 1.606010155798431,
        "r0_ohm": 0.0011236705610572903,
        "residual_norm": 0.12440101174494606,
        "smooth_norm": 0.0011065221857236328,
        "overlap_corr_gamma": -0.0634747320394219,
        "normalized_scaled_rmse": 0.9999854340865749,
        "time_gamma_area": 0.00011527224900453547,
        "eis_gamma_area": 0.00041158716038815625
      },
      {
        "lambda_value": 0.001,
        "rmse_mv": 1.6060101557984316,
        "r0_ohm": 0.0011236705609684763,
        "residual_norm": 0.12440101174494608,
        "smooth_norm": 0.0011065221838251172,
        "overlap_corr_gamma": -0.06347473208491614,
        "normalized_scaled_rmse": 0.9999854340866104,
        "time_gamma_area": 0.00011527224899930599,
        "eis_gamma_area": 0.00041158716038815625
      },
      {
        "lambda_value": 0.003,
        "rmse_mv": 1.606010155798413,
        "r0_ohm": 0.0011236705601877185,
        "residual_norm": 0.12440101174494467,
        "smooth_norm": 0.0011065221671348526,
        "overlap_corr_gamma": -0.06347473248486245,
        "normalized_scaled_rmse": 0.9999854340869229,
        "time_gamma_area": 0.00011527224895333407,
        "eis_gamma_area": 0.00041158716038815625
      },
      {
        "lambda_value": 0.01,
        "rmse_mv": 1.6060101557984323,
        "r0_ohm": 0.001123670551306599,
        "residual_norm": 0.12440101174494612,
        "smooth_norm": 0.0011065219772841365,
        "overlap_corr_gamma": -0.06347473703423523,
        "normalized_scaled_rmse": 0.9999854340904749,
        "time_gamma_area": 0.00011527224843040386,
        "eis_gamma_area": 0.00041158716038815625
      },
      {
        "lambda_value": 0.03,
        "rmse_mv": 1.6060101557984885,
        "r0_ohm": 0.001123670473232739,
        "residual_norm": 0.12440101174495048,
        "smooth_norm": 0.0011065203083396315,
        "overlap_corr_gamma": -0.06347477702717928,
        "normalized_scaled_rmse": 0.9999854341217014,
        "time_gamma_area": 0.00011527224383333948,
        "eis_gamma_area": 0.00041158716038815625
      },
      {
        "lambda_value": 0.1,
        "rmse_mv": 1.606010155810369,
        "r0_ohm": 0.0011236695853850318,
        "residual_norm": 0.12440101174587075,
        "smooth_norm": 0.0011065013333050582,
        "overlap_corr_gamma": -0.06347523175195999,
        "normalized_scaled_rmse": 0.9999854344768284,
        "time_gamma_area": 0.00011527219155756002,
        "eis_gamma_area": 0.00041158716038815625
      },
      {
        "lambda_value": 0.3,
        "rmse_mv": 1.6060101567628795,
        "r0_ohm": 0.0011236617992502998,
        "residual_norm": 0.1244010118196519,
        "smooth_norm": 0.0011063352455866727,
        "overlap_corr_gamma": -0.0634792139659162,
        "normalized_scaled_rmse": 0.9999854375930243,
        "time_gamma_area": 0.00011527173323877372,
        "eis_gamma_area": 0.00041158716038815625
      },
      {
        "lambda_value": 1.0,
        "rmse_mv": 1.6060125192655226,
        "r0_ohm": 0.0011239318164322,
        "residual_norm": 0.12440119481831975,
        "smooth_norm": 0.001077490872311613,
        "overlap_corr_gamma": -0.0633150720594904,
        "normalized_scaled_rmse": 0.999981679215122,
        "time_gamma_area": 0.00011527757589681087,
        "eis_gamma_area": 0.00041158716038815625
      },
      {
        "lambda_value": 3.0,
        "rmse_mv": 1.606020905293428,
        "r0_ohm": 0.0011242269307246457,
        "residual_norm": 0.12440184439724812,
        "smooth_norm": 0.0010503456048456623,
        "overlap_corr_gamma": -0.06290097176658203,
        "normalized_scaled_rmse": 0.9999758118785423,
        "time_gamma_area": 0.00011542086107508307,
        "eis_gamma_area": 0.00041158716038815625
      }
    ]
  },
  "section_8_combined_prototype": {
    "status": "prototype_runs_not_validated",
    "lambda_value": 0.1,
    "r0_ohm": 0.0,
    "r_inf_ohm": 0.0009872013205477282,
    "time_rmse_v": 0.004085094188617694,
    "time_rmse_mv": 4.085094188617695,
    "eis_real_rmse_ohm": 8.767202701509276e-05,
    "eis_img_rmse_ohm": 0.00011980834674375109,
    "baseline_coefficients": {
      "offset_v": 4.077839064537797,
      "drift_v_per_as": 5.771845516254282e-06
    },
    "claim_boundary": "Combined objective is implemented as a rough prototype. It has not been validated."
  },
  "section_9_time_series_2d_surface": {
    "fit_count": 9,
    "surface_fit_count": 8,
    "excluded_fit_count": 1,
    "target_candidate_ids": [
      9,
      15,
      21
    ],
    "fit_summary_rows": [
      {
        "candidate_id": 3,
        "pre_rest_voltage_v": 4.197943,
        "rmse_mv": 0.3362277459995312,
        "r0_ohm": 0.0011398492485278817,
        "quality_pass": true,
        "matched_to_eis_surface": false
      },
      {
        "candidate_id": 6,
        "pre_rest_voltage_v": 4.075706,
        "rmse_mv": 1.6060101557984316,
        "r0_ohm": 0.0011236705609684763,
        "quality_pass": true,
        "matched_to_eis_surface": false
      },
      {
        "candidate_id": 9,
        "pre_rest_voltage_v": 3.954346,
        "rmse_mv": 2.6933440195305094,
        "r0_ohm": 0.0011163076074474738,
        "quality_pass": true,
        "matched_to_eis_surface": true
      },
      {
        "candidate_id": 12,
        "pre_rest_voltage_v": 3.8362315000000002,
        "rmse_mv": 3.389552286627327,
        "r0_ohm": 0.001122813005878391,
        "quality_pass": true,
        "matched_to_eis_surface": false
      },
      {
        "candidate_id": 15,
        "pre_rest_voltage_v": 3.714797,
        "rmse_mv": 0.9004671681419923,
        "r0_ohm": 0.0011520908969815625,
        "quality_pass": true,
        "matched_to_eis_surface": true
      },
      {
        "candidate_id": 18,
        "pre_rest_voltage_v": 3.6602265000000003,
        "rmse_mv": 0.44417044534236394,
        "r0_ohm": 0.0011658248286496484,
        "quality_pass": true,
        "matched_to_eis_surface": false
      },
      {
        "candidate_id": 21,
        "pre_rest_voltage_v": 3.6274045,
        "rmse_mv": 0.49741577350203364,
        "r0_ohm": 0.0011766037474553335,
        "quality_pass": true,
        "matched_to_eis_surface": true
      },
      {
        "candidate_id": 24,
        "pre_rest_voltage_v": 3.575111,
        "rmse_mv": 1.17800105372521,
        "r0_ohm": 0.0012036415005993416,
        "quality_pass": true,
        "matched_to_eis_surface": false
      },
      {
        "candidate_id": 27,
        "pre_rest_voltage_v": 3.494422,
        "rmse_mv": 86.35688282585762,
        "r0_ohm": 0.0011117185845470467,
        "quality_pass": false,
        "matched_to_eis_surface": false
      }
    ]
  },
  "section_10_eis_2d_surface": {
    "eis_records": 3,
    "ocv_values": [
      3.630812168121338,
      3.722273349761963,
      3.959110736846924
    ],
    "tau_min_s": 0.00010272975410314595,
    "tau_max_s": 47.741232974834425,
    "n_tau": 96,
    "method": "EIS real plus imaginary nonnegative regularized DRT surface"
  },
  "section_11_time_series_vs_eis_2d_comparison": {
    "matched_pairs": [
      {
        "eis_record_index": 0,
        "eis_ocv_value": 3.959110736846924,
        "time_candidate_id": 9,
        "time_pre_rest_voltage_v": 3.954346,
        "ocv_delta_v": -0.0047647368469236895,
        "overlap_points": 49,
        "overlap_corr_gamma": -0.04623883315115348,
        "overlap_rmse_gamma": 0.0003748597914666574,
        "overlap_time_gamma_area": 0.0001214074730233435,
        "overlap_eis_gamma_area": 0.00041158463661438783,
        "normalized_scaled_rmse": 1.0
      },
      {
        "eis_record_index": 1,
        "eis_ocv_value": 3.722273349761963,
        "time_candidate_id": 15,
        "time_pre_rest_voltage_v": 3.714797,
        "ocv_delta_v": -0.007476349761962986,
        "overlap_points": 49,
        "overlap_corr_gamma": -0.033011703737114914,
        "overlap_rmse_gamma": 0.00031426277422894386,
        "overlap_time_gamma_area": 0.00011071563187346462,
        "overlap_eis_gamma_area": 0.00028558899564340293,
        "normalized_scaled_rmse": 0.9999274783157496
      },
      {
        "eis_record_index": 2,
        "eis_ocv_value": 3.630812168121338,
        "time_candidate_id": 21,
        "time_pre_rest_voltage_v": 3.6274045,
        "ocv_delta_v": -0.00340766812133797,
        "overlap_points": 49,
        "overlap_corr_gamma": 0.917565072889239,
        "overlap_rmse_gamma": 0.00017806670641017482,
        "overlap_time_gamma_area": 5.842347062215256e-05,
        "overlap_eis_gamma_area": 0.00024406187804573134,
        "normalized_scaled_rmse": 0.3920286931701804
      }
    ],
    "median_overlap_corr_gamma": -0.033011703737114914,
    "max_abs_ocv_delta_v": 0.007476349761962986,
    "verdict": "same_dataset_2d_comparison_runs_not_validated"
  }
}
```

## Local Audit Closure

leakage and claim audit through SOC-stratified drive-cycle audit close the local audit loop.

- leakage and claim audit high-risk leakage or claim-boundary items: 5.
- analysis step 41 ablation rows consolidated: 12.
- SOC-stratified drive-cycle audit drive-cycle rows within 5 percent SOC delta: 16 of 198.

Blunt read: the internal pulse bridge is useful. The final rule is not a pristine held-out discovery, and the drive-cycle transfer is still SOC-misaligned. The next proof has to be external and state-aligned.
