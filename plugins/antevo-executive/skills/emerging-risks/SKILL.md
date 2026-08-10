---
name: emerging-risks
description: >-
  Track how the Antevo Executive Brief's risk radar has changed over weeks —
  which risks are newly on the board, which have been carried a long time, which
  dropped off, and how their trend, impact and probability moved. Use when the
  user asks "what new risks are emerging", "how have the risks changed", "what's
  escalating", "what dropped off the radar", "how has [risk/theme] developed",
  "what's been building", or wants the direction of travel rather than today's
  snapshot. For what's on the board RIGHT NOW use risk-radar instead; for the
  narrative of a story over time use story-timeline. Universal market risk — no
  account, no portfolio access. Read-only.
compatibility: >-
  Requires the Antevo Executive connector (public, no sign-in). If the tools are
  not available, tell the user to add https://api.antevo.ch/mcp/executive/mcp,
  then stop.
---

# Antevo — Emerging risks

The direction of travel: what has arrived on the risk board, what has hardened,
and what has quietly left.

## Step 1 — Pull the window
`track_risk_evolution(days_back)` returns **every risk board published in the
window in one call** — oldest first, each with its date, regime and risks.

- "recently", "lately" → 30 (default)
- "this quarter", "since the summer" → 90
- "this week", "the last few days" → 7 or 14

It also returns `window.dates`. **Read it.** The brief isn't published every
calendar day, so "30 days" may be 18 boards. Say how many you actually read.

## Step 2 — Group the risks yourself
**This is the core of the skill.** The tool deliberately does *not* thread risks
across days, because the brief rewords each one every morning and matching on
wording was measured to be unreliable — it grouped unrelated risks that shared a
turn of phrase and split the same risk when the phrasing moved.

So do it by **meaning**. These are one risk:

> *"Central-bank independence becomes an explicit market event"* (7 Aug)
> *"Fed independence turns from a legal question into a market variable"* (9 Aug)
> *"Fed independence stops being a legal story and becomes a term-premium story"* (10 Aug)

These are two, despite the shared construction:

> *"Fed independence stops being a legal story and becomes a term-premium story"*
> *"The discount stops being a rates story and becomes a funding-cost one"*

Work through the boards in date order and build the threads as you read.

## Step 3 — Classify what you found
For each thread, from the dates you grouped:

| Reading | What it means |
|---------|---------------|
| **New** | First appears in the last few boards, absent before |
| **Escalating** | Carried a while, but `trend` / `impact` / `probability` stepped up |
| **Entrenched** | On nearly every board across the window, grades steady |
| **Faded** | On earlier boards, absent from the latest |

**Be careful with "faded".** A risk leaves the board because it eased, because
it was absorbed into a bigger risk, or because the desk had five slots and
something else took one. Say it left the board — don't say it resolved.

## Step 4 — Output
```
# How the risk picture has changed — {first date} to {last date}
*{N} boards published in this window.*

## New on the board
**{Risk}** — first appeared {date}
{what it is · why it showed up now · current grades}

## Escalating
**{Risk}** — on the board since {date}
{date}: {grades} → {date}: {grades}
{what changed}

## Entrenched
**{Risk}** — {N} of {M} boards, {grades} throughout

## No longer on the board
**{Risk}** — last seen {date}
{what it was; note we can't tell from the board alone why it left}

---
*Grouped from {N} Antevo Executive Brief risk radars, {range}. Dates and grades
are as published; grouping the same risk across days is my reading. Editorial
market intelligence — not investment advice.*
```

## Guardrails
- **Cite the dates you grouped.** That footer line is not boilerplate — it's what
  lets the reader check your grouping. Keep it.
- **Grades are verbatim.** Quote `trend` / `impact` / `probability` as published
  on each date; never average them or smooth a jump.
- **Don't count a rewording as a change.** Only call something escalating if a
  *grade* moved, not if the sentence got sharper.
- **Don't infer causes.** The board says a risk was there, not why it arrived or
  left.
- **No personal advice.** If they want their own exposure to a theme, that's the
  Antevo Wealth connector.
