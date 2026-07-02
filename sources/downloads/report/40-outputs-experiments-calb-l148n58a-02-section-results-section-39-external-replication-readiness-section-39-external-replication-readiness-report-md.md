# CALB L148N58A, external-validation claim boundary External Replication Readiness

## Purpose

Check whether the local repo already has a defensible external dataset for rerunning the CALB bridge and drive-cycle audits.

## Result

- Assets reviewed: 13
- Blockers: 3
- Ready for external replication: False
- Preferred external dataset: `KIT_RADAR4KIT`
- Verdict: `external_replication_blocked_missing_corrected_eis`

## Blockers

- `kit_local_eis_archive_incomplete` (hard): Local DOI 10.35097/1947 cell_eisv2.zip is incomplete; use corrected EIS addendum before validation. Action: Locate or download the corrected EIS addendum before using KIT/RADAR4KIT as validation evidence.
- `zenodo_expt4_no_same_cell_eis` (hard): Expt4 README says the same-cell EIS finder found zero EIS evidence in the local public package. Action: Keep Expt4 as health-feature work, not EIS DRT validation.
- `dib_overlap_too_small` (hard): Only five exact paired rows exist, all from one cell/SOH/temp condition. Shape agreement is weak except SOC 95, and EIS/time gamma scales differ by large ratios. Action: Do not use the local DIB comparison as final external validation.

## Blunt Read

External replication is not done. The local KIT/RADAR4KIT manifest says the EIS archive is incomplete. Using it anyway would be fake validation. Get the corrected EIS addendum first.

## Outputs

- `section_39_candidate_assets.csv`
- `section_39_blockers.csv`
- `section_39_summary.json`
