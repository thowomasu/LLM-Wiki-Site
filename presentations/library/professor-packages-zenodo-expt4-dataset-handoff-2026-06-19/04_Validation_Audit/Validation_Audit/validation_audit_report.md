# LG M50T 21700 Expt 4 drive-cycle aging Validation Audit

## Verdict

The dataset provenance is strong, but the modeling claim is weaker than the previous headline scores suggest.
The local Expt4 zip matches the Zenodo MD5, so the input source is not the problem.
The problem is that several features are capacity, duration, or same-test resistance proxies.

Defensible claim: Expt4 supports an internal health-feature benchmark using grouped validation.
Not defensible: DRT physics validation, EIS validation, or a claim that hybrid pulse features independently predict SOH/C10.

## Provenance Status

- Zenodo record: [https://zenodo.org/records/10637534](https://zenodo.org/records/10637534)
- Dataset DOI: [https://doi.org/10.5281/zenodo.10637534](https://doi.org/10.5281/zenodo.10637534)
- Related paper DOI listed by Zenodo: [https://doi.org/10.1016/j.jpowsour.2024.234185](https://doi.org/10.1016/j.jpowsour.2024.234185)
- Local zip: `[local path redacted]`
- Published Expt4 MD5: `99083707bc7a24e72d9865abac19ce50`
- Local Expt4 MD5: `99083707bc7a24e72d9865abac19ce50`
- Provenance verdict: `complete_md5_match`

## Leakage Findings

- `discharge_*capacity_mah_integrated_or_reported` is direct leakage for SOH and C10 capacity.
- `discharge_*duration_per_mah_s` divides by measured capacity. It is not a clean feature.
- `hybrid_*current_transition_count` is the nasty one. It mostly counts how long the hybrid discharge ran before cutoff, so it tracks usable capacity.
- `gitt_r0_ohm` is not a DRT feature. For `resistance_0p1s_ohm`, it is a same-test resistance proxy.
- `voltage_at_*pct_capacity` is target-conditioned, because the point is chosen using the measured capacity axis. Useful, but do not call it independent.

Top suspicious correlations:

- c10_capacity_mah / discharge_0p1c_capacity_mah_integrated_or_reported: Spearman 1.000, n=80
- c10_capacity_mah / discharge_0p5c_capacity_mah_integrated_or_reported: Spearman 1, n=40
- c10_capacity_mah / hybrid_0p5c_current_transition_count: Spearman 0.999, n=40
- c10_capacity_mah / hybrid_1c_current_transition_count: Spearman 0.997, n=40
- soh / discharge_0p1c_capacity_mah_integrated_or_reported: Spearman 0.996, n=80
- soh / hybrid_1c_current_transition_count: Spearman 0.995, n=40
- soh / hybrid_0p5c_current_transition_count: Spearman 0.995, n=40
- soh / discharge_0p5c_capacity_mah_integrated_or_reported: Spearman 0.989, n=40

## Validation Results

### leave_one_cell_out
soh:
- voltage_only: MAE 0.01316, baseline 0.04947, skill 0.734, n=80, features=6
- all_protocols: MAE 0.01552, baseline 0.04947, skill 0.686, n=80, features=18
- hybrid_only: MAE 0.02694, baseline 0.05018, skill 0.463, n=40, features=8
- discharge_only: MAE 0.0284, baseline 0.04947, skill 0.426, n=80, features=6
c10_capacity_mah:
- voltage_only: MAE 71.368, baseline 244.7, skill 0.708, n=80, features=6
- all_protocols: MAE 81.972, baseline 244.7, skill 0.665, n=80, features=18
- hybrid_only: MAE 139.3, baseline 248.7, skill 0.44, n=40, features=8
- discharge_only: MAE 138.5, baseline 244.7, skill 0.434, n=80, features=6
resistance_0p1s_ohm:
- r0_only: MAE 0.0004643, baseline 0.001851, skill 0.749, n=40, features=1
- drt_plus_r0: MAE 0.0005016, baseline 0.001851, skill 0.729, n=40, features=4
- voltage_only: MAE 0.0009264, baseline 0.001851, skill 0.5, n=40, features=6
- all_protocols: MAE 0.0009985, baseline 0.001851, skill 0.461, n=40, features=24

### leave_one_temperature_out
soh:
- all_protocols: MAE 0.01916, baseline 0.04917, skill 0.61, n=80, features=18
- voltage_only: MAE 0.0203, baseline 0.04917, skill 0.587, n=80, features=6
- hybrid_only: MAE 0.02619, baseline 0.04934, skill 0.469, n=40, features=8
- r0_only: MAE 0.02925, baseline 0.04928, skill 0.406, n=40, features=1
c10_capacity_mah:
- all_protocols: MAE 101.2, baseline 241.8, skill 0.582, n=80, features=18
- voltage_only: MAE 104.5, baseline 241.8, skill 0.568, n=80, features=6
- hybrid_only: MAE 136.1, baseline 243.2, skill 0.44, n=40, features=8
- r0_only: MAE 151.4, baseline 242.1, skill 0.375, n=40, features=1
resistance_0p1s_ohm:
- r0_only: MAE 0.0005126, baseline 0.001899, skill 0.73, n=40, features=1
- drt_plus_r0: MAE 0.0005885, baseline 0.001899, skill 0.69, n=40, features=4
- all_protocols: MAE 0.000752, baseline 0.001814, skill 0.585, n=10, features=24
- voltage_only: MAE 0.001137, baseline 0.001899, skill 0.401, n=40, features=6

## Honest Claim

DRT bands alone do not carry the result. R0 is doing the useful resistance work.
Hybrid looks impressive only before you notice the duration and transition-count proxy problem.
After strict proxy exclusion, any remaining hybrid result should be treated as exploratory, not proof.
Leave-one-temperature-out is the reality check. If a feature set collapses there, it is learning temperature or protocol context, not a durable health law.

## What Is Defensible

- The Expt4 pipeline can parse and align processed GITT, discharge, and hybrid time-series features.
- Same-dataset, leave-one-cell-out health prediction is possible for some targets.
- `gitt_r0_ohm` is a strong internal predictor of `resistance_0p1s_ohm`.
- Non-GITT voltage and pulse summaries may contain health signal, but they need stricter external validation.

## What Is Not Defensible

- Do not claim EIS validation. This audit found no EIS comparison target in the inspected outputs.
- Do not claim recovered DRT peaks are physically validated by this dataset.
- Do not present hybrid-only SOH/C10 scores as independent health inference.
- Do not sell all-protocol performance as proof that DRT adds major value.

## Next Experiment Recommendation

Run a preregistered comparison with three locked baselines: R0 only, DRT bands without R0, and R0 plus DRT bands.
Use leave-one-temperature-out as the headline validation, not the appendix.
Add a true external target if the goal is DRT physics, ideally EIS-derived resistance or EIS DRT measured on the same cells and RPTs.

## Output Files

- `validation_metrics.csv`
- `leakage_feature_audit.csv`
- `feature_target_correlations.csv`
- `validation_audit_summary.json`

## Sources

- Zenodo record for the dataset and Expt4 zip: [https://zenodo.org/records/10637534](https://zenodo.org/records/10637534)
- Zenodo dataset DOI: [https://doi.org/10.5281/zenodo.10637534](https://doi.org/10.5281/zenodo.10637534)
- Related Journal of Power Sources article DOI, as listed by Zenodo: [https://doi.org/10.1016/j.jpowsour.2024.234185](https://doi.org/10.1016/j.jpowsour.2024.234185)
