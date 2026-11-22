---
name: strategy-setup
description: >-
  Set up Antevo Strategy Radar for the user's company: five short questions
  (about three minutes, no figures) become a profile of exposure tags and
  objectives that stays in the user's assistant, then today's business board is
  matched to it at once. Use when the user says "set up Strategy Radar", "set
  up the radar for my company", "match the business board to my company",
  "build my company profile", or asks for Strategy Radar and no profile exists
  yet in the conversation. Read-only; nothing about the company is sent to
  Antevo.
compatibility: >-
  Requires the Antevo Strategy Radar connector (public, no sign-in). If the
  tools are not available, tell the user to add
  https://api.antevo.ch/mcp/strategy/mcp, then stop.
---

# Antevo — Set up Strategy Radar

Turn five plain answers into a company profile, then show what on today's
board touches it.

## Privacy (important)
The company's answers, objectives, tags and name **never go to Antevo**. No
Antevo tool takes them: `get_strategy_radar_setup` takes nothing and
`get_business_board` takes only a date. The profile lives in this conversation
(and, if the user wants one, in their own morning task). Say this once, plainly,
before the questions.

## Step 1 — Gather the method
Call `get_strategy_radar_setup()` once. It returns the five questions, the
fuller profile, the tag vocabulary (themes, regions, tags), the matching method,
the morning-task text, the page layout and the two disclosure lines. Follow
`matching_method` as written; the steps below are its order.

## Step 2 — Ask the five questions
Ask `setup_questions` in plain conversation, one at a time. They need no
figures, numbers or confidential documents. Keep the **three to five
objectives in the user's own words, numbered**. If the user pastes a strategy
summary or annual report instead, read the answers from it and confirm them.

## Step 3 — Tag the answers
- Map each answer to tag ids from `vocabulary.tags`; each question's `fills`
  names the tag groups it fills.
- Regional tags are written `<tag_id>:<region_id>` with a region id from
  `vocabulary.regions`, e.g. `buys_from:middle_east`, `sells_in:european_union`.
- **Show the tags back in their labels** ("Buys from or makes in: Middle East")
  and let the user correct them before going on.

## Step 4 — Show today's board at once
Call `get_business_board()` and draw today's matched page straight away, before
offering anything else — the matching rules and layout are in the
**strategy-today** skill (match, one sentence per link naming the objective,
count the unlinked, sort by impact then objectives touched).

## Step 5 — Offer the morning page (once)
Offer to save `morning_task.text` as a weekday task in the user's assistant
(default 08:00 local), filling its placeholders with their tags, numbered
objectives and today's date. Only if the assistant can schedule tasks; if it
can't, say they can ask "what changed for my strategy today?" any morning.
The fuller profile (`fuller_profile`) is offered once, after the first week —
never during setup.

## Guardrails
- **Never send company details to Antevo.** No company name, tag or objective
  goes into any tool call.
- **Rivals**: looking a rival up by name sends that name to Antevo. Say so first
  and look it up only if the user agrees.
- **Grades are words.** Impact, likelihood and trend stay in the board's words;
  never a number, score or percentage.
- **Options, never advice.** Responses are possible responses with their reasons
  and the event that would make each right.
- End the page with both `disclosures` lines, word for word.
