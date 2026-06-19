# VestAI — Claude plugin & marketplace

One-install distribution of the **VestAI Wealth** connector + skills for Claude.
Installing the `vestai-wealth` plugin wires up the VestAI MCP connector **and**
the private-banker skills in a single step.

> You need a [VestAI](https://vestai.ai) account to see your own data. The
> universal market surfaces (markets brief, CIO desk, executive brief) work on a
> free account; the personal surfaces (net worth, portfolio, real assets,
> liabilities, family, documents) show your household once you connect.

## Install

```text
# 1. add this marketplace
/plugin marketplace add VESTAI-LTD/vestai-claude-plugin

# 2. install the plugin
/plugin install vestai-wealth@vestai
```

On first use Claude will open the **VestAI OAuth** consent screen — sign in and
approve (no credentials are shared with the assistant). Works in Claude Code,
Claude.ai (web) and Claude Desktop.

## What's inside

| Component | What it is |
|-----------|------------|
| **MCP connector** (`.mcp.json`) | Remote VestAI MCP server (`https://api.vestai.ai/mcp/sse`, OAuth 2.1). Gives Claude your portfolios, net worth, real assets, liabilities, accounts, risk, markets, family and document metadata. |
| **Skill: `wealth-portfolio-review`** | A banker-grade portfolio review that orchestrates the connector — net worth, allocation/concentration, risk & drift, leverage, real-asset yield and the market backdrop → a dated memo. Invoke with `/vestai-wealth:wealth-portfolio-review`, or just ask "review my portfolio". |

Read-only: the connector surfaces recommendations and only ever makes a change
after you approve a plan. AI outputs are informational support only — not
investment, tax, or legal advice.

## Structure

```
.claude-plugin/marketplace.json          # the catalog (lists the plugin)
plugins/vestai-wealth/
├── .claude-plugin/plugin.json           # plugin manifest
├── .mcp.json                            # remote VestAI MCP connector
└── skills/
    └── wealth-portfolio-review/SKILL.md  # the review skill
```

## Links
- Connector docs: https://vestai.ai/mcp
- Privacy: https://vestai.ai/policies/privacy-policy · Terms: https://vestai.ai/policies/terms-of-use
- Support: support@vestai.ai

---
*This repo contains only the plugin manifest, skills, and a pointer to the hosted
VestAI MCP endpoint — no VestAI backend code.*
