# CALB L148N58A, HPPC candidate fit HPPC Candidate Fit

## Purpose

Fit the existing time-domain DRT solver to one CALB HPPC pulse/rest window.

## Result

- Candidate id: 6
- Fit rows: 6000
- Pre-rest voltage estimate: 4.07571 V
- R0 estimate: 0.0011236706 ohm
- Voltage RMSE: 1.60601 mV
- Tau range: 0.2002s to 559.626s

## Critical Read

Voltage fit quality is necessary, not sufficient. A low RMSE means the local voltage window can be reconstructed. It does not prove the recovered gamma matches EIS.

## Outputs

- `section_4_hppc_selected_window.csv`
- `section_4_hppc_window_drt.csv`
- `section_4_summary.json`

## Linked Graph

![HPPC candidate fit HPPC candidate fit](section_4_hppc_candidate_fit_plot.png)
