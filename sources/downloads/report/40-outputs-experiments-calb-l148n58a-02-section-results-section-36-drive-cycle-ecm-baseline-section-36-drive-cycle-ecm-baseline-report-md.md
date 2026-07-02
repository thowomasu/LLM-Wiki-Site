# CALB L148N58A, drive-cycle ECM baseline check Drive-Cycle ECM Baseline Audit

## Purpose

Check whether the drive-cycle transfer test drive-cycle win survives against stronger drive-cycle-fitted ECM-style baselines.
The baseline family fits the same calibration prefix and scores the same held-out drive-cycle tail.

## Result

- Source drive-cycle transfer test rows: 198
- Error count: 0
- Median fixed DRT holdout RMSE: 150.9172295922953 mV
- Median best ECM holdout RMSE: 134.8626012268972 mV
- Median DRT minus best ECM RMSE: 3.0704702158353285 mV
- DRT win fraction versus best ECM: 0.12121212121212122
- Best median ECM variant: `ohmic_2rc_10_300s`
- Verdict: `drive_cycle_ecm_baseline_beats_fixed_drt`

## By Model Variant

| Variant | Rows | Median DRT RMSE mV | Median variant RMSE mV | Median DRT minus variant mV | DRT win fraction |
| --- | ---: | ---: | ---: | ---: | ---: |
| baseline_only | 198 | 150.9172295922953 | 164.95303653565315 | -16.830790799673707 | 1.0 |
| ohmic_1rc_30s | 198 | 150.9172295922953 | 150.79238757830163 | 0.2198696475397668 | 0.3939393939393939 |
| ohmic_2rc_10_300s | 198 | 150.9172295922953 | 134.8626012268972 | 3.0704702158353285 | 0.15151515151515152 |
| ohmic_4rc_1_10_100_1000s | 198 | 150.9172295922953 | 158.07213976163268 | -5.726213193993502 | 1.0 |
| ohmic_only | 198 | 150.9172295922953 | 154.9951231564915 | -5.542149356906876 | 1.0 |

## Best ECM By Drive Protocol

| Drive protocol | Rows | Median DRT RMSE mV | Median best ECM RMSE mV | Median DRT minus ECM mV | DRT win fraction |
| --- | ---: | ---: | ---: | ---: | ---: |
| DV_UDDS | 66 | 131.2081976466422 | 128.2821352539987 | 3.05192775418832 | 0.0 |
| DV_US06 | 66 | 152.8682174709113 | 124.40485570894795 | 26.35090247004746 | 0.24242424242424243 |
| DV_WLTP | 66 | 159.53376528724039 | 153.62915645634274 | 2.816927674014707 | 0.12121212121212122 |

## Blunt Read

drive-cycle transfer test was a useful first transfer test, but its baseline was weak. drive-cycle ECM baseline check is the honest follow-up.
If the ECM baseline wins, the drive-cycle claim must be downgraded to `fixed DRT beats baseline-only, but not a stronger calibrated ECM baseline`.
If fixed DRT wins, the drive-cycle transfer claim is stronger, but still not SOH, aging, or external validation.

## Outputs

- `section_36_ecm_baseline_rows.csv`
- `section_36_by_model_variant.csv`
- `section_36_best_ecm_by_drive_protocol.csv`
- `section_36_errors.csv`
- `section_36_summary.json`

## Linked Graph

![drive-cycle ECM baseline check ecm baseline audit](section_36_drive_cycle_ecm_baseline.png)
