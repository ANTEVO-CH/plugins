---
name: crypto-performance
description: >-
  How a major crypto pair has moved over a period, from Antevo's daily reference
  prices — the return, the range, the worst drawdown, and how pairs compare. Use
  when the user asks "how has bitcoin done this year", "ETH over the last
  quarter", "what was the drawdown", "compare BTC and SOL since June", "what's
  the range", or "when did it peak". Up to 365 days of daily history. Read-only,
  no account needed.
compatibility: >-
  Requires the Antevo Crypto connector (public, no sign-in). If the tools are
  not available, tell the user to add https://api.antevo.ch/mcp/crypto/mcp,
  then stop.
---

# Antevo — Crypto performance

What a pair actually did over a window, measured on one consistent daily price.

## Scope (important)
- Built from the **Antevo reference price**: one composite daily bar per pair,
  whole UTC days only. It is not intraday data, so it cannot tell you what
  happened within a day beyond that day's high and low.
- **Up to 365 days.** For a longer window, say the connector serves a year and
  answer for the year.
- It cannot see holdings or cost bases, so it measures the market, not the
  user's return.

## Step 1 — Gather
| Need | Tool |
|------|------|
| A pair over a window | `get_crypto_price_history(symbol, days)` — `days` 1..365, default 90 |
| Pairs to compare | one `get_crypto_price_history` per pair, same `days` |
| Is the pair covered | `list_crypto_pairs()` |

Translate the window into days: "this year" is the days since 1 January,
"last quarter" 90, "since June" the days since 1 June. `bars` come back oldest
first.

## Step 2 — Compute, from the bars only
- **Return:** last `close` ÷ first `close` − 1, over the dates actually returned.
- **Range:** the highest and lowest `close`, each with its date.
- **Worst drawdown:** the largest fall from a running peak `close` to a later
  `close`, with both dates.
- **Gaps:** compare the first and last date with the number of bars. If days are
  missing, say how many — a return across a gap is still right, a "daily
  volatility" across one is not.
- **Comparisons** use the same start date for every pair. Compare percentage
  moves, never price levels.

## Step 3 — Output
```
# {BASE}/{QUOTE} — {first date} to {last date}

**{return}%** over the period · from {first close} to {last close} {QUOTE}
Range: {low} ({date}) – {high} ({date}) · Worst drawdown: {dd}% ({peak date} → {trough date})
```
For comparisons, a table: Pair | Return | Worst drawdown | High | Low.

End with: *From Antevo daily reference prices, whole UTC days. Past moves are not
a forecast. Not investment advice.*

## Guardrails
- **Only what the bars show.** No annualising a 30-day return, no extrapolation.
- **State the exact dates used**, not just "this year".
- **No forecasts and no views** on what comes next.
- Never name or guess the exchanges behind the price.
