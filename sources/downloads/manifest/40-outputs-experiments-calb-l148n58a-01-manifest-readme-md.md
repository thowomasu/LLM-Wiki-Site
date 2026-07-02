# CALB L148N58A Dataset Manifest

## Inputs

- Archive: `[local path redacted]`
- Archive size: 6.5 GB
- ZIP entries: 466
- Parsed test MAT files: 264
- Processed MAT files: 264

## Protocol Coverage

- Temperatures: 10 C, 25 C, 40 C
- Cells in processed data: 59294, 59485, 59627, 59690, 59861, 60031, 60129, 60195, 60403, 60644, 60710
- Protocols: C20_Charge, C20_Discharge, DV_UDDS, DV_US06, DV_WLTP, EIS_test, HPPC_1C, HPPC_C3

## Validation Fit

- Variable-current discharge: present as `DV_WLTP`, `DV_UDDS`, and `DV_US06`.
- RPT-like characterization: present as `C20_Charge`, `C20_Discharge`, `HPPC_1C`, and `HPPC_C3`.
- EIS: present as `EIS_test`, with measured `Frequency`, `Zreal`, and `Zimg` arrays.
- Caveat: the dataset does not use the literal folder name `RPT`; call it RPT-like characterization unless the paper/professor accepts HPPC plus low-rate capacity tests as RPT.

## Recommended First Integration Slice

- Cell: `59294`
- Temperature: `25 C`
- Time-domain input: `DV_WLTP` first, then `DV_UDDS` and `DV_US06`.
- EIS target: `EIS_test` for the same cell and temperature.
- Health/characterization context: `C20_Discharge`, `HPPC_1C`, and `HPPC_C3`.

## Sample Probe

- Sample MAT files probed: 7
- See `mat_sample_summary.json` for fields and numeric ranges.

## Output Files

- `zip_listing.csv`: all ZIP file entries.
- `manifest.csv`: parsed MAT data stage, temperature, protocol, cell, and size.
- `protocol_summary.csv`: counts by stage, temperature, and protocol.
- `mat_sample_summary.json`: in-memory schema probe for representative MAT files.
- `summary.json`: compact machine-readable summary.

## Blunt Next Step

Build a CALB adapter that reads MAT members directly from the ZIP. Do not extract the full archive unless a downstream tool truly needs filesystem paths.
