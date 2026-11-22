---
name: board-read
description: >-
  Read Antevo's business board without a company profile — today's or any
  morning in the last 400 days — by theme, exposure or region, or compare two
  mornings to see what is new, what rose and what left the board. Use when the
  user asks "what's on the business board today", "what are the risks for
  companies this week", "anything on shipping or energy for companies", "which
  entries touch companies that import from Asia", "what changed on the board
  since Monday", or "show me the board for 20 November". Read-only; not about
  one company — for that, use strategy-today.
compatibility: >-
  Requires the Antevo Strategy Radar connector (public, no sign-in). If the
  tools are not available, tell the user to add
  https://api.antevo.ch/mcp/strategy/mcp, then stop.
---

# Antevo — Read the business board

The day's risks and opportunities for companies, read across the whole board.

## Scope (important)
This reads the board as published, the same for everyone. It doesn't know the
user's company. If they want it matched to their company, hand off to
**strategy-setup** (no profile yet) or **strategy-today** (profile in hand).

## Step 1 — Gather
| Need | Tool |
|------|------|
| Today's board | `get_business_board()` |
| A given morning | `get_business_board(as_of="YYYY-MM-DD")` |
| Theme, region and tag labels | `get_strategy_radar_setup()` → `vocabulary` |

For "since Monday" or "this week", call the board for each morning needed and
compare by `entry_id`.

## Step 2 — Read it the way it is built
- **Lead with consequence.** Sort by impact (severe, high, medium, low), then
  likelihood; give the count of risks and opportunities from `counts`.
- **Filter on the board's own fields.** A theme question filters on `theme`; an
  exposure or region question filters on `tags` (regional tags are
  `<tag_id>:<region_id>`, and `buys_from` is not `sells_in`). Use the
  vocabulary's labels in the answer, not the ids.
- **Say who it touches** from `who_it_touches`, and how long it has been there
  from `mornings_on_board` ("new today" on its first morning).
- **Comparing mornings:** new entries (`entry_id` not on the earlier board),
  entries whose impact, likelihood or trend changed (say from what to what), and
  entries that left. Name the dates.
- **An empty theme is an answer.** If nothing on the board touches the theme,
  say so plainly; don't fill it from memory.

## Step 3 — Output
```
# Business board — {date}
{n} risks · {n} opportunities · Antevo Executive Brief

**{title}** — {theme label}
{Impact} impact · {likelihood} likelihood · {Trend} · {tenure}
{why} ({why_date})
Who it touches: {who_it_touches}
Watch: {watch}
Possible responses: {label} — {reason} (right if {right_if}); …

---
{disclosures.not_advice}
```

## Guardrails
- **Grades in words only**, as the desk wrote them; never numbers or
  percentages.
- **Options, never advice.** Responses are possible responses with reasons.
- **No outlets or links.** Credit "Antevo Executive Brief" and the date.
- **Don't forecast** beyond the entry's own watch and act_when lines.
