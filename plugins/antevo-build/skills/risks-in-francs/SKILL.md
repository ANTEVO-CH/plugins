---
name: risks-in-francs
description: >-
  Put a figure in the person's own currency next to each risk on Antevo's
  morning list, using Antevo Wealth and, for the story, Executive Brief: the
  what-if that stands for each risk and what it would cost the household, in
  total and for each portfolio — "what would this cost me", "what do today's
  risks mean for my portfolio", "how exposed am I to tariffs", "which risk would
  hurt us most". Read-only; a what-if is not a forecast, a risk with no fitting
  what-if gets no figure, and it never says what to buy or sell.
compatibility: >-
  Uses two of the connectors this plugin adds. Wealth asks for an Antevo sign-in
  on first use and reads the person's own household. Executive Brief needs no
  account and is optional. If a connector is missing or a tool is refused, name
  it, skip it and mark its part "not checked".
---
# Today's risks, in francs, built on Antevo

You take Antevo's list of risks for today and put next to each one what it would cost this
household, as a what-if. You never forecast and never say what to buy or sell. Every figure
comes from an Antevo answer read in this conversation, with its date.

## What you need first

One question, only if it is not already clear: is what they recorded in Antevo Wealth
everything they own, or part of it? The figures cover what is recorded.

## Connect

Antevo Wealth (`https://api.antevo.ch/mcp/wealth/mcp`), with a sign-in: the person's own
household. Optional, free with no account: Executive Brief
(`https://api.antevo.ch/mcp/executive/mcp`). If the household holds nothing yet, say so and
stop. If a tool is refused because the plan does not include it, say which one and mark that
part "not checked". Never fill a gap from memory.

## Step 1 · The list with its figures

`get_today_brief`. Read `risk_scenarios`: one line per risk on today's list, each with

- `title`, `trend`, `impact`, `as_of`;
- `scenario`: the what-if that stands for the risk (`name`, `what_it_is`, and `matched_on`:
  `risk` when it was chosen for this risk, `theme` when it stands for the risk's wider theme),
  or nothing when no what-if fits;
- `household_impact_abs` and `household_impact_pct`: the cost in the household's currency and
  as a share of everything;
- `by_portfolio`: the same for each portfolio;
- `note`: keep its meaning with the figure.

If `risk_scenarios` is empty, say there is no list with figures today and stop there. Do not
pair risks with what-ifs yourself.

## Step 2 · Say each line in plain words

For each risk: what could happen, in one sentence; the what-if, by its name and in plain words
("prices that keep rising while growth stalls"); the cost; the portfolio that moves most and
the one that moves least. When `matched_on` is `theme`, say the what-if stands for the wider
theme, not this exact risk.

A risk with no what-if: say "no what-if fits, so there is no figure. That is not the same as no
effect." Never invent one.

## Step 3 · The story behind each line (optional)

**Executive Brief** `get_risk_radar`: the description of each risk and what to watch. Match by
title. Use it for the words, never for the figures.

## Step 4 · Past crashes, for scale

From the same `get_today_brief` answer, `stress`: the worst replays of past crashes. Give one
or two, as "a replay of a past event on today's holdings, not a forecast".

## Read each line

Order the risks by cost, largest first; the ones with no figure last. A verdict in a few words:
the cost and its share of everything, or "no figure".

How to say it: "If tariffs push prices up while growth stalls, the what-if costs 15% of
everything." Never "will", "expect", "likely to lose", "you should" or "protect yourself by".

## The workspace

One artifact, in this order: header; the list, risk by risk, with the what-if and the cost;
what is worth a look, with links; each portfolio against each risk; past crashes for scale; how
a risk gets its figure; sources.

If the template from antevo.ch/mcp/build is available, fill its `workspace.json`: `tries` (one
item per risk: `name`, `verdict`, `level`, `evidence`), `steps`, `sections` (with `so_what`),
`links` and `watch`.

Links from this table only:

| What | Link |
|---|---|
| How the what-ifs work | https://antevo.ch/stress-testing/ |
| The holdings | https://antevo.ch/wealth/ |
| Today's read | https://antevo.ch/executive/ |
| What is inside your funds | https://antevo.ch/mcp/build/inside-your-funds/ |

## Rules

- Keep this with the figures, every time: "A what-if is not a forecast: the risk may play out
  differently, or not at all."
- The figure is the cost of one named what-if, not of the risk. Always give the what-if's name.
- Never pair a risk with a what-if yourself, and never give a figure the tool did not give.
- Amounts in the household's own currency, with the date of the list.
- Never advice: nothing about what to buy, sell or hedge.
