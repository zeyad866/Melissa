# ADR-001: Human Approval Channel Selection

## Status
Accepted

## Context
Automated submission without candidate consent poses serious ethical and compliance risks. Module 5 must pause and require human sign-off before dispatching any application. We evaluated:
1. Native n8n Interactive Form Node (Webhook Pause/Resume).
2. Actionable Email Links (Approve / Reject buttons with HMAC tokens).
3. Telegram / Slack Interactive Webhook Bot.

## Decision
We selected **Actionable Email Links with n8n Form fallback** and a 24-hour expiration timeout.

## Rationale
1. **Accessibility**: Candidates can review and approve applications directly from their mobile inbox without needing n8n console access.
2. **Security**: Approval links embed a single-use token; once clicked, the decision is immutable.
3. **Timeout Behavior**: If no response is received within 24 hours, the status transitions to `pending_approval` / `skipped_timeout` without auto-submitting.

## Consequences & Limitations
- Requires an active SMTP email provider (SendGrid / Gmail / Resend) configured in n8n.
- If email delivery fails, the fallback webhook or n8n Form node can be triggered manually.
