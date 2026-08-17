# Job Hunter Agent – AIE314 Summer26

A modular, multi-agent automated job application system built on **n8n**. Five independent modules operate autonomously on mock inputs from Day 1 and connect via frozen JSON interface contracts.

Repository: [https://github.com/zeyad866/Melissa](https://github.com/zeyad866/Melissa)

---

## 🏛️ System Architecture

```mermaid
flowchart LR
    subgraph Intake["Intake & Discovery"]
        M1["Module 1: CV Intelligence<br/>(Student 1)"]
        M2["Module 2: Job Discovery<br/>(Student 2)"]
    end

    subgraph Decision["Evaluation & Tailoring"]
        M3["Module 3: Matching & Ranking<br/>(Student 3)"]
        M4["Module 4: CV Tailoring & Docs<br/>(Student 4)"]
    end

    subgraph Operations["Execution & Tracking"]
        M5["Module 5: App & Tracking<br/>(Student 5)"]
    end

    CV["Original CV (.tex/.pdf)"] --> M1
    M1 -->|candidate_profile.json (3.1)| M3
    
    SearchConfig["search_config.json"] --> M2
    M2 -->|jobs.json (3.2)| M3
    
    M3 -->|ranked_jobs.json (3.3)| M4
    CV --> M4
    
    M4 -->|application_package.json (3.4)| M5
    M5 -->|application_status.json (3.5)| Completed["Application Logged & Tracked"]
```

---

## 👥 Module Breakdown & Documentation

| Module | Role | Primary Responsibility | Directory & Docs | Architecture Diagram |
|---|---|---|---|---|
| **Module 1** | **CV & AI Engineer** | CV intake, parsing, structured LLM extraction, schema validation. | [`Module_1_CV_Intelligence/`](./Module_1_CV_Intelligence/) | [View Flow](./Module_1_CV_Intelligence/README.md#module-architecture--dataflow) |
| **Module 2** | **Job Retrieval Engineer** | Dual-source retrieval, API normalization, deduplication, filtering. | [`Module_2_Job_Discovery/`](./Module_2_Job_Discovery/) | [View Flow](./Module_2_Job_Discovery/README.md#module-architecture--dataflow) |
| **Module 3** | **Matching Engineer** | Hybrid scoring (Keyword, Semantic, Experience), ranking, explainability. | [`Module_3_Matching_Ranking/`](./Module_3_Matching_Ranking/) | [View Flow](./Module_3_Matching_Ranking/README.md#module-architecture--dataflow) |
| **Module 4** | **Document Engineer** | Truthful tailoring, anti-hallucination gate, LaTeX/PDF compilation. | [`Module_4_CV_Tailoring/`](./Module_4_CV_Tailoring/) | [View Flow](./Module_4_CV_Tailoring/README.md#module-architecture--dataflow) |
| **Module 5** | **Operations Engineer** | Human approval gate, submission, persistence, notifications, retries. | [`Module_5_Application_Tracking/`](./Module_5_Application_Tracking/) | [View Flow](./Module_5_Application_Tracking/README.md#module-architecture--dataflow) |
| **Integration** | **Integration Lead** | Interface contracts, master workflow, pairwise smoke testing. | [`Integration/`](./Integration/) | [View Pipeline](./Integration/README.md#integration-architecture) |

---

## 📑 Interface Contracts (Frozen v1.0)

All payloads adhere to formal JSON Schema definitions located in [`contracts/schemas/`](./contracts/schemas/):

1. **Contract 3.1 (`candidate_profile.json`)**: Output of Module 1 consumed by Module 3.
2. **Contract 3.2 (`jobs.json`)**: Output of Module 2 consumed by Module 3.
3. **Contract 3.3 (`ranked_jobs.json`)**: Output of Module 3 consumed by Module 4.
4. **Contract 3.4 (`application_package.json`)**: Output of Module 4 consumed by Module 5.
5. **Contract 3.5 (`application_status.json`)**: Final output of Module 5.

Full contract specifications and mock data: [`contracts/README.md`](./contracts/README.md).

---

## 🛠️ Automated Testing & Validation

### Validate Interface Contracts
```bash
python scripts/validate_contracts.py
```

### Validate Evaluation Metrics Formulae
```bash
python scripts/calculate_metrics.py --test
```

---

## 📅 Milestones & Deliverables

- **Milestone 1**: Module architecture design, contract freeze v1.0, and n8n skeleton workflows.
- **Milestone 2**: Independent prototype running on sample inputs (happy path).
- **Milestone 3**: AI, retrieval, ranking, and operations logic implemented with error handling.
- **Milestone 4**: Test cases, ground-truth evaluation (P/R/F1), selection matrices, and decision records.
- **Milestone 5**: Pairwise integration smoke testing.
- **Milestone 6**: End-to-end acceptance demonstration, team report, and individual defense.
