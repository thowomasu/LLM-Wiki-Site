# External Validation Dataset Qualification

## Scope

This is dataset qualification, not validation.

The frozen CALB rule has not been externally validated here. The rule is the internal CALB pulse-to-EIS rule. In plain English, it asks whether a current/voltage pulse window can recover impedance-like information that agrees with EIS, which means Electrochemical Impedance Spectroscopy.

These manifests and adapter outputs answer a narrower question: do local external datasets have enough same-cell evidence to justify an unchanged-rule run, and if the run happened, did it beat a simple baseline?

## Inputs Reviewed

- NASA wrapper ZIP: `[local path redacted]`
- CALCE Storage folder: `[local path redacted]`
- NASA manifest output: `40 Outputs/Experiments/External Validation Dataset Qualification/01_NASA_Battery/`
- CALCE manifest output: `40 Outputs/Experiments/External Validation Dataset Qualification/02_CALCE_Storage_25C/`
- CALCE frozen-join adapter output: `40 Outputs/Experiments/External Validation Dataset Qualification/02_CALCE_Storage_25C/03_Adapter/`
- CALCE frozen input, rule-run readiness, baseline, and validation report outputs: `40 Outputs/Experiments/External Validation Dataset Qualification/02_CALCE_Storage_25C/04_Frozen_Inputs/` through `07_Validation_Report/`
- Validation protocol: `40 Outputs/Experiments/External Validation Dataset Qualification/VALIDATION_PROTOCOL.md`
- RADAR4KIT corrected-EIS status: `40 Outputs/Experiments/External Validation Dataset Qualification/03_RADAR4KIT_Corrected_EIS_Status/`
- RADAR4KIT frozen adapter run: `40 Outputs/Experiments/External Validation Dataset Qualification/06_RADAR4KIT_Frozen_Adapter/`
- Stanford SECL INR21700-M50T frozen adapter run: `40 Outputs/Experiments/External Validation Dataset Qualification/07_Stanford_SECL_INR21700_M50T_Frozen_Adapter/`
- KIT/RADAR4KIT manifest output: `40 Outputs/Experiments/KIT RADAR4KIT/01_Manifest/`

## Comparison

| Criterion | CALCE Storage 25 C | KIT/RADAR4KIT | Stanford SECL INR21700-M50T | Panasonic 18650PF | NASA Battery Data Set |
| --- | --- | --- | --- | --- | --- |
| Priority | First qualification path | Second after corrected EIS addendum | Clean same-cell HPPC plus EIS external check | New runnable adapter smoke test | Later robustness |
| Current local status | Manifest, adapter, frozen inputs, and blocked validation report | Corrected EIS addendum available locally; frozen adapter run completed with `no support` | Diagnostic ZIP available locally; frozen adapter run completed with `no support` | Frozen adapter run completed with `no support` | Manifest only |
| Same-cell EIS | Yes, same PLN capacity and impedance candidates | Yes from corrected `cell_eisv2_fixed.zip`; do not use the incomplete original `cell_eisv2.zip` | Yes, by diagnostic round, cell label, channel, and SOC20/50/80 | Yes, by matched pulse/EIS IDs | Yes, 34 unique cells with charge, discharge, and impedance |
| Time-domain evidence | Capacity workbooks tied to PLN IDs, but no HPPC-compatible pulse windows in current inputs | Profile ageing, pulse pattern, and drive/profile data | HPPC diagnostic files for the same cells and channels | Long discharge windows in selected `dis5_10p` files | Charge and discharge cycling |
| Explicit SOC labels | Strong: 0, 50, and 100 percent SOC metadata | Promising, dataset-dependent | Strong: EIS SOC20, SOC50, and SOC80 | Uses voltage/state matching, weaker than explicit SOC | Weak for bridge alignment |
| Temperature | Direct 25 C target subset | Dataset-dependent | 23 C nominal diagnostic tests | 25 C, 10 C, 0 C, -10 C, -20 C | Present, but mixed with other ambient conditions |
| Candidate pairings | 24 same-PLN capacity plus EIS rows at 25 C, 0 frozen-rule runnable rows in current inputs | 228 corrected EIS plus PULSE joins; 456 runnable frozen-rule rows; 411 quality-pass rows; 454 voltage-only baseline-pass rows; verdict `no support` | 61 same-cell HPPC plus EIS joins; 182 runnable frozen-rule rows; 0 quality-pass rows; 76 voltage-only baseline-pass rows; verdict `no support` | 3 adapter joins; 33 rule rows; 0 quality-pass rows; 14 voltage-only baseline-pass rows; verdict `no support` | 68 same-cell impedance plus charge/discharge rows |
| Fit to CALB failure mode | Best first qualification path, still blocked for actual pulse validation | Best drive/profile-ageing candidate, but the unchanged frozen run lost to baseline | Good data class, but the unchanged frozen run failed | Runnable and useful, but the unchanged frozen run failed | Later robustness check, weak for the pulse/drive-profile failure mode |

## Recommendation

Use CALCE Storage 25 C first, but be precise about what happened.

Reason: CALCE has the cleaner external qualification path for the frozen CALB rule because it exposes PLN IDs, SOC labels, 25 C conditions, capacity workbooks, and same-cell impedance CSVs. The frozen input build produced 24 same-join qualification rows, but 0 rows are scientifically runnable by the frozen pulse-to-EIS rule because the current inputs do not expose HPPC-compatible pulse windows.

Use KIT/RADAR4KIT second with the corrected EIS addendum, but be blunt: the frozen adapter run does not support the CALB rule because it fails to beat the voltage-only baseline. The incomplete local `cell_eisv2.zip` from DOI `10.35097/1947` is still not validation evidence.

Use Stanford SECL as a real external HPPC plus EIS check, but do not rescue the claim. It has the right data class and clean same-cell joins, yet the unchanged frozen rule produced 0 quality-pass rows and lost to the voltage-only baseline.

Use Panasonic 18650PF as a useful external adapter smoke test, not as success. It was runnable, but the unchanged frozen rule produced 0 quality-pass rows and did not beat the voltage-only baseline.

Use NASA third as a robustness check. It is not useless, but it is the wrong first fight. It has same-cell impedance plus charge/discharge cycling, not the pulse or drive-profile structure that already broke confidence in the drive-cycle ECM baseline check, SOC alignment audit, leakage and claim audit, and SOC-stratified drive-cycle audit. If you start with NASA because it has more rows, you are optimizing for comfort instead of the actual failure mode. That would be bad science.

## Claim Boundary

Allowed:

- CALCE Storage 25 C is the better first external dataset for same-cell capacity plus EIS qualification.
- KIT/RADAR4KIT is second with the corrected EIS addendum, but the current frozen adapter verdict is `no support`.
- Stanford SECL is a real same-cell HPPC plus EIS external check, but the current frozen adapter verdict is `no support`.
- Panasonic 18650PF is runnable external evidence, but the current frozen adapter verdict is `no support`.
- NASA is usable later as a same-cell impedance plus charge/discharge robustness check.

Not allowed:

- The CALB rule is externally validated.
- NASA validates the drive-cycle bridge.
- CALCE validates drive-cycle behavior. It does not.
- The corrected RADAR4KIT adapter run validates the frozen CALB rule. It does not; it fails to beat the voltage-only baseline.
- The Stanford SECL adapter run validates the frozen CALB rule. It does not; it has 0 quality-pass rows.
- The incomplete local RADAR4KIT `cell_eisv2.zip` validates the frozen CALB rule. It does not.

## Next Step

Current CALCE status:

1. Join keys are frozen: `pln_id`, `temperature_c`, `storage_period`, and `soc_percent`.
2. `04_Frozen_Inputs/` records 24 same-join qualification rows.
3. `05_Frozen_Rule_Run/` records `blocked/inconclusive`; the frozen rule was not run.
4. `06_Baseline_Comparison/` records that no fair baseline comparison exists yet.
5. `07_Validation_Report/` gives the only allowed verdict: `blocked/inconclusive`.

Next requirement: find or build a same-PLN CALCE path with HPPC-compatible pulse windows tied to the same 25 C, storage-period, and SOC rows. If that evidence does not exist, do not pretend capacity summaries are pulse evidence.

## Generated Artifacts

- `40 Outputs/Experiments/External Validation Dataset Qualification/01_NASA_Battery/README.md`
- `40 Outputs/Experiments/External Validation Dataset Qualification/01_NASA_Battery/summary.json`
- `40 Outputs/Experiments/External Validation Dataset Qualification/02_CALCE_Storage_25C/README.md`
- `40 Outputs/Experiments/External Validation Dataset Qualification/02_CALCE_Storage_25C/summary.json`
- `40 Outputs/Experiments/External Validation Dataset Qualification/02_CALCE_Storage_25C/03_Adapter/README.md`
- `40 Outputs/Experiments/External Validation Dataset Qualification/02_CALCE_Storage_25C/03_Adapter/adapter_summary.json`
- `40 Outputs/Experiments/External Validation Dataset Qualification/02_CALCE_Storage_25C/03_Adapter/adapter_candidate_table.csv`
- `40 Outputs/Experiments/External Validation Dataset Qualification/02_CALCE_Storage_25C/04_Frozen_Inputs/README.md`
- `40 Outputs/Experiments/External Validation Dataset Qualification/02_CALCE_Storage_25C/05_Frozen_Rule_Run/README.md`
- `40 Outputs/Experiments/External Validation Dataset Qualification/02_CALCE_Storage_25C/06_Baseline_Comparison/README.md`
- `40 Outputs/Experiments/External Validation Dataset Qualification/02_CALCE_Storage_25C/07_Validation_Report/README.md`
- `40 Outputs/Experiments/External Validation Dataset Qualification/03_RADAR4KIT_Corrected_EIS_Status/README.md`
- `40 Outputs/Experiments/External Validation Dataset Qualification/05_Panasonic_18650PF_Frozen_Adapter/README.md`
- `40 Outputs/Experiments/External Validation Dataset Qualification/06_RADAR4KIT_Frozen_Adapter/README.md`
- `40 Outputs/Experiments/External Validation Dataset Qualification/07_Stanford_SECL_INR21700_M50T_Frozen_Adapter/README.md`
