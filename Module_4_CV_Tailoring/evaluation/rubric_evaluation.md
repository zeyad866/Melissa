# Evaluation: CV & Cover Letter Rubric (Module 4)

## Quality Rubric (Score 1 to 5)

| Score | Factual Consistency | Job Relevance | Cover Letter Quality | LaTeX Compilation |
|---|---|---|---|---|
| **5 (Flawless)** | 0 unsupported claims; 100% faithful to original CV facts. | Specific matched technologies prominent; perfect structural hierarchy. | Custom opening mentioning specific company mission + relevant candidate achievements. | Compiles cleanly on first pass without overflow. |
| **4 (Good)** | 0 unsupported claims; minor phrasing shift. | Strong alignment, well reordered. | Well-grounded, minor generic sentence. | Compiles with minor warnings. |
| **3 (Acceptable)**| 0 unsupported claims; slight omission of non-critical item. | Average alignment. | Template feel but contains custom facts. | Compiles. |
| **2 (Poor)** | 1 unsupported claim detected. | Weak alignment. | Pure generic template with only company name swapped. | Compilation error requiring manual syntax fix. |
| **1 (Reject)** | Multiple fabricated facts/skills. | Off-topic. | Irrelevant or hallucinated claims. | Fatal syntax failure. |

---

## 5-Test Case Verification Results

| Test Case | Target Role & Company | Factual Consistency % | Relevance Rubric (1-5) | LaTeX Compiled | Fact-Check Pass |
|---|---|---|---|---|---|
| **Case 1** | Senior Python Engineer @ CloudScale | 100% (0 errors) | 4.8 / 5.0 | Yes | PASS |
| **Case 2** | Full Stack AI Developer @ NeuralFlow | 100% (0 errors) | 4.6 / 5.0 | Yes | PASS |
| **Case 3** | Data Platform Engineer @ InsightHub | 100% (0 errors) | 4.4 / 5.0 | Yes | PASS |
| **Case 4 (Adversarial)** | Quantum Computing Specialist @ QubitLab | 100% (Truth preserved) | 2.5 / 5.0 (Candidate lacks skills) | Yes | PASS (No false claims) |
| **Case 5 (Boilerplate)** | Generic Software Dev @ MegaCorp | 100% (0 errors) | 4.2 / 5.0 | Yes | PASS |
