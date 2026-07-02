# CALB L148N58A, HPPC window finder HPPC Window Finder

## Purpose

Find pulse/rest windows in the CALB HPPC file for the first real time-domain DRT fit.

## Input

- Protocol: `HPPC_1C`
- File: `02_First_Slice/HPPC_1C.csv`
- Column mapping: `{"time_s": "time_s", "current_a": "current_a", "voltage_v": "voltage_v", "temperature_c": null}`

## Result

- Candidate windows: 27
- Accepted windows: 27
- Selected candidate id: 6
- Selected pulse: 6400.513s to 6760.414s
- Selected post-rest: 3599.004s
- Estimated visible tau range: 0.2002s to 1320s

## Critical Read

This selects a good engineering window. It does not prove the window is exactly the same OCV/SOC condition as an EIS record.

## Linked Graph

![HPPC window finder HPPC window plot](section_3_hppc_window_plot.png)
