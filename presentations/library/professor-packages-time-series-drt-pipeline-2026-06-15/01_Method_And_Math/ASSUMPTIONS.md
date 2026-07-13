# Time-Domain DRT Prototype Assumptions

## Read This First

This project tries to estimate DRT-like information from pulse/rest time-series battery data.

That is not the same thing as doing EIS.

EIS directly measures impedance under a controlled small-signal frequency sweep. This prototype uses ordinary time-series data: time, current, voltage, temperature, and some nearby EIS labels. The pipeline then asks a risky question:

Can a carefully chosen pulse/rest window produce a relaxation spectrum that is meaningfully comparable to an EIS-derived DRT curve?

The honest answer right now is:

- The engineering scaffold works.
- The method is not scientifically validated.
- The largest current weakness is not code execution. It is whether the assumptions are true enough.

If you only take one thing from this file, take this:

> A clean voltage fit does not prove the recovered DRT is correct.

The solver can reconstruct voltage while assigning the wrong resistance to the wrong time constants. That is the central danger.

## What The Pipeline Is Assuming

The core assumption is:

Given one DIB capacity-check time-series file and nearby EIS metadata, selected low-current pulse/rest windows can be compared against EIS-derived DRT at the same cell, SOH label, temperature, and approximate SOC.

That sentence hides a lot. It assumes:

- the capacity CSV and EIS row describe the same battery state closely enough
- the selected pulse is near the EIS SOC label
- the pulse excites relaxation processes that overlap with EIS processes
- baseline voltage drift is not being mistaken for DRT resistance
- the regularization setting is not chosen after seeing the EIS answer
- the time-domain and EIS gamma curves are comparable over their shared tau range

Each one can fail.

## The Pipeline In Plain English

The current flow is:

1. Find a capacity-check CSV with matching EIS metadata.
2. Load time, current, voltage, and temperature.
3. Detect pulse/rest windows.
4. Prefer low-current discharge pulses, because they are less aggressive than high-current capacity segments.
5. Assign selected pulse windows to EIS SOC labels: 95, 70, 50, 20, and 5 percent.
6. Fit a DRT-like time-domain model to each selected window.
7. Compare the fitted time-domain gamma curve against the matched EIS-derived gamma curve over the tau range they share.
8. Stress-test the result under different SOC mapping modes, baseline modes, and lambda values.

That last step matters. A result that only works under one convenient assumption is weak.

## Assumption Map

| ID | Assumption | What It Means | Why We Use It | Main Failure Mode |
|---|---|---|---|---|
| A1 | Matching by cell, SOH label, and temperature is enough for a first comparison. | A capacity file and an EIS row are treated as comparable if they share those metadata fields. | Those fields exist in the DIB filenames and EIS workbook. | The battery may be at a different protocol step, history state, or true SOC even when the metadata matches. |
| A2 | EIS SOC labels are the comparison targets. | The target SOC labels are 95, 70, 50, 20, and 5 percent because those labels exist in the EIS data. | The EIS workbook and filenames expose these SOC labels. | The capacity CSV does not directly mark which pulse is exactly 70 percent SOC, 50 percent SOC, and so on. |
| A3 | Low-current discharge pulses are the best first windows. | The selector prefers discharge pulses with moderate current, short duration, stable temperature, and rest context. | These are closer to small-signal behavior than high-current charge/discharge segments. | A pulse is still not EIS. It may excite different dynamics, nonlinear behavior, or SOC drift. |
| A4 | `Prog Time` is the correct time axis for DIB capacity CSVs. | Use the continuous program clock instead of `Step Time`, which resets every protocol step. | The DRT window needs continuous timing before, during, and after the pulse. | If a file has malformed `Prog Time`, the fit window and tau grid become wrong. Checked files have not shown that issue yet. |
| A5 | SOC can be approximated from current integration. | Current is integrated over time to estimate how far the file has moved through charge. | The CSV contains current and capacity-like Ah columns. | SOC depends on sign convention, capacity scale, anchor point, OCV hysteresis, and protocol details. |
| A6 | Time-domain gamma and EIS gamma can be compared over shared tau. | The code compares only tau values visible to both curves. | Both methods output a tau-indexed gamma-like curve. | The two inverse problems use different kernels and regularization, so equal tau does not guarantee equal physics or equal scale. |
| A7 | Good voltage reconstruction is necessary but not sufficient. | High voltage RMSE means the fit is bad. Low voltage RMSE only means the model can reconstruct voltage. | Voltage is the measured signal. If the model cannot fit it, gamma is useless. | Many gamma curves can fit nearly the same voltage. Low RMSE can hide a wrong DRT shape. |
| A8 | Baseline/OCV drift can be separated from DRT resistance. | The fit includes free offset, time drift, and charge drift terms so gamma does not absorb slow voltage drift. | Pulse windows include slow voltage movement that is not all relaxation resistance. | Baseline terms can steal real slow relaxation, or weak baseline terms can force OCV drift into gamma. |
| A9 | Lambda must be selected without looking at EIS agreement. | Lambda controls gamma smoothness. It should be chosen from time-domain fit quality and stability first. | Picking lambda after seeing EIS is validation leakage. | The chosen lambda may still be wrong, but at least the validation is less contaminated. |
| A10 | A pre-declared model rule is more honest than picking the prettiest plot. | The model rule fixes baseline mode, tests a lambda grid, and selects lambda before EIS metrics are used. | This blocks the easiest way to fool ourselves. | The rule can still select a poor model if its internal criteria are weak. |
| A11 | Quality flags are triage, not proof. | Rows pass checks for current range, temperature drift, voltage RMSE, tau overlap, correlation, and SOC error. | The flags keep suspicious rows visible. | A row can pass all flags and still be scientifically wrong. |
| A12 | Synthetic recovery does not validate real data. | The synthetic case checks whether the inverse code can recover a controlled RC-like signal. | It catches broken math before touching real DIB files. | Real batteries have OCV drift, hysteresis, temperature effects, protocol artifacts, and unknown state history. |

## The Most Important Blind Spot

The old version of this document made all assumptions look equally risky. They are not.

Right now, the evidence says:

- SOC mapping was not the main driver in the first small sensitivity run.
- Baseline handling and lambda choice were much more dangerous.
- The pre-declared rule made the validation more honest, but it did not make EIS agreement good.

That is a useful result. It narrows the problem.

The next pressure point is baseline/OCV modeling and whether pulse relaxation is comparable to EIS-derived DRT at all.

## SOC Mapping Assumptions

The capacity file does not directly say, "this pulse is the 70 percent SOC EIS match."

So the batch runner supports four SOC mapping modes. These are not four truths. They are four stress tests.

| Mode | Rule | What It Tests | Weak Spot |
|---|---|---|---|
| `voltage` | Sort candidate pulses by pre-rest voltage and assign SOC labels from high voltage to low voltage. | Does a simple voltage-order assumption change the result? | Voltage is not exact SOC, especially under hysteresis, rest-time differences, and aging. |
| `coulomb` | Treat the highest-voltage selected pulse as the high-SOC anchor, then use integrated current and the raw capacity scale to estimate later SOC. | Does current integration plus a capacity scale give stable matches? | Depends on capacity column quality, sign convention, and the anchor being correct. |
| `endpoint` | Treat the highest-voltage selected pulse as 95 percent and the lowest-voltage selected pulse as 5 percent, then interpolate SOC by integrated current. | Does the result survive without trusting one raw capacity column? | Forces endpoints to be true even if the selected endpoint pulses are not true 95 and 5 percent SOC. |
| `linear` | Use voltage-ranked candidates as provisional labels, fit a linear SOC-vs-Ah map, then reselect nearest pulses. | Does a label-informed linear correction change the conclusion? | It is closer to fitting the labels, so it can look cleaner without being more true. |

The current default is `coulomb` when raw DIB data is available.

## What The SOC Sensitivity Run Actually Said

The first SOC sensitivity run used:

- 3 DIB capacity cases
- 4 SOC mapping modes: `voltage`, `coulomb`, `endpoint`, and `linear`
- 60 total comparisons
- 0 errors

Result:

| Check | Result |
|---|---:|
| Unique time-domain fits after caching | 15 |
| Targets with different candidate IDs across modes | 0 |
| Targets with correlation range above 0.1 across modes | 0 |
| Median EIS correlation under every mode | about 0.105 |
| Median normalized RMSE under every mode | about 0.866 |

Interpretation:

In this small run, changing SOC mapping did not change which low-current pulse windows were selected. The weak EIS agreement stayed weak.

Do not overclaim this. It does not prove SOC is solved. It only says SOC mapping is not the easiest explanation for the current weak match.

## Baseline Assumptions

The measured terminal voltage contains more than relaxation resistance.

It also contains:

- a voltage offset
- slow OCV movement as charge moves
- possible time drift
- temperature and protocol artifacts

If the model does not include baseline terms, gamma may fake slow voltage drift by creating a slow tau peak. That looks scientific, but it can be garbage.

The fitter supports these baseline modes:

| Mode | Free Terms | Why It Exists | Main Risk |
|---|---|---|---|
| `offset` | constant voltage offset | Minimal baseline. | Can force slow OCV drift into gamma. |
| `time` | constant offset plus linear time drift | Allows slow drift unrelated to current throughput. | Can absorb real slow relaxation. |
| `charge` | constant offset plus integrated-current drift | Represents local OCV change from charge moved. | Depends on current sign and assumes local OCV is linear in charge. |
| `time_charge` | constant offset, integrated-current drift, and time drift | Most flexible first-pass baseline. | Can hide model error by absorbing too much voltage structure. |

The model sensitivity run showed this layer is dangerous.

## What The Model Sensitivity Run Actually Said

The first model sensitivity run used:

- 2 DIB capacity cases
- 3 baseline modes: `offset`, `charge`, and `time_charge`
- 4 lambda values: `0.001`, `0.1`, `1.0`, and `3.0`
- 120 comparisons
- 0 errors
- 112 quality-pass comparisons

Best summary values:

| Criterion | Best Setting | Value |
|---|---|---:|
| Best median normalized RMSE | `time_charge`, lambda `3.0` | about 0.301 |
| Best median correlation | `offset`, lambda `3.0` | about 0.374 |
| Targets with correlation range above 0.1 across settings | 10 of 10 | all tested targets |

Interpretation:

The result is model-sensitive. Baseline and lambda choices can move EIS agreement a lot while voltage RMSE barely changes.

That is the problem. If you let yourself choose the best baseline or lambda after seeing EIS, you are tuning on the validation target.

## Lambda Assumption

Lambda controls gamma smoothness.

Low lambda lets gamma become more flexible and jagged. High lambda forces gamma to be smoother. Neither is automatically correct.

The danger:

- low lambda can overfit voltage noise
- high lambda can blur separate processes together
- EIS agreement can improve simply because smoothing makes curves look more similar
- choosing lambda after looking at EIS makes the validation dishonest

So the model rule chooses lambda before EIS scoring.

## Pre-Declared Model Rule

The current rule is:

- use `coulomb` SOC selection when raw DIB data is available
- use low-current discharge windows from the candidate selector
- fix `baseline_mode = time_charge`
- test a lambda grid
- keep lambda values within best voltage RMSE plus max 5 percent or 0.25 mV
- prefer lower gamma roughness
- prefer more stable fast/mid/slow band areas across neighboring lambdas
- add EIS metrics only after lambda is selected

This rule is not magic. It does one specific job:

It prevents lambda selection from using EIS as the answer key.

## What The Pre-Declared Rule Actually Said

The first saved model-rule result used existing model-sensitivity output:

- selected comparisons: 10
- lambda candidates scored: 40
- errors: 0
- quality-pass comparisons: 10 of 10
- median voltage RMSE: about 1.711 mV
- median EIS correlation after rule selection: about 0.141
- median normalized RMSE after rule selection: about 0.978
- selected lambda values: all `0.001`

Interpretation:

The rule improved honesty, not scientific agreement.

That is not a failure of the rule. That is the rule doing its job. It stopped the pipeline from quietly selecting settings that make EIS agreement look better after the fact.

Bluntly: if the honest rule gives weak EIS agreement, believe the weakness.

## What Counts As Robust

A result is more believable if it survives changes in assumptions.

Useful robustness signs:

- the selected pulse windows stay similar across SOC mapping modes
- voltage RMSE stays low without extreme baseline flexibility
- broad fast/mid/slow gamma areas stay stable across neighboring lambda values
- EIS shape correlation stays reasonable after the model rule, not only after hand-tuning
- tau overlap is large enough to compare the curves
- results repeat across cells, SOH labels, temperatures, and cycles

Weak signs:

- only one lambda value gives a pretty EIS comparison
- voltage fit is good but EIS shape correlation is weak
- a gamma peak sits at the tau boundary
- baseline mode changes the conclusion
- a single selected pulse carries the whole claim
- quality flags pass, but sensitivity tests fail

## What We Must Not Claim Yet

Do not claim:

- time-domain DRT is a validated substitute for EIS-derived DRT
- selected time-domain windows are true SOC matches
- low voltage RMSE proves the recovered gamma curve is physically correct
- the EIS labels are ground truth for pulse windows
- lambda or baseline can be chosen by whichever EIS plot looks best
- these labels are ready for training a final health model

If you make those claims right now, you are overreaching.

## Current Honest Claim

The prototype can:

- find pulse/rest windows in time-series battery data
- fit a DRT-like relaxation spectrum from those windows
- compare the result against EIS-derived DRT over shared tau
- test sensitivity to SOC mapping, baseline handling, and lambda
- enforce a pre-declared model-selection rule before EIS scoring

That is enough for a research scaffold.

It is not enough for a final scientific claim.

## What Would Make The Assumptions Stronger

The next work should focus on evidence, not prettier plots.

Needed evidence:

- protocol annotations that tie pulse windows to SOC targets
- confirmed current sign conventions and capacity scales
- repeated pulse windows at the same nominal condition
- better OCV/baseline handling, ideally protocol-aware
- validation on synthetic data with known OCV drift, temperature drift, and SOC drift
- model-rule results across more cells and SOH labels
- agreement that survives new data, not just the current run

The brutal version:

The code is now useful. The science is still on probation.
