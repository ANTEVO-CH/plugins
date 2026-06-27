---
name: geopolitical-risk
description: >-
  Read the world's geopolitical risks and tie them to a VestAI wealth client's
  exposure. Use whenever the user asks about geopolitical risk, "what's happening
  in the world", conflict / war / sanctions / cyber risk, a chokepoint (Hormuz,
  Suez, Taiwan Strait, Red Sea), supply-chain or energy-security risk, or "how
  exposed am I to [region/event]". Orchestrates the VestAI MCP connector's
  intelligence.geo tools (15 live layers + country drilldown) and, when portfolio
  tools are connected, cross-references where the household's capital actually sits.
  Read-only.
compatibility: >-
  Requires the VestAI MCP connector (intelligence.geo). If the tools are not
  available, tell the user to connect VestAI, then stop.
---

# VestAI — Geopolitical risk

Turn the raw geo layers into a read that answers the only question that matters to
a principal: **does this touch my capital, and what do I watch?**

## Before you start
- **Connector check.** No `intelligence.geo` tools → ask the user to connect VestAI, then stop. Never invent events.
- **Scope.** Geo data is global/universal (free). Portfolio exposure is household-scoped — only cross-reference if the portfolio tools are connected and a household resolves.

## Step 1 — Gather
- `list_layers` — see what's available (conflict, maritime, infrastructure, sanctions, cyber, narrative).
- `get_geo_map(layers, days_back, region, country, severity)` — the global picture over a window (default ~30d for a considered read; 7d for "right now").
- `get_country_brief(iso2, days_back)` — drill into a specific jurisdiction the client is exposed to.
- If portfolio tools are present: pull the household's country / sector / currency footprint (e.g. positions, real-asset locations, custody) to know where the capital sits.

## Step 2 — Analyse (tie it to the book)
- **Rank by relevance, not volume.** A flag near where the client holds capital or sources income beats a louder one that doesn't touch them.
- **Chokepoints & energy.** Hormuz / Suez / Taiwan Strait status → who carries it (energy holdings, shipping, FX).
- **Sanctions / cyber / regulatory.** Anything that hits a held name, sector, or domicile.
- **Narrative shift (GDELT).** Where sentiment is turning on a theme the client is exposed to.
- **So-what per item.** One line: why it matters *to this book*, and what would escalate it.

## Step 3 — Write it
```
# Geopolitical risk — {as-of}

**The read.** {1–2 sentences: the risks that actually touch this book.}

## What's live
- {region/event} — {severity}; {why it touches the client or "watch, low exposure"}

## Your exposure  (if portfolio connected)
- {country/sector/chokepoint} → {holdings/income affected}

## Watch
- {1–3 forward triggers}

---
*Read-only geopolitical intelligence from your VestAI data as of {date}.
Informational only — not investment advice.*
```

## Guardrails
- Cite layers/dates from the tools; an empty layer is data ("quiet"), not a gap to fill.
- If the portfolio isn't connected, say the exposure tie-in is unavailable rather than guessing.
- Not advice. Signals and context, not a recommendation.
