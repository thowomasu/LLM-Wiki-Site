# CALB L148N58A, EIS robustness audit EIS Robustness Audit

## Purpose

Check whether the EIS-derived DRT target is stable when reasonable frequency bands are removed.

## Result

- EIS variant fits: 492
- Variant-vs-full comparisons: 369
- Error count: 0
- Weakest variant: mid_0p03_to_100hz
- Weakest median correlation vs full: -0.014424236857425133

## Variant Summary

| Variant | Rows | Median corr vs full | Median scaled RMSE | Low corr rows < 0.5 |
| --- | ---: | ---: | ---: | ---: |
| drop_high_gt_100hz | 123 | 0.9809334571427006 | 0.19317572581287729 | 0 |
| drop_low_lt_0p03hz | 123 | 0.10373112874464605 | 0.9893386246517515 | 121 |
| mid_0p03_to_100hz | 123 | -0.014424236857425133 | 0.9996384645400845 | 123 |

## Blunt Read

If trimming ordinary EIS frequency bands changes gamma shape badly, the EIS target is not stable enough to serve as a strict truth label.
If it is stable, stop blaming EIS preprocessing and move to model-form mismatch.

## Outputs

- `section_18_eis_variant_fits.csv`
- `section_18_eis_variant_vs_full.csv`
- `section_18_by_variant.csv`
- `section_18_by_record_variant.csv`
- `section_18_errors.csv`
- `section_18_summary.json`

## Linked Graph

![EIS robustness audit EIS robustness audit](section_18_eis_robustness_audit.png)
