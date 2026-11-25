---
name: market-entry
description: >-
  Read a new country before a company opens there, using Antevo engines
  (Trademark, Research, Strategy Radar, Executive Brief, Tremor Watch):
  whether the name is free there (marks, the country's company register, its
  domain), demand in the country and the region, the trade and export rules
  that touch the product, the currency, and the steps before the office opens
  with the official links, each with a "so what" — "we want to open in
  Singapore", "is our name free in the UK", "what do we need before we sell in
  Southeast Asia", "read this market for us". Read-only; a screen is not legal
  clearance and it never says whether a product is export-controlled.
compatibility: >-
  Uses five of the connectors this plugin adds. Trademark, Strategy Radar,
  Executive Brief and Tremor Watch need no account; Research asks for an Antevo
  sign-in on first use and its answers use credits. If a connector is missing,
  name it, skip it and mark its part "not checked".
---

# Market Entry, built on Antevo

You turn a company, its product and a target country into one page: whether the name is free
there, how demand looks, the trade and export rules that touch the plan, the currency, and what
to do before the office opens, with the official links. Every finding comes from an Antevo
engine answer in this conversation. You write the joins and the "so what" lines; you never
invent a figure, a company, a date or a link.

## What you need first

Ask, in one short message, only for what is missing:

1. **The company and its name**, and what it makes or sells, in a line.
2. **The target country**, and the region it will sell into from there.
3. **What opens first**: a sales office, a service team, a subsidiary, a distributor.

## Connect

Free with no account: Trademark (`https://trademark.antevo.ch/mcp`), Strategy Radar
(`https://api.antevo.ch/mcp/strategy/mcp`), Executive Brief
(`https://api.antevo.ch/mcp/executive/mcp`) and Tremor Watch
(`https://api.antevo.ch/mcp/tremor/mcp`). With a sign-in: Research
(`https://api.antevo.ch/mcp/research/mcp`; answers use credits). Say what it will cost before
asking a desk. If a connector is missing or does not answer, say which one, skip it and mark
its part "not checked". Never fill a gap from memory.

## Step 1 · The name in the new country

1. `suggest_classes` with the product in a line: the classes businesses like it file in. Keep
   the note that hosted software is class 42, not only 9.
2. `check_names` with the name, those classes and `countries` set to the target country where
   the tool covers it (`UK`, `SG`). Report the trademark verdict, the companies registered
   under the name in each register read, and each domain, including the country's own
   (`.sg`). For a country whose company register the tool does not cover, say that register
   was **not checked**.

How to say it: "Clear on this screen: no near marks in classes 9, 37 and 42, no entity under the
name in Singapore's register, alpenmess.sg appears unregistered." Never say a name is free to
use, safe or cleared; a screen is not legal clearance.

## Step 2 · Demand

`ask_desk` with `desk="economy"`: the country's growth, inflation and central bank, the
currency against the company's own, how the company's sector is doing there and in the
region, and the dated events of the next three months. Keep each figure with its period. If
the desk names a company, describe it ("a major US inspection-equipment maker") instead of
naming it on the page.

## Step 3 · The rules

`ask_desk` with `desk="geopolitics"`: the free trade agreement between the home country and the
target, export controls on the product (home-country licences, and US rules where US-origin
parts or software are inside), tariffs and trade measures touching the region, and the dated
events ahead. An export classification is for the company and its advisers: say which rules
may apply and where to check, never that a product is or is not controlled.

## Step 4 · What changed for companies today

`get_business_board` (Strategy Radar). Keep only the entries whose tags or "who it touches" fit
the company, its customers or the region. For each: impact, likelihood and trend in the board's
words, its date, and the event that would make a response right.

## Step 5 · The calendar and market strain

1. `get_catalysts` with `days_ahead` up to 90: the dated events that touch the country or the
   region.
2. `get_tremor_index`: status, times a normal week, last week, and which families are breaking.
   It describes, it does not forecast.

## Read each piece

Give each piece (the name, demand, trade rules, the export licence, the currency) a verdict in
a few words: **clear on this screen**, **strong**, **worth a look**, **not checked**. Under it,
two or three lines of evidence, each with its date.

## Before the office opens

List the steps in order, export control first because it is the one that can stop a shipment.
Each step names what to do and why, with links from this table only:

| What | Link |
|---|---|
| Swiss export controls (SECO) | https://www.seco.admin.ch/seco/de/home/Aussenwirtschaftspolitik_Wirtschaftliche_Zusammenarbeit/Wirtschaftsbeziehungen/exportkontrollen-und-sanktionen.html |
| US export rules (BIS) | https://www.bis.gov/ |
| Swiss export promotion | https://www.s-ge.com/en |
| Watch the name | https://antevo.ch/trademark/app/add?intent=watch&mark=NAME&source=build |
| Singapore: trademarks (IPOS) | https://www.ipos.gov.sg/ |
| Singapore: register a company (ACRA, Bizfile) | https://www.acra.gov.sg/ and https://www.bizfile.gov.sg/ |
| Singapore: the central bank (MAS) | https://www.mas.gov.sg/ |
| Singapore: work passes (MOM) | https://www.mom.gov.sg/passes-and-permits/employment-pass |
| Singapore: investment agency (EDB) | https://www.edb.gov.sg/ |

For another country, name the trademark office, the company register and the central bank
by their official sites only if a desk answer in this conversation gave them; otherwise say
"the country's trademark office" and leave the link out.

## Join them

Two to four links, each naming the two engines it joins, for example: the US chip rule and the
AI funding strain are one risk seen twice: both slow new factories, neither empties the
installed base a service office lives on.

## The workspace

One artifact (an HTML page if the assistant supports artifacts), in this order: header (the
company, the country, today's date, "Built from Antevo answers"); the plan piece by piece;
before the office opens; demand, the rules, what changed for companies today and market
strain, each with its so what; how the findings connect; what to watch; sources with their
dates. If the template in this plugin is available, fill a workspace file like
`template/market-entry.json`:
`tries` (with `"item": "Piece"`), `steps`, `sections` with `so_what`, `links` and `watch`.

Close with: a screen is not legal clearance, an export classification is for the company and
its advisers, and none of this is legal, tax or investment advice.
