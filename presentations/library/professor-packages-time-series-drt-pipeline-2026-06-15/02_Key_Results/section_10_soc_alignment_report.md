# Time-Domain DRT Pilot, EIS 2D DRT surface

## Purpose

This section checks whether the pulse windows used for EIS matching actually line up with the requested SOC labels.
The previous sections used pre-rest voltage as the main clue. This section adds coulomb counting from the current time series.

## Capacity Clues From Raw CSV

- AhAccu_max_abs: 4.95561
- AhAccu_max: 4.61182
- AhAccu_min: -4.95561
- AhPrev_max_abs: 4.96156
- AhPrev_max: 4.96156
- AhPrev_min: 0.0

## SOC Alignment Results

- label 95 percent, candidate 6: pre-rest V=4.1647, SOC from 95 anchor=95, error=0 percentage points, endpoint-fit SOC=95
- label 70 percent, candidate 10: pre-rest V=4.0106, SOC from 95 anchor=76.1, error=6.07 percentage points, endpoint-fit SOC=76.6
- label 50 percent, candidate 14: pre-rest V=3.7029, SOC from 95 anchor=46.6, error=-3.45 percentage points, endpoint-fit SOC=48
- label 20 percent, candidate 20: pre-rest V=3.4611, SOC from 95 anchor=17, error=-2.97 percentage points, endpoint-fit SOC=19.3
- label 5 percent, candidate 24: pre-rest V=3.1803, SOC from 95 anchor=2.28, error=-2.72 percentage points, endpoint-fit SOC=5

## Summary

- Capacity used from raw columns: 4.96156 Ah
- Endpoint capacity implied by 95 to 5 percent cases: 5.111550165177415 Ah
- Max absolute error using 95 anchor and raw capacity: 6.069810835845232 percentage points
- Max absolute error using 95 to 5 endpoint fit: 6.625286593261137 percentage points
- Max absolute error using all-label linear fit: 4.833788266328355 percentage points

## Interpretation

The SOC labels are plausible but not exact under simple coulomb counting.
The 70 percent case is the biggest problem: it lands closer to the mid-70s by coulomb counting from the 95 percent anchor.

Blunt takeaway: the matched validation is contaminated by SOC uncertainty. Before claiming time-domain DRT disagrees with EIS, we need either exact protocol SOC annotations or a defensible SOC reconstruction rule.

## Outputs

- `section_10_soc_alignment_report.md`
- `section_10_matched_soc_alignment.csv`
- `section_10_all_candidate_soc_alignment.csv`
- `section_10_soc_alignment_summary.json`
- `section_10_soc_alignment.png`

<!-- BEGIN BEGINNER_MATH_EXPLANATION -->
## How This Section Works, Plain Math

This section checks whether the selected pulse windows really match the target EIS SOC labels.

### Coulomb counting

SOC can be estimated by integrating current over time:

```text
charge moved in Ah = integral(current over time) / 3600
```

Then SOC changes according to capacity:

```text
SOC change in percent = 100 * charge moved / capacity Ah
```

The script anchors one high-SOC candidate, then estimates the rest relative to that anchor.

### SOC error

The error is:

```text
SOC error = estimated SOC - EIS SOC label
```

Positive error means the selected pulse looks higher SOC than the EIS label. Negative error means it looks lower.

### What this section proves

It checks the matched-pair story. If SOC alignment is off, a weak EIS comparison may be caused partly by bad matching.

In the current result, the 70 percent case is approximate, not exact.

### Actual Equations Used

Coulomb counting estimates charge moved:

$$
Q(t) = \frac{1}{3600}\int_{t_0}^{t} I(u)\,du
$$

The estimated SOC is:

$$
\widehat{\mathrm{SOC}}(t)
=
\mathrm{SOC}_{\text{anchor}}
-100\frac{Q(t)-Q(t_{\text{anchor}})}{C_{\text{Ah}}}
$$

\(C_{\text{Ah}}\) is the assumed cell capacity in amp-hours.

The SOC matching error is:

$$
e_{\text{SOC}}
=
\widehat{\mathrm{SOC}}_{\text{candidate}}
- \mathrm{SOC}_{\text{EIS label}}
$$

Large \(|e_{\text{SOC}}|\) means the pulse window may not match the EIS condition well.
<!-- END BEGINNER_MATH_EXPLANATION -->
