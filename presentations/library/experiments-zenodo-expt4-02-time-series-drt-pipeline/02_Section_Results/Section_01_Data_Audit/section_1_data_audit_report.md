# LG M50T 21700 Expt 4 drive-cycle aging Time-Series DRT Pipeline, first-slice protocol inventory

## Purpose

This section checks what data exists before fitting anything.
The point is to avoid pretending the Zenodo folder has the same validation target as the DIB pipeline.

## Findings

- Converted raw CSV manifest rows: 305
- Converted statuses: `{"converted_existing": 305}`
- Processed time-series CSV files: 280
- Processed families: `{"0.1C Voltage Curves": 80, "0.5C Voltage Curves": 40, "GITT Voltage Curves": 80, "Hybrid CC-Pulse Voltage Curves": 80}`
- Performance-summary label rows: 80

## Interpretation

The useful first-pass DRT target is processed GITT and hybrid-pulse data.
The converted raw BioLogic CSVs are useful for traceability and raw-protocol checks, but they are not automatically cleaner than the processed time-series files.
I did not find an obvious EIS-derived DRT target in the inspected Expt4 tree, so direct EIS validation is not claimed here.
