# Column Guide

This is a practical guide, not a full formal schema.
Use it to understand the output CSVs in this package.

## Common Raw Time-Series Columns

| Normalized name | Common source name | Meaning |
|---|---|---|
| `time_s` | `Time (s)`, `time/s` | Time in seconds. |
| `current_a` | `Current (mA)`, `I/mA` | Current converted to amps when needed. Sign convention depends on source file. |
| `voltage_v` | `Voltage (V)`, `Ecell/V` | Cell voltage in volts. |
| `temperature_c` | `Temperature (degC)`, `Temperature/degC` | Cell or test temperature in Celsius. |

## GITT / DRT Feature Columns

| Column | Meaning | Caveat |
|---|---|---|
| `r0_ohm` | Immediate resistance-like voltage step estimate. | Useful, but not a DRT peak. |
| `rmse_mv` | Fit error in millivolts. Lower is better. | Good fit error does not prove physical correctness. |
| `main_peak_tau_s` | Time constant of strongest recovered peak. | Model-sensitive. Do not overinterpret. |
| `main_peak_gamma_ohm` | Strength of strongest recovered peak. | Depends on regularization and preprocessing. |
| `fast_band_*`, `mid_band_*`, `slow_band_*` | Summed DRT-like resistance over tau bands. | Exploratory without EIS validation. |

## Health Label Columns

| Column | Meaning |
|---|---|
| `soh` | State of health. |
| `c10_capacity_mah` | Capacity from C/10 discharge. |
| `c2_capacity_mah` | Capacity from C/2 discharge where available. |
| `resistance_0p1s_ohm` | 0.1 second resistance label from the dataset summary. |
| `charge_throughput_ah` | Accumulated charge throughput. |
| `energy_throughput_wh` | Accumulated energy throughput. |
| `days_degradation` | Days of degradation since ageing began. |

## Leakage-Prone Columns

Treat these carefully:

| Pattern | Why it is risky |
|---|---|
| `*_capacity_mah_integrated_or_reported` | Can directly encode capacity targets. |
| `*_duration_per_mah_s` | Divides by measured capacity. |
| `hybrid_*_current_transition_count` | Can act as a proxy for discharge duration before cutoff. |
| `voltage_at_*pct_capacity` | Uses measured capacity axis to choose the point. |
| `gitt_r0_ohm` for `resistance_0p1s_ohm` | Same-test resistance proxy, not independent DRT evidence. |

## Where To Find Tables

| Output | Location |
|---|---|
| Processed time-series manifest | `../02_Pipeline_Report/02_Section_Results/Section_01_Data_Audit/section_1_processed_timeseries_manifest.csv` |
| Performance labels | `../02_Pipeline_Report/02_Section_Results/Section_01_Data_Audit/section_1_performance_summary_labels.csv` |
| GITT batch features | `../02_Pipeline_Report/02_Section_Results/Section_05_GITT_Batch/section_5_gitt_batch_results.csv` |
| Health label join | `../02_Pipeline_Report/02_Section_Results/Section_08_Health_Label_Join/section_8_health_label_join_results.csv` |
| Held-out validation metrics | `../02_Pipeline_Report/02_Section_Results/Section_09_Held_Out_Cell_Validation/section_9_held_out_cell_metrics.csv` |
| Multi-protocol metrics | `../02_Pipeline_Report/02_Section_Results/Section_13_Multi_Protocol_Validation/section_13_multi_protocol_metrics.csv` |
| Leakage audit | `../04_Validation_Audit/Validation_Audit/leakage_feature_audit.csv` |
