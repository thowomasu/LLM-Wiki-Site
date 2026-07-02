# CALB L148N58A Docs

## Files

- `DRT_PAPER_MATH_AUDIT.md`: math check against Wildfeuer, Gieler, and Karger 2021.
- `PACKAGE_AUDIT.md`: audit of CALB scripts and generated outputs, including evidence/useful/disposable classification.
- `sources.json`: source paths and URLs used by the package.

## Claim Boundary

CALB is useful for internal pulse-bridge mechanics. It is not an aging-SOH validation dataset by itself.

frozen pulse-to-EIS rule is the current internal pulse-bridge evidence. drive-cycle ECM baseline check and SOC-stratified drive-cycle audit limit the drive-cycle claim. external-validation claim boundary says external validation is still blocked.

CALCE update: the frozen input path produced 24 same-join qualification rows and 0 frozen pulse-to-EIS rule runnable rows. The current CALCE inputs do not expose HPPC-compatible pulse windows, so the verdict is `blocked/inconclusive`. Do not describe this as external support.
