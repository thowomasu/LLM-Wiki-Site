# Graph Explanation: lambda sensitivity check Raw Window Plot

Graph file: `section_7_raw_window_plot.png`

## What This Figure Shows

This graph overlays detected pulse/rest candidates on current and voltage.

## How To Read It

Green accepted regions are current events with enough step size, pulse duration, and following rest. The voltage panel shows whether those current events produce visible relaxation.

## What We Can Learn

For processed GITT, repeated accepted windows mean the data is structurally suitable for time-domain DRT fitting. For converted raw files, accepted windows prove the loader can parse the file, but raw protocol segmentation still needs caution.

## Caveat

The detector is generic. It does not understand every BioLogic protocol step. Do not treat accepted raw windows as final scientific selections without protocol review.
