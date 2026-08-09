# Changelog

All notable changes to the Antevo plugins are documented here.

## [unreleased] — marketplace + Executive plugin
- Repo renamed `wealth-plugin` → **`plugins`** — it is a marketplace, not one
  plugin. Install: `/plugin marketplace add ANTEVO-CH/plugins`.
- New **`antevo-executive`** plugin (v0.1.0) — the public Executive Brief
  connector (`/mcp/executive/sse`, **no account**) with two skills:
  **world-brief** (what's happening now) and **story-timeline** (how a story
  developed, from the dated archive).
- README reframed around two plugins; `antevo-wealth` unchanged.

## [0.4.2] — daily-brief skill
- New **daily-brief** skill for the `/wealth/today` surface — the morning note:
  what matters today, unread alerts, open compliance breaches, drift and the
  upcoming calendar, triaged into one executive read (10 skills total).
- Equity + technical analysis are already covered by **security-analysis** (one
  instrument, both lenses) — deliberately one skill, so the descriptions don't
  overlap and degrade auto-triggering.

## [0.4.1] — Antevo-branded endpoints
- Connector URLs use **`api.antevo.ch`**; MCP server keys namespaced `antevo-*`.
- The backend advertises the Antevo issuer on that host, so the endpoint is
  self-consistent for strict OAuth clients.

## [0.4.0] — Antevo Wealth
- Repo, catalog and plugin aligned to Antevo Wealth. Install:
  `/plugin marketplace add ANTEVO-CH/plugins` →
  `/plugin install antevo-wealth@antevo`.
- Links to antevo.ch (homepage, policies); contact **contact@antevo.ch**.

## [0.3.0]
- Connector tools went live in production — geopolitics, technical analysis,
  equity fundamentals, watchlist and goals — plus a cash-inclusive AUM fix.
- Added skills: **geopolitical-risk**, **security-analysis**, **watchlist-review**,
  **goals-review**.

## [0.2.0]
- Reframed around the agent-agnostic MCP connector (any MCP client), with the
  Claude plugin as one packaging.
- Added skills: **portfolio-stress-radar**, **concentration-and-drift**,
  **liquidity-and-leverage**, **market-signals-period**.

## [0.1.0]
- Initial release of the **antevo-wealth** plugin.
- Bundles the Antevo Wealth MCP connector (remote SSE, OAuth 2.1) — portfolios,
  net worth, real assets, liabilities, accounts, risk, markets, family, documents.
- Adds the **wealth-portfolio-review** skill.
