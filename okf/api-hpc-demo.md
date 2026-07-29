---
type: API Demo
title: API to HPC Demo
description: Minimal local prototype proving API job submission, worker execution, status tracking, and result retrieval before VM/HPC deployment.
resource: ../demo-api-hpc/
tags: [fastapi, hpc, vm, job-runner, battery-csv]
timestamp: 2026-07-21T00:00:00+02:00
---

# API to HPC Demo

The demo proves the control flow for a future HPC-backed battery pipeline.

## Control Flow

1. Client submits a job request to the API.
2. API creates a job id.
3. A local worker processes a sample battery CSV.
4. Worker writes a JSON summary.
5. API exposes status and result endpoints.

## Future HPC Replacement Point

The local worker call can later be replaced by a scheduler command such as:

```bash
sbatch run_battery_job.slurm <job_id> <input_csv> <output_json>
```

## Linked Concepts

- [Pipeline Handoff](./pipeline-handoff.md)
- [LLM Wiki Site](./llm-wiki-site.md)
