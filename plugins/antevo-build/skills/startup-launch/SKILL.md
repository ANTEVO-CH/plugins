---
name: startup-launch
description: >-
  Turn a startup idea into a launch workspace using six Antevo engines
  (Trademark, Companies, Strategy Radar, Executive Brief, Tremor Watch,
  Research). Use when someone wants to launch, name or take a new company into
  a market and asks to check the name, the competition, the economy, the risks
  and a first 90-day plan — "help me launch…", "can we use this name…",
  "build me a launch plan". Read-only.
compatibility: >-
  Uses the six connectors this plugin adds. Trademark, Strategy Radar,
  Executive and Tremor Watch need no account; Companies and Research ask for an
  Antevo sign-in on first use, and Research answers use credits. If a connector
  is missing, name it, skip it and mark its section "not checked".
---

# Startup Launch Intelligence, built on Antevo

You turn one founder's idea into a launch workspace. Every finding comes from an Antevo engine
answer in this conversation. You write the joins between them and the plan; you never invent a
figure, a company or a date.

## What you need first

Ask, in one short message, only for what is missing:

1. **The idea** in one sentence (what it does, for whom).
2. **Home country** and **the next market** (for example Switzerland, then Germany).
3. **Up to five candidate names.** If they have none, offer three and say they are only
   suggestions.

## The six engines, in this order

Antevo's connectors must be added to this assistant. Free with no account: Trademark, Strategy
Radar, Executive Brief, Tremor Watch. Companies and Research need a sign-in with an Antevo
account, and Research answers use credits. If a connector is missing, say which one, skip it, and
mark its section "not checked" in the workspace. Never fill a gap from memory.

1. **Brand: Antevo Trademark.** `check_names` with the candidate names, the Nice classes that
   fit the idea (`suggest_classes` if unsure) and `countries` for any register beyond
   Switzerland (for example `["UK"]`). Keep: the verdict, `near_marks`, `found_in`, the closest
   mark with its office, status and filing date, the companies registered under the name, the
   domains. A screen is not clearance: say so.
2. **Competition: Antevo Companies.** `find_company` with the sector word and the candidate
   name (Swiss companies only in this version). Keep names, legal forms and seats. Count where
   they cluster. Finding is free; do not open files unless the founder asks (opening uses
   credits).
3. **Strategy: Antevo Strategy Radar.** `get_business_board`. Keep only the entries that touch
   the idea or the two markets, with their date, impact, likelihood, what to watch and the
   event that would make a response right.
4. **Economy today: Antevo Executive Brief.** `get_executive_brief` with
   `sections="hero,regime,what_matters"`, and `get_risk_radar`. Keep the regime in one line and
   the risks that touch funding, costs or the target markets.
5. **Market strain: Antevo Tremor Watch.** `get_tremor_index`. Keep the status, how many times a
   normal week, and which families are breaking.
6. **The economy desk: Antevo Research.** `ask_desk` with `desk="economy"` and the founder's
   question about rates, inflation, currency, growth and funding conditions in both markets.
   Keep each figure with its period. If the answer is "reused", say when it was written.

## Join them

This is the part only you can do. Write three to five links, each one sentence, each naming the
two engines it joins. Examples of the shape (use the real findings, not these):

- Trademark × Strategy Radar: an identical mark registered in the EU blocks the name in the
  growth market the board points to.
- Strategy Radar × Research: demand is strongest where money costs most.
- Tremor Watch × Executive Brief: markets are unsettled while the cost of money has not moved,
  so funding timing matters.

## The workspace

Produce it as one artifact (an HTML page if the assistant supports artifacts, otherwise a
structured document) with these sections, in this order:

1. **Header:** the idea, the two markets, today's date, "Built from Antevo answers".
2. **Brand:** a verdict per name (keep, risky, rename), with the evidence.
3. **Market entry:** home market, then next market, with the Strategy Radar and Research
   evidence.
4. **Competition:** who is already there, and where they cluster.
5. **Risk:** Tremor Watch status and the radar risks that touch the plan, each with what would
   confirm it.
6. **How the findings connect:** the links you wrote.
7. **90-day roadmap:** three blocks (days 1 to 30, 31 to 60, 61 to 90), each tied to a finding.
8. **What to watch:** the dates and indicators the engines named.
9. **Sources:** each engine with the date of its answer.

If the user wants the template, fill `template/workspace.json` from this plugin (schema below in the example) and open `template/index.html`.

## Rules

- Every number carries its date or period, as the engine gave it.
- Quote Antevo's answers as Antevo's; never name the outlets behind them.
- The roadmap is the founder's to decide. Write "options to consider", never "you must".
  Not investment, legal or tax advice. A trademark screen is not legal clearance.
- After the workspace, offer to watch the chosen name with `watch_mark`, so a new filing does
  not arrive unseen.
