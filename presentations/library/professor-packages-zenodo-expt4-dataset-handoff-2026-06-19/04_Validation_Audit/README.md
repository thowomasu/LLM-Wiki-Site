# Validation Audit

This is the most important folder for judging the scientific strength of the work.

## Files

| File | Meaning |
|---|---|
| `Validation_Audit/validation_audit_report.md` | Human-readable audit report. Start here. |
| `Validation_Audit/validation_metrics.csv` | Grouped validation metrics after stricter checks. |
| `Validation_Audit/leakage_feature_audit.csv` | Features flagged as target proxies or leakage risks. |
| `Validation_Audit/feature_target_correlations.csv` | Feature-target correlation scan. |
| `Validation_Audit/validation_audit_summary.json` | Machine-readable audit summary. |

## Main Audit Verdict

The dataset provenance is strong.
The modeling claim is weaker than the raw scores suggest.

Some features leak or proxy the target, especially capacity, duration, and same-test resistance features.
After removing those illusions, the safest claim is internal health-feature benchmarking.

## Do Not Claim

- EIS validation.
- Physically validated DRT peaks.
- Independent hybrid-only SOH or capacity prediction.
- That DRT bands alone explain the result.

## Safer Claim

Expt4 supports a useful internal benchmark for battery health features, and GITT-derived resistance features are informative for resistance-like labels.
