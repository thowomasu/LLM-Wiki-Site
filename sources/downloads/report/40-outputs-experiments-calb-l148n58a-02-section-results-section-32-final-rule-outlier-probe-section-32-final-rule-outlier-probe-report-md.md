# CALB L148N58A, outlier probe Final-Rule Outlier Probe

## Purpose

Probe the only multi-temperature rule outlier: 40 C, cell 59861, EIS record 1.

## Result

- Candidate rows: 1200
- Error count: 0
- Best row: `{'cell_id': '59861', 'temperature_c': 40, 'hppc_protocol': 'HPPC_1C', 'eis_record_index': 1, 'eis_ocv_value': 3.728813648223877, 'candidate_rank_by_ocv': 1, 'candidate_id': 13, 'candidate_rule': 'outlier_probe_nearby_candidate', 'pre_rest_voltage_v': 3.723876, 'abs_ocv_delta_v': 0.004937648223876767, 'pulse_duration_s': 9.900400000013178, 'post_rest_s': 599.9003999999841, 'median_current_a': -57.99917, 'fmin_hz': 0.05, 'fmax_hz': 50.0, 'eis_lambda': 10.0, 'variant': 'cand_13_f_0p05_50_lam_10', 'eis_points': 18, 'eis_frequency_min_hz': 0.05185290053486824, 'eis_frequency_max_hz': 13.950889587402344, 'time_rmse_mv': 0.5176712957870458, 'r0_ohm': 0.0008170523828122451, 'corr': 0.9425299412076248, 'scaled_rmse': 0.33431751870831866, 'quality_pass': True, 'quality_flags': ''}`
- Verdict: `outlier_candidate_found`

## Blunt Read

If a gate-passing local candidate exists, fold the rule back into the final pipeline only if the rule is defensible and not cell-specific magic.

## Outputs

- `section_32_outlier_rows.csv`
- `section_32_errors.csv`
- `section_32_summary.json`

## Linked Graph

![outlier probe final rule outlier probe](section_32_final_rule_outlier_probe.png)
