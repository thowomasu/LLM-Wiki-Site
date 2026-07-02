# CALB L148N58A, drive-cycle transfer test Drive-Cycle Validation

## Purpose

Test whether HPPC/EIS bridge parameters from frozen pulse-to-EIS rule transfer to real drive-cycle voltage prediction.
This is a held-out voltage test, not an SOH or aging test.

## Method

- Select the frozen pulse-to-EIS rule bridge row nearest the drive-cycle calibration voltage.
- Refit that HPPC window to recover fixed `R0` and `gamma(tau)`.
- On the drive cycle, fit only free baseline terms on the calibration prefix.
- Evaluate voltage prediction on the held-out remainder.
- Compare against a baseline-only model using the same calibration prefix and baseline terms.

## Result

- Row count: 198
- Error count: 0
- DRT win rows vs baseline: 198
- DRT win fraction vs baseline: 1.0
- Median DRT holdout RMSE: 150.9172295922953 mV
- Median baseline holdout RMSE: 164.95303653565315 mV
- Median DRT improvement vs baseline: 16.830790799673707 mV
- Median absolute drive-to-EIS voltage delta: 0.05646359671020518 V
- Verdict: `drive_cycle_transfer_supports_hppc_drt`

## By Drive Protocol

| Drive protocol | Rows | DRT win fraction | Median DRT RMSE mV | Median baseline RMSE mV | Median improvement mV |
| --- | ---: | ---: | ---: | ---: | ---: |
| DV_UDDS | 66 | 1.0 | 131.2081976466422 | 134.39836852785044 | 3.1314767266472714 |
| DV_US06 | 66 | 1.0 | 152.8682174709113 | 173.32145509516408 | 22.283620970532525 |
| DV_WLTP | 66 | 1.0 | 159.53376528724039 | 179.69523664488855 | 19.786231814408538 |

## By Temperature

| Temperature | Rows | DRT win fraction | Median DRT RMSE mV | Median baseline RMSE mV |
| ---: | ---: | ---: | ---: | ---: |
| 10 | 66 | 1.0 | 142.19544996787465 | 148.4199799105207 |
| 25 | 66 | 1.0 | 152.24146203296473 | 174.12741750826908 |
| 40 | 66 | 1.0 | 151.72285195785346 | 166.92168241501076 |

## By HPPC Source

| HPPC protocol | Rows | DRT win fraction | Median DRT RMSE mV | Median baseline RMSE mV |
| --- | ---: | ---: | ---: | ---: |
| HPPC_1C | 99 | 1.0 | 150.93190829684113 | 164.95303653565315 |
| HPPC_C3 | 99 | 1.0 | 150.9015473639156 | 164.95303653565315 |

## Blunt Read

This is the first real dynamic transfer test after the pulse/EIS bridge was solved. If the DRT model does not beat the baseline-only model on held-out drive-cycle voltage, the method is not validated for drive cycles yet.
Even when it helps, this still does not prove SOH or aging prediction.

## Outputs

- `section_34_drive_cycle_rows.csv`
- `section_34_by_drive_protocol.csv`
- `section_34_by_temperature.csv`
- `section_34_by_hppc_protocol.csv`
- `section_34_errors.csv`
- `section_34_summary.json`

## Linked Graph

![drive-cycle transfer test drive cycle validation](section_34_drive_cycle_validation.png)
