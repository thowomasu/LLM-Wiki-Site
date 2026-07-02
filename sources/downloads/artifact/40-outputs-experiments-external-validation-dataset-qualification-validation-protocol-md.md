# External Validation Protocol

## Scope

This protocol freezes the next external validation path for the CALB L148N58A time-domain DRT work.

Hard boundary: frozen pulse-to-EIS rule is internal CALB pulse-bridge evidence only. drive-cycle ECM baseline check and SOC-stratified drive-cycle audit limit the drive-cycle claim. external-validation claim boundary says external validation is still blocked. No document in this vault should claim external validation unless a pre-declared external run passes under this protocol.

## Frozen Rule Policy

The frozen rule is the frozen pulse-to-EIS rule adaptive final rule as implemented before any external dataset result is inspected:

- Candidate selection: unchanged from frozen pulse-to-EIS rule.
- Time-domain lambda: unchanged.
- EIS lambda sequence: unchanged.
- EIS frequency window: unchanged.
- Time window and baseline mode: unchanged.
- Quality gates: unchanged.
- Fallback policy: unchanged, limited to the frozen pulse-to-EIS rule correlation-only fallback.

Not allowed:

- Retuning lambda, windows, candidate selection, thresholds, pass criteria, or fallback logic on CALCE, RADAR4KIT, NASA, or any other external dataset.
- Trying multiple external mappings and only reporting the winner.
- Treating CALCE storage ageing, NASA cycling, or incomplete RADAR4KIT EIS as proof of drive-cycle validation.

## Dataset Order

1. CALCE Storage 25 C first.
2. KIT/RADAR4KIT second only after the corrected EIS addendum is available.
3. NASA third as a robustness check.

Do not reorder this because a later dataset is easier. That would optimize for comfort, not for the failure mode already exposed by drive-cycle ECM baseline check and SOC alignment audit, 40, and 42.

## Allowed Inputs

CALCE Storage 25 C rows may enter the frozen input table only when the row has same-PLN, same-temperature, same-storage-period, and same-SOC evidence from the existing CALCE manifest and adapter outputs.

For a frozen pulse-to-EIS rule run, the row must also expose the information frozen pulse-to-EIS rule actually needs:

- Same-cell EIS spectrum.
- Same-cell time-domain pulse window compatible with the frozen pulse-to-EIS rule HPPC window finder.
- OCV or rest-voltage evidence usable by the frozen candidate selector.
- Enough current and voltage samples to compute the frozen time-domain fit.

Rows that have EIS plus capacity summaries but no HPPC-compatible pulse window are qualification rows, not runnable validation rows.

## Outcomes

Pass:

- The frozen frozen pulse-to-EIS rule runs unchanged on predeclared external rows.
- All required rows pass the frozen frozen pulse-to-EIS rule quality gates.
- The frozen rule beats the required baseline on the same rows.
- No dirty joins or post-result tuning are needed.

Partial pass:

- The frozen rule runs unchanged and beats the required baseline, but only on a defensible predeclared subset.
- Blocked or excluded rows are fully reported with row-level reasons.
- The result is reported as partial external support, not full validation.

Fail:

- The frozen rule runs unchanged and does not pass the quality gates, or it loses to the required baseline.
- Dirty joins are needed to make the result work.
- The correct verdict is no support. Do not soften this.

Blocked:

- The dataset lacks the required time-domain pulse evidence, EIS evidence, SOC alignment, or same-cell join evidence.
- The corrected RADAR4KIT EIS addendum is unavailable.
- Required raw files are missing or unreadable.
- The result is blocked or inconclusive, not external support.

## Required Baseline

Every runnable external validation must include a boring baseline on the same rows before any claim is made.

Minimum acceptable baseline:

- A simple resistance or capacity-only baseline if the target is pulse voltage.
- A simple ECM-style baseline if the target is drive-cycle voltage.
- A persistence or same-condition baseline if the target is ageing or capacity.

If the DRT rule loses to the baseline, say it loses.

## Current CALCE Decision Rule

The existing CALCE adapter output is enough to build frozen qualification inputs. It is not enough by itself to run frozen pulse-to-EIS rule unless the input path exposes HPPC-compatible pulse windows. Capacity workbook summaries are not a substitute for the frozen pulse-to-EIS rule pulse bridge.

Verdict labels for CALCE reports must be one of:

- external support
- partial support
- no support
- blocked/inconclusive
