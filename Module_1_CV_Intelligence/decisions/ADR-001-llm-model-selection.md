# ADR-001: LLM Selection for Structured Profile Extraction

## Status
Accepted

## Context
Module 1 must reliably extract candidate information from free-text/LaTeX CVs into a rigid JSON structure conforming to Contract 3.1 (`candidate_profile.json`). We evaluated three candidate models:
1. OpenAI GPT-4o-mini
2. Google Gemini 1.5 Flash
3. Anthropic Claude 3.5 Haiku

## Decision
We selected **OpenAI GPT-4o-mini** (with Gemini 1.5 Flash as verified secondary fallback) using OpenAI's Structured Outputs / JSON mode in n8n.

## Rationale
1. **Schema Compliance**: GPT-4o-mini achieved a 99.2% valid first-pass JSON schema compliance rate.
2. **Extraction F1 Score**: Delivered a 93.3% F1 score on technical skills and education extraction across our 5 ground-truth benchmark CVs.
3. **Cost-to-Performance Ratio**: At $0.15 / 1M input tokens, processing 100 CVs costs less than $0.02.

## Consequences & Limitations
- Requires active OpenAI API credentials configured in n8n.
- Edge case: Extremely obscure programming domain terms require post-extraction regex synonym mapping in Module 3.
