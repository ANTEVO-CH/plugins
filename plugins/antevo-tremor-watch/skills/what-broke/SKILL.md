---
name: what-broke
description: >-
  List the market relationships that stopped behaving — the pairs whose
  correlation is two standard deviations from their own previous two years,
  most unusual first, and the new breaks of the last four weeks. Use when the
  user asks "which correlations broke", "what's moving together that shouldn't",
  "is gold still a hedge", "are stocks and bonds still moving opposite", "what
  changed this week between markets", or names a market and asks how it is
  behaving against the others. Descriptive, not a forecast. Read-only.
compatibility: >-
  Requires the Antevo Tremor Watch connector (public, no sign-in). If the tools
  are not available, tell the user to add https://api.antevo.ch/mcp/tremor/mcp,
  then stop.
---

# Antevo — What broke

The relationships between markets that stopped behaving this week, named.

## Step 1 — Gather
| Need | Tool |
|------|------|
| This week's breaking pairs | `get_tremor_pairs()` — breaking only, most unusual first |
| One market against the rest | `get_tremor_pairs(market="Gold", breaking_only=false)` |
| One family | `get_tremor_pairs(family="Bonds")` |
| A past week | `get_tremor_pairs(week="YYYY-MM-DD")` — any date in that week |
| What is newly broken | `get_tremor_breaks()` — new breaks of the last four weeks |

Families: Equity regions, US sectors, Credit, Bonds, Commodities, FX and
crypto, Volatility.

## Step 2 — Read each pair honestly
- **Direction first.** `z` positive = moving **closer** than usual
  (`strengthening`); negative = coming **apart** (`weakening`). Say it in those
  words, not as a number alone.
- **How unusual.** |z| ≥ 2 is a break; 3 or more is rare. Rank by |z|, as
  returned.
- **The correlation itself.** `correlation` is weighted to the last few months
  (half-life nine weeks); `correlation_26w` and `correlation_52w` are the plain
  half-year and one-year figures. Quote the weighted one, and the 52-week one
  when the contrast tells the story (e.g. 0.49 now against 0.27 over a year).
- **New or persisting.** A pair in `get_tremor_breaks` is a *new* break (first
  in thirteen weeks the same way); otherwise it has been breaking for a while.
- **A market that holds is an answer too.** If the user asked about gold and
  nothing involving gold is breaking, say that its relationships are holding.

## Step 3 — Output
```
# What broke — week ending {week}

{pairs_breaking} of {pairs_read} pairs breaking.

| Pair | Family | Direction | Correlation | z |
|------|--------|-----------|-------------|---|
| {anchor} – {asset} | {family} | came apart / moved closer | {r} | {z} |

**New this month:** {new breaks, newest first, or "none"}

---
*Antevo Tremor Index, week of {week}. Descriptive, not a forecast, and not
investment advice.*
```

Ten pairs is usually enough; say how many more there are (`more`).

## Guardrails
- **Don't explain causes as fact.** You may offer a plausible reason as a
  reading ("consistent with…"), never as what happened.
- **Don't forecast**, and don't say a relationship "will" return to normal.
- **No price levels** — the connector returns none; don't add any.
- **No personal advice** ("sell your gold") — this is about markets, not the
  user's holdings.
