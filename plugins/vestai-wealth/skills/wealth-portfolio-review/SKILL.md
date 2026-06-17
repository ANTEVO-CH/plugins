---
name: wealth-portfolio-review
description: >-
  Produce a private-banker-grade portfolio review for a VestAI wealth client by
  orchestrating the VestAI MCP connector. Use this whenever the user asks for a
  portfolio review, a wealth check-up, "how am I doing", a net-worth breakdown,
  a risk / concentration / drift review, leverage or liquidity analysis, or a
  quarterly / periodic review of their holdings — even if they don't say the word
  "review". Prefer this skill over answering from a single tool call when the user
  wants a considered, multi-factor read on their wealth. Requires the VestAI MCP
  connector to be connected (tools under markets.core, portfolio.core,
  portfolio.risk, portfolio.credit, portfolio.real_assets). Read-only: it
  surfaces findings and recommendations, never executes trades or changes.
compatibility: >-
  Requires the VestAI MCP connector. If the VestAI tools are not available, tell
  the user to connect VestAI in their assistant's connector settings, then stop.
---

# VestAI — Portfolio Review

Turn the raw VestAI tools into one considered, banker-grade review of a household's
wealth. The value you add over a single tool call is **synthesis**: tying net
worth, allocation, risk, leverage, real-asset yield and the market backdrop into a
clear picture of *what changed, what's at risk, and what to consider* — in the
client's reporting currency, with every figure dated.

## Before you start

- **Connector check.** If the VestAI tools aren't present, say so and ask the user
  to connect VestAI, then stop — don't fabricate numbers.
- **Identify the household.** If the user gave a household, use it. Otherwise call
  the households listing (or `get_net_worth` with their default) — if there's more
  than one, ask which before proceeding. You need a `household_id` for the scoped
  tools.
- **Read-only.** This skill never calls a write/delete tool. You propose; the user
  acts. Make that explicit in the memo.

## Step 1 — Gather (call tools, don't guess)

Pull the inputs, then reason. Tools are tolerant of an empty book — an empty result
is data, not an error (a new account simply has nothing yet); say so rather than
inventing figures. Where a tool needs a `portfolio_id`, get the list first from the
portfolio summary / positions.

| Dimension | Tool(s) |
|-----------|---------|
| Net worth (assets − liabilities, FX-converted) | `get_net_worth` |
| Holdings & allocation | `get_portfolio_summary`, `get_portfolio_positions` |
| Accounts / custody | `list_accounts` |
| Risk (vol, VaR, concentration) | `get_risk_dashboard`, `get_portfolio_risk` (per portfolio) |
| Drift vs targets / breaches | `get_portfolio_drift` (per portfolio) |
| Leverage | `list_facilities` (balances, rates, utilisation, covenants, collateral) |
| Real-asset yield | `list_real_assets`, `get_real_asset_economics` |
| Market backdrop | `get_market_brief` |

Call only what's relevant to the user's ask — a "net worth check" doesn't need the
full risk pass — but for a general "review", cover all rows. Note the `as_of` /
valuation dates the tools return; surface the freshest and flag anything stale.

## Step 2 — Analyse (the methodology)

Think like a private banker preparing for a client meeting. For each dimension,
look for the *signal*, not just the number:

- **Net-worth bridge.** Total assets (securities + real assets) vs total
  liabilities = net worth. Note the split and the currency mix; call out if a
  large share sits in one currency or one asset.
- **Allocation.** Weight by asset class and region. Is it deliberate or drifted?
- **Concentration.** Top-position weight and the Herfindahl/HHI from the risk
  tool. A single holding > ~25–30% of liquid assets is worth flagging.
- **Risk.** Volatility, VaR/CVaR, max drawdown, Sharpe — in plain language
  ("roughly a 1-in-20 day could cost ~X"). Compare to what a household of this
  profile would expect.
- **Drift & breaches.** Any portfolio off its targets, any open compliance breach.
- **Leverage & covenants.** Facility utilisation (outstanding ÷ limit), weighted
  interest cost, maturities, and **covenant headroom** (LTV vs margin-call LTV,
  DSCR/ICR). Rising rates + high utilisation + tight covenants = the thing to flag.
- **Real-asset yield.** Net cashflow and net yield % per asset; loss-making or
  thin-yield assets (e.g. carrying cost > charter income).
- **Liquidity.** Liquid (securities + cash) vs illiquid (real assets) — could the
  household meet a capital call or a margin call without forced sales?
- **Market backdrop.** One or two lines from the market brief that actually bear on
  *this* book (not generic macro).

## Step 3 — Write the memo

Keep it tight, specific, and dated. Lead with the answer. Use this structure:

```
# Portfolio review — {household name} · {as-of date}

**The picture.** {2–3 sentences: net worth, the one or two things that matter most.}

## Net worth
- Net worth: {amount, reporting ccy}  (assets {X} − liabilities {Y})
- Assets: securities {…}, real assets {…}; by currency {…}
- Liabilities: {total}, across {n} facilities

## Allocation & concentration
- {asset-class weights}; top position {name} at {%}; HHI {…}
- {one line on whether it's deliberate or drifted}

## Risk
- Volatility {…}, VaR(95) {…}, max drawdown {…}; {plain-language read}
- Drift / breaches: {portfolio} {status}; {open breaches or "none"}

## Leverage & liquidity
- Facilities: {total} drawn, {weighted rate}, utilisation {…}; covenant headroom {…}
- Liquidity: {liquid vs illiquid}; {can/cannot cover a shock without forced sales}

## Real assets
- {class: net yield %, cashflow}; flag {underperformers}

## What I'd look at  (recommendations, not instructions)
1. {specific, tied to a finding above}
2. …

---
*Read-only review from your VestAI data as of {dates}. Informational only — not
investment, tax, or legal advice. Any change is yours to make and confirm.*
```

## Guardrails

- **Cite, don't invent.** Every figure comes from a tool result with its date. If
  a tool returned empty or stale, say so — never fill a gap with a plausible
  number.
- **Recommendations, never execution.** Frame actions as "consider / I'd look at",
  and remind the user that VestAI confirms every change before it happens.
- **Not advice.** Close with the informational-only line. You support the client's
  judgement; you don't replace it.
- **Currency discipline.** Report in the household's reporting currency; when you
  mix native-currency figures (e.g. real assets), label them.
