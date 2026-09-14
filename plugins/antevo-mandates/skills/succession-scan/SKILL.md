---
name: succession-scan
description: >-
  Which clients in the firm's book have incomplete succession planning, ranked by
  how much of their checklist is still open. Use when the user asks "which
  clients have no succession plan", "where are the succession gaps", "who should
  we talk to about succession", or "how complete is succession planning across
  the book". Reads the signed-in firm's own book. Needs an Antevo Mandates firm
  account.
compatibility: >-
  Requires the Antevo Mandates connector, signed in with an Antevo Mandates firm
  account. If the tools are not available, tell the user to add
  https://api.antevo.ch/mcp/mandates/mcp and sign in, then stop.
---

# Antevo Mandates — Succession scan

Where the book's succession planning is thin.

## Before you start
- **Connector check.** No `get_succession_scan` tool → ask the user to connect
  Antevo Mandates, then stop.
- **Firm.** The scan needs `firm_id`. No tool on this connector looks it up, so
  ask the user for it once and reuse it. **Never guess one.**

## Step 1 — Gather
| Need | Tool |
|------|------|
| The whole book | `get_succession_scan(firm_id)` |
| Context on a client that stands out | `get_client_dossier(firm_id, client_id)` |

## Step 2 — Read it carefully
Each row carries `confirmed`, `total`, `completion_pct` and `urgency`.
- `urgency` is **HIGH** below 30% complete, **MEDIUM** below 70%, else **LOW**.
- **A client with `total` = 0 has no checklist at all.** The connector marks that
  row LOW, which reads as "fine". It is the opposite: nothing has been started.
  **Report these separately as "not started"** and never as low urgency.
- The scan covers **active clients**, at most 50, least complete first. If 50
  come back, say more may exist.

## Step 3 — Output
```
# Succession planning — {firm}, {date}

## Not started ({n})
{clients with no checklist}

## Mostly open — below 30%
| Client | Confirmed | Of | Complete |

## Under way — 30 to 70%
| Client | Confirmed | Of | Complete |

## Largely complete — 70% and above
{count}

---
*From {firm}'s Antevo Mandates record, {date}. Measures checklist completion, not
the quality of a plan. Not legal or tax advice.*
```

## Guardrails
- **Completion is not quality.** A fully checked list says the steps were
  confirmed, not that the plan is sound.
- **No legal, tax or estate advice** — surface the gap, leave the plan to the
  firm and the client's advisers.
- **Nothing is changed** by this skill.
