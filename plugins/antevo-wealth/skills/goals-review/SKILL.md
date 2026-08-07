---
name: goals-review
description: >-
  Review a Antevo Wealth household's financial goals and funding progress. Use
  when the user asks "how am I tracking against my goals", "am I on track for
  retirement / the property / the exit", "what's my progress toward [goal]", "what
  do I need to stay on plan", or wants a read on their wealth goals. Orchestrates
  the Antevo Wealth MCP connector's wealth.goals tool (target vs current, progress %, gap,
  ahead/behind). Read-only.
compatibility: >-
  Requires the Antevo Wealth MCP connector (wealth.goals). If the tools are not
  available, tell the user to connect Antevo Wealth, then stop.
---

# Antevo Wealth — Goals review

Turn the goals list into a clear "on track / at risk, and what closes the gap"
read.

## Before you start
- **Connector check.** No `wealth.goals` tool → ask the user to connect Antevo Wealth, then stop.
- **Household.** Resolve a `household_id` (ask if more than one).

## Step 1 — Gather
- `list_goals(household_id)` — each goal with type, target vs current funding, progress %, gap to target, whether it's ahead/behind, and a talking point.

## Step 2 — Analyse
- **On track vs at risk.** Group by status; lead with the goals most behind / largest gap.
- **The gap.** For at-risk goals, the shortfall and what would close it (time, contribution, return) — framed as planning, not a product pitch.
- **Priority.** Flag the primary goal and any with a near target date.

## Step 3 — Output
```
# Goals — {household} · {as-of}

**Read.** {1–2 lines: what's on track, what's at risk.}

## Goals
- {name} ({type}): {current}/{target} · {progress%} · {ahead/behind} · gap {…}

## What I'd focus on
- {goal} — {what closes the gap}
```

## Guardrails
- Empty goals = data ("no goals set — define them on the web"), not a gap to fill.
- Planning guidance, **not investment advice**; say so.
- Read-only: this skill reviews goals; it doesn't create or edit them.
