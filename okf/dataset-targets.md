---
type: research_target
title: TS, EIS, and DRT dataset matching frame
updated: 2026-07-23
status: active
owner: Faisal
related_pages:
  - ../dataset-targets/
  - ../weekly/2026-07-23/
  - ../implementation/
---

# TS, EIS, and DRT dataset matching frame

The main dataset target is not generic battery data. The target is a matched research frame:

- TS: time-series cycling data such as current, voltage, temperature, capacity, cycle number, and state of charge.
- EIS: impedance spectra with frequency, real impedance, imaginary impedance, and test conditions.
- DRT: EIS data quality and metadata good enough to support distribution-of-relaxation-time analysis.

## Selection rule

A dataset is high value when the same cell or experiment can connect time-series cycling records with EIS measurements by cell ID, cycle number, state of charge, temperature, aging condition, or test date.

## Candidate source classes

- BatteryArchive for public battery cycling and comparison datasets.
- NASA PCoE battery datasets for aging, charge/discharge, and impedance measurements.
- Zenodo for group-specific lithium-ion EIS and aging datasets.
- Mendeley Data for paper-linked raw EIS and cycling datasets.
- ScienceDirect and Nature Scientific Data for curated paper-linked datasets.

## Next work

Create a dataset screening table with source link, cell chemistry, cell format, time-series availability, EIS availability, DRT readiness, labels, download status, and demo-pipeline suitability.
