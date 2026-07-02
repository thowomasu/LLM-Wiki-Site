# CALB L148N58A, file and protocol screen File/Protocol Screen

## Purpose

Screen the first-slice files before fitting. The point is to avoid feeding drive-cycle mess straight into a pulse-relaxation inverse problem.

## Result

- Recommended first fit protocol: `HPPC_1C`.
- Drive cycles are kept for later validation after the bridge mechanics are working.
- `C20_Discharge` is useful for capacity/OCV context, but it is weak pulse excitation.

## Critical Read

If a protocol has many accepted windows, that only means the generic detector found current events. It does not mean the windows are aligned to EIS SOC/OCV.

## Outputs

- `section_2_protocol_screen.csv`
- `section_2_summary.json`

## Linked Graph

![file and protocol screen protocol screen](section_2_file_protocol_screen.png)
