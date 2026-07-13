# Meeting Walkthrough: Time-Series To DRT Pipeline

Use this as a live walkthrough path. Do not treat it like slides. Open the files
in this order and talk through the evidence.

## Goal For The Meeting

Show that the pipeline is now a serious research scaffold, then ask for the
protocol information needed to validate it properly.

The main message:

The code works mechanically. The science is not validated yet. I need your help
checking whether the time-series pulse windows are truly comparable to the EIS
conditions.

## 0. Start With The Honest Status

Open:

```text
00_Read_First/VIABILITY_REPORT.md
```

Say:

I built a pipeline that can go from current-voltage-time data to a DRT-like
curve, then compare that curve against EIS-derived DRT. The engineering scaffold
is viable, but the method is not validated yet.

Point to:

- synthetic inverse check passes
- DIB batch runner passes
- SOC mapping sensitivity passes
- model sensitivity runs
- pre-declared model rule runs
- scientific verdict is still `not_validated`

Key number to say:

The current pre-declared rule-selected median EIS correlation is only about
0.141. So I am not claiming success yet.

What to ask:

Does this framing sound scientifically honest to you?

## 1. Show The Pipeline Map

Open:

```text
00_Read_First/ROUGH_PROTOTYPE_HANDOFF.md
```

Show this path:

```text
time series CSV
-> column normalization
-> pulse/rest window finder
-> candidate window fit
-> time-domain DRT-like tau/gamma curve
-> EIS-derived DRT comparison
-> sensitivity checks
-> pre-declared model rule
```

Say:

I did not just fit one hand-picked curve. I built the checks around the curve:
window detection, SOC alignment diagnostics, batch testing, SOC mapping
sensitivity, model sensitivity, and a rule that chooses lambda before EIS
scoring.

Achievement to highlight:

The pipeline is no longer just plotting. It has diagnostics and failure modes.

What to ask:

Which part of this workflow seems scientifically weakest to you?

## 2. Show The Math

Open:

```text
01_Method_And_Math/TIME_DOMAIN_DRT_MATH.html
```

Show these sections:

- Forward Model
- Discrete RC Kernel
- Optimization Problem
- Why Gamma Is Fragile

Say:

The model reconstructs voltage as baseline plus instantaneous resistance plus a
sum of RC relaxation responses. The gamma curve is constrained nonnegative and
smoothed, but I am treating it as fragile because many gamma shapes can explain
similar voltage.

Achievement to highlight:

I separated baseline drift from DRT resistance so slow OCV movement does not
automatically become fake slow gamma.

What to ask:

Is this baseline treatment acceptable as a first approximation, or should the
OCV/baseline model be more protocol-aware?

## 3. Show The Synthetic Sanity Check

Open plot:

```text
03_Key_Plots/synthetic_section_1_plots.png
```

Open report if needed:

```text
02_Key_Results/../00_Read_First/README.md
```

Say:

Before using real data, I tested the inverse on synthetic data with known RC
branches. It reconstructs voltage near the injected noise level, about 0.8 mV
RMSE.

Achievement to highlight:

The math and code pass a controlled inverse check.

Weakness to say out loud:

The slow branch is still fragile. Even synthetic data shows exact peak position
is not fully trustworthy.

What to ask:

For this project, should we care about exact DRT peak locations, or should we
focus on broad tau-band areas?

## 4. Show Real Cell28 Sweep

Open plot:

```text
03_Key_Plots/section_8_cell28_soc_sweep_summary.png
```

Open table:

```text
02_Key_Results/section_8_cell28_soc_sweep_summary.csv
```

Say:

I tested Cell28 across multiple SOC labels. Voltage reconstruction is good, but
EIS agreement is weak.

Achievement to highlight:

This is not one cherry-picked SOC. It runs across 95, 70, 50, 20, and 5 percent
SOC.

Weakness to say out loud:

Good voltage reconstruction does not mean the DRT shape is correct.

What to ask:

Are these Cell28 pulse windows actually the right windows to compare against
the EIS SOC labels?

## 5. Show SOC Alignment Problem

Open plot:

```text
03_Key_Plots/section_10_soc_alignment.png
```

Open table:

```text
02_Key_Results/section_10_matched_soc_alignment.csv
```

Say:

I added coulomb-counting checks. The nominal 70 percent case looks closer to
about 76 percent under the simple anchor method. That contaminates the matched
validation story.

Achievement to highlight:

I did not just trust pre-rest voltage. I checked SOC alignment using integrated
current and capacity clues.

What to ask:

Can you provide protocol annotations that map exact time-series steps to exact
SOC targets?

## 6. Show Generalized Batch Result

Open:

```text
02_Key_Results/DIB Batch/dib_batch_report.md
02_Key_Results/DIB Batch/dib_batch_results.csv
```

Say:

I generalized beyond Cell28. The first batch processed cells 15, 18, and 20,
with 15 SOC comparisons and no errors. Median voltage RMSE is about 1.586 mV,
but median EIS correlation is only about 0.105.

Achievement to highlight:

The code runs across multiple cells and exports quality flags.

Weakness to say out loud:

The method still does not agree with EIS strongly.

What to ask:

Does weak EIS agreement surprise you, given the difference between pulse
relaxation and frequency-domain EIS?

## 7. Show Sensitivity Checks

Open:

```text
02_Key_Results/SOC Mapping Sensitivity/soc_mapping_sensitivity_report.md
02_Key_Results/Model Sensitivity/model_sensitivity_report.md
```

Say:

SOC mapping was not the easy explanation in the first sensitivity run. Different
SOC mapping modes selected the same windows. But model sensitivity showed
baseline and lambda choices change the EIS comparison a lot.

Achievement to highlight:

I tested assumptions instead of hiding them.

Weakness to say out loud:

Baseline and regularization are currently the biggest modeling risk.

What to ask:

What baseline or OCV correction would you consider scientifically defensible for
these pulse windows?

## 8. Show The Pre-Declared Model Rule

Open:

```text
02_Key_Results/Model Rule/model_rule_report.md
```

Say:

To avoid cherry-picking, I added a rule that selects lambda before looking at EIS
metrics. It chooses from voltage RMSE, gamma roughness, and broad-band stability.
Only after selection does it report EIS agreement.

Achievement to highlight:

This blocks validation leakage.

Weakness to say out loud:

Even with the honest rule, EIS agreement is still weak. That is important.

What to ask:

Should the model-selection rule use repeated-pulse stability, EIS agreement, or
some other criterion?

## 9. End With The Concrete Ask

Open:

```text
00_Read_First/QUESTIONS_FOR_PROFESSOR.md
```

Say:

The next step is not training a model. The next step is validating the
experimental alignment.

Ask for:

- exact protocol annotations tying time-series pulse windows to SOC targets
- current sign convention
- measured capacity rule
- whether low-current pulses are comparable to EIS
- reference EIS preprocessing and DRT method
- one trusted matched validation example

## If He Only Has 5 Minutes

Show only:

1. `00_Read_First/VIABILITY_REPORT.md`
2. `01_Method_And_Math/TIME_DOMAIN_DRT_MATH.html`
3. `02_Key_Results/Model Rule/model_rule_report.md`
4. `00_Read_First/QUESTIONS_FOR_PROFESSOR.md`

Say:

I built the scaffold. It runs. It is honest about not being validated. I need
your protocol knowledge to decide whether the mismatch is a modeling problem or
an experimental-comparability problem.

## What Not To Say

Do not say:

- I solved time-series DRT.
- This replaces EIS.
- These are training labels.
- The model works because voltage RMSE is low.

Say instead:

- I built a reproducible research scaffold.
- The first validation comparison is weak.
- The next step is protocol-confirmed matching and baseline modeling.
- I want your feedback on the experimental assumptions.
