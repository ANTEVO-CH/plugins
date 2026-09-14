---
name: meeting-prep
description: >-
  Prepare for a client meeting from the firm's own record — who the client is,
  the state of their book and review, goals and progress, the team, recent
  correspondence, and the questions worth raising. Use when the user asks
  "prepare me for my meeting with the Birch family", "brief me on this client",
  "what do I need to know before seeing X", or "what's open with this client".
  Reads the signed-in firm's own book. Needs an Antevo Mandates firm account.
compatibility: >-
  Requires the Antevo Mandates connector, signed in with an Antevo Mandates firm
  account. If the tools are not available, tell the user to add
  https://api.antevo.ch/mcp/mandates/mcp and sign in, then stop.
---

# Antevo Mandates — Meeting prep

One page to walk in with.

## Before you start
- **Connector check.** No `get_client_dossier` tool → ask the user to connect
  Antevo Mandates, then stop.
- **Firm.** Leave `firm_id` out — the connector uses the signed-in member's own
  firm. If they belong to several, the tool answers with each firm's name and ID;
  ask which one they mean, then pass that `firm_id` for the rest of the
  conversation. **Never guess one.**
- **The client.** `get_eam_clients(search=name)` → `eam_client_id`. If
  several match, ask which.

## Step 1 — Gather
| Need | Tool |
|------|------|
| Who they are, AUM, review status, team | `get_client_dossier(client_id)` |
| Goals and progress | `get_client_goals(client_id)` |
| The assigned team | `get_client_team(client_id)` |
| Recent correspondence and its flags | `get_email_messages(client_id=client_id)` |
| The full generated brief | `generate_meeting_brief(client_id)` — **uses credits** |

Start from the dossier, goals and correspondence: they are free and usually
enough. `generate_meeting_brief` builds an eleven-section brief and **consumes
credits** — offer it, say that it costs credits, and call it only on a yes. If it
answers that the service is not available, carry on from the dossier.

## Step 2 — Compose
- **Lead with what changed or is open**: a review that is due, a goal behind
  plan, an email flagged for compliance or awaiting a reply.
- **Goals:** say which are on track and which are behind, with the figures the
  record holds.
- **Correspondence:** summarise the subject and what is pending. Quote only what
  the meeting needs; a brief is not the place to reproduce a client's email.
- **Questions to raise** come from gaps in the record — a goal with no recent
  progress, a missing document, an unanswered request — not from market views.

## Step 3 — Output
```
# {client} — meeting brief, {date}

**In one line:** {the thing to walk in knowing}

## The relationship
{type, segment, team, last review and next due}

## Goals
| Goal | Target | Progress | Status |

## Open items
- {item — from the record, dated}

## Worth raising
- {question}

---
*From {firm}'s Antevo Mandates record, {date}. Preparation support, not
investment, tax or legal advice.*
```

## Guardrails
- **Only the record.** Never invent a holding, a goal or a conversation.
- **No investment recommendations** for the client.
- **Nothing is changed** by this skill. If the user wants a note filed or a goal
  updated, say what would change and wait for a clear yes before any write tool.
