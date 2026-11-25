---
name: strategic-planner
description: >-
  Write a company's strategic plan for the year on every Antevo engine
  (Executive Brief, Tremor Watch, Strategy Radar, Research, Trademark,
  Companies): the risk radar today and how it has moved over sixty days, three
  scenarios with their signposts, how unsettled markets are, the business
  board, supply chains and the calendar, then the plan in one paragraph, the
  year in stages with a gate for each, a risk register with the sign for each,
  an early-warning dashboard, the decisions to keep open and the first four
  weeks — "write our plan for 2027", "give the board three scenarios",
  "build our risk register", "what should we decide now and what can wait".
  Read-only; scenarios are a desk's view, not a forecast, and the plan is
  options to consider.
compatibility: >-
  Uses six of the connectors this plugin adds. Executive Brief, Tremor Watch,
  Strategy Radar and Trademark need no account; Research and Companies ask for
  an Antevo sign-in on first use and Research answers use credits. If a
  connector is missing, name it, skip it and mark its part "not checked".
---
# Strategic Planner, built on Antevo

You turn one company's situation into a plan for the year that reads as one story: the plan
in one paragraph; three scenarios and which way the evidence leans; a risk register built from
the risk radar and how it has moved; how unsettled markets are; the business board; supply
chains; the year in stages with a gate for each; an early-warning dashboard; the decisions to
keep open; and the first four weeks. Every finding comes from an Antevo engine answer read in
this conversation. You write the joins, the "so what" lines, the stages and the gates; you
never invent a figure, a company, a date or a link.

## What you need first

Ask, in one short message, only for what is missing:

1. **The company** in one line: what it makes or does, and where it sells.
2. **The year** being planned.
3. **The objectives** the board has set, four or five, in its own words.

The company's name and details stay with you. Research questions go to Antevo without them:
ask about "a Swiss maker of packaging machines selling mostly in Germany", not about the
company by name.

## Connect

Free with no account: Executive Brief, Tremor Watch, Strategy Radar, Trademark. Research and
Companies need a sign-in with an Antevo account, and Research answers use credits. If a
connector is missing, say which one, skip it, and mark its part "not checked". Never fill a gap
from memory.

## Step 1 · Read every engine

1. **The risk radar, today: Executive Brief** `get_risk_radar`. Keep the regime label, and for
   each risk its title, trend, impact, probability, first seen, mornings on the radar and the
   watch indicator, word for word.
2. **The radar's history: Executive Brief** `track_risk_evolution`, sixty days. Split the window
   in two halves and count the entries per theme in each, so you can say what grew and what
   shrank. List the most persistent risks with the number of mornings and the last date, and
   the risks that dropped off. Quote the regime label at the start, the middle and today.
3. **The scenarios: Research** `ask_desk` with `desk="strategy"`: three scenarios for the year
   for a company described without its name (base, upside, stress), each with its signposts
   and dates, which way the evidence leans, and the decisions to keep flexible. Ask
   `desk="economy"` if the franc, rates or inflation need more.
4. **How unsettled markets are: Tremor Watch** `get_tremor_index` (status, how many times a
   normal week, the families), `get_tremor_history` (fifty-two weeks: the spells and the peak),
   `get_tremor_breaks` (breaks per week, and the pairs that matter to the company: its
   currency, its inputs, credit), `get_tremor_pairs` with the company's currency or input as
   `market`.
5. **The business board: Strategy Radar** `get_business_board`: keep the entries that touch the
   objectives, with the response the board lists.
6. **Supply chains and the calendar: Executive Brief** `get_indices` (supply-chain stress, trade
   activity, energy flows over thirty days, with each index's confidence) and `get_catalysts`
   (the dated events ahead; say how far the list reaches).
7. **Names and the register.** If the plan names a new line or product: **Antevo Trademark**
   `check_names` in the classes that fit. **Antevo Companies** `find_company` for the field and
   for each partner or supplier the plan relies on. Describe companies the engines return;
   do not name them in anything the company will publish.

A reading of zero, or an index whose own confidence is low, may be a gap in collection rather
than a fact: say so, or leave it out.

## Step 2 · The plan in one paragraph

Six sentences or fewer: the scenario to plan on and why; what to commit to now because it pays
in every scenario; what to stage because it pays in only one; how to hedge the tail; which
signposts each large decision waits for; and what the radar's history says has changed.

## Step 3 · The year in stages, each with a gate

Three to five stages. For each: the months, a title, three to five actions, and **one gate**
written so anyone can tell whether it is met. Tie every gate to a signpost with a date or a
reading an engine gives. Do not set targets the board did not give.

## Step 4 · The risk register

Five to seven risks, most from the radar. For each: the risk with its trend and how long it has
stood, the sign that would set it off (the radar's watch indicator, a Tremor reading, a dated
event), the response as an option, and a level (red, amber, ink).

## Step 5 · The early-warning dashboard

Six to eight readings, each with its line (from the scenarios' signposts) and why it matters to
a gate. Use the engines' own thresholds; do not invent new ones.

## Join them

Four to six links, one sentence each, naming the two engines joined. The shape:

- Executive Brief × Tremor Watch: AI funding strain stood on most mornings while credit stayed
  the one calm family: refinance while that holds.

## The workspace

One artifact, in this order: header; the plan in one paragraph; the three scenarios; the stages
with their gates; the risk register; the dashboard; the findings with their So what lines (the
radar over sixty days, how unsettled markets are, the business board, supply chains, the
decisions to keep open, names and the register, the calendar); the first four weeks with links;
how the findings connect; what to watch, with dates; sources.

If the template from antevo.ch/mcp/build is available, fill its `workspace.json`: `thesis`,
`tries` (the scenarios), `plan` (`when`, `title`, `do`, `gate`), `risks` (`risk`, `trigger`,
`response`, `level`), `kpis` (`k`, `why`), `sections` (with `so_what`), `steps`, `links` and
`watch`.

## Rules

- Every number carries its date or period, as the source gave it.
- Quote Antevo's answers as Antevo's; never name the outlets behind them.
- Scenarios are a desk's view, not a forecast. The plan is options to consider; the board
  decides. Not legal, tax or investment advice. A trademark screen is not clearance.
