# Mini Presentation: Reproduction

## Slide 1: Results

- The package documents how to run a synthetic smoke test without raw DIB data.
- Full pipeline reproduction requires DIB capacity CSVs and the EIS workbook.
- Expected saved verdict is `research_scaffold_viable`, `not_validated`, and median EIS correlation about 0.141.

---

## Slide 2: Achievements

- Reproduction commands are separated into synthetic, full pipeline, model rule, and HTML rebuild paths.
- The expected result is stated, so a suspiciously strong rerun can be challenged.
- Environment variables are documented for non-default DIB locations.

---

## Slide 3: Open Issues

- This is not a standalone raw-data package.
- The full pipeline cannot be fairly rerun without the original DIB files.
- A stronger result after rerun may indicate validation leakage if lambda or baseline was chosen after seeing EIS.

---

## Slide 4: Roadmap

- Verify the Python environment and dependency versions before rerunning.
- Run synthetic-only first, then full data.
- Rebuild HTML after Markdown updates.
- Compare rerun outputs against the saved expected verdict before presenting.
