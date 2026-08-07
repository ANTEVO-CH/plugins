---
name: security-analysis
description: >-
  Analyse a single security (equity, index, FX, crypto, commodity) for a Antevo Wealth
  user — fundamentals and technicals in one read. Use whenever the user asks to
  "analyse [ticker]", "is [name] expensive / cheap", "what are the technicals on
  X", "valuation / P/E / margins / growth of X", "RSI / trend / momentum / signal
  on X", "should I look at [stock]", or wants a considered read on one instrument.
  Orchestrates the Antevo Wealth MCP connector — markets.equity (fundamentals) and
  markets.technical (signal consensus + backtest). Read-only.
compatibility: >-
  Requires the Antevo Wealth MCP connector (markets.equity, markets.technical). If the
  tools are not available, tell the user to connect Antevo Wealth, then stop.
---

# Antevo Wealth — Security analysis

One instrument, both lenses: **what the business is worth** (fundamentals) and
**what the tape is saying** (technicals) → a single, considered read. Cheaper and
faster than a single tool call because you synthesise the two.

## Before you start
- **Connector check.** No `markets.equity` / `markets.technical` tools → ask the user to connect Antevo Wealth, then stop.
- **Resolve the instrument.** Accept ticker / ISIN / name. Equity tools cover equities; technical covers equity, index, FX, crypto, commodity.

## Step 1 — Gather
| Lens | Tool |
|------|------|
| Fundamentals: valuation (P/E, EV/EBITDA, FCF yield, ROIC), revenue growth, margins, peers | `get_equity_fundamentals(identifier, frequency, year_history, peers)` |
| Technicals: multi-indicator signal consensus, regime; optional backtest (Sharpe, drawdown, hit-rate) | `run_technical_analysis(identifier, analysis_mode, frequency, history_days)` |

Use both for an equity; for a non-equity (index/FX/crypto/commodity), use technical only and say so. The fundamentals tool returns FREE structured data — *you* write the narrative.

## Step 2 — Analyse
- **Valuation in context.** P/E and EV/EBITDA vs the peer set, not in isolation. Is the premium/discount earned by growth and returns (ROIC, FCF)?
- **Quality.** Margins, growth durability, balance sheet.
- **Technical read.** How many indicators agree (consensus), the regime (trend/range/vol), key levels; if backtested, the Sharpe / max drawdown / hit-rate.
- **Where they agree or diverge.** "Cheap and improving" vs "rich but strong trend" vs "weak on both" — the synthesis is the value.

## Step 3 — Write the memo
```
# {Name} ({ticker}) — security read · {as-of}

**Verdict.** {one line: quality + valuation + tape, e.g. "Quality compounder, richly priced; trend intact."}

## Fundamentals
- Valuation: P/E {…}, EV/EBITDA {…}, FCF yield {…} vs peers {…}
- Quality/growth: revenue {…}, margins {…}, ROIC {…}

## Technicals
- Consensus: {bullish/bearish, N of M agree}; regime {…}; key levels {…}
- {backtest line if run}

## Bull / bear in two lines
- Bull: {…}   ·   Bear: {…}

---
*Read-only analysis from your Antevo Wealth data as of {date}. Descriptive, not
investment advice.*
```

## Guardrails
- Cite figures from the tools with their dates; if a tool returns empty (e.g. no FMP coverage), say so.
- The free fundamentals tool is data-only — never imply Antevo Wealth is recommending the security.
- Not advice. You inform the client's judgement; you don't replace it.
