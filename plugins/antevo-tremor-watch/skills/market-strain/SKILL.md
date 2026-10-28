---
name: market-strain
description: >-
  Read this week's Antevo Tremor Index — how many market relationships stopped
  behaving in the week that ended on Friday, against a normal Friday since 2001.
  Use when the user asks "are markets under strain", "is this a stressed
  market", "how bad is it this week", "is something breaking in markets", "are
  correlations breaking down", "is diversification holding", or wants a
  temperature check on markets as a whole. This is a DESCRIPTIVE reading of the
  whole market, not a forecast and not about the user's holdings. Read-only.
compatibility: >-
  Requires the Antevo Tremor Watch connector (public, no sign-in). If the tools
  are not available, tell the user to add https://api.antevo.ch/mcp/tremor/mcp,
  then stop.
---

# Antevo — Market strain this week

How many of the usual relationships between markets broke this week, and how
unusual that is.

## Scope (important)
The index describes the **whole market**: 753 pairs of markets in seven
families. It knows nothing about the user's portfolio. If they ask "what does
this mean for my holdings", say plainly that this connector can't see holdings
and point them to the Antevo Wealth connector. It is **not a forecast**: it
measures how many relationships are breaking at once and says nothing about
where prices go next.

## Step 1 — Gather
| Need | Tool |
|------|------|
| This week's reading | `get_tremor_index()` |
| Which pairs are behind it | `get_tremor_pairs()` — breaking pairs, most unusual first |
| The last few months for context | `get_tremor_history(weeks=13)` |

The index call alone usually carries the answer. Add the pairs when the user
wants to know *what* broke (or hand off to **what-broke**).

## Step 2 — Read it the way it is built
- **Lead with `times_normal` and `status`.** "2.9 times a normal Friday,
  Elevated" is the headline. A normal Friday is the median week since 2001; the
  status lines are the 75th, 90th and 97th percentiles since 2001.
- **Give the rank.** `rank_since_2001` of `fridays_since_2001` puts the week in
  history ("the 211th most unsettled of 1,347 Fridays").
- **Say which way the links moved.** `weakening` is links coming apart;
  `strengthening` is links moving closer than usual (often everything falling
  together). Name the larger one.
- **Name the families above their own normal.** Each family has its own
  `times_normal`; the ones at 2× or more are where the breaks gather.
- **Compare with `last_week`** in one line: rising, easing or flat.
- **If `provisional` is present, say so**: fewer pairs were read because a
  source was late, and next Saturday revises the week.
- **Context only:** `reading.context.realized_volatility_vs_normal` (1.0 =
  normal) says whether prices are also moving more than usual. Breaks without
  high volatility are worth pointing out.

## Step 3 — Output
```
# Market strain — week ending {week}

**{status}: {times_normal}× a normal Friday** — the {rank}th most unsettled of
{fridays} Fridays since 2001. {Mostly coming apart | mostly moving closer}.

**Where:** {families above 2× their normal, with breaking/pairs}
**Last week:** {times_normal}×, {status} — {rising/easing/flat}
{provisional note if present}

---
*Antevo Tremor Index, week of {week}. Descriptive, not a forecast, and not
investment advice.*
```

## Guardrails
- **Cite the week.** Use the `cite_as` line; the index is weekly, written on
  Saturday for the week that ended on Friday.
- **Don't forecast.** No "this means a crash is coming", no probabilities of
  anything. Past episodes may be named for scale, not as predictions.
- **Don't invent levels.** The connector returns no price or index levels and no
  VIX figure; don't add any from memory.
- **No personal advice**, no "you should de-risk".
