# Model Sensitivity

## Purpose

This section tests whether the weak EIS agreement is sensitive to baseline/OCV handling or regularization strength.

## Run Settings

- Baseline modes: offset, charge, time_charge
- Lambda values: 0.001, 0.1, 1.0, 3.0
- SOC selection: coulomb
- Max cases: 2
- Selected cases: 2

## Best Settings

- Best median normalized RMSE: baseline=time_charge, lambda=3.0, value=0.3011107720820195, median corr=0.14760612639932447
- Best median correlation: baseline=offset, lambda=3.0, value=0.3738388077129163, median normalized RMSE=0.33418999009003286

## Setting Summary

- charge, lambda=0.001: median RMSE=1.7113682815841929 mV, median corr=0.10902106758239541, median norm RMSE=0.8896191162514121, median gamma sum=0.04398831696234896
- charge, lambda=0.1: median RMSE=1.7113834873969909 mV, median corr=0.22974845371424693, median norm RMSE=0.44111572047914127, median gamma sum=0.043122020476219776
- charge, lambda=1.0: median RMSE=1.7114833431352077 mV, median corr=0.17372090679326743, median norm RMSE=0.3053339546990582, median gamma sum=0.04181652872559176
- charge, lambda=3.0: median RMSE=1.7115899287271688 mV, median corr=0.03087938421115595, median norm RMSE=0.30499663318792514, median gamma sum=0.04105738360499571
- offset, lambda=0.001: median RMSE=1.8396118788544007 mV, median corr=0.13054111148537278, median norm RMSE=1.0923426244253451, median gamma sum=0.05903835220789183
- offset, lambda=0.1: median RMSE=1.8405363429824861 mV, median corr=0.2304372052848756, median norm RMSE=0.6828498958427484, median gamma sum=0.05876880201908978
- offset, lambda=1.0: median RMSE=1.8461854797710933 mV, median corr=0.3450617377692924, median norm RMSE=0.42963791968252635, median gamma sum=0.05608056146075951
- offset, lambda=3.0: median RMSE=1.850768963763851 mV, median corr=0.3738388077129163, median norm RMSE=0.33418999009003286, median gamma sum=0.05400920662461784
- time_charge, lambda=0.001: median RMSE=1.7106937066290135 mV, median corr=0.14067984833877545, median norm RMSE=0.978374331390654, median gamma sum=0.055231280679961664
- time_charge, lambda=0.1: median RMSE=1.7108166299677716 mV, median corr=0.2572686504096158, median norm RMSE=0.5208833137625286, median gamma sum=0.05228274278776213
- time_charge, lambda=1.0: median RMSE=1.7111486859282312 mV, median corr=0.30332558661224873, median norm RMSE=0.3417273586545014, median gamma sum=0.0469592902291226
- time_charge, lambda=3.0: median RMSE=1.7114262270499985 mV, median corr=0.14760612639932447, median norm RMSE=0.3011107720820195, median gamma sum=0.04328637375438954

## Stability Summary

- Targets with correlation range above 0.1 across model settings: 10
- Errors: 0

## Interpretation

A viable research pipeline should not rely on one lucky baseline or lambda setting.
If stronger smoothing improves EIS agreement without hurting voltage reconstruction too much, the next step is to define a pre-declared lambda rule.
If baseline mode changes the result a lot, the next step is OCV/baseline modeling, not model training.

Blunt warning: picking the best setting after looking at EIS is tuning on the validation target. Use this to learn, not to claim final performance.

## Outputs

- `model_sensitivity_results.csv`
- `model_sensitivity_setting_summary.csv`
- `model_sensitivity_by_target.csv`
- `model_sensitivity_case_summaries.json`
- `model_sensitivity_errors.csv`
- `model_sensitivity_report.md`

<!-- BEGIN BEGINNER_MATH_EXPLANATION -->
## How This Section Works, Plain Math

This section changes model assumptions to see whether the result is stable.

### Baseline modes

The baseline is the slow voltage level underneath the relaxation response.

Different baseline modes allow different drift terms:

```text
offset       constant baseline
charge       baseline changes with charge moved
time_charge  baseline changes with time and charge
```

### Lambda values

Lambda controls gamma smoothness. If EIS agreement changes a lot with lambda, the result is model-sensitive.

### What this section proves

It identifies weak assumptions. The current result is sensitive to baseline and lambda, so the method is not robust yet.

### Actual Equations Used

The baseline mode changes \(\mathbf{b}\) in the voltage model:

$$
\hat{\mathbf{V}} = \mathbf{b} + R_0\mathbf{I} + K\gamma
$$

Offset baseline:

$$
b_n = b_0
$$

Charge baseline:

$$
b_n = b_0 + b_q q_n
$$

Time-charge baseline:

$$
b_n = b_0 + b_t t_n + b_q q_n
$$

The smoothness setting stays:

$$
\min_{\gamma \ge 0}
\left\|\mathbf{V}-\hat{\mathbf{V}}\right\|_2^2
+ \lambda\left\|L\gamma\right\|_2^2
$$

If metrics change strongly across baseline modes or \(\lambda\), the method is model-sensitive.
<!-- END BEGINNER_MATH_EXPLANATION -->
