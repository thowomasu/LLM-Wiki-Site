# SOC Mapping Sensitivity

## Purpose

This run treats SOC mapping as an assumption layer. It reruns the same DIB cases under multiple SOC mapping rules and checks whether the comparison metrics change.

## Run Settings

- Modes: voltage, coulomb, endpoint, linear
- Max cases: 3
- Temperature: 25 C
- Cycle rule: earliest
- Lambda value: 0.001
- Selected capacity cases: 3

## Mode Summary

- coulomb: comparisons=15, errors=0, median RMSE=1.5860375265071827 mV, median corr=0.10456968399932068, median normalized RMSE=0.8655229771443936, median abs SOC error=3.0040876726529575
- endpoint: comparisons=15, errors=0, median RMSE=1.5860375265071827 mV, median corr=0.10456968399932068, median normalized RMSE=0.8655229771443936, median abs SOC error=0.6863347295694382
- linear: comparisons=15, errors=0, median RMSE=1.5860375265071827 mV, median corr=0.10456968399932068, median normalized RMSE=0.8655229771443936, median abs SOC error=2.445991031022345
- voltage: comparisons=15, errors=0, median RMSE=1.5860375265071827 mV, median corr=0.10456968399932068, median normalized RMSE=0.8655229771443936, median abs SOC error=None

## Stability Summary

- Targets with different candidate IDs across modes: 0
- Targets with correlation range above 0.1 across modes: 0

## Interpretation

If the same conclusion only appears under one SOC mapping mode, it is fragile.
If weak EIS agreement persists across all modes, the mismatch is probably not only an SOC-mapping artifact.

Blunt warning: this does not create ground truth. It only tells us whether our assumptions are steering the result.

## Outputs

- `soc_mapping_sensitivity_results.csv`
- `soc_mapping_sensitivity_mode_summary.csv`
- `soc_mapping_sensitivity_by_target.csv`
- `soc_mapping_sensitivity_case_summaries.json`
- `soc_mapping_sensitivity_errors.csv`
- `soc_mapping_sensitivity_report.md`

<!-- BEGIN BEGINNER_MATH_EXPLANATION -->
## How This Section Works, Plain Math

This section tests SOC assignment assumptions.

### The modes

`voltage` sorts candidates by pre-rest voltage.

`coulomb` uses current integration from a high-SOC anchor.

`endpoint` forces the highest-voltage and lowest-voltage candidates to match endpoint SOC labels.

`linear` fits a straight line between integrated charge and SOC labels.

### Why this matters

If changing SOC mode changes the EIS comparison a lot, then SOC matching is a major uncertainty.

If the result barely changes, then SOC mapping is probably not the main reason for the mismatch in this small run.

### Actual Equations Used

Voltage-order mapping sorts windows by pre-rest voltage:

$$
V_{\text{pre},k}=\operatorname{median}(V_{\text{rest before window }k})
$$

Coulomb mapping uses integrated charge:

$$
Q_k = \frac{1}{3600}\int_{t_{\text{anchor}}}^{t_k} I(t)\,dt
$$

$$
\widehat{\mathrm{SOC}}_k
=
\mathrm{SOC}_{\text{anchor}}
-100\frac{Q_k}{C_{\text{Ah}}}
$$

Linear mapping fits a line from integrated charge to SOC:

$$
\widehat{\mathrm{SOC}}_k = aQ_k+b
$$

The sensitivity question is whether changing this mapping changes the EIS comparison metrics.
<!-- END BEGINNER_MATH_EXPLANATION -->
