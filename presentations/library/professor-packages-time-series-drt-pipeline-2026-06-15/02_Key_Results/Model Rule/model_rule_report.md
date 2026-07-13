# Pre-Declared Model Rule

## Purpose

This section selects the time-domain model setting before looking at EIS agreement.
That matters because choosing lambda or baseline after seeing EIS is validation leakage.

## Rule

- Baseline mode is fixed at `time_charge`.
- SOC selection is `coulomb` when raw data is available.
- Tested lambda values: 0.001, 0.1, 1.0, 3.0
- Lambda must stay within best voltage RMSE plus max 5% or 0.25 mV.
- Within that RMSE band, prefer lower gamma roughness and more stable fast/mid/slow band areas.
- EIS metrics are reported after selection. They are not allowed into the selection score.

## Run Summary

- Input mode: existing model-sensitivity CSV
- Discovery: {"source_rows": 40, "selected_case_count": 10, "target_count": 10}
- Selected comparisons: 10
- Lambda candidates scored: 40
- Errors: 0
- Quality-pass comparisons: 10 of 10
- Median voltage RMSE: 1.7106937066290135 mV
- Median EIS correlation after rule selection: 0.1406798483387754
- Median normalized RMSE after rule selection: 0.978374331390654

## Selected Settings

- Cell 15, SOH 80, SOC 5: lambda 0.001, RMSE 2.453939421743068 mV, corr -0.1265397461419299, norm_RMSE 0.8348886970647139
- Cell 15, SOH 80, SOC 20: lambda 0.001, RMSE 1.7602909654926566 mV, corr 0.1711563289826563, norm_RMSE 0.963384725467954
- Cell 15, SOH 80, SOC 50: lambda 0.001, RMSE 1.707345639066683 mV, corr 0.1235206298583345, norm_RMSE 1.1449411226020272
- Cell 15, SOH 80, SOC 70: lambda 0.001, RMSE 1.7140417741913443 mV, corr 0.1431196141299693, norm_RMSE 0.993363937313354
- Cell 15, SOH 80, SOC 95: lambda 0.001, RMSE 1.843328008934464 mV, corr 0.1205178183642547, norm_RMSE 1.148760961863879
- Cell 18, SOH 80, SOC 5: lambda 0.001, RMSE 2.2677522881010104 mV, corr -0.0966331156982791, norm_RMSE 1.0599420440685534
- Cell 18, SOH 80, SOC 20: lambda 0.001, RMSE 1.5860296058503212 mV, corr 0.1813068040303565, norm_RMSE 0.918411490941448
- Cell 18, SOH 80, SOC 50: lambda 0.001, RMSE 1.5106343240204447 mV, corr 0.1382400825475815, norm_RMSE 1.0545358802461242
- Cell 18, SOH 80, SOC 70: lambda 0.001, RMSE 1.5052806002076426 mV, corr 0.157819597243833, norm_RMSE 0.9111891114649304
- Cell 18, SOH 80, SOC 95: lambda 0.001, RMSE 1.544494474143958 mV, corr 0.1720153824416916, norm_RMSE 0.8136607016125303

## Selection Diagnostics

- Selected lambda values: [0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]
- Median selection score: 1.4

## Interpretation

This improves the pipeline because the model choice is now explicit and reproducible.
It still does not validate time-domain DRT as a substitute for EIS. If the post-selection EIS metrics remain weak, believe the weakness.

Blunt takeaway: this script makes the pipeline more honest. It does not make the science magically true.

## Outputs

- `model_rule_results.csv`: one selected setting per target with EIS metrics added afterward.
- `model_rule_lambda_candidates.csv`: every lambda candidate and internal selection score.
- `model_rule_errors.csv`: failures.
- `model_rule_case_summaries.json`: raw-case or existing-output run metadata.
- `model_rule_report.md`: this report.

<!-- BEGIN BEGINNER_MATH_EXPLANATION -->
## How This Section Works, Plain Math

This section uses a pre-declared rule to choose model settings before looking at EIS agreement.

### Why this matters

If we choose lambda after seeing EIS, we are tuning to the answer key. That makes the validation look better than it really is.

### The rule

The rule prefers candidates with:

- low voltage RMSE
- smoother gamma
- stable broad-band areas
- enough nonzero gamma points

It does not use EIS correlation while choosing.

### What this section proves

It gives a more honest validation check. In the current result, the honest rule still gives weak EIS agreement. That is bad news scientifically, but useful because it prevents false confidence.

### Actual Equations Used

The model rule chooses settings before looking at EIS agreement. It combines voltage fit, roughness, and stability:

$$
\mathrm{score}
=
w_1\,\widetilde{\mathrm{RMSE}}
+w_2\,\widetilde{\left\|L\gamma\right\|_2}
+w_3\,\widetilde{\mathrm{band\ instability}}
+w_4\,\widetilde{\mathrm{sparsity\ penalty}}
$$

The selected model is:

$$
\theta^*
=
\arg\min_{\theta\in\Theta}\mathrm{score}(\theta)
$$

\(\theta\) represents choices like baseline mode and \(\lambda\). EIS correlation is not part of the selection score.

After choosing \(\theta^*\), the report computes:

$$
r_{\text{held-out style}}
=
\operatorname{corr}
\left(\gamma_{\text{TD}}(\tau;\theta^*),\gamma_{\text{EIS}}(\tau)\right)
$$

That is the honest check. If it is weak, the method is weak under the declared rule.
<!-- END BEGINNER_MATH_EXPLANATION -->
