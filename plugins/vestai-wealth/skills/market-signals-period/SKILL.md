---
name: market-signals-period
description: >-
  Summarise VestAI market signals and alternative-index moves over a time window
  and pull out the insights. Use when the user asks for analytics "over the last N
  weeks/months", "what's trended / changed lately", "summarise the signals across
  [period]", "what's been moving", "how have correlations shifted", or "give me a
  read on the period". Pulls recent signals and results over a chosen look-back
  (days), the correlation regime, and per-instrument history, then writes a period
  narrative: what trended, what's new, what rolled off, and which correlations
  changed. Orchestrates the VestAI MCP connector (markets.alt_indices). Read-only.
compatibility: >-
  Requires the VestAI MCP connector. If the VestAI tools are not available, tell
  the user to connect VestAI in their assistant's connector settings, then stop.
---

# VestAI — Signals over a period

This is the connector's genuine *time-series* skill. Turn a look-back window of
signals, results and correlations into a narrative of **what changed and what it
means** — not a table dump.

## Scope & honesty
- **What's backable now:** the **alt-index / market-signal** stream supports a
  look-back window (days, up to ~365) plus per-instrument history and a correlation
  window. That's the real "over a period" data today.
- **What's not yet:** a *portfolio/household* time series (net-worth trajectory,
  risk-radar across 6 months, drawdown/VaR history) is **not** exposed as a
  connector tool yet. If the user asks for those, say so plainly and offer the
  signals-period read instead — don't fabricate a portfolio history.

## Before you start
- **Connector check.** No VestAI tools → ask the user to connect, then stop.
- **Window.** Pick the look-back from the user's ask ("last 3 months" → ~90 days; "last quarter" → ~90; "this month" → ~30). Default ~90 days if unspecified; cap at 365. State the window you used.

## Step 1 — Gather
| Dimension | Tool(s) |
|-----------|---------|
| Signals over the window | `get_signals_recent(days_back=…)` |
| Results / index moves over the window | `get_recent_results(days_back=…)` |
| Correlation regime | `get_correlations(window=…)` |
| Per-instrument trajectory | the per-instrument history tool, for names the user names |

Call `list_capabilities` first if unsure which alt-index tools/params are live.

## Step 2 — Analyse
- **What trended.** The strongest sustained moves over the window — direction, magnitude, and whether they're building or fading.
- **What's new vs rolled off.** Signals that appeared this period vs ones that decayed out — change is the insight.
- **Correlation shifts.** Pairs/clusters whose correlation rose or broke down — a regime tell (e.g. risk-on → everything correlates).
- **So-what.** For each, one line on why it matters to an investor; if the user named holdings/themes, tie the period moves to those.

## Step 3 — Output
```
# Signals — last {window} · as of {date}

**The period in a line.** {dominant trend + the regime read.}

## What trended
- {signal/index} {direction, magnitude} — {building/fading}; {why it matters}

## New this period / rolled off
- New: {…}   ·   Faded: {…}

## Correlation regime
- {pairs/clusters that shifted}; {what it implies}

## Watch into next period
- {1–3 forward items tied to the above}

---
*Read-only over the {window} look-back from your VestAI data. Signals computed from
market data — informational only, not investment advice.*
```

## Guardrails
- Always state the look-back window and the as-of date.
- Distinguish *signal* from *portfolio* history — never present alt-index trends as the household's own performance.
- Cite with dates; an empty window is data ("quiet period"), not a gap to fill.
