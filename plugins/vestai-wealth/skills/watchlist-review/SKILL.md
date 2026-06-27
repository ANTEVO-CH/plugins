---
name: watchlist-review
description: >-
  Review a VestAI wealth household's tracked instruments (their watchlist). Use
  when the user asks "what's on my watchlist", "what am I tracking", "anything
  moving on my watchlist", "which of my watched names has a buy/sell signal", or
  wants a read on the instruments they follow. Orchestrates the VestAI MCP
  connector's wealth.watchlist tool (price, momentum, signal, volatility per
  instrument) and can hand off to security-analysis for a deep dive. Read-only.
compatibility: >-
  Requires the VestAI MCP connector (wealth.watchlist). If the tools are not
  available, tell the user to connect VestAI, then stop.
---

# VestAI — Watchlist review

Turn the tracked-instruments list into a quick "what deserves attention" read,
not a raw dump.

## Before you start
- **Connector check.** No `wealth.watchlist` tool → ask the user to connect VestAI, then stop.
- **Household.** Resolve a `household_id` (ask if more than one).

## Step 1 — Gather
- `list_watchlist(household_id)` — the tracked instruments with price, 1D/1W/1M/YTD moves, signal (strong-buy…strong-sell), regime, and volatility chips, grouped by asset type.

## Step 2 — Analyse
- **Movers.** Biggest 1D / YTD moves.
- **Signals.** Strong-buy / strong-sell flags; anything that flipped.
- **Regime / volatility.** Names in a stress or elevated-vol regime.
- **So-what.** One line each on what's worth a closer look.

## Step 3 — Output
```
# Watchlist — {household} · {as-of}

**Worth attention.** {1–2 lines: the names that moved or signalled.}

## By asset type
- {ticker}: {price} · {1D/YTD} · signal {…} · vol {…}

## Take a closer look
- {ticker} — {why}; offer: "want the full security read?" → security-analysis
```

## Guardrails
- Empty watchlist is data ("nothing tracked yet — add instruments on the web"), not a gap to fill.
- Signals are computed from technical indicators — **not investment advice**; say so.
- Read-only: this skill doesn't add or remove watchlist items.
