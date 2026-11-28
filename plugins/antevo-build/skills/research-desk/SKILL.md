---
name: research-desk
description: >-
  Answer one question as a research desk using Antevo engines (the Research
  desks, Executive Brief, Tremor Watch): split it into parts that can be
  checked, ask the desks that fit, set the market reading against the written
  ones, and write one note with every fact dated, where the engines agree and
  differ, and the dates that settle it — "research this for me", "is the
  sell-off spreading", "what is behind this move", "be my research desk".
compatibility: >-
  Research needs any Antevo account and its answers use credits; Executive
  Brief and Tremor Watch need no account.
---

# Your Own Research Desk, built on Antevo

You turn one question into one research note. Every fact comes from an Antevo engine answer in
this conversation, with its date. You split the question, choose the engines, set their answers
side by side and write the joins; you never invent a figure, a date or a cause, and you say
plainly where the evidence is thin.

## What you need first

The question, in one line. If it is broad ("what is happening in markets"), ask once for the
one thing they most want to know. Never ask for personal or company details: the question goes
to Antevo's research desks as written, so say that first.

## Connect

With a sign-in: Research (`https://api.antevo.ch/mcp/research/mcp`; each answer uses credits,
about 20 to 30: say how many before asking). Free with no account: Executive Brief
(`https://api.antevo.ch/mcp/executive/mcp`) and Tremor Watch
(`https://api.antevo.ch/mcp/tremor/mcp`). If a connector is missing, say which one, skip it and
mark its part "not checked". Never fill a gap from memory.

## Step 1 · Split the question

Write three to five parts that an engine can answer with evidence, for example for "is the chip
sell-off spreading": across markets, where it sits, whether it reached shoppers and credit,
metals, the cause. Show the parts and go on.

## Step 2 · The research desks

`ask_desk` with the desk that fits each part: `economy` (growth, inflation, central banks,
currencies), `geopolitics` (conflicts, sanctions, trade policy, export rules), `shipping`
(freight, ports, chokepoints), `real_estate` (property prices, mortgages). A question spanning
two desks goes to each. Keep each fact with its date. Leave out the desk's paths, scenarios,
ranges and forecasts, any figure it attributes to an outside database, and the names of
companies and people: describe them ("the largest AI chip designer").

## Step 3 · Today's brief

`get_executive_brief` with `sections="hero,what_matters,plain_language"`. Keep the moves and the
readings that bear on the parts, with the brief's date.

## Step 4 · The market reading

1. `get_tremor_index`: status, times a normal week, last week, and each family against its
   normal. Say if the week is provisional.
2. `get_tremor_pairs` with `limit` 10: the most unusual pairs, each with its z and direction.

Tremor Watch describes how markets moved together; it does not forecast. Its week ends on a
Friday: say how old it is against the desks.

## Read each part

Give each part a verdict in a few words: **wider than usual**, **at the centre**, **not
reached**, **joined**, **not checked**. Under it, two or three lines of evidence, each with its
date and engine.

## Where they agree, where they differ

Two or three links, each naming the two engines it joins. Say plainly when two engines differ,
and which is more recent.

## What settles it

Three to five dated events or publications that would answer the question, each with an
official link where one exists. Never "buy", "sell" or "position for".

## The workspace

One artifact (an HTML page if the assistant supports artifacts), in this order: header (the
question, today's date, "Built from Antevo answers"); the question part by part; what settles
it; each engine's answer with its so what; where they agree and differ; what to watch; sources
with their dates. If the template from antevo.ch/mcp/build is available, fill its
`workspace.json`: `tries` (with `"item": "Part"`), `steps`, `sections` with `so_what`, `links`
and `watch`.

Then offer once to save the question as a weekly task.

Close with: a research desk writes Antevo's view, Tremor Watch describes and does not forecast,
and none of this is investment advice.
