---
name: fintech-launch
description: >-
  Plan a Swiss fintech end to end using Antevo engines (Trademark, Companies,
  Strategy Radar, Executive Brief, Tremor Watch, Research) and the regulators'
  own pages: the name, the field, the licence route with FINMA and in the next
  market, rates, the franc and the funding window, then the strategy in one
  paragraph, a twelve-month plan in stages with a gate for each, the risks with
  the sign that would set each off, what to measure and the first four weeks
  with the official links — "we're founding a payments company in Zurich",
  "plan our fintech launch", "which licence do we need, and when do we raise",
  "take our fintech into Germany". Read-only; it never says a product does not
  need a licence, and a screen is not legal clearance.
compatibility: >-
  Uses six of the connectors this plugin adds. Trademark, Strategy Radar,
  Executive Brief and Tremor Watch need no account; Companies and Research ask
  for an Antevo sign-in on first use and Research answers use credits. Reads
  finma.ch and sif.admin.ch with the assistant's own web tool where it has one.
  If a connector is missing, name it, skip it and mark its part "not checked".
---

# Fintech Launch Strategy, built on Antevo

You turn one founder's fintech idea into a launch strategy that reads as one story: the ground
it stands on, the strategy in one paragraph, a twelve-month plan in stages with a gate for each,
the risks with the sign that would set each off, what to measure, and the first four weeks with
the official links. Every finding comes from an Antevo engine answer or an official page read in
this conversation. You write the joins, the "so what" lines, the stages and the gates; you never
invent a figure, a company, a date, a rule or a link.

## What you need first

Ask, in one short message, only for what is missing:

1. **The company** in one line: its name, what it does and for whom.
2. **Money or software:** will it hold or move clients' money, or only software around money?
3. **The markets:** home (Switzerland) and the next one (for example Germany).
4. **The runway:** how far the money raised so far reaches, in months, if they will say.

If there is no name yet, run the Startup launch build first (antevo.ch/mcp/build/startup-launch)
and come back with the name that held.

## Connect

Free with no account: Trademark, Strategy Radar, Executive Brief, Tremor Watch. Companies and
Research need a sign-in with an Antevo account, and Research answers use credits. If a connector
is missing, say which one, skip it, and mark its part "not checked". Never fill a gap from memory.

## Step 1 · The ground

1. **The name: Antevo Trademark.** `check_names` with the name and the classes for finance and
   software (`suggest_classes` if unsure; payments usually 9, 36 and 42). Verdict as in the
   Startup launch recipe: clear on this screen, close call, or taken, with the evidence.
2. **The field: Antevo Companies.** `find_company` with the activity word ("payments",
   "fintech", "lending"). Count where the companies sit. **Describe them, do not name them** in
   anything the founder will publish. Finding is free; do not open files unless asked.
3. **The licence route: the regulator's own pages.** Read them; do not rely on memory.
   - FinTech licence: https://www.finma.ch/en/authorisation/fintech/fintech-bewilligung/
   - What falls under the Anti-Money Laundering Act, and the self-regulatory organisations:
     https://www.finma.ch/en/authorisation/fintech/
   - FINMA's preliminary assessment and its fast track:
     https://www.finma.ch/en/authorisation/fintech/fintech-bewilligung/fintech-fast-track/
   - Any proposed change to the licence categories, from the State Secretariat for International
     Finance (sif.admin.ch) or the Federal Council (admin.ch). Say what stage it has reached and
     when; if you cannot find a later stage, say so.
   Then ask **Antevo Research**, `ask_desk` with `desk="geopolitics"`, for the rules in the next
   market: whether a Swiss licence reaches it (for the EU it does not), which licence is needed
   there, and the payment, anti-money-laundering and AI rules in motion, each with its date.
   When a desk answer and an official page disagree, the official page wins; say so.
4. **Money and timing.** Antevo Research, `desk="economy"`: rates, inflation, the franc against
   the next market's currency, and venture funding conditions. Antevo Strategy Radar,
   `get_business_board`: keep the entries on funding and on demand in the next market, with the
   response the radar lists. Antevo Tremor Watch, `get_tremor_index`: the status and how many
   times a normal week. Antevo Executive Brief, `get_catalysts`: the dated events ahead.

## Step 2 · The strategy in one paragraph

Write it in six sentences or fewer, from the findings. The shape that usually holds for a
company that will hold clients' money:

- **What it can do before a licence:** software that holds no money reaches paying customers
  sooner. Whether that first product needs a licence is the regulator's call; the preliminary
  assessment is how to ask.
- **The licence:** which one, and how to write the application if the law may change under it.
- **The next market:** an EU licence of its own, or a licensed partner first.
- **How it earns:** at a zero policy rate there is no income on balances, and the FinTech
  licence forbids paying interest; say what that means for pricing.
- **When to raise:** from the funding and market findings.

## Step 3 · Twelve months, in stages with gates

Three to five stages. For each: the months, a title, three to five actions, and **one gate**: the
condition that must hold before the next stage starts, written so anyone can tell whether it is
met. Tie every stage to a finding or a dated event. Do not set numeric targets the founder did
not give; say the thresholds are set at the first gate.

## Step 4 · Risks, each with its sign

Four to seven risks. For each: the risk, **the sign that would set it off** (a dated event, an
engine reading, a published rule, a register change), and the response as an option. Use the
engines' own triggers where they give them ("act if...").

## Step 5 · What to measure

Five to eight measures, each with why it matters to a gate. Names only; the founder sets the
numbers.

## Join them

Three to five links, one sentence each, naming the two engines joined. The shape:

- Research × Strategy Radar: zero rates remove float income and the funding window is
  narrowing; both point to a fee-based product that reaches paying customers early.

## The workspace

One artifact, in this order: header; the strategy in one paragraph; the ground, piece by piece;
the stages with their gates; the risks with their signs; what to measure; the findings with
their So what lines; the first four weeks with the official links; how the findings connect;
what to watch, with dates; sources.

If the template from antevo.ch/mcp/build is available, fill its `workspace.json`: `thesis`,
`tries`, `plan` (`when`, `title`, `do`, `gate`), `risks` (`risk`, `trigger`, `response`,
`level`), `kpis` (`k`, `why`), `sections` (with `so_what`), `steps`, `links` and `watch`.

## Rules

- Every number carries its date or period, as the source gave it.
- Quote Antevo's answers as Antevo's; never name the outlets behind them.
- Whether a product needs a licence is for the regulator, the company and its advisers to
  decide. Write "may", "options to consider", "the regulator decides"; never "you do not need a
  licence". Not legal, regulatory, tax or investment advice. A trademark screen is not clearance.
