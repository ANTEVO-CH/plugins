# Changelog

All notable changes to the Antevo plugins are documented here.

## [unreleased] — signal read + plain-language decode

- **`antevo-executive` 0.3.0** — two more skills, taking it to six:
  **signal-read** (Antevo's own probability layer — the odds it carries on named
  outcomes, which way they moved, and what the shape means) and **decode**
  (what a move actually means, in plain language).
- **signal-read enforces live bands only.** The desk once published an expired
  band as a current probability and corrected it in the open; `why_it_leads`
  carries that correction. The skill reads it before quoting any number, and
  describes direction rather than quoting a figure it cannot date.
- **decode uses the desk's own plain-language copy rather than paraphrasing.**
  Simplifying a financial claim is where meaning quietly changes — a hedge gets
  dropped, "the odds fell" becomes "it won't happen". The brief already carries
  an authored jargon-free rendering, so the skill routes and frames it instead
  of rewriting it.
- Both lean on the connector's new `sections` argument, so `decode` pulls ~2KB
  instead of the full ~24KB brief.

## [unreleased] — risk radar + Streamable HTTP

- **`antevo-executive` 0.2.0** — two new skills:
  **risk-radar** (what could go wrong from here: each risk graded by trend,
  impact and probability, paired with the reading that would settle it, plus
  the dated forward calendar) and **emerging-risks** (how the board has changed
  over weeks — what's new, escalating, entrenched or gone).
- Backed by three new connector tools: `get_risk_radar`, `track_risk_evolution`
  and `get_catalysts`.
- **emerging-risks groups the risks itself, on purpose.** The connector returns
  every dated board in one call but does NOT thread a risk across days: the
  brief rewords each risk every morning, and matching on wording was measured
  against 14 real briefs to be unreliable (true continuations and unrelated
  pairs scored in the same band). Grouping by meaning is the model's job; the
  skill says so and cites the dates it grouped.
- **Both plugins now connect over Streamable HTTP** (`/mcp/…/mcp`) instead of
  HTTP+SSE (`/mcp/…/sse`). SSE is deprecated in the MCP spec; the streamable
  endpoints were verified live in production before this switch. The SSE
  endpoints remain available for anything still pointed at them.
- Tool titles and read-only/destructive hints now reach `tools/list`, so hosts
  can label what a tool does before running it.

## [unreleased] — marketplace + Executive plugin
- Repo renamed `wealth-plugin` → **`plugins`** — it is a marketplace, not one
  plugin. Install: `/plugin marketplace add ANTEVO-CH/plugins`.
- New **`antevo-executive`** plugin (v0.1.0) — the public Executive Brief
  connector (`/mcp/executive/sse`, **no account**) with two skills:
  **world-brief** (what's happening now) and **story-timeline** (how a story
  developed, from the dated archive).
- README reframed around two plugins; `antevo-wealth` unchanged.

## [0.5.0] — one connection for all of Wealth
- `antevo-wealth` now connects through the single **`/mcp/wealth/sse`** aggregate
  instead of 14 per-domain servers: **one connection, one sign-in**, same tools
  (names unchanged, so every skill works as before). Verified live in PROD.
- The backend also now advertises the **Antevo** brand and a host-aware OAuth
  issuer, so `api.antevo.ch` is self-consistent for strict clients.
- Per-domain endpoints remain available for a narrower tool set.

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
