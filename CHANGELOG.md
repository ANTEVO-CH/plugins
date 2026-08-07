# Changelog

All notable changes to the Antevo Wealth plugin are documented here.

## [0.4.0] — rebrand to Antevo Wealth
- The wealth product moved to **antevo.ch/wealth** (vestai.ai/wealth is retired).
  Rebranded the plugin accordingly — VestAI → **Antevo Wealth** across the
  manifest, marketplace, README, SECURITY, and all skill copy.
- Repo renamed `vestai-plugin` → `antevo-wealth-plugin`; catalog `vestai` → `antevo`;
  plugin `vestai-wealth` → `antevo-wealth`. New install:
  `/plugin marketplace add VESTAI-LTD/antevo-wealth-plugin` →
  `/plugin install antevo-wealth@antevo`.
- Links → antevo.ch (homepage, policies); contact → **contact@antevo.ch**.
- **Unchanged:** the connector endpoints + OAuth issuer stay on `api.vestai.ai`
  (the API/backend did not move — only the product brand + web surface did). No
  functional change to how the tools work.

## [0.3.0] — 2026-06
- New connector tools went live in PROD — geo, technical, equity, watchlist, goals —
  plus the MCP↔web parity fix (cash-inclusive AUM). The connector config now lists
  the full v3 wealth leaf set (one MCP server per domain).
- Added four skills:
  - **geopolitical-risk** — world risk read tied to the household's exposure (`intelligence.geo`).
  - **security-analysis** — one instrument, fundamentals + technicals (`markets.equity` + `markets.technical`).
  - **watchlist-review** — tracked instruments: movers, signals, vol (`wealth.watchlist`).
  - **goals-review** — funding progress vs targets, gap to plan (`wealth.goals`).
- Note: this is the **multi-server interim** — the client connects each domain once
  (all share one VestAI login). v0.4.0 will collapse them behind a single
  `/mcp/wealth/sse` aggregate endpoint for a one-connect / one-login experience.

## [0.2.0] — 2026-06
- Repo renamed `vestai-claude-plugin` → `vestai-plugin`; README reframed around the
  agent-agnostic MCP connector (any MCP client) with the Claude plugin as one
  packaging. Install command is now `/plugin marketplace add VESTAI-LTD/vestai-plugin`.
- Added four skills:
  - **portfolio-stress-radar** — cross-domain "where could I get hurt" chain
    (concentration → risk → leverage/covenants → liquidity → consequence + pre-emptions).
  - **concentration-and-drift** — concentration map + drift vs target + trim candidates.
  - **liquidity-and-leverage** — liquidity ladder + leverage + covenant headroom.
  - **market-signals-period** — time-series read over a look-back window.
- Added a "critical questions" catalog to the README for direct, deep-dive prompts.

## [0.1.0] — 2026-06
- Initial release of the **vestai-wealth** plugin.
- Bundles the VestAI MCP connector (remote SSE, OAuth 2.1) — portfolios, net
  worth, real assets, liabilities, accounts, risk, markets, family, documents.
- Adds the **wealth-portfolio-review** skill — a banker-grade review that
  orchestrates the connector into a dated memo.
