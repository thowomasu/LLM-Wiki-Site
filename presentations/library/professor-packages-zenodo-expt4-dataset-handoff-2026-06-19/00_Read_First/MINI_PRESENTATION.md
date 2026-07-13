# Mini Presentation: Read First

## Slide 1: Results

- LG M50T 21700 Expt 4 drive-cycle aging was converted into a reviewable handoff focused on battery health features.
- The pipeline parses GITT, discharge, and hybrid-pulse files.
- GITT fitting worked on a batch of 40 files with no batch errors in the current run.
- The honest verdict: useful health-feature pipeline, not EIS-validated DRT physics.

---

## Slide 2: Achievements

- The package includes an executive summary, caveats, source notes, and a read-first guide.
- Source provenance is strong: the Expt4 checksum matched the Zenodo-published MD5.
- The package states what is defensible and what is not defensible.

---

## Slide 3: Open Issues

- Some features leak or proxy the target.
- GITT `r0_ohm` is useful for resistance labels, but it is not a DRT peak feature.
- Recovered DRT peaks are not physically validated without measured EIS DRT.
- Hybrid-pulse features are not proven independent predictors of SOH or capacity.

---

## Slide 4: Roadmap

- Use a locked comparison: R0 only, DRT bands without R0, and R0 plus DRT bands.
- Use leave-one-temperature-out as the headline test.
- Present this as feature engineering plus internal validation, not final physics.
- Keep leakage warnings visible in every summary.
