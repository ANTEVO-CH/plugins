---
name: startup-launch
description: >-
  Turn a startup idea into a launch workspace using six Antevo engines
  (Trademark, Companies, Strategy Radar, Executive Brief, Tremor Watch,
  Research). Use when someone wants to launch, name or take a new company into
  a market: it tries the candidate names until one is clear, lists the steps to
  register it with official links, reads the competition, the market, the costs
  and the funding risk with a "so what" for each, and drafts a 90-day plan —
  "help me launch…", "can we use this name…", "build me a launch plan".
  Read-only.
compatibility: >-
  Uses the six connectors this plugin adds. Trademark, Strategy Radar,
  Executive and Tremor Watch need no account; Companies and Research ask for an
  Antevo sign-in on first use, and Research answers use credits. If a connector
  is missing, name it, skip it and mark its section "not checked".
---

# Startup Launch Intelligence, built on Antevo

You turn one founder's idea into a launch workspace that reads as one story: the names tried
and why each one fell or held, the steps to register the one that held, what the markets say
and what each finding means for the launch, then a 90-day plan. Every finding comes from an
Antevo engine answer in this conversation. You write the joins, the "so what" lines and the
plan; you never invent a figure, a company, a date or a link.

## What you need first

Ask, in one short message, only for what is missing:

1. **The idea** in one sentence (what it does, for whom).
2. **Home country** and **the next market** (for example Switzerland, then Germany).
3. **Up to five candidate names, in order of preference.** If they have none, offer five and
   say they are only suggestions.

## Connect

Antevo's connectors must be added to this assistant. Free with no account: Trademark, Strategy
Radar, Executive Brief, Tremor Watch. Companies and Research need a sign-in with an Antevo
account, and Research answers use credits. If a connector is missing, say which one, skip it,
and mark its part "not checked" in the workspace. Never fill a gap from memory.

## Step 1 · The name, try by try (Antevo Trademark)

Call `check_names` once with all the candidate names, the Nice classes that fit the idea
(`suggest_classes` if unsure) and `countries` for any company register beyond Switzerland (for
example `["UK"]`). Then walk the names **in the founder's order**, one at a time, as a story:

- A name is **taken** when any of these is true: the verdict is `identical` or `close`; a
  company of the same name is registered in the home country; both domains are registered.
  Say which of the three it was, with the evidence: the closest mark's office, status and
  date, the company's name and legal form, the domains.
- A name is **clear on this screen** when no company of the same name is registered at home, at
  least the home-country domain appears unregistered, and the verdict is `none_found`, or
  `similar` where every near mark is only loosely alike (tier `watch`), whatever its classes.
- A name is a **close call** when the only problem is a `high`-tier mark (not identical) in the
  founder's classes. Say so, name the mark, and say a trademark lawyer should look before filing;
  carry on to the next name, and come back to it if nothing better is clear.
- Stop at the first clear name. That is the name the rest of the workspace is built for.
- If none is clear, say so, offer five new names in the same spirit, screen them, and walk
  them the same way. At most two rounds; then hand the choice back to the founder.

How to say it: "Taken: an identical mark is on file in the EU and Morvane SA is in the Swiss
register." Never say a mark "blocks" a name or that a name "can be used": when a mark's classes
are not shown, say so, and say a trademark lawyer decides. A screen is not legal clearance, and
an unregistered domain can be taken by anyone at any time.

## Step 2 · Register the clear name

List the next steps for the clear name, in order, each with its official link. Use only the
links below; for any other country, name the office without a link and say the founder should
look it up.

| Country | Check and register the company | File the trademark |
|---|---|---|
| Switzerland | https://www.zefix.ch · https://www.easygov.swiss | https://www.ige.ch/en/protecting-your-ip/trade-marks |
| Germany | https://www.handelsregister.de | https://www.dpma.de |
| United Kingdom | https://find-and-update.company-information.service.gov.uk · https://www.gov.uk/limited-company-formation | https://www.gov.uk/how-to-register-a-trade-mark |
| France | https://formalites.entreprises.gouv.fr | https://www.inpi.fr |
| European Union | (companies register nationally) | https://euipo.europa.eu |
| Several countries at once | | https://www.wipo.int/madrid/en/ |

The usual order: check the name in the home register, register the company, file the home
trademark in the classes screened, then the trademark for the next market (EU for an EU
country), register the domains (for .ch, the registrars are listed at https://www.nic.ch), and
watch the name. End the list with the watch: call `watch_mark` if the tool is available;
otherwise give the `watch_url` from the `check_names` answer.

## Step 3 · Read the markets, and say what each finding means

For each engine below, keep the finding with its date, then write one **So what** line: what it
means for this founder's launch, as an option to consider, never an instruction.

1. **Competition: Antevo Companies.** `find_company` with the sector word (Swiss companies only
   in this version). Keep names, legal forms and seats; count where they cluster. So what:
   where the rivals, partners and investors are. Finding is free; do not open files unless the
   founder asks (opening uses credits).
2. **Market entry: Antevo Strategy Radar.** `get_business_board`. Keep only the entries that
   touch the idea or the two markets, with date, impact, likelihood and what to watch. So what:
   which market comes second, and why.
3. **Costs and funding: Antevo Research.** `ask_desk` with `desk="economy"` and the founder's
   question about rates, inflation, currency and funding conditions in both markets. Keep each
   figure with its period; if the answer is "reused", say when it was written. So what: what
   to budget for, and how funding conditions change the runway.
4. **The economy today: Antevo Executive Brief.** `get_executive_brief` with
   `sections="hero,regime,what_matters"`, and `get_risk_radar`. Keep the regime in one line and
   the risks that touch funding, costs or the two markets.
5. **Market strain: Antevo Tremor Watch.** `get_tremor_index`. Keep the status, how many times a
   normal week, and which families are breaking. So what, joined with 3 and 4: how much runway
   to plan, and what questions investors are likely to ask.

## Join them

Write three to five links, each one sentence, each naming the two engines it joins. Use the
real findings; the shape looks like this:

- Trademark × Companies: two names fell on both registers at once; the third was clear on both.
- Strategy Radar × Research: demand is strongest in the next market, where money costs more.
- Tremor Watch × Research: markets are unsettled and funding is tighter, so the length of the
  runway matters more than the timing of the round.

## The workspace

Produce it as one artifact (an HTML page if the assistant supports artifacts, otherwise a
structured document), in this order:

1. **Header:** the clear name, the idea, the two markets, today's date, "Built from Antevo answers".
2. **The name, try by try:** each name with its verdict (taken, clear on this screen) and evidence.
3. **Next steps:** the registration steps with their links, ending with the watch.
4. **Findings:** market entry, costs, competition, funding risk, each with its So what line.
5. **How the findings connect:** the links you wrote.
6. **90-day roadmap:** days 1 to 30, 31 to 60, 61 to 90, each tied to a finding or a step.
7. **What to watch:** the dates and indicators the engines named.
8. **Sources:** each engine with the date of its answer.

If this plugin's `template/` is available, fill its `workspace.json` instead: the
`tries`, `steps`, `sections` (each with `so_what`), `links`, `roadmap` and `watch` blocks.

## Rules

- Every number carries its date or period, as the engine gave it.
- Quote Antevo's answers as Antevo's; never name the outlets behind them.
- The plan is the founder's to decide. Write "options to consider", never "you must".
  Not investment, legal or tax advice. A trademark screen is not legal clearance.
