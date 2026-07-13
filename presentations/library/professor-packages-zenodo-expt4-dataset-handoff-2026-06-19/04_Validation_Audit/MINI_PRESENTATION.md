# Mini Presentation: Validation Audit

## Slide 1: Results

- This is the most important folder for judging scientific strength.
- The audit found that some features leak or proxy the target, especially capacity, duration, and same-test resistance features.
- Safer claim: Expt4 supports internal battery health-feature benchmarking, and GITT-derived resistance features are informative for resistance-like labels.

---

## Slide 2: Achievements

- The package includes grouped validation metrics after stricter checks.
- It includes a leakage feature audit and a feature-target correlation scan.
- It separates raw score strength from scientific claim strength.
- It explicitly blocks overclaims about EIS validation and physically validated DRT peaks.

---

## Slide 3: Open Issues

- The modeling claim is weaker than raw scores suggest.
- Leave-one-cell-out can still be too friendly.
- Leave-one-temperature-out is harsher and should be treated as the headline test.
- DRT bands alone have not yet been proven to explain the result.

---

## Slide 4: Roadmap

- Run the locked comparison: R0 only, DRT bands without R0, R0 plus DRT bands.
- Remove target-proxy features before making any prediction claim.
- Prefer leave-one-temperature-out for headline claims.
- Bring in measured EIS DRT if the goal is real DRT physics validation.
