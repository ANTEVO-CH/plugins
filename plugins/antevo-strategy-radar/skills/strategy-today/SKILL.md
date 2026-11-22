---
name: strategy-today
description: >-
  What changed today for the user's company strategy: read Antevo's business
  board for the day and match it to the company profile held in this
  conversation, then draw the Strategy Radar page — linked risks and
  opportunities sorted by impact, one sentence per link naming the objective it
  touches, what to watch, when to act and the possible responses with their
  reasons. Use when the user asks "what changed for my strategy today", "draw
  my radar", "anything on today's board for us", "what should we keep an eye
  on this morning", or runs the Strategy Radar morning task. If no profile
  exists yet, run strategy-setup first. Read-only.
compatibility: >-
  Requires the Antevo Strategy Radar connector (public, no sign-in). If the
  tools are not available, tell the user to add
  https://api.antevo.ch/mcp/strategy/mcp, then stop.
---

# Antevo — What changed for your strategy today

Today's business board, matched to this company in this conversation.

## Scope (important)
The board is the same for every company; the matching happens here. The
profile — exposure tags and three to five numbered objectives — must already be
in the conversation or the morning task. **If it isn't, hand off to
strategy-setup** rather than guessing the company's exposures.

## Step 1 — Gather
| Need | Tool |
|------|------|
| Today's board | `get_business_board()` |
| An earlier morning | `get_business_board(as_of="YYYY-MM-DD")` — within the last 400 days |
| The page layout, if not already in hand | `get_strategy_radar_setup()` → `page_layout` |

If `status` says no board is published this morning, say so in one line and
stop. Never send company details: the board call takes only a date.

## Step 2 — Match
- An entry **links** when at least one of its `tags` is among the company's
  tags.
- A regional tag meets **only the same tag with the same region**:
  `buys_from:middle_east` does not meet `sells_in:middle_east`.
- For each linked entry write **one sentence** on how it touches the objective
  it bears on, **naming that objective**. If it touches none, write the sentence
  against the exposure it met.
- **Count** the entries that did not link and give the number; don't list them
  unless asked.
- **Sort** linked entries by impact (severe, high, medium, low), then by how
  many of the company's objectives they touch, most first.

## Step 3 — Output
Draw it in `page_layout`:
```
# What changed for your strategy today
{board date} · Antevo Executive Brief

{n} linked risks · {n} linked opportunities · {n} other entries

Your objectives: 1. … ({n} entries)  2. … ({n})  …

RISK · {THEME LABEL}
**{title}**
{Impact} impact · {likelihood} likelihood · {Trend} · {on the board N mornings | new today}
{why} ({why_date})
Touches your plan: {one sentence naming the objective}
Watch: {watch}
Act when: {act_when}
Possible responses:
- {response label}: {reason} Right if: {right_if}

…

{n} other entries on today's board did not link to your company.

**How this page was made** — Antevo's desk writes the business board each
morning, the same for every company. This assistant matched it to your answers,
which stayed here and never went to Antevo. Grades are words, never
probabilities.

**Not advice** — {disclosures.not_advice}
{disclosures.privacy}
```

## Guardrails
- **Grades in words only.** Never turn impact, likelihood or trend into a
  number, score or percentage.
- **Options, never advice.** Present responses as possible responses with their
  reasons and `right_if`; don't tell the company what it should do.
- **No outlets or links.** The only credit is "Antevo Executive Brief" and the
  board's date. Official bodies named inside an entry's text stay as written.
- **Don't add facts.** Use the entry's own why, watch and act_when; no figures
  from memory.
