# CALB L148N58A, leakage and claim audit Leakage And Claim Audit

## Purpose

Separate engineering progress from validation proof. This is where sloppy claims go to die.

## Result

- Audit items: 5
- High-risk items: 5
- Claim boundary: `internal_engineering_result_not_clean_holdout_or_external_validation`
- Verdict: `local_leakage_and_claim_limits_documented`

## Blunt Read

frozen pulse-to-EIS rule is useful, but it is not a pristine held-out validation. The rule was shaped by earlier CALB probes. That is acceptable for building a rule; it is not acceptable as proof of generalization.

## Outputs

- `section_40_leakage_items.csv`
- `section_40_summary.json`
