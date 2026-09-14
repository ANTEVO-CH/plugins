---
name: reviews-due
description: >-
  Which clients in the firm's book are due or overdue a review, in the order they
  need attention — and, only on the user's go, record a review as done. Use when
  the user asks "who is due a review", "which reviews are overdue", "what's on my
  review list this month", "has the Alder household been reviewed", or "mark
  this review done". Reads the signed-in firm's own book. Needs an Antevo
  Mandates firm account.
compatibility: >-
  Requires the Antevo Mandates connector, signed in with an Antevo Mandates firm
  account. If the tools are not available, tell the user to add
  https://api.antevo.ch/mcp/mandates/mcp and sign in, then stop.
---

# Antevo Mandates — Reviews due

The review list, in the order it needs working.

## Before you start
- **Connector check.** No `get_client_reviews_due` tool → ask the user to connect
  Antevo Mandates, then stop. Never invent clients or dates.
- **Firm.** Leave `firm_id` out — the connector uses the signed-in member's own
  firm. If they belong to several, the tool answers with each firm's name and ID;
  ask which one they mean, then pass that `firm_id` for the rest of the
  conversation. **Never guess one.**
- **A client by name.** `get_eam_clients(search="Alder")` returns
  `eam_client_id`. If several match, ask which.

## Step 1 — Gather
| Need | Tool |
|------|------|
| Every scheduled review | `get_client_reviews_due()` |
| One client's review | `get_client_reviews_due(client_id)` |
| Context on a client near the top | `get_client_dossier(client_id)` |
| Record a review as done | `complete_review(client_id, notes, next_review_months)` — **a write** |

## Step 2 — Order it
Each row carries `next_review_date`, `last_reviewed_at`, `days_until_due` and
`risk_tier`.
- **Overdue first** (`days_until_due` below zero), most overdue at the top.
- Then **due within 30 days**, higher `risk_tier` before lower, soonest first.
- Then the rest.
- The list holds **active clients with a scheduled date** only, and at most 50
  of them, soonest first. If 50 come back, say more may exist. A client with no
  review date will not appear here; say that, rather than implying the book is
  complete.

## Step 3 — Output
```
# Reviews — {firm}, {today}

## Overdue
| Client | Due | Overdue by | Risk tier | Last reviewed |

## Due in the next 30 days
| Client | Due | In | Risk tier | Last reviewed |

## Later
{count} more scheduled, the next on {date}.
```

## Recording a review (a write)
`complete_review` stamps the review as done today, moves the next review forward
by `next_review_months` (default 12) and files any `notes` against the client.
**It changes the record.** Only call it when the user has asked for that client
in this conversation, and first say exactly what will happen: "Mark {client}
reviewed today, next review {date}, with this note: …". Wait for a yes. If the
user's sign-in is read-only, the tool refuses — say so; don't retry.

## Guardrails
- **Dates come from the record**, never from inference.
- **Never mark a review done** without an explicit go for that client.
- **No compliance judgement.** Report what is scheduled and what is late; the
  firm decides what that means.
