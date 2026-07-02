# CALB L148N58A, cold time-window probe Cold Time-Window Probe

## Purpose

Test whether baseline mode and fit-window length fix the remaining 10 C failures after applying the cold EIS-window probe EIS window.

## Result

- Temperature tested: 10 C
- Protocols: HPPC_1C, HPPC_C3
- Cells attempted per protocol: 11
- Row count: 328
- Error count: 0
- Fixed EIS rule: 0.03 to 50.0 Hz, lambda 3.0
- Best variant summary: `{'variant': 'time_charge_pre_120_post_1200', 'baseline_mode': 'time_charge', 'include_pre_s': 120.0, 'include_post_s': 1200.0, 'rows': 82, 'quality_pass_rows': 66, 'quality_pass_fraction': 0.8048780487804879, 'median_corr_quality': 0.9282648777010276, 'corr_ge_0p75_rows_quality': 66, 'corr_ge_0p75_fraction_quality': 1.0, 'median_scaled_rmse_quality': 0.372018885032928, 'median_time_rmse_mv_quality': 5.68612625058436}`
- Verdict: `cold_time_window_candidate_fix`

## Top Variant Summary

| Variant | Quality-pass fraction | Median corr | Corr >= 0.75 fraction | Median time RMSE mV |
| --- | ---: | ---: | ---: | ---: |
| time_charge_pre_120_post_1200 | 0.8048780487804879 | 0.9282648777010276 | 1.0 | 5.68612625058436 |
| charge_pre_120_post_1200 | 0.6829268292682927 | 0.928248017443013 | 1.0 | 6.077196430384479 |
| time_charge_pre_120_post_2400 | 0.8048780487804879 | 0.9282208395916197 | 1.0 | 5.307169438706226 |
| charge_pre_120_post_2400 | 0.5609756097560976 | 0.9280617994824578 | 1.0 | 6.234901110172778 |

## Blunt Read

The target is not a pretty subset. A valid time-window rule needs high correlation and broad quality-pass coverage.
Record 3 remains a separate OCV comparability problem if it still fails the strict OCV gate.

## Outputs

- `section_28_variant_rows.csv`
- `section_28_by_variant.csv`
- `section_28_by_record_variant.csv`
- `section_28_by_protocol_variant.csv`
- `section_28_errors.csv`
- `section_28_summary.json`

## Linked Graph

![cold time-window probe cold time window probe](section_28_cold_time_window_probe.png)
