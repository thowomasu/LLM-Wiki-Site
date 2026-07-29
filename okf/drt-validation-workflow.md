---
type: Validation Workflow
title: DRT Validation Workflow
description: Practical validation workflow for DRT results using EIS consistency checks, reconstruction residuals, non-negativity, regularization stability, and uncertainty.
tags: [drt, eis, validation, kramers-kronig, battery]
timestamp: 2026-07-21T00:00:00+02:00
---

# DRT Validation Workflow

DRT does not have one universally accepted direct replacement for
Kramers-Kronig validation. The recommended workflow is layered.

## Workflow

1. Validate the raw EIS spectrum with Kramers-Kronig or another EIS consistency
   method.
2. Fit DRT only on spectra that pass basic EIS checks.
3. Reconstruct impedance from DRT.
4. Check real and imaginary reconstruction residuals.
5. Check whether residuals are random rather than structured.
6. Check non-negativity/passivity where expected.
7. Repeat across regularization settings.
8. Report uncertainty if the method supports it.

## Project Use

This concept should be linked from future pages that discuss DRT model
trustworthiness, EIS preprocessing, and validation claims.
