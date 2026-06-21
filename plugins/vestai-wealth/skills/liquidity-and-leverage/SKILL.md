---
name: liquidity-and-leverage
description: >-
  Assess a VestAI wealth household's liquidity and leverage — how fast it can raise
  cash and how much covenant headroom it has. Use when the user asks "can I raise
  cash / how liquid am I", "could I meet a capital call or margin call", "how
  levered am I", "what's my loan-to-value", "covenant headroom", "how much can I
  borrow against the book", or "what's my interest cost". Produces a liquidity
  ladder (raisable in days / weeks–a quarter / months+), a leverage summary
  (facilities, weighted rate, utilisation), and covenant headroom with distance to
  any margin-call / DSCR / ICR trigger. Orchestrates the VestAI MCP connector
  (portfolio.credit, portfolio.core, portfolio.real_assets). Read-only.
compatibility: >-
  Requires the VestAI MCP connector. If the VestAI tools are not available, tell
  the user to connect VestAI in their assistant's connector settings, then stop.
---

# VestAI — Liquidity & leverage

Answer the two questions that decide whether a shock is survivable: **how fast can
this household raise cash, and how much room is left before a facility bites?**

## Before you start
- **Connector check.** No VestAI tools → ask the user to connect, then stop.
- **Household.** Resolve `household_id` (ask if more than one).
- **Read-only.** Any drawdown/repayment/posting idea is a proposal to confirm in VestAI.

## Step 1 — Gather
| Dimension | Tool(s) |
|-----------|---------|
| Liquid assets, cash, AUM | `get_household_aum`, `get_portfolio_summary`, `get_portfolio_positions` |
| Illiquid real assets | `list_real_assets`, `get_real_asset_economics` |
| Facilities: balance, limit, rate, maturity, covenants, collateral | `list_facilities`, `get_facility` (per facility) |

## Step 2 — Analyse
- **Liquidity ladder.** Bucket assets by how fast they convert: *within days* (cash + listed securities), *weeks–a quarter* (marketable but slower), *months+ / illiquid* (real estate, vessels, collections). Give the % and amount in each.
- **The binding number.** What share can be raised inside a week without a forced sale at a discount? That's the real liquidity figure.
- **Leverage.** Total drawn, weighted interest cost, utilisation (drawn ÷ limit), maturity wall (anything refinancing soon).
- **Covenant headroom.** Per facility: current LTV vs **margin-call LTV**, plus DSCR/ICR vs their floors and any cure period. Express as *distance to trigger* (e.g. "LTV 52% vs 60% call = 8 points of room; a ~13% book drop closes it").
- **Tie it together.** Cross-reference: would meeting a margin call force a sale of the illiquid book? That's the squeeze.

## Step 3 — Output
```
# Liquidity & leverage — {household} · {as-of}

**Read.** {raisable-in-a-week figure} liquid; {tightest covenant} is the constraint.

## Liquidity ladder
- Within days: {amount} ({%})
- Weeks–a quarter: {amount} ({%})
- Months+ / illiquid: {amount} ({%})

## Leverage
- Drawn {total} across {n} facilities · weighted rate {…} · utilisation {…}
- Maturity wall: {nearest refinancings or "none < 12m"}

## Covenant headroom
- {facility}: LTV {x}% vs call {y}% → {distance}; DSCR/ICR {…}

## What I'd watch / consider
1. {tied to the tightest constraint}
2. …

---
*Read-only from your VestAI data as of {dates}. Informational only — not investment,
tax, or legal advice. Any facility action is yours to confirm in VestAI.*
```

## Guardrails
- Distinguish *liquid* from *marketable-but-slow* — don't count trophy assets as cash.
- Covenant maths: show the distance-to-trigger, not just the current ratio.
- Cite with dates; empty/stale → say so. Recommendations, never execution.
