# ADR-001: Job Retrieval Source Selection

## Status
Accepted

## Context
Module 2 must integrate at least two independent job retrieval sources providing diverse, clean technical vacancy data without breaching Terms of Service. Candidates evaluated:
1. **Adzuna API** (Official REST API)
2. **JSearch API via RapidAPI** (Aggregates LinkedIn, Indeed, Glassdoor)
3. **Jooble API**
4. **Arbeitnow API** (Direct remote European jobs)

## Decision
We selected **Adzuna API** and **JSearch (RapidAPI)** as the primary dual sources, with **Arbeitnow** as a secondary failover.

## Rationale
1. **Source Independence**: Adzuna operates its own crawler network; JSearch aggregates major corporate career portals.
2. **Schema Depth**: Both sources supply rich salary, seniority, geographic location, and long-form description fields.
3. **Rate Limits & Free Tiers**: Provide sufficient free monthly requests (Adzuna: 250 req/day; RapidAPI JSearch: 500 req/month) to run all student test suites.

## Consequences & Limitations
- Requires managing two separate API authentication keys in n8n credentials.
- When one API experiences a 429 rate limit or outage, the workflow gracefully returns available records from the active source.
