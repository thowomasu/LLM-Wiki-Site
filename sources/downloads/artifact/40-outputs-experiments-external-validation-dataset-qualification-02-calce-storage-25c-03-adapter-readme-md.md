# CALCE Storage 25 C Frozen-Join Adapter

## Scope

This is an adapter smoke artifact, not an external validation result.

The frozen join keys are `pln_id`, `temperature_c`, `storage_period`, and `soc_percent`. A later validation run must use these rows without tuning the CALB frozen pulse-to-EIS rule to fit CALCE.

## Result

- Candidate rows: 24
- Ready rows: 24
- Blocked rows: 0
- Candidate PLN IDs: PLN45, PLN46, PLN47, PLN48, PLN51, PLN52, PLN53, PLN54, PLN59, PLN63, PLN64, PLN65, PLN67, PLN68, PLN69, PLN70, PLN71, PLN72, PLN73, PLN74, PLN75, PLN76, PLN77, PLN78

## Claim Boundary

- CALCE is the first external qualification target for the frozen CALB rule.
- This table only proves the local CALCE manifests can be joined cleanly enough to build frozen inputs.
- It does not prove the CALB rule generalizes.
- RADAR4KIT remains second only after the corrected EIS addendum is available.
- NASA remains a later robustness check, not the first external validation target.

## Outputs

- `adapter_candidate_table.csv`
- `adapter_summary.json`
- `README.md`
