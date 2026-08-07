---
name: portfolio-stress-radar
description: >-
  Find where a Antevo Wealth household could actually get hurt — and trace it
  across domains. Use whenever the user asks "where could I get hurt", "what's my
  biggest risk", "stress my book/portfolio", "where am I exposed", "what happens
  if markets fall / oil spikes / rates rise", "am I over-leveraged", or "margin-call
  risk". The value is the CHAIN: not a list of metrics, but how a shock in one place
  (concentration, a market move) propagates through risk → leverage/covenants →
  liquidity into a real consequence, then what to do about it. Orchestrates the
  Antevo Wealth MCP connector (portfolio.risk, portfolio.credit, portfolio.core,
  portfolio.real_assets). Read-only — proposes pre-emptions, never executes.
compatibility: >-
  Requires the Antevo Wealth MCP connector. If the Antevo Wealth tools are not available, tell
  the user to connect Antevo Wealth in their assistant's connector settings, then stop.
---

# Antevo Wealth — Stress radar

Most tools answer "what is my volatility?" This skill answers the better question:
**"what could actually hurt me, and how?"** You earn your keep by drawing the
*chain* — the same way a desk thinks — from a trigger to a consequence to a fix.

## Before you start
- **Connector check.** No Antevo Wealth tools present → ask the user to connect Antevo Wealth, then stop. Never fabricate figures.
- **Household.** Resolve a `household_id` (ask if there's more than one). Scoped tools need it.
- **Read-only.** You propose pre-emptions; the user acts and confirms in Antevo Wealth.

## Step 1 — Gather (current-state)
| Link | Tool(s) |
|------|---------|
| Concentration, vol, VaR, drawdown | `get_risk_dashboard`, `get_portfolio_risk` (per portfolio) |
| Drift / open breaches | `get_portfolio_drift` (per portfolio) |
| Leverage, LTV, covenants, collateral | `list_facilities` |
| Book size / liquid vs illiquid | `get_household_aum`, `get_portfolio_summary`, `get_portfolio_positions` |
| Illiquid real assets + yield | `list_real_assets`, `get_real_asset_economics` |

> Period note: full historical stress *replay* over months is not yet exposed as a
> connector tool — work from the current dashboard + covenant math. If the user
> wants a 6-month risk trend, say that period-history tools are coming and offer
> the point-in-time read now.

## Step 2 — Build the chain (the method)
Don't dump metrics. For the top 1–3 exposures, connect the dots:

1. **Trigger** — the largest concentration, the tightest covenant, or the shock the user named (equity −20%, oil/rates up).
2. **Transmission** — which holdings/facilities carry it. Tie the same names through every link (e.g. the top position is *also* the collateral).
3. **Stress impact** — estimate the book move (use VaR/drawdown as the scale; be explicit it's an estimate).
4. **Leverage hinge** — re-check covenant headroom *after* the impact: does the stressed book push LTV past the margin-call line, or DSCR/ICR under its floor? This is usually where point-in-time risk turns into a real event.
5. **Liquidity bite** — could the household meet the resulting call from liquid assets, or only by forced-selling illiquid trophy assets at a discount?
6. **Consequence** — state it in one line, in reporting currency.

Rank chains by severity (a covenant breach under a plausible shock beats a large-but-contained drawdown).

## Step 3 — Write it
```
# Where you could get hurt — {household} · {as-of}

**The one that matters.** {single most important chain, one sentence.}

## {Chain 1 title}
{Trigger} → {transmission} → est. impact {amount/%} → {covenant/liquidity consequence}.
**Pre-empt:** {option A} · {option B} — {effect on the hinge}, est. cost {…}.

## {Chain 2 …}

## Also on the radar
- {contained risks worth noting, one line each}

---
*Read-only stress read from your Antevo Wealth data as of {dates}. Estimates, not a
guaranteed outcome; informational only — not investment advice. Any change is
yours to confirm in Antevo Wealth.*
```

## Guardrails
- **Chain, don't list.** If you're just printing metrics, you've failed the skill.
- **Label estimates.** Stress impacts are modelled approximations — say so.
- **Cite or omit.** Every figure from a tool with its date; empty/stale → say so.
- **Pre-emptions, not orders.** "Consider / I'd look at"; Antevo Wealth confirms every change.
