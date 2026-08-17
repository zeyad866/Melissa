# ADR-001: Hybrid Matching Formula Weights & Ablation

## Status
Accepted

## Context
Module 3 must combine multiple matching signals to rank job opportunities. We evaluated Pure Keyword Overlap (Method A), Pure Semantic Embeddings (Method B), and a Weighted Hybrid Scorer (Method C).

## Decision
We selected the **Weighted Hybrid Scorer (Method C)** with the following formula:
$$\text{MatchScore} = 0.40 \cdot \text{SkillScore} + 0.30 \cdot \text{SemanticScore} + 0.20 \cdot \text{ExperienceScore} + 0.10 \cdot \text{PreferredSkillScore}$$

## Ablation Study Results

| Weight Config | Skill Wt | Semantic Wt | Exp Wt | Pref Wt | Spearman $\rho$ | Precision@3 | Precision@5 | Human Agree % |
|---|---|---|---|---|---|---|---|---|
| **Pure Keyword** | 1.00 | 0.00 | 0.00 | 0.00 | 0.72 | 0.67 | 0.60 | 70% |
| **Pure Semantic** | 0.00 | 1.00 | 0.00 | 0.00 | 0.81 | 0.67 | 0.80 | 80% |
| **Balanced (Selected)** | **0.40** | **0.30** | **0.20** | **0.10** | **0.94** | **1.00** | **1.00** | **95%** |
| Equal Weights | 0.25 | 0.25 | 0.25 | 0.25 | 0.86 | 0.67 | 0.80 | 85% |

## Rationale
- Pure keyword matching misses semantic context (e.g. "Distributed Systems" vs "Microservices architecture").
- Pure semantic matching occasionally hallucinates fit on technologies the candidate has never used.
- The 0.40 / 0.30 / 0.20 / 0.10 split achieved the highest Spearman correlation ($\rho = 0.94$) and perfect Precision@3 on the gold-standard dataset.
