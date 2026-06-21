---
name: concentration-and-drift
description: >-
  Diagnose concentration and allocation drift for a VestAI wealth household and
  surface what to rebalance. Use when the user asks "am I too concentrated",
  "single-stock / single-name risk", "have I drifted from my target allocation",
  "is my allocation off", "what should I trim or rebalance", or "how diversified am
  I". Produces a concentration map (by position, asset class, currency, region), the
  drift vs target with any open breaches, and ranked trim/add candidates with the
  reasoning. Orchestrates the VestAI MCP connector (portfolio.core, portfolio.risk).
  Read-only — proposes, never trades.
compatibility: >-
  Requires the VestAI MCP connector. If the VestAI tools are not available, tell
  the user to connect VestAI in their assistant's connector settings, then stop.
---

# VestAI — Concentration & drift

Turn the positions and the risk dashboard into a clear read on *how lopsided the
book is* and *how far it has wandered from plan* — with specific, ranked moves.

## Before you start
- **Connector check.** No VestAI tools → ask the user to connect, then stop.
- **Household.** Resolve `household_id` (ask if more than one).
- **Read-only.** Trim/add ideas are proposals the user confirms in VestAI.

## Step 1 — Gather
| Dimension | Tool(s) |
|-----------|---------|
| Positions & weights | `get_portfolio_positions`, `get_portfolio_summary` |
| Concentration (HHI, top-weight), allocation | `get_risk_dashboard` |
| Drift vs target, breaches | `get_portfolio_drift` (per portfolio) |

## Step 2 — Analyse
- **Concentration map.** Top-position weight; top-5 share; HHI. Repeat the lens by **asset class, currency, and region** — a book can look diversified by name yet be 70% one currency or one sector.
- **Thresholds.** Flag a single holding > ~25–30% of liquid assets, or a top-5 > ~60%. State the threshold you used.
- **Drift.** Per portfolio, distance from target by sleeve; note direction (over/under) and any open compliance breach.
- **So-what.** Connect concentration to risk — the over-weight name is usually also the biggest VaR and drawdown contributor.

## Step 3 — Recommend (ranked)
Give 2–5 concrete moves, each tied to a finding: which sleeve/name, rough size to bring it back toward target/threshold, and the trade-off (tax, conviction, liquidity). Frame as candidates, not instructions.

## Output
```
# Concentration & drift — {household} · {as-of}

**Read.** {one line: most concentrated axis + biggest drift.}

## Concentration
- Top position {name} {%}; top-5 {%}; HHI {…}
- By class {…} · by currency {…} · by region {…}
- Flags: {threshold breaches or "within bounds"}

## Drift vs target
- {portfolio}: {sleeve} {+/−x%} vs target; breaches {…/none}

## What I'd rebalance  (candidates)
1. {name/sleeve} — trim/add ~{size} → {effect}; trade-off {…}
2. …

---
*Read-only from your VestAI data as of {dates}. Informational only — not investment
advice. Any change is yours to confirm in VestAI.*
```

## Guardrails
- State your thresholds explicitly; don't flag without a yardstick.
- Cite every figure with its date; empty book = say so, don't invent.
- Recommendations, never execution.
