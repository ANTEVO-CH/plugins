# Antevo — plugins & MCP connectors

Antevo's MCP connectors and Claude plugins, in one marketplace.

| Plugin | What it is | Account |
|---|---|---|
| **`antevo-wealth`** | Your portfolios, net worth, real assets, liabilities, risk, markets, geopolitics and daily brief — plus ten private-banker skills. | Antevo Wealth account |
| **`antevo-executive`** | The Antevo Executive Brief — editorial market and world intelligence, today and back through the dated archive. | **None — public** |

MCP is an open standard, so these work with **any MCP client** (Claude, Cursor,
VS Code/Copilot, Goose, and others). This repo packages them as one-install
Claude plugins that wire up the connector *and* the skills in a single step.

> You need an [Antevo Wealth](https://antevo.ch/wealth) account to see your own
> data. The universal market surfaces (markets brief, executive brief, signals,
> geopolitics) work on a free account; the personal surfaces (net worth, portfolio,
> real assets, liabilities, family, documents) show your household once you connect.

## Use with any MCP client

Point your client at the remote Antevo Wealth MCP servers — they advertise
OAuth 2.1, so the client walks you through sign-in (no credentials are shared with
the assistant). Each domain is its own endpoint, e.g.:

```text
https://api.antevo.ch/mcp/portfolio/core/sse     # net worth, positions, AUM
https://api.antevo.ch/mcp/intelligence/geo/sse   # geopolitics
https://api.antevo.ch/mcp/markets/equity/sse     # equity fundamentals
```

(See `.mcp.json` for the full list. A single one-connect aggregate endpoint,
`/mcp/wealth/sse`, is rolling out.)

## Install in Claude

```text
# 1. add the marketplace (once)
/plugin marketplace add ANTEVO-CH/plugins

# 2. install what you need
/plugin install antevo-executive@antevo    # public — nothing to sign in to
/plugin install antevo-wealth@antevo       # your account — OAuth on first use
```

Works in Claude Code, Claude.ai (web) and Claude Desktop.

### Try it without an account

`antevo-executive` needs no sign-in — add it and ask:

```text
https://api.antevo.ch/mcp/executive/sse
```

> *"What's happening in the markets?"* · *"What did the brief say on 9 August?"* ·
> *"How did the energy story develop?"*

## What's inside

| Component | What it is |
|-----------|------------|
| **MCP connector** (`.mcp.json`) | The Antevo Wealth MCP servers (remote SSE, OAuth 2.1, on `api.antevo.ch`) — portfolio & net worth (cash-inclusive AUM), risk, credit/leverage, real assets, markets & daily brief, **equity & technical analysis**, **geopolitics**, **watchlist**, **goals**, family and documents. Currently one server per domain (multi-server); a single `/mcp/wealth/sse` aggregate is on the way. |
| **Skill: `daily-brief`** | The morning note — what matters today, what needs you: brief, alerts, open breaches, drift and the upcoming calendar in one read. |
| **Skill: `wealth-portfolio-review`** | Banker-grade review → net worth, allocation/concentration, risk & drift, leverage, real-asset yield, market backdrop → a dated memo. |
| **Skill: `portfolio-stress-radar`** | "Where could I get hurt?" — traces a shock across concentration → risk → leverage/covenants → liquidity into a consequence, with pre-emptions. |
| **Skill: `concentration-and-drift`** | Concentration map (name/class/currency/region) + drift vs target + ranked trim/rebalance candidates. |
| **Skill: `liquidity-and-leverage`** | Liquidity ladder (raisable in days / weeks / months+), leverage, and covenant headroom with distance to margin-call / DSCR / ICR triggers. |
| **Skill: `market-signals-period`** | Time-series read over a look-back window — what trended, what's new, how correlations shifted. |
| **Skill: `security-analysis`** | One instrument, both lenses — fundamentals (valuation, growth, margins, peers) + technicals (signal consensus, backtest). |
| **Skill: `geopolitical-risk`** | World risk read tied to your exposure — conflict, chokepoints, sanctions, cyber, narrative; cross-references where your capital sits. |
| **Skill: `watchlist-review`** | Your tracked instruments — movers, buy/sell signals, regime & volatility; hands off to `security-analysis`. |
| **Skill: `goals-review`** | Funding progress vs targets, the gap to plan, what's on track vs at risk. |

### `antevo-executive` — public, no account

| Component | What it is |
|-----------|------------|
| **MCP connector** | `https://api.antevo.ch/mcp/executive/sse` — the published Executive Brief, its dated archive, market snapshot and world events. Read-only, rate-limited, no personal data reachable. |
| **Skill: `world-brief`** | What's happening in markets and the world — the editorial read, grounded in the numbers. |
| **Skill: `story-timeline`** | How a story developed — reconstructs the arc from the dated archive, including where the view shifted. |

Invoke a skill explicitly with `/antevo-wealth:<skill>` (e.g.
`/antevo-wealth:portfolio-stress-radar`), or just ask in plain language — the skills
auto-trigger on the questions below.

## Critical questions you can ask

Once connected, fire these directly — each routes to a skill and drills straight
into the detail:

**Start the day**
- "What's my brief?" · "Anything I should know today?" · "What needs my attention?"

**Where am I exposed**
- "Where could I get hurt this week?" · "Stress my book against an oil shock / equity −20% / rates +50bp."
- "Am I over-leveraged? What's my margin-call risk?"

**Concentration & allocation**
- "Am I too concentrated? What's my single-name risk?"
- "Have I drifted from my target allocation — what should I trim?"

**Liquidity & leverage**
- "How fast could I raise cash? Could I meet a capital call without forced sales?"
- "What's my blended LTV and covenant headroom?"

**Markets over a period**
- "Summarise the signals over the last 3 months." · "How have correlations shifted this quarter?"
- "What's been trending — and what rolled off?"

**Analyse a security**
- "Analyse NVDA." · "Is Apple expensive?" · "Technicals on the S&P 500."

**Geopolitics**
- "What are the geopolitical risks right now?" · "How exposed am I to the Strait of Hormuz / China?"

**Watchlist & goals**
- "What's on my watchlist — anything signalling?" · "How am I tracking against my goals?"

**The whole picture**
- "Review my portfolio." · "How am I doing?" · "Give me a net-worth breakdown."

> Period analytics that span the *household over time* (net-worth trajectory, risk
> radar across 6 months, drawdown/VaR history) need connector history tools that
> aren't exposed yet — on the roadmap. Market-signal trends over a window work today.

Read-only: the connector surfaces recommendations and only makes a change after you
approve a plan. AI outputs are informational support only — not investment, tax, or
legal advice.

## Structure

```
.claude-plugin/marketplace.json              # the catalog
plugins/antevo-executive/
├── .claude-plugin/plugin.json
├── .mcp.json                                # public Executive connector (no auth)
└── skills/
    ├── world-brief/SKILL.md
    └── story-timeline/SKILL.md
plugins/antevo-wealth/
├── .claude-plugin/plugin.json               # plugin manifest
├── .mcp.json                                # remote Antevo Wealth MCP connector (multi-server)
└── skills/
    ├── daily-brief/SKILL.md
    ├── wealth-portfolio-review/SKILL.md
    ├── portfolio-stress-radar/SKILL.md
    ├── concentration-and-drift/SKILL.md
    ├── liquidity-and-leverage/SKILL.md
    ├── market-signals-period/SKILL.md
    ├── security-analysis/SKILL.md
    ├── geopolitical-risk/SKILL.md
    ├── watchlist-review/SKILL.md
    └── goals-review/SKILL.md
```

## Links
- Connectors: https://antevo.ch/mcp · Wealth: https://antevo.ch/wealth · Executive: https://antevo.ch/executive
- Privacy: https://antevo.ch/policies/privacy-policy · Terms: https://antevo.ch/policies/terms-of-use
- Contact: contact@antevo.ch

---
*This repo contains only plugin manifests, skills, and pointers to the hosted
Antevo MCP endpoints — no backend code.*
