# CALB L148N58A, time-series 2D DRT surface Time-Series 2D DRT Surface

## Purpose

Build a 2D time-series DRT surface from long CALB HPPC discharge pulses: gamma over tau and pre-rest voltage.

## Result

- Long discharge HPPC windows fitted: 9
- Fits kept in 2D surface after RMSE gate: 8
- Fits excluded from 2D surface: 1
- Candidate IDs nearest the three EIS OCV records: 9, 15, 21
- Output table: `section_9_time_series_2d_drt_long.csv`.
- Output matrix: `section_9_time_series_2d_matrix.csv`.

## Critical Read

This is a real time-series 2D DRT pipeline, but voltage is only a SOC proxy.
No one gets to call this calibrated SOC until protocol-aware SOC reconstruction is done.
The lowest-voltage tail fit is excluded if its voltage RMSE is too high. Keeping a bad fit just to make a prettier surface would be dishonest.

## Linked Graph

![time-series 2D DRT surface time series 2D DRT surface](section_9_time_series_2d_drt_surface.png)
