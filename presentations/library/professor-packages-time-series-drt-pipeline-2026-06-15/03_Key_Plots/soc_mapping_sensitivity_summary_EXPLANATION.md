# Graph Explanation: Soc Mapping Sensitivity Summary

Graph file: `soc_mapping_sensitivity_summary.png`

Folder: `Package_Key_Plots`
## What This Figure Shows

This figure compares different ways of assigning pulse windows to EIS SOC labels:

- voltage ordering
- coulomb counting
- endpoint anchoring
- linear SOC-vs-charge fitting

Each mode is an assumption, not ground truth.

## How To Read It

Look for whether the chosen candidate windows and EIS-comparison metrics change across SOC mapping modes. If the result changes a lot, SOC matching is a major uncertainty. If the result barely changes, SOC mapping is probably not the main explanation for the current mismatch.

## What We Can Learn

In the tested cases, changing SOC mapping did not explain the weak EIS match. Candidate IDs stayed stable and the weak median correlation stayed weak.

That pushes attention toward baseline handling, lambda selection, and whether pulse relaxation is comparable to EIS DRT at all.

## Why It Matters

SOC matching is an obvious weak spot. This plot checks whether that weak spot is actually driving the current result. In the small run, it was not the easy excuse.

## Caveat

This is a small run. A bigger dataset could reveal SOC sensitivity that this run does not show.

## What To Check Next

Do not stop at this plot. Move to model sensitivity. If SOC mapping is not moving the result, baseline and regularization deserve more pressure.
