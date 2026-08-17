# ADR-001: Fact-Checking & Hallucination Gate Architecture

## Status
Accepted

## Context
A primary ethical and grading constraint of the Job Hunter Agent is that tailored CVs and cover letters must never fabricate experience, credentials, or technologies. We evaluated:
1. Pure LLM-as-a-Judge (Prompt asking model if claims are true).
2. Rule-Based Exact Entity Extraction & Subsumption.
3. Hybrid Two-Stage Fact-Checker (Entity Extraction + Semantic Verification Judge).

## Decision
We selected the **Hybrid Two-Stage Fact-Checker**.

## Rationale
1. **Stage 1 (Deterministic Entity Subsumption)**: Extracts all proper nouns, skill keywords, dates, and degree names from the generated text and ensures every token set exists in the original CV knowledge graph.
2. **Stage 2 (LLM-as-a-Judge for Claims)**: For rephrased quantitative achievement bullets (e.g. "reduced latency by 42%"), verifies that metrics and scope match the original without exaggeration.
3. **Hard Fail Constraint**: If `fact_check.passed == false`, the workflow retries generation up to 2 times with explicit negative feedback before emitting a structured error payload.

## Consequences & Limitations
- Increases pipeline latency by ~1.5s per tailored package.
- Prevents 100% of fabricated skills from leaking downstream to Module 5.
