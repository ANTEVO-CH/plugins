---
name: macro-history
description: >-
  Answer questions about long-run economic history from Antevo's reference
  series — consumer prices, policy and market interest rates, house prices,
  industrial production, equity indices and commodities, for around 180
  countries, some running back to 1920. Use when the user asks "what was
  inflation in X", "how have rates moved since Y", "show me house prices in Z",
  "what did CPI do in the seventies", "compare inflation in France and Italy",
  or any question whose answer is a dated series rather than today's news. These
  are QUARTERLY published levels and they LAG — this is the wrong skill for
  today's market move or a live quote; use decode or world-brief for that.
  Read-only, no account.
compatibility: >-
  Requires the Antevo Executive connector (public, no sign-in). If the tools are
  not available, tell the user to add https://api.antevo.ch/mcp/executive/mcp,
  then stop.
---

# Antevo — Macro history

Reference economics: the kind of question whose answer does not change once it
is published. Around 80,000 series, so they cannot be listed — you search for
the ticker, then fetch it.

## Scope (important)
These are **published quarterly levels**. The newest observation is a quarter
end and is never today. If the user wants a live price, a today move, or this
morning's read, this is the wrong skill — hand off to **decode** or
**world-brief**. Say so rather than serving a stale number as current.

## Step 1 — Find the series
| Need | Tool |
|------|------|
| Find a ticker | `search_macro_indicators(query, country?, limit?)` |
| Fetch one series | `get_macro_series(ticker, since?, until?, limit?)` |

`query` is free text over the series name, the ticker and the country —
`"CPI"`, `"house prices"`, `"industrial production"`, `"policy rate"`.

`country` takes **either form**: a name (`"Switzerland"`) or an ISO-3 code
(`"CHE"`). Both work; use whichever the user said.

Search first, always. Do not guess a ticker — the naming is not uniform
(`"CHE CPI"`, `"CHE IR10Y"`, `"CHE Interest Rate 10-Year"` are all real, and
they are not interchangeable).

## Step 2 — Read the coverage before you read the numbers
Every hit carries `covers.from` and `covers.to`. **`covers.to` is that series'
own newest quarter — it is not today and it differs between series.** Two
countries' CPI can end three quarters apart.

Before comparing two series, check both spans. If they do not overlap where the
user's question sits, say that instead of comparing them anyway.

## Step 3 — Fetch and answer
`get_macro_series(ticker)` returns newest first with `as_of` on the response.
`since` and `until` are **YYYY-MM-DD** and narrow the window.

A bound that is not a date is refused, by design — it will not quietly return
the whole series in place of the window you asked for. If you get that refusal,
reformat the date; do not drop the bound and present the full history as though
it were the requested range.

## Step 4 — Say what the numbers are
Four rules, and they are the reason this data is worth quoting:

- **Date every figure.** "Swiss CPI was 105.4 at 2025-12-31", never "Swiss CPI
  is 105.4". The lag is real and the user cannot see it.
- **These are levels, as published.** Nothing is rebased, interpolated or
  seasonally adjusted. An index level is not a percentage — if the user wants
  an inflation *rate*, compute it from two levels and show your working.
- **Index levels are only comparable within one series.** Two countries' CPI
  indices sit on different bases; comparing the levels is meaningless. Compare
  *changes*.
- **Never fill a gap.** If a quarter is missing, it is missing.

## Worked shape
> **"What has Swiss inflation done since 2020?"**
>
> `search_macro_indicators(query="CPI", country="Switzerland")` → `CHE CPI`,
> covering 1955-03-31 to 2025-12-31.
> `get_macro_series(ticker="CHE CPI", since="2020-01-01")` → 24 quarters.
>
> Then: the index moved 99.1 (2020-03-31) to 105.4 (2025-12-31) — about 6.4%
> over five and a half years — and say plainly that the series ends at the end
> of 2025, so it does not cover this year.

## Hand-offs
- Today's market move, a live level → **decode**
- What it means for the week ahead → **world-brief**
- Antevo's editorial view on a sector → **desk-read**
