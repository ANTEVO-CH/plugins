# Changelog

All notable changes to the VestAI plugin are documented here.

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
