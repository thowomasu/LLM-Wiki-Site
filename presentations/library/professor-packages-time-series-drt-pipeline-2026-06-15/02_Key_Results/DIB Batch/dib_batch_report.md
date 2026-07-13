# Generalized DIB Batch Prototype

## Purpose

This section tests whether the time-domain DRT prototype can run on multiple DIB cells instead of one hand-picked Cell28 case.

## Run Settings

- SOH filter: all
- Cell filter: auto
- Temperature: 25 C
- Max cases: 3
- Capacity file rule: earliest cycle per cell/SOH/temp
- SOC selection method: coulomb
- Baseline mode: charge
- Lambda value: 0.001
- SOC quality threshold: 8.0 percentage points

## Outputs

- `dib_batch_results.csv`
- `dib_batch_errors.csv`
- `dib_batch_case_summaries.json`
- `dib_batch_summary.png`
- `dib_batch_report.md`

## Result Summary

- Capacity cases attempted: 3
- Matched SOC comparisons produced: 15
- Errors: 0
- Median voltage RMSE: 1.586 mV
- Median EIS correlation: 0.1046
- Quality-pass comparisons: 15 of 15
- Quality flag counts: none
- Cells processed: [15, 18, 20]
- SOH labels processed: [80, 85]
- Median absolute SOC selection error: 3.004 percentage points
- Max absolute SOC selection error: 6.069 percentage points

## Per-Cell Snapshot

- Cell 15, SOH 80, cycle 0: 5 SOC comparisons, median RMSE 1.76 mV, median corr 0.1135
- Cell 18, SOH 80, cycle 0: 5 SOC comparisons, median RMSE 1.547 mV, median corr 0.1046
- Cell 20, SOH 85, cycle 0: 5 SOC comparisons, median RMSE 1.491 mV, median corr 0.09531

## Interpretation

The generalized batch runner is a pipeline test, not proof of electrochemical validity.
It checks whether discovery, window selection, DRT fitting, and EIS comparison work across DIB cells.

Blunt warning: candidate selection is still assumption-driven. The batch runner supports voltage, coulomb, endpoint, and linear SOC mapping modes because none of them is protocol ground truth.
The `quality_pass` column is only a triage flag. Passing it means the row cleared basic engineering checks, not that the DRT is scientifically valid.

## Next Fix

Use this batch output with the SOC-mapping and model-sensitivity runners.
If SOC mapping does not change the selected windows, move the pressure to baseline/OCV handling and lambda selection.
A conclusion that only exists under one baseline or lambda setting is not robust enough to claim.

<!-- BEGIN BEGINNER_MATH_EXPLANATION -->
## How This Section Works, Plain Math

This section generalizes the pipeline beyond one hand-picked Cell28 case.

### Workflow

For each matched case:

```text
1. find capacity-check CSV
2. find matching EIS row
3. detect pulse windows
4. assign likely SOC windows
5. fit time-domain DRT
6. compare to EIS-derived DRT
7. apply quality flags
```

### Quality flags

A quality pass means the row is not obviously broken. It checks practical things like voltage RMSE, temperature drift, current size, SOC error, and overlap points.

### What this section proves

It proves the code can run across multiple cells. It does not prove the method is scientifically valid. Batch success is engineering evidence, not physics validation.

### Actual Equations Used

Each batch case repeats the same core metrics:

$$
\mathrm{RMSE}_{\mathrm{mV}}
=1000\sqrt{\frac{1}{N}\sum_{n=1}^{N}
\left(V_n-\hat{V}_n\right)^2}
$$

$$
r=\operatorname{corr}
\left(\gamma_{\text{TD}}(\tau),\gamma_{\text{EIS}}(\tau)\right)
$$

$$
\rho_A
=
\frac{\int \gamma_{\text{TD}}(\tau)\,d\log\tau}
{\int \gamma_{\text{EIS}}(\tau)\,d\log\tau}
$$

A row passes quality gates only if practical checks are acceptable:

$$
\mathrm{pass}
=
\left[
\mathrm{RMSE}_{\mathrm{mV}} \le R_{\max}
\right]
\land
\left[
|\Delta T| \le T_{\max}
\right]
\land
\left[
N_{\text{overlap}} \ge N_{\min}
\right]
$$

The exact thresholds are stored in the corresponding JSON and CSV outputs.
<!-- END BEGINNER_MATH_EXPLANATION -->
