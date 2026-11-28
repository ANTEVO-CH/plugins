---
name: intelligence-terminal
description: >-
  Build a custom intelligence terminal on the free Antevo engines (Executive
  Brief, Tremor Watch, Strategy Radar, Trademark): connect over MCP from code,
  call the tools, write workspace.json for the Antevo build template, and
  schedule it — "build me a market dashboard on Antevo", "call the Antevo MCP
  from Python", "a morning page from Antevo", "automate the Antevo brief".
compatibility: >-
  No account needed; Python 3.9+ for the reference script in scripts/.
---

# Intelligence Terminal, built on Antevo

You help a developer build a page, or a script that writes one, from the free Antevo engines.
Every line on the page comes from an engine answer with its date. The script adds no opinion;
judgement, if the developer wants it, is a separate layer written by an assistant and labelled
as such.

## The engines

All four answer any MCP client with no account and no API key, over streamable HTTP:

| Engine | Endpoint | Tools worth starting with |
|---|---|---|
| Executive Brief | https://api.antevo.ch/mcp/executive/mcp | `get_executive_brief` (pass `sections`), `get_catalysts`, `get_risk_radar` |
| Tremor Watch | https://api.antevo.ch/mcp/tremor/mcp | `get_tremor_index`, `get_tremor_pairs`, `get_tremor_history` |
| Strategy Radar | https://api.antevo.ch/mcp/strategy/mcp | `get_business_board`, `get_strategy_radar_setup` |
| Trademark | https://trademark.antevo.ch/mcp | `check_names`, `suggest_classes`, `holder_read` |

Call `tools/list` on each for the full set and each tool's input schema.

## The handshake

POST JSON-RPC 2.0 with `Content-Type: application/json` and
`Accept: application/json, text/event-stream`:

1. `initialize` with `protocolVersion`, empty `capabilities` and a `clientInfo`. Keep the
   `Mcp-Session-Id` response header if one comes back and send it on every later request.
2. The notification `notifications/initialized`.
3. `tools/call` with `name` and `arguments`. The answer is in `result.content[0].text`, a JSON
   string. A reply may arrive as server-sent events: read the last `data:` line.

The reference script, standard library only, is at
`scripts/antevo-terminal.py` in this skill (also at
https://antevo.ch/mcp/build/intelligence-terminal/antevo-terminal.py). Start from it.

## The page

Write `workspace.json` in the build template's format: `kind`, `title`, `subtitle`, `built`,
`note`; `tries` (`label`, `item`, `source`, `items` with `name`, `verdict`, `level` of
green/amber/red/ink, `evidence`); `steps` (`items` with `do`, `why`, `links`); `sections` (`title`,
`verdict`, `level`, `so_what`, `evidence`, `source`); `links` (`a`, `b`, `text`); `watch`;
`disclaimer`. The template from antevo.ch/mcp/build renders it with no other input.

## The rules

1. **No added opinion.** A script copies engine answers; it does not write so what lines. Use
   fields the engines already provide (the board's `who_it_touches`, the catalysts' `signal`).
2. **Every line dated**, with its engine: "Antevo Executive Brief, 25 Nov 2026"; "Antevo Tremor
   Index, week of 2026-11-20". Credit the business board as "Antevo Executive Brief".
3. **Grades stay words.** Never turn impact, likelihood or a Tremor status into a score.
4. **Tremor Watch describes.** Never present it as a forecast or a signal to trade.
5. **A trademark screen is today only** and is not legal clearance; say so on the panel.
6. **Be polite to the engines.** One run a morning is enough: the brief and board are written
   daily, Tremor Watch weekly.

## Schedule it

A cron line or a scheduled task on weekdays at 07:00 local time. If an engine does not answer,
write the panel as "not checked" and keep the rest; never fill a gap from an older run without
its date.

## A judgement layer, if wanted

Point an assistant at the same endpoints with the build recipes from antevo.ch/mcp/build: it
can write the joins and so what lines. Label that layer as the assistant's reading, separate
from the engine answers.

Close any page with: every line is an Antevo engine answer with its date, Tremor Watch
describes and does not forecast, and none of this is investment advice.
