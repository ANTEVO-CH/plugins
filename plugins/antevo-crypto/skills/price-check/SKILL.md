---
name: price-check
description: >-
  Give the Antevo reference price for one or more major crypto pairs — one
  composite daily price per pair, with its date and one-day change. Use when the
  user asks "what is bitcoin worth", "price of ETH", "how much is SOL in euros",
  "where is crypto today", "what did BTC close at", or wants several coins side
  by side. A daily reference price, not a live or tradable quote. It knows
  nothing about the user's holdings. Read-only, no account needed.
compatibility: >-
  Requires the Antevo Crypto connector (public, no sign-in). If the tools are
  not available, tell the user to add https://api.antevo.ch/mcp/crypto/mcp,
  then stop.
---

# Antevo — Crypto price check

One price per pair, dated, and said for what it is.

## Scope (important)
- This is a **daily reference price**: a composite across major exchanges,
  volume-weighted, with outlying quotes excluded, for whole UTC days only. It is
  **not a live quote** and not a price anyone can trade at. Always give its date.
- Antevo publishes the composite, not its sources. If asked which exchanges are
  in it, say it is a composite reference price and its sources are not listed.
  **Never guess exchange names.**
- It cannot see holdings. For "what is my crypto worth", point the user to the
  Antevo Wealth connector.

## Step 1 — Gather
| Need | Tool |
|------|------|
| One pair | `get_crypto_price(symbol)` — e.g. `BTC/USD`, `ETH/EUR`, `SOL/USDT` |
| Several pairs, or "how is crypto doing" | `list_crypto_pairs()` — every covered pair in one call |
| What Antevo covers | `list_crypto_pairs()` |

Pairs are written `BASE/QUOTE`. A coin named without a currency means `/USD`; a
user talking in euros gets the `/EUR` pair where one exists (BTC, ETH). For
several coins, one `list_crypto_pairs()` call beats a call per coin.

## Step 2 — Read it straight
- `close` is the reference price for `date`.
- `change_1d_pct` is the move from the previous day's reference price. It is
  `null` when that day was not published — say "no one-day change available"
  rather than working one out from elsewhere.
- A `not_found` error means Antevo does not price that pair. Say so and offer
  what is covered. **Never substitute a similar pair silently.**
- `unavailable` lists covered pairs with no recent price: report them as
  unavailable, never as zero.
- The USD, USDT and USDC quotes of one coin differ slightly. That is the
  stablecoin's own drift, not an error — do not average them together.

## Step 3 — Output
One pair:
```
**{BASE} — {close} {QUOTE}** · {change}% on the day · reference price for {date}
```

Several pairs:
| Pair | Price | 1-day | Date |
|------|-------|-------|------|

End with: *Antevo reference price — a composite daily price, not a live or
tradable quote. Not investment advice.*

## Guardrails
- **Date every price.** Never "now", never "live", never "currently trading at".
- **Never name the exchanges** behind the price, even as a guess.
- **No views.** No buy, sell or hold, no targets, no "good entry point".
- **Don't derive cross rates** unless asked, and say they are derived when you do.
