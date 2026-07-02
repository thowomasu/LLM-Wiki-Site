# CALB L148N58A, cold-temperature diagnosis Cold-Temperature Diagnosis

## Purpose

Diagnose why the 10 C tau-constrained bridge stays weak while 25 C and 40 C pass.
This is a diagnostic probe, not a validation shortcut. Picking a best candidate by correlation is not a deployable method.

## Result

- Temperature tested: 10 C
- Protocols: HPPC_1C, HPPC_C3
- Cells attempted per protocol: 11
- Candidate probe rows: 653
- Case rows: 82
- Error count: 0
- Median nearest OCV correlation, strict pass only: -0.024996621549416252
- Median nearest OCV correlation, including failed quality rows: 0.8165076252865685
- Median best-within-20mV correlation: -0.024996621549416252
- Median best-any-voltage-pass correlation: 0.9105986934027989

## Diagnosis Counts

| Diagnosis | Cases |
| --- | ---: |
| nearest_ocv_ok | 26 |
| only_bad_ocv_candidate_rescues | 56 |

## By EIS Record And Protocol

| EIS record | Protocol | Cases | Nearest strict pass | Nearest ok | Best <=20mV ok | Best voltage-pass ok | Nearest strict corr | Best <=20mV corr | Best any corr |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | HPPC_1C | 11 | 11 | 0 | 0 | 11 | -0.03043887451459624 | -0.03043887451459624 | 0.9086451955326511 |
| 0 | HPPC_C3 | 11 | 11 | 0 | 0 | 11 | -0.033760900005029675 | -0.033760900005029675 | 0.9080397047337717 |
| 1 | HPPC_1C | 11 | 11 | 3 | 3 | 11 | -0.027761263197862488 | -0.027761263197862488 | 0.9092734264447823 |
| 1 | HPPC_C3 | 11 | 11 | 1 | 1 | 11 | -0.030199057581557838 | -0.030199057581557838 | 0.9088861630272687 |
| 2 | HPPC_1C | 11 | 11 | 11 | 11 | 11 | 0.9099581065430711 | 0.9099581065430711 | 0.9099581065430711 |
| 2 | HPPC_C3 | 11 | 11 | 11 | 11 | 11 | 0.9113824092255232 | 0.9113824092255232 | 0.9113824092255232 |
| 3 | HPPC_1C | 8 | 0 | 0 | 0 | 8 | None | None | 0.9137587349767049 |
| 3 | HPPC_C3 | 8 | 0 | 0 | 0 | 8 | None | None | 0.9147527563425193 |

## Blunt Read

If best-within-20mV rescues a failed record, the next fix is better cold-temperature alignment.
If only far-away OCV candidates rescue it, that is not a valid fix because it breaks same-state comparison.
If no candidate rescues it, the 10 C failure is a model/EIS-shape mismatch and should stay excluded from the main viability claim until the method is revised.

## Outputs

- `section_24_candidate_probe_rows.csv`
- `section_24_case_summary.csv`
- `section_24_by_record_protocol.csv`
- `section_24_diagnosis_counts.csv`
- `section_24_errors.csv`
- `section_24_summary.json`

## Linked Graph

![cold-temperature diagnosis cold-temperature diagnosis](section_24_cold_temperature_diagnosis.png)
