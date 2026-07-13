# Graph Explanation: first-slice protocol inventory Data Audit

Graph file: `section_1_data_audit.png`

## What This Figure Shows

This graph counts the processed LG M50T 21700 Expt 4 drive-cycle aging time-series files by family.

## How To Read It

The highest bars show where the reusable time-series data lives. GITT and hybrid-pulse files are the most relevant for DRT-style pulse/rest fitting. Plain 0.1C and 0.5C discharge files are useful ageing context, but they are weak DRT inputs because they do not provide repeated rest relaxations.

## What We Can Learn

The dataset has enough processed GITT files to build a real batch section. It is not just one hand-picked trace.

## Caveat

File count is not data quality. A file can exist and still be a poor DRT target if the current profile has no usable rest period.
