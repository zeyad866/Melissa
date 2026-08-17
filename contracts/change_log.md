# Interface Contracts Change Log

> **Rule (Section 3.6):** Contracts change only through formal written requests signed by producing and consuming module owners, version bumped, and sample files synchronized.

| Version | Date | Target Contract | Requester | Approver(s) | Description of Change | Impacted Modules |
|---|---|---|---|---|---|---|
| **v1.0** | 2026-08-17 | All (3.1 to 3.5) | Integration Lead | All Module Leads (M1–M5) | Initial Contract Freeze Milestone 1 | M1, M2, M3, M4, M5 |

---

## Contract Change Request (CCR) Procedure

1. **Submit Request**: Requester opens a PR / Issue with rationale and exact JSON diff.
2. **Impact Assessment**: Producer and every consumer evaluate changes.
3. **Sign-off**: Producing owner + Consuming owner(s) approve.
4. **Integration Lead Action**:
   - Updates `contracts/schemas/*.schema.json`
   - Bumps `schema_version` (e.g. `1.0` $\rightarrow$ `1.1`)
   - Updates all sample payloads in `contracts/sample_payloads/`
   - Records the entry in this file.
