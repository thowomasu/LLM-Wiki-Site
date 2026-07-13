# Rough Prototype Runner Log

Skipping Cell28 validation steps: synthetic-only flag set

## first-slice protocol inventory synthetic DRT

Command:

```text
python scripts/experiments/time_domain_drt_pilot.py
```

Exit code: 0
Elapsed seconds: 0.42

Output:

```text
{
  "section": "synthetic_inverse_sanity_check",
  "r0_truth_ohm": 0.002,
  "r0_estimated_ohm": 0.0018142762769506023,
  "true_branches": [
    {
      "tau_s": 8.0,
      "resistance_ohm": 0.0012
    },
    {
      "tau_s": 45.0,
      "resistance_ohm": 0.003
    },
    {
      "tau_s": 180.0,
      "resistance_ohm": 0.0022
    }
  ],
  "top_recovered_peaks": [
    {
      "tau_s": 54.344648128606295,
      "gamma_ohm": 0.0018384784508566334
    },
    {
      "tau_s": 58.68249451317397,
      "gamma_ohm": 0.0017730562382480145
    },
    {
      "tau_s": 317.86876342004655,
      "gamma_ohm": 0.00171577212409773
    },
    {
      "tau_s": 9.291069523303076,
      "gamma_ohm": 0.0010721264899128027
    },
    {
      "tau_s": 10.032692364342543,
      "gamma_ohm": 0.00034996763892467865
    },
    {
      "tau_s": 2.0,
      "gamma_ohm": 9.603145817779018e-05
    }
  ],
  "broad_band_summary": [
    {
      "band": "fast_band_4_to_16_s",
      "tau_start_s": 4.0,
      "tau_stop_s": 16.0,
      "gamma_sum_ohm": 0.0014220941288374813
    },
    {
      "band": "mid_band_25_to_90_s",
      "tau_start_s": 25.0,
      "tau_stop_s": 90.0,
      "gamma_sum_ohm": 0.003611534689104648
    },
    {
      "band": "slow_band_90_to_450_s",
      "tau_start_s": 90.0,
      "tau_stop_s": 450.0,
      "gamma_sum_ohm": 0.00171577212409773
    }
  ],
  "rmse_v": 0.0008007468089348458,
  "rmse_mv": 0.8007468089348458,
  "tau_min_s": 2.0,
  "tau_max_s": 466.66666666666663,
  "n_tau": 72,
  "lambda_value": 0.001
}
Output folder: $REPO_ROOT\40 Outputs\Experiments\Time Domain DRT Pilot
```

## file and protocol screen synthetic window finder

Command:

```text
python scripts/experiments/time_domain_window_finder.py
```

Exit code: 0
Elapsed seconds: 0.86

Output:

```text
{
  "rows_loaded_after_cleaning": 1401,
  "time_start_s": 0.0,
  "time_stop_s": 1400.0,
  "duration_s": 1400.0,
  "median_dt_s": 1.0,
  "rest_current_threshold_a": 0.16499999999999998,
  "step_current_threshold_a": 0.55,
  "current_min_a": -5.0,
  "current_max_a": 6.0,
  "voltage_min_v": 3.673950620636613,
  "voltage_max_v": 3.7304970730068887,
  "candidate_count": 5,
  "accepted_count": 5
}
Output folder: $REPO_ROOT\40 Outputs\Experiments\Time Domain DRT Pilot
```

## HPPC window finder synthetic candidate fit

Command:

```text
python scripts/experiments/time_domain_candidate_fit.py
```

Exit code: 0
Elapsed seconds: 0.83

Output:

```text
{
  "input_path": "40 Outputs/Experiments/Time Domain DRT Pilot/synthetic_section_1_timeseries.csv",
  "candidate_path": "40 Outputs/Experiments/Time Domain DRT Pilot/section_2_window_candidates.csv",
  "column_mapping": {
    "time_s": "time_s",
    "current_a": "current_a",
    "voltage_v": "voltage_v",
    "temperature_c": null
  },
  "candidate": {
    "candidate_id": 5,
    "accepted": true,
    "start_idx": 980,
    "end_idx": 1014,
    "start_time_s": 980.0,
    "end_time_s": 1014.0,
    "pulse_duration_s": 34.0,
    "pre_rest_s": 250.0,
    "post_rest_s": 385.0,
    "median_current_a": 6.0,
    "current_step_a": 6.0,
    "max_abs_step_a": 6.0,
    "voltage_span_v": 0.0212466027395956,
    "temperature_drift_c": null,
    "median_dt_s": 1.0,
    "tau_min_s": 2.0,
    "tau_max_s": 139.66666666666666,
    "excitation_score": 54.31690154025722
  },
  "include_pre_s": 30.0,
  "include_post_s": 180.0,
  "lambda_value": 0.001,
  "baseline_mode": "charge",
  "fit_rows": 245,
  "r0_ohm": 0.0017473016378956225,
  "rmse_v": 0.0008033859491540868,
  "rmse_mv": 0.8033859491540868,
  "offset_v": 3.6984048519166524,
  "drift_v_per_as": 6.167820618838442e-06,
  "time_drift_v_per_s": 0.0,
  "baseline_coefficients": {
    "offset_v": 3.6984048519166524,
    "drift_v_per_as": 6.167820618838442e-06
  },
  "tau_min_s": 2.0,
  "tau_max_s": 81.33333333333334,
  "n_tau": 72,
  "top_recovered_peaks": [
    {
      "tau_s": 62.65300581153676,
      "gamma_ohm": 0.0028443783279508373
    },
    {
      "tau_s": 10.084521341455945,
      "gamma_ohm": 0.0015267299212430583
    },
    {
      "tau_s": 59.467075253542355,
      "gamma_ohm": 0.0009286685732344727
    },
    {
      "tau_s": 2.0,
      "gamma_ohm": 0.00014504048833832465
    },
    {
      "tau_s": 69.54606713506362,
      "gamma_ohm": 0.0
    },
    {
      "tau_s": 73.27197663253354,
      "gamma_ohm": 0.0
    }
  ],
  "broad_band_summary": [
    {
      "band": "fast_band_4_to_16_s",
      "tau_start_s": 4.0,
      "tau_stop_s": 16.0,
      "gamma_sum_ohm": 0.0015267299212430583
    },
    {
      "band": "mid_band_25_to_90_s",
      "tau_start_s": 25.0,
      "tau_stop_s": 90.0,
      "gamma_sum_ohm": 0.00377304690118531
    },
    {
      "band": "slow_band_90_to_450_s",
      "tau_start_s": 90.0,
      "tau_stop_s": 450.0,
      "gamma_sum_ohm": 0.0
    }
  ]
}
Output folder: $REPO_ROOT\40 Outputs\Experiments\Time Domain DRT Pilot
```

## HPPC candidate fit DIB-style CSV smoke test

Command:

```text
python scripts/experiments/time_domain_real_csv_smoke_test.py
```

Exit code: 0
Elapsed seconds: 0.90

Output:

```text
{
  "section": "real_csv_format_smoke_test",
  "input": "[local path redacted]",
  "window_summary": {
    "rows_loaded_after_cleaning": 1401,
    "time_start_s": 0.0,
    "time_stop_s": 1400.0,
    "duration_s": 1400.0,
    "median_dt_s": 1.0,
    "rest_current_threshold_a": 0.16499999999999998,
    "step_current_threshold_a": 0.55,
    "current_min_a": -5.0,
    "current_max_a": 6.0,
    "voltage_min_v": 3.673950620636613,
    "voltage_max_v": 3.7304970730068887,
    "candidate_count": 5,
    "accepted_count": 5
  },
  "fit_summary": {
    "smoke_test": true,
    "input_path": "[local path redacted]",
    "candidate": {
      "candidate_id": 5,
      "accepted": true,
      "start_idx": 980,
      "end_idx": 1014,
      "start_time_s": 980.0,
      "end_time_s": 1014.0,
      "pulse_duration_s": 34.0,
      "pre_rest_s": 250.0,
      "post_rest_s": 385.0,
      "median_current_a": 6.0,
      "current_step_a": 6.0,
      "max_abs_step_a": 6.0,
      "voltage_span_v": 0.021246602739595666,
      "temperature_drift_c": 0.0002478675582828771,
      "median_dt_s": 1.0,
      "tau_min_s": 2.0,
      "tau_max_s": 139.66666666666666,
      "excitation_score": 54.31690154025722
    },
    "fit_rows": 245,
    "r0_ohm": 0.0017473016378956236,
    "rmse_v": 0.0008033859491540828,
    "rmse_mv": 0.8033859491540828,
    "offset_v": 3.6984048519166524,
    "drift_v_per_as": 6.167820618838442e-06,
    "tau_min_s": 2.0,
    "tau_max_s": 81.33333333333334,
    "n_tau": 72,
    "trend_info": {
      "offset_v": 3.7061641887498213,
      "drift_v_per_as": -4.048136317597622e-06
    },
    "top_recovered_peaks": [
      {
        "tau_s": 62.65300581153676,
        "gamma_ohm": 0.002844378327950809
      },
      {
        "tau_s": 10.084521341455945,
        "gamma_ohm": 0.0015267299212430537
      },
      {
        "tau_s": 59.467075253542355,
        "gamma_ohm": 0.0009286685732345038
      },
      {
        "tau_s": 2.0,
        "gamma_ohm": 0.0001450404883383315
      },
      {
        "tau_s": 69.54606713506362,
        "gamma_ohm": 0.0
      },
      {
        "tau_s": 73.27197663253354,
        "gamma_ohm": 0.0
      }
    ],
    "broad_band_summary": [
      {
        "band": "fast_band_4_to_16_s",
        "tau_start_s": 4.0,
        "tau_stop_s": 16.0,
        "gamma_sum_ohm": 0.0015267299212430537
      },
      {
        "band": "mid_band_25_to_90_s",
        "tau_start_s": 25.0,
        "tau_stop_s": 90.0,
        "gamma_sum_ohm": 0.003773046901185313
      },
      {
        "band": "slow_band_90_to_450_s",
        "tau_start_s": 90.0,
        "tau_stop_s": 450.0,
        "gamma_sum_ohm": 0.0
      }
    ]
  }
}
Output folder: $REPO_ROOT\40 Outputs\Experiments\Time Domain DRT Pilot
```

## weighting probe HTML documentation export

Command:

```text
python scripts/experiments/time_domain_export_html.py
```

Exit code: 0
Elapsed seconds: 0.13

Output:

```text
40 Outputs/Experiments/Time Domain DRT Pilot/README.html
40 Outputs/Experiments/Time Domain DRT Pilot/ROUGH_PROTOTYPE_HANDOFF.html
40 Outputs/Experiments/Time Domain DRT Pilot/ASSUMPTIONS.html
40 Outputs/Experiments/Time Domain DRT Pilot/CODE_NOTES.html
40 Outputs/Experiments/Time Domain DRT Pilot/TIME_DOMAIN_DRT_MATH.html
40 Outputs/Experiments/Time Domain DRT Pilot/VIABILITY_REPORT.html
40 Outputs/Experiments/Time Domain DRT Pilot/Model Rule/model_rule_report.html
```
