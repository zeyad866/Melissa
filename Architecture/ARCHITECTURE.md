# Job Hunter Agent – Multi-Agent System Architecture

## 1. High-Level Concept
The **Job Hunter Agent** is an autonomous, multi-agent AI system built on **n8n** that streamlines the job acquisition process:
1. Ingests and extracts structured intelligence from raw CVs (Module 1).
2. Discovers and normalizes live vacancies across diverse job boards (Module 2).
3. Evaluates, scores, and ranks candidate-job compatibility with explainability (Module 3).
4. Truthfully tailors CVs and synthesizes personalized cover letters while enforcing strict anti-hallucination controls (Module 4).
5. Secures human approval, coordinates reliable submission, tracks application states in a database, and notifies candidates (Module 5).

---

## 2. Decoupled Pipeline Design
To enable parallel development across five independent engineers, the system implements a strict **black-box architecture** governed by frozen JSON interface contracts:

```
[Original CV (.tex/.pdf)]
         │
         ▼
┌──────────────────┐           ┌──────────────────┐
│     Module 1     │           │     Module 2     │
│  CV Intelligence │           │   Job Discovery  │
└────────┬─────────┘           └────────┬─────────┘
         │ candidate_profile.json       │ jobs.json
         │ (Contract 3.1)               │ (Contract 3.2)
         └───────────────┬──────────────┘
                         │
                         ▼
               ┌──────────────────┐
               │     Module 3     │
               │ Matching/Ranking │
               └────────┬─────────┘
                        │ ranked_jobs.json (Contract 3.3)
                        ▼
               ┌──────────────────┐
               │     Module 4     │ ◄── [Original CV (.tex)]
               │   CV Tailoring   │
               └────────┬─────────┘
                        │ application_package.json (Contract 3.4)
                        ▼
               ┌──────────────────┐
               │     Module 5     │
               │ App & Tracking   │
               └────────┬─────────┘
                        │ application_status.json (Contract 3.5)
                        ▼
               [Candidate Notified & Logged]
```

---

## 3. Data Contracts Summary

| Contract | Producing Module | Consuming Module | Primary Payload Structure |
|---|---|---|---|
| **3.1** | Module 1 (CV & AI) | Module 3 (Matching) | Structured profile: skills, languages, education, experience years, search keywords. |
| **3.2** | Module 2 (Job Retrieval) | Module 3 (Matching) | Normalized job array: titles, descriptions, companies, URLs, required skills. |
| **3.3** | Module 3 (Matching) | Module 4 (Documents) | Ranked jobs sorted by match score with explainability and `APPLY`/`REVIEW`/`REJECT` decision. |
| **3.4** | Module 4 (Documents) | Module 5 (Operations)| Verified package containing compiled PDF/LaTeX paths, cover letter, and fact-check audit. |
| **3.5** | Module 5 (Operations)| Final Output / Store | Application record: ID, candidate ID, approval state, submission method, confirmation log. |

---

## 4. Key Architectural Safeguards
1. **Zero Hallucination Gate (Module 4)**: The system strictly prohibits fabricating credentials. If an unsupported claim is generated, the fact-check gate intercepts the payload and triggers a repair loop or fails loudly.
2. **Human-in-the-Loop Gate (Module 5)**: AI never submits an application automatically without explicit user authorization via email or interactive form.
3. **Idempotency & Duplicate Shield (Module 5)**: Application requests are keyed by `hash(candidate_id + job_id)` to prevent spamming employers.
