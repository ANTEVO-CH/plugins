# VestAI — MCP connector & plugin

The **VestAI Wealth** connector exposes your portfolios, net worth, real assets,
liabilities, risk, markets and daily brief over the Model Context Protocol — with
confirmation on every change.

MCP is an open standard, so the connector works with **any MCP client** (Claude,
Cursor, VS Code/Copilot, Goose, and others). This repo additionally packages it as
a **one-install Claude plugin** that wires up the connector *and* the private-banker
skills in a single step.

> You need a [VestAI](https://vestai.ai) account to see your own data. The universal
> market surfaces (markets brief, executive brief, signals) work on a free account;
> the personal surfaces (net worth, portfolio, real assets, liabilities, family,
> documents) show your household once you connect.

## Use with any MCP client

Point your client at the remote VestAI MCP server — it advertises OAuth 2.1, so the
client walks you through sign-in (no credentials are shared with the assistant):

```text
https://api.vestai.ai/mcp/sse
```

## Install in Claude (one step)

```text
# 1. add this marketplace
/plugin marketplace add VESTAI-LTD/vestai-plugin

# 2. install the plugin
/plugin install vestai-wealth@vestai
```

On first use you'll see the **VestAI OAuth** consent screen — sign in and approve.
Works in Claude Code, Claude.ai (web) and Claude Desktop.

## What's inside

| Component | What it is |
|-----------|------------|
| **MCP connector** (`.mcp.json`) | Remote VestAI MCP server (`https://api.vestai.ai/mcp/sse`, OAuth 2.1) — portfolios, net worth, real assets, liabilities, accounts, risk, markets, signals, family and document metadata. |
| **Skill: `wealth-portfolio-review`** | Banker-grade review → net worth, allocation/concentration, risk & drift, leverage, real-asset yield, market backdrop → a dated memo. |
| **Skill: `portfolio-stress-radar`** | "Where could I get hurt?" — traces a shock across concentration → risk → leverage/covenants → liquidity into a consequence, with pre-emptions. |
| **Skill: `concentration-and-drift`** | Concentration map (name/class/currency/region) + drift vs target + ranked trim/rebalance candidates. |
| **Skill: `liquidity-and-leverage`** | Liquidity ladder (raisable in days / weeks / months+), leverage, and covenant headroom with distance to margin-call / DSCR / ICR triggers. |
| **Skill: `market-signals-period`** | Time-series read over a look-back window — what trended, what's new, how correlations shifted. |

Invoke a skill explicitly with `/vestai-wealth:<skill>` (e.g.
`/vestai-wealth:portfolio-stress-radar`), or just ask in plain language — the skills
auto-trigger on the questions below.

## Critical questions you can ask

Once connected, fire these directly — each routes to a skill and drills straight
into the detail:

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
.claude-plugin/marketplace.json              # the catalog (lists the plugin)
plugins/vestai-wealth/
├── .claude-plugin/plugin.json               # plugin manifest
├── .mcp.json                                # remote VestAI MCP connector
└── skills/
    ├── wealth-portfolio-review/SKILL.md
    ├── portfolio-stress-radar/SKILL.md
    ├── concentration-and-drift/SKILL.md
    ├── liquidity-and-leverage/SKILL.md
    └── market-signals-period/SKILL.md
```

## Links
- Connector docs: https://vestai.ai/mcp
- Privacy: https://vestai.ai/policies/privacy-policy · Terms: https://vestai.ai/policies/terms-of-use
- Support: support@vestai.ai

---
*This repo contains only the plugin manifest, skills, and a pointer to the hosted
VestAI MCP endpoint — no VestAI backend code.*
