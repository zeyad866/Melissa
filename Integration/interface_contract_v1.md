# Interface Contracts Specification (Version 1.0)

This document formalizes the five interface contracts governing the Job Hunter Agent system. All team members must adhere to these schemas without ad-hoc renaming.

---

## Contract 3.1: `candidate_profile.json` (Module 1 $\rightarrow$ Module 3)
- **Schema File:** [`contracts/schemas/candidate_profile.schema.json`](../contracts/schemas/candidate_profile.schema.json)
- **Sample Payload:** [`contracts/sample_payloads/sample_candidate_profile.json`](../contracts/sample_payloads/sample_candidate_profile.json)
- **Key Fields:** `schema_version`, `candidate_id`, `candidate_name`, `email`, `experience_years`, `job_titles`, `technical_skills`, `programming_languages`, `frameworks`, `tools`, `keywords`, `education`, `extraction_meta`.

---

## Contract 3.2: `jobs.json` (Module 2 $\rightarrow$ Module 3)
- **Schema File:** [`contracts/schemas/jobs.schema.json`](../contracts/schemas/jobs.schema.json)
- **Sample Payload:** [`contracts/sample_payloads/sample_jobs.json`](../contracts/sample_payloads/sample_jobs.json)
- **Key Fields:** `schema_version`, `job_id`, `job_title`, `company`, `location`, `source`, `description`, `application_url`, `required_skills`, `retrieved_at`.

---

## Contract 3.3: `ranked_jobs.json` (Module 3 $\rightarrow$ Module 4)
- **Schema File:** [`contracts/schemas/ranked_jobs.schema.json`](../contracts/schemas/ranked_jobs.schema.json)
- **Sample Payload:** [`contracts/sample_payloads/sample_ranked_jobs.json`](../contracts/sample_payloads/sample_ranked_jobs.json)
- **Key Fields:** `match_score`, `score_breakdown`, `matched_skills`, `missing_skills`, `experience_match`, `semantic_similarity`, `decision`, `explanation`, `method`, `ranked_at`.

---

## Contract 3.4: `application_package.json` (Module 4 $\rightarrow$ Module 5)
- **Schema File:** [`contracts/schemas/application_package.schema.json`](../contracts/schemas/application_package.schema.json)
- **Sample Payload:** [`contracts/sample_payloads/sample_application_package.json`](../contracts/sample_payloads/sample_application_package.json)
- **Key Fields:** `candidate_id`, `job_id`, `cv_file`, `cv_tex_file`, `cover_letter_file`, `tailoring_meta`, `fact_check` (`unsupported_claims`, `passed`), `latex_compiled`.

---

## Contract 3.5: `application_status.json` (Module 5 Output)
- **Schema File:** [`contracts/schemas/application_status.schema.json`](../contracts/schemas/application_status.schema.json)
- **Sample Payload:** [`contracts/sample_payloads/sample_application_status.json`](../contracts/sample_payloads/sample_application_status.json)
- **Key Fields:** `application_id`, `approval_decision`, `application_status`, `submission_method`, `submitted_at`, `attempts`, `confirmation_sent`, `error`.
