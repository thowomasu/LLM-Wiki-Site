# CALB L148N58A, cold baseline-sign probe Cold Baseline/Sign Probe

## Purpose

Test whether the 10 C strict-match failure is caused by the time-domain baseline form or by an inverted current sign convention.

## Result

- Temperature tested: 10 C
- Protocols: HPPC_1C, HPPC_C3
- Cells attempted per protocol: 11
- Variant rows: 656
- Error count: 0
- Best variant summary: `{'variant': 'time|sign_+1', 'baseline_mode': 'time', 'current_sign': 1, 'rows': 82, 'quality_pass_rows': 4, 'median_corr_quality': 0.9177546505204854, 'corr_ge_0p75_rows_quality': 4, 'positive_rows_quality': 4, 'median_scaled_rmse_quality': 0.3975818864770942, 'median_time_rmse_mv_quality': 9.765979694561757, 'median_r0_ohm_quality': 0.0017839619738805586}`
- Best variant quality-pass fraction: 0.04878048780487805
- Verdict: `baseline_or_sign_changes_tiny_subset_not_validation`

## Variant Summary

| Variant | Quality-pass | Median corr | Corr >= 0.75 rows | Median time RMSE mV |
| --- | ---: | ---: | ---: | ---: |
| time\|sign_+1 | 4 | 0.9177546505204854 | 4 | 9.765979694561757 |
| charge\|sign_+1 | 66 | -0.024996621549416252 | 26 | 3.9467462307603114 |
| time_charge\|sign_+1 | 66 | -0.02664342136126762 | 19 | 2.7100584621321975 |
| charge\|sign_-1 | 0 | None | 0 | None |
| offset\|sign_+1 | 0 | None | 0 | None |
| offset\|sign_-1 | 0 | None | 0 | None |
| time_charge\|sign_-1 | 0 | None | 0 | None |
| time\|sign_-1 | 0 | None | 0 | None |

## Blunt Read

If inverted current wins while voltage RMSE stays acceptable, the sign convention was suspect.
If a richer baseline wins only by fitting away the pulse shape, it is a warning, not validation.
A valid fix needs broad coverage, strong correlation under strict OCV matching, and voltage RMSE inside the gate.

## Outputs

- `section_26_variant_rows.csv`
- `section_26_by_variant.csv`
- `section_26_by_record_variant.csv`
- `section_26_by_protocol_variant.csv`
- `section_26_errors.csv`
- `section_26_summary.json`

## Linked Graph

![cold baseline-sign probe cold baseline sign probe](section_26_cold_baseline_sign_probe.png)
