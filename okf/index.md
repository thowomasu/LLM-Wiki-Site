---
okf_version: "0.1"
title: "Battery DRT Research OKF Bundle"
description: "Starter Open Knowledge Format bundle for the LLM Wiki Site, API/HPC demo, DRT validation work, and battery research pipeline handoff."
tags: [battery, drt, llm-wiki, okf, pipeline]
timestamp: 2026-07-21T00:00:00+02:00
---

# Battery DRT Research OKF Bundle

This folder is a starter Open Knowledge Format (OKF) bundle for the current
LLM Wiki / battery research pipeline.

OKF is useful here because the project already behaves like an LLM wiki:
research pages, dataset summaries, validation notes, code handoff pages, and
pipeline instructions are all stored as version-controlled files.

## Concepts

- [LLM Wiki Site](./llm-wiki-site.md)
- [Pipeline Handoff](./pipeline-handoff.md)
- [API to HPC Demo](./api-hpc-demo.md)
- [DRT Validation Workflow](./drt-validation-workflow.md)
- [Weekly Research Update](./weekly-research-update.md)

## Why This Matters

The current site is human-readable. This OKF bundle adds an agent-readable
layer so future tools can index the project by typed concepts instead of only
scraping rendered HTML.

The first goal is not to replace the site. The first goal is to keep the site
and the research pipeline documented in a portable format that can later feed
search, agent workflows, knowledge catalogs, or VM/HPC runbooks.
