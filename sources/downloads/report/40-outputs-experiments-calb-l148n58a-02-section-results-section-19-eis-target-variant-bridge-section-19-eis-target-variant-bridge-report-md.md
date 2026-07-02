# CALB L148N58A, EIS target variant bridge EIS Target Variant Bridge

## Purpose

Compare HPPC time-domain DRT against several EIS-derived DRT target definitions.

## Result

- Comparison rows: 492
- Error count: 0
- Best variant by median correlation: mid_0p03_to_100hz
- Best median correlation: -0.03691909818439151
- Most frequent best variant by case: mid_0p03_to_100hz

## Variant Summary

| Variant | Rows | Quality-pass | Median corr | Positive rows | Corr > 0.5 rows |
| --- | ---: | ---: | ---: | ---: | ---: |
| drop_high_gt_100hz | 123 | 99 | -0.0554144244556703 | 23 | 8 |
| drop_low_lt_0p03hz | 123 | 99 | -0.038109207668236826 | 19 | 13 |
| full | 123 | 99 | -0.0485998081564577 | 20 | 11 |
| mid_0p03_to_100hz | 123 | 99 | -0.03691909818439151 | 16 | 13 |

## Blunt Read

If the HPPC time-domain DRT only agrees with a fragile EIS target variant, the validation target is not trustworthy.
If no variant gives a strong median correlation, stop tuning around the edges and revisit the model form.

## Outputs

- `section_19_variant_bridge_rows.csv`
- `section_19_by_variant.csv`
- `section_19_by_record_variant.csv`
- `section_19_by_temperature_variant.csv`
- `section_19_best_variant_by_case.csv`
- `section_19_errors.csv`
- `section_19_summary.json`

## Linked Graph

![EIS target variant bridge EIS target variant bridge](section_19_eis_target_variant_bridge.png)
