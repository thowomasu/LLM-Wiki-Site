# Mini Presentation: Read First

## Slide 1: Results

- The pipeline can load current-voltage-time data, find pulse/rest windows, fit a DRT-like curve, and compare it with EIS-derived DRT.
- Current saved verdict: engineering scaffold is viable.
- Current saved scientific verdict: not validated.
- Rule-selected median EIS correlation is about 0.141, which is weak.

---

## Slide 2: Achievements

- The package now has a plain-English overview, meeting walkthrough, viability report, dataset recommendation, and professor questions.
- The story is honest: useful research scaffold, not a validated EIS replacement.
- The strongest contribution is workflow discipline: window detection, fitting, comparison, sensitivity checks, and pre-declared model selection are separated.

---

## Slide 3: Open Issues

- SOC-window matching still needs professor or protocol confirmation.
- DIB is not a clean drive-cycle dataset.
- Current sign convention and capacity assumptions still need confirmation.
- Good voltage RMSE does not prove the recovered gamma shape is correct.

---

## Slide 4: Roadmap

- Ask the professor to confirm the project target: SOC, SOH, EIS replacement, or DRT label generation.
- Get one trusted matched cell/SOC/temp/SOH validation case.
- Keep DIB for pulse/rest plus EIS work.
- If the project needs drive-cycle loading, move that track to a real drive-cycle dataset.
