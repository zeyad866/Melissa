# Interface Contracts Specification & Starter Kit

## Overview
This directory contains the single source of truth for all data passing between the five modules of the Job Hunter Agent system.

Contracts are **frozen at Milestone 1**. Any changes require a signed **Contract Change Request (CCR)** recorded in [`change_log.md`](./change_log.md) and synchronized across both schema files and sample payloads.

---

## Directory Organization

```
contracts/
├── schemas/                         # JSON Schema (Draft 7) formal definitions
│   ├── candidate_profile.schema.json# Contract 3.1: M1 -> M3
│   ├── jobs.schema.json             # Contract 3.2: M2 -> M3
│   ├── ranked_jobs.schema.json      # Contract 3.3: M3 -> M4
│   ├── application_package.schema.json # Contract 3.4: M4 -> M5
│   └── application_status.schema.json  # Contract 3.5: M5 final output
│
├── sample_payloads/                 # Concrete mock payloads for independent development
│   ├── sample_candidate_profile.json
│   ├── sample_jobs.json
│   ├── sample_ranked_jobs.json
│   ├── sample_application_package.json
│   └── sample_application_status.json
│
├── sample_cv.tex                    # Starter LaTeX CV template
└── change_log.md                    # Formal audit trail for all contract revisions
```

---

## Contract Rules (Section 3)

1. **Naming & Types:** All field names use `lower_snake_case`. Timestamps use ISO-8601 UTC.
2. **Lists and Nulls:** Arrays are always JSON arrays (never comma-separated strings). Missing values are explicit `null`s, never empty strings.
3. **Immutability of Identifiers:** `candidate_id` and `job_id` are preserved across the entire pipeline.
4. **Validation:** Every module must validate its inputs and fail loudly on contract violations.
5. **Verification Command:**
   ```bash
   python scripts/validate_contracts.py
   ```
