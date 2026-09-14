---
name: technical-read
description: >-
  The technical picture for a major crypto pair on Antevo's reference price —
  moving averages, MACD, RSI, Bollinger bands and ATR, each with its buy, sell or
  neutral vote, and how the votes add up. Use when the user asks "what do the
  technicals say on BTC", "is ETH overbought", "where is SOL against its 200-day",
  "what's the trend", or "RSI on bitcoin". Indicator readings, never a trading
  recommendation. Read-only, no account needed.
compatibility: >-
  Requires the Antevo Crypto connector (public, no sign-in). If the tools are
  not available, tell the user to add https://api.antevo.ch/mcp/crypto/mcp,
  then stop.
---

# Antevo — Technical read

What the indicators say about a pair, and how far that should be taken.

## Scope (important)
- Signals are **computed on the Antevo reference price**: daily bars, so this is
  a daily-timeframe read, not an intraday one.
- **Indicator readings are not advice.** The connector labels its tally
  `BUY`, `SELL`, `STRONG_BUY` and so on. Those are vote counts. **Never pass a
  label on as a recommendation** — translate it: "six of ten indicators lean
  bullish".
- Stablecoin pairs (USDC/USD, USDT/USD, USDC/USDT) are refused on purpose: a peg
  has no trend, and a signal on one is noise.

## Step 1 — Gather
| Need | Tool |
|------|------|
| The technical picture | `get_crypto_technicals(symbol)` |
| Today's price for context | `get_crypto_price(symbol)` |
| How it got here | hand off to **crypto-performance** |

## Step 2 — Read it
The response carries `as_of`, `bars_used`, `missing_days` and `signals`:
- `signals.overall` — the tally: `buy_count`, `sell_count`, `neutral_count`,
  `score`. Lead with the counts, not the label.
- `signals.moving_averages` — price against SMA and EMA at 10, 50 and 200 days.
  Above the 200-day with the 50 above it is a longer uptrend; below both is the
  reverse. Say which, in words.
- `signals.oscillators` — RSI (above 70 is conventionally overbought, below 30
  oversold) and MACD. Give the RSI value.
- `signals.volatility` — Bollinger position and ATR, which is the typical daily
  range in price terms. Useful context, rarely a vote.
- If `missing_days` is above zero, say the series has gaps. The indicators count
  bars, not calendar days.

**Refusals:** `invalid_argument` on a stablecoin pair — explain why and offer the
price instead. `not_found` with "need 200" — there is not yet enough history for
the 200-day measures; say so rather than reading the rest as complete.

## Step 3 — Output
```
# {BASE}/{QUOTE} — technical read, {as_of}

**The tally:** {buy} lean bullish · {sell} lean bearish · {neutral} neutral
**Trend:** {price vs 50- and 200-day, in words}
**Momentum:** RSI {value} — {reading} · MACD {above/below} its signal line
**Volatility:** typical daily range about {ATR} {QUOTE}

---
*Indicator readings on the Antevo daily reference price ({bars_used} days).
Not investment advice and not a trading recommendation.*
```

## Guardrails
- **Never say buy, sell, enter, exit or target.** Describe the readings.
- **Name the timeframe:** daily bars.
- **Don't blend in outside charts** or indicators the connector did not return.
- Never name or guess the exchanges behind the price.
