# CALB L148N58A, EIS DRT baseline EIS DRT Baseline

## Purpose

Compute an EIS-derived DRT baseline from `EIS_test.csv` for the same cell and temperature.

## Method

This section fits real and imaginary EIS components together with nonnegative gamma and R-infinity.
It is a local NumPy prototype, not pyDRTtools and not a publication-grade EIS inversion.

## Result

- Record 0, OCV 3.95911 V: 34 points, gamma area 0.00132732, Rinf 0.000790291 ohm.
- Record 1, OCV 3.72227 V: 34 points, gamma area 0.00115683, Rinf 0.000804772 ohm.
- Record 2, OCV 3.63081 V: 34 points, gamma area 0.00108013, Rinf 0.000814531 ohm.

## Critical Read

This is now stronger than an imaginary-only sketch because real and imaginary EIS residuals both constrain the same gamma. It is still a baseline, not final math validation.

## Linked Graph

![EIS DRT baseline EIS DRT baseline](section_5_eis_drt_baseline.png)
