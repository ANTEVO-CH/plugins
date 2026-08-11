---
name: world-brief
description: >-
  Brief the user on what's happening in markets and the world, from the Antevo
  Executive Brief. Use when the user asks "what's happening in the world",
  "brief me on the markets", "what's the news", "what happened this week",
  "where are markets", "what's the read on [theme/region/asset]", or wants an
  editorial take on current events. This is UNIVERSAL market and world
  intelligence — it needs no account and knows nothing about the user's own
  holdings. If they ask about *their* portfolio, positions or net worth, this is
  the wrong skill. Read-only.
compatibility: >-
  Requires the Antevo Executive connector (public, no sign-in). If the tools are
  not available, tell the user to add https://api.antevo.ch/mcp/executive/mcp,
  then stop.
---

# Antevo — World brief

Turn the published Executive Brief into a crisp read on **what's happening and
why it matters** — the editorial view, not a headline dump.

## Scope (important)
This connector is **public and universal**. It has no access to anyone's
portfolio. If the user asks about *their* holdings, exposure or net worth, say
so and point them to the Antevo Wealth connector — don't guess.

## Step 1 — Gather
| Layer | Tool |
|-------|------|
| Today's editorial read | `get_executive_brief()` |
| Where markets stand | `get_market_snapshot()` |
| How markets moved | `get_indices(days_back)` — for "this week/month" |
| World events | `get_world_events(days_back)` — conflict, chokepoints, sanctions |
| Longer-form analysis | `get_executive_desk()` — when they want depth |

For a plain "what's happening", the brief + snapshot is usually enough. Add the
others only when the question calls for them.

## Step 2 — Compose
- **Lead with the one thing.** The brief has a hero takeaway — open with it in your own words, not a quote dump.
- **Then the regime.** What kind of market is this, and what's driving it.
- **Then two or three themes** that actually matter, each with its "so what".
- **Ground it in numbers** from the snapshot where they sharpen the point.
- **If they named a topic**, filter hard to it and say plainly if the brief doesn't cover it.

## Step 3 — Output
```
# {The headline read} — {date}

{2–3 sentences: what matters most right now and why.}

## The regime
{what kind of market this is; what's driving it}

## What matters
- **{Theme}** — {the read} · {so what}

## Markets
{the handful of levels that support the story}

---
*From the Antevo Executive Brief, {date}. Editorial market intelligence —
not investment advice.*
```

## Guardrails
- **Attribute it** — this is the Antevo Executive Brief's view, and say the date.
- **Don't invent.** If the brief is silent on their topic, say so; offer `story-timeline` to search the archive.
- **No personal advice.** Universal commentary only — not investment advice.
- If they want *their* exposure to a theme, hand off to the Antevo Wealth connector.
