# NASA Battery External Validation Manifest

## Scope

This is dataset qualification only. It does not validate the frozen CALB rule.

The script inspected the wrapper ZIP and inner BatteryAgingARC ZIPs in memory. It did not bulk-extract the archive.

## Input

- Archive: `[local path redacted]`
- Archive size: 200.0 MB

## Coverage

- Inner ZIPs: 6
- MAT files parsed: 38
- Unique cells: 34
- Unique cells with charge: 34
- Unique cells with discharge: 34
- Unique cells with impedance: 34
- Ambient temperatures: 4 C, 22 C, 24 C, 43 C, 44 C
- Discharge capacity range: 0.0 to 2.6401491157387014 Ah

## Impedance Fields

- Fields seen: `Battery_current; Battery_impedance; Current_ratio; Rct; Re; Rectified_Impedance; Sense_current`
- The common fields include `Battery_impedance`, `Rectified_Impedance`, `Re`, and `Rct`.
- The README says the EIS sweep is 0.1 Hz to 5 kHz, but the MAT records do not expose a plain `Frequency` vector in the sampled schema.

## Candidate Pairings

- Same-cell impedance plus charge/discharge pairing rows: 68
- These are candidates only. NASA has repeated same-cell charge/discharge/impedance operations, but not drive-cycle operation coverage like the CALB drive-cycle question needs.

## Blunt Read

NASA is useful for checking whether a time-domain bridge can survive on a classic same-cell impedance/cycling dataset. It is third priority for the frozen CALB rule: CALCE goes first, RADAR4KIT goes second only when the corrected EIS addendum exists, and NASA stays a later robustness check. Its time-domain side is mostly charge/discharge cycling, not drive-cycle or HPPC-like pulse validation.

## Outputs

- `zip_listing.csv`
- `cell_manifest.csv`
- `operation_counts.csv`
- `capacity_summary.csv`
- `impedance_schema.csv`
- `candidate_pairings.csv`
- `summary.json`
