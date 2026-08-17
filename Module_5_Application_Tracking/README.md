# Module 5: Application & Tracking
**Owner:** Student 5 (Automation & Operations Engineer)

## Overview
This module receives a verified application package (`application_package.json`), checks against past submissions to prevent duplicate applications, pauses execution for **Human Approval**, dispatches the application via API or realistic mock, persists complete lifecycle records to a tracking database, sends candidate confirmations with attached PDFs, and manages retries and failure logging.

---

## Module Architecture & Dataflow

```mermaid
flowchart TD
    subgraph Ingest["1. Package Ingestion & Duplicate Shield"]
        Pkg["application_package.json (Contract 3.4)"] --> Dedup{"Duplicate Check<br/>hash(candidate_id + job_id)"}
        Dedup -- "Duplicate Exists" --> Skip["application_status: 'skipped_duplicate'<br/>Log Audit & Return"]
        Dedup -- "Unique Application" --> Gate["2. Human Approval Gate"]
    end

    subgraph Approval["2. Human Approval Gate"]
        Gate --> NotifyUser["Send Approval Request<br/>(Actionable Email Link / n8n Form)"]
        NotifyUser --> WaitDecision{"Wait for Human Decision<br/>(24h Timeout)"}
        
        WaitDecision -- "REJECTED" --> StatusReject["application_status: 'failed'<br/>Log Rejection & Abort"]
        WaitDecision -- "TIMEOUT" --> StatusTimeout["application_status: 'pending_approval'<br/>Log Stalled State"]
        WaitDecision -- "APPROVED" --> Submit["3. Submission Engine"]
    end

    subgraph Execution["3. Submission & Error Handling"]
        Submit --> HttpPost["HTTP POST Submission (API / Realistic Mock)"]
        HttpPost --> SubmitResult{"Submission Outcome"}
        
        SubmitResult -- "Transient 5xx" --> RetryLoop{"Attempts < 3?<br/>(Exponential Backoff)"}
        RetryLoop -- "Yes" --> HttpPost
        RetryLoop -- "No" --> PermanentFail["application_status: 'failed'<br/>Log Diagnostic Trace"]
        
        SubmitResult -- "200 OK (Success)" --> Persist["4. Tracking Store & Notification"]
    end

    subgraph Output["4. Persistence & Candidate Confirmation"]
        Persist --> DB["Upsert Record to Database<br/>(Postgres / Supabase / Sheets)"]
        DB --> EmailCandidate["Send Confirmation Email<br/>(Attach Tailored CV + Cover Letter)"]
        EmailCandidate --> ContractOut["application_status.json<br/>(Interface Contract 3.5)"]
    end
```

---

## Detailed Node Responsibilities

| Stage | Node Name | Description | Key Fault Tolerances |
|---|---|---|---|
| **1. Duplicate Shield** | `Duplicate Check` | Checks database for existing `candidate_id` + `job_id` record. | Prevents spamming employers with duplicate submissions. |
| **2. Approval Gate** | `Human Approval Gate` | Pauses workflow and presents match score, tailored CV, and cover letter to human. | Mandatory safety gate; timeout handling. |
| **3. Submission** | `Submission Dispatcher` | Dispatches application payload to company endpoint (or mock server). | Explicit retry loop with exponential backoff on 5xx errors. |
| **4. Persistence** | `Database Upsert` | Records timestamps, status (`submitted`, `failed`), and submission attempts. | Connection pooling and retry on database unavailability. |
| **5. Confirmation** | `Email Notification` | Dispatches email confirmation to candidate with generated PDF documents attached. | Attachment verification before sending. |

---

## Inputs and Outputs

- **Sample Input File:** [`test_data/sample_application_package.json`](./test_data/sample_application_package.json)
- **Output Schema:** [`../contracts/schemas/application_status.schema.json`](../contracts/schemas/application_status.schema.json)
- **Sample Output:** [`../contracts/sample_payloads/sample_application_status.json`](../contracts/sample_payloads/sample_application_status.json)

---

## Evaluation: 10 Failure & Edge Scenarios

Per Section 4 requirements, this module is validated against **10 discrete scenarios**:
1. **Happy Path:** Approved and successfully submitted.
2. **Human Rejection:** Explicit rejection at the approval gate.
3. **Approval Timeout:** Human does not respond within the configured window.
4. **Duplicate Blocked:** Immediate bypass when candidate has already applied to this job ID.
5. **Transient Failure Recovery:** Simulated 503 error recovered on retry attempt #2.
6. **Permanent Failure:** 400 Bad Request caught, logged with stage diagnostics without retrying.
7. **Email Service Down:** Application submitted to employer, email failure flagged in output.
8. **Missing Attachment:** Detected before email dispatch; fails with explicit error code.
9. **Database Store Unavailable:** Fallback logging to local disk without dropping state.
10. **Malformed Contract Ingestion:** Schema validator rejects input before triggering approval.

---

## Decision Records (ADRs)
- [`decisions/ADR-001-approval-channel.md`](./decisions/ADR-001-approval-channel.md): Evaluation of Actionable Emails vs n8n Form vs Webhook Bots.
- [`decisions/ADR-002-storage-system.md`](./decisions/ADR-002-storage-system.md): Comparison of PostgreSQL, Supabase, and Google Sheets for audit persistence.

---

## Checklist to Mark Done
- [x] Runs standalone with a sample mock package on Day 1.
- [x] Absolute rule enforced: Nothing is EVER submitted without explicit human approval.
- [x] Repeated executions of the same job never result in duplicate submissions.
- [x] Every failure mode ends in an explicit, structured status payload—never a silent failure.
