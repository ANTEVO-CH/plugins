---
name: risk-radar
description: >-
  Show what the Antevo Executive Brief judges could go wrong from here — the
  risk radar, with each risk's trend, impact, probability and the readings that
  would confirm or kill it. Use when the user asks "what are the risks", "what
  could go wrong", "what's the downside", "what should I be worried about",
  "what's on the risk radar", "what's the bear case", or wants to know what's
  coming that could move markets. Also handles the forward calendar — "what's
  coming up this week", "what data is due". This is UNIVERSAL market risk, not
  portfolio risk: it needs no account and knows nothing about the user's
  holdings. If they ask what THEIR portfolio is exposed to, this is the wrong
  skill. Read-only.
compatibility: >-
  Requires the Antevo Executive connector (public, no sign-in). If the tools are
  not available, tell the user to add https://api.antevo.ch/mcp/executive/mcp,
  then stop.
---

# Antevo — Risk radar

What the desk thinks could go wrong, graded, with the thing to watch that would
settle it either way.

## Scope (important)
This is **market and world risk**, published for everyone. It knows nothing
about the user's positions. If they ask "how exposed am I to this" or "what does
this mean for my portfolio", say plainly that this connector can't see holdings
and point them to the Antevo Wealth connector.

## Step 1 — Gather
| Need | Tool |
|------|------|
| The board now | `get_risk_radar()` |
| The board on a past date | `get_risk_radar(as_of="YYYY-MM-DD")` |
| What's coming | `get_catalysts(days_ahead)` — default 14 |
| Context for a risk | `get_executive_brief()` — the regime and the wider read |
| How a risk developed | hand off to **emerging-risks** |

For "what are the risks", the radar alone usually carries it. Add catalysts when
the question is forward-looking ("what's coming up", "what should I watch").

## Step 2 — Read the grades honestly
Each risk carries `trend`, `impact` and `probability` **as published**. Use them:

- **Lead with impact × probability**, not with whatever is listed first. A
  `severe` / `medium` outranks a `high` / `low`.
- **`trend` is the live part.** A risk marked *Rising* is the story; one marked
  *Stable* is background. Say which is which.
- **Never invent a grade.** If a field is missing, leave it out rather than
  inferring one.
- **Don't convert to numbers.** "high probability" is the desk's word; turning it
  into "70%" fabricates precision it never claimed.

## Step 3 — Pair each risk with its tell
The radar comes with a `watch` list — the readings that would confirm or kill
these risks. A risk without its tell is an opinion; a risk with one is
monitorable. Attach them where they line up.

## Step 4 — Output
```
# What could go wrong — {date}

**The regime:** {label} — {one line}

## On the board
### {Risk title}
{impact} impact · {probability} probability · **{trend}**
{why it matters, in your own words}
*Watch:* {the reading that would settle it}

## Coming up
| Date | Event | What it would tell us |
|------|-------|-----------------------|
| {date} | {event} | {signal} |

---
*From the Antevo Executive Brief risk radar, {date}. Editorial market
intelligence — not investment advice.*
```

Order risks by consequence, not by list position. Three well-drawn risks beat
five summarised flat.

## Guardrails
- **Attribute and date it.** This is the brief's judgement on a given morning,
  not a permanent truth.
- **Don't editorialise the severity up.** If the desk said *medium*, it's medium.
- **Don't predict.** These are risks the desk is watching, not forecasts.
- **No personal advice**, and no "you should hedge X" — universal commentary only.
- If the brief has no radar for the date requested, say so and offer the nearest
  published date rather than falling back to today's and implying it's theirs.
