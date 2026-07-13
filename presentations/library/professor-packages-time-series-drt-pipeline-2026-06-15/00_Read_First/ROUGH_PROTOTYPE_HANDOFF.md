# Rough Prototype Handoff

## Status

- Runner mode: synthetic only
- Steps run: 4
- Failed steps: 0
- Total runner time: 3.01 seconds

## What Exists Now

- A synthetic time-domain DRT sanity check.
- A CSV loader that handles DIB-style metadata headers.
- A pulse/rest window finder.
- A candidate-window time-domain DRT fitter.
- A pyDRTtools-based EIS comparison path.
- A multi-SOC Cell28 validation sweep.
- Scale, regularization, and SOC-alignment diagnostics.
- A generalized DIB batch runner tested on multiple cells.
- SOC-mapping, model-assumption, and viability reports when those outputs exist.
- A pre-declared model-rule step that selects lambda before EIS scoring.
- HTML mirrors of the main handoff docs when the export step has run.

## Reproduction Command

```powershell
python "scripts\experiments\run_time_domain_rough_prototype.py"
```

Use `--synthetic-only` if the local DIB folder is not available.

## Synthetic Check

- R0 truth: 0.002 ohm
- R0 recovered: 0.001814 ohm
- Voltage RMSE: 0.8007 mV

Interpretation: the inverse math works on a controlled synthetic case, but exact peak recovery is fragile.

## Real Cell28 Sweep

| SOC label | Candidate | Time RMSE mV | Corr | Time area | EIS area |
|---:|---:|---:|---:|---:|---:|
| 95 | 6 | 1.492 | -0.04173 | 0.001387 | 0.0122 |
| 70 | 10 | 1.437 | 0.1209 | 0.001913 | 0.01705 |
| 50 | 14 | 1.427 | 0.08484 | 0.00128 | 0.01233 |
| 20 | 20 | 1.493 | 0.1907 | 0.001052 | 0.04803 |
| 5 | 24 | 2.277 | 0.1092 | 0.001853 | 0.07002 |

Interpretation: voltage reconstruction is good, but EIS agreement is weak. This is not a validated substitute for EIS-derived DRT.

## Scale And Regularization

- Best scale factor spread across SOC: 8.731x
- Best 70 percent SOC normalized-RMSE lambda: 3.0
- Best 70 percent SOC correlation lambda: 0.3

Interpretation: stronger smoothing improves one case, but it is not a clean fix. A tuning rule is needed before any claim is credible.

## SOC Alignment

| EIS SOC label | Candidate | Coulomb-count SOC | Error percentage points |
|---:|---:|---:|---:|
| 95 | 6 | 95 | 0 |
| 70 | 10 | 76.07 | 6.07 |
| 50 | 14 | 46.55 | -3.446 |
| 20 | 20 | 17.03 | -2.968 |
| 5 | 24 | 2.279 | -2.721 |

- Max absolute SOC error from simple anchor method: 6.07 percentage points

Interpretation: the current matched validation is contaminated by SOC uncertainty, especially the nominal 70 percent case.

## Generalized DIB Batch

- SOC comparisons produced: 15
- Errors: 0
- Quality-pass comparisons: 15 of 15
- Median voltage RMSE: 1.586 mV
- Median EIS correlation: 0.1046
- Cells processed: 15, 18, 20
- SOH labels processed: 80, 85

Interpretation: the generalized DIB pipeline works mechanically across cells, but EIS agreement remains weak.

## SOC Mapping Sensitivity

- Modes tested: coulomb, endpoint, linear, voltage
- Total comparisons: 60
- Errors: 0
- Targets with different selected candidates across modes: 0
- Targets with correlation range above 0.1 across modes: 0
- Median EIS correlation across mode summaries: 0.1046

Interpretation: SOC mapping did not explain the weak EIS agreement in the first sensitivity run.

## Model Sensitivity

- Total comparisons: 120
- Errors: 0
- Quality-pass comparisons: 112 of 120
- Targets with correlation range above 0.1 across model settings: 10
- Best median normalized RMSE: time_charge, lambda 3.0, value 0.3011
- Best median correlation: offset, lambda 3.0, value 0.3738

Interpretation: baseline and lambda choices change the EIS shape comparison a lot. This is the current strongest warning sign.

## Pre-Declared Model Rule

- Selected comparisons: 10
- Lambda candidates scored: 40
- Errors: 0
- Quality-pass comparisons: 10 of 10
- Selected lambda values: 0.001
- Median EIS correlation after rule selection: 0.1407
- Median normalized RMSE after rule selection: 0.9784

Interpretation: this is the honest model-selection gate. It picks settings from time-domain fit quality and stability before EIS metrics are read.

## Viability Report

- Engineering scaffold: research_scaffold_viable
- Scientific method: not_validated
- Batch median EIS correlation: 0.1046
- Rule-selected median EIS correlation: 0.1407
- Model-sensitive targets: 10

Interpretation: the prototype is useful for research iteration. It is not safe as a training-label generator.

## Rough Prototype Verdict

The rough prototype is complete as a research scaffold. It can load time-series data, find pulse windows, estimate a time-domain DRT-like spectrum, compare against EIS-derived DRT, run diagnostics, batch-test multiple DIB cells, flag obvious low-quality windows, test assumption sensitivity, and apply a pre-declared model-selection rule.

It is not complete as a scientific method. The main blockers are baseline/OCV handling, EIS/time-domain comparability, pre-declared regularization, and stronger quality gates for selecting valid pulse windows.

## What To Ask The Professor For

- Exact protocol annotations tying time-series steps to SOC targets.
- Current sign convention and whether discharge current is positive or negative.
- Nominal and measured cell capacity for each test.
- Whether the low-current capacity-check pulses are intended to be comparable to EIS.
- The exact EIS preprocessing and DRT method used in the prior master's thesis.
- A matched cell/SOC/temp/SOH example that the professor considers ground truth.

## Next Engineering Step

Run the pre-declared model-selection rule on more protocol-confirmed cases. If rule-selected outputs still do not match EIS, stop pretending the problem is presentation. The model assumptions need work.

Blunt warning: do not train any model yet. Training now would teach the model your preprocessing uncertainty.
