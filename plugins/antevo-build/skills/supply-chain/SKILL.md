---
name: supply-chain
description: >-
  Check a supply route leg by leg before the next order, using Antevo engines
  (Guard, Executive Brief, Strategy Radar, and Research's shipping and
  geopolitics desks): the supplier, export rules at the origin, the sea route,
  the last mile, fuel and freight. Lists what to settle before the order with
  the official links and says what each finding means — "is our supply chain
  at risk", "what is happening on our route from Asia", "should we order
  early". Read-only.
compatibility: >-
  Uses four of the connectors this plugin adds. Guard, Executive Brief and
  Strategy Radar need no account; Research asks for an Antevo sign-in on first
  use and its answers use credits. If a connector is missing or a desk does
  not answer, name it, skip it and mark what it covers "not checked".
---

# Supply Chain Watch, built on Antevo

You turn one supply route into a workspace that reads as one story: the route checked leg by
leg and what each leg showed, what to settle before the next order with the official links,
what each finding means, and what to watch. Every finding comes from an Antevo engine answer in
this conversation. You write the joins and the "so what" lines; you never invent a figure, a
route, a date or a link.

## What you need first

Ask, in one short message, only for what is missing:

1. **The goods** (what they are, and the product code if they know it).
2. **The supplier**: company, country, website and the email domain orders come from.
3. **The route**: origin port, how the goods travel (sea, air, rail), the ports or hubs on the
   way, the last leg to the site.
4. **When the next order goes out.**

## Connect

Free with no account: Guard (`https://api.antevo.ch/mcp/guard/mcp`), Executive Brief
(`https://api.antevo.ch/mcp/executive/mcp`) and Strategy Radar
(`https://api.antevo.ch/mcp/strategy/mcp`). Research
(`https://api.antevo.ch/mcp/research/mcp`) needs a sign-in with an Antevo account and its
answers use credits; say so before the first question. If a connector is missing or a desk does
not answer, say which one, skip it and mark what it covers "not checked". Never fill a gap from
memory.

## Step 1 · Leg by leg

Walk the route in order and give each leg a verdict: **running** (nothing in the sources read),
**worth a look** (a fact to settle before the next order), **disrupted** (a source says the leg
is closed, diverted or stopped), or **not checked**.

1. **The supplier.** `check_payee` (Guard) with `company`, `country`, `domain`, `email_domain`,
   and `vat_number`, `lei` or `registration_number` if they have them. Report each finding with
   its source. Guard's company registers cover Cyprus, Switzerland, the United Kingdom and
   Singapore; elsewhere say the register was not checked and name the country's register. A
   domain registered days ago or a lookalike of the supplier's usual domain is a **mismatch**:
   say so plainly.
2. **Leaving the origin.** `get_risk_radar` and `get_business_board`: keep only entries on
   tariffs, export rules or curbs that touch the origin countries or the goods (tags such as
   `buys_from:china_and_hong_kong`, `bought_in_components`), with impact, likelihood and trend.
3. **The route.** `get_world_events` three times, one layer each: `waterways` (which listed
   chokepoints the route passes and which countries border them), `hotspots` (where those
   countries rank, with the period the fatality figures cover), and `disasters` with
   `days_back` 7 (only events in the route's countries or near its chokepoints; say plainly if
   there are none). Add `get_business_board` entries with theme `shipping_chokepoints`. Then
   `ask_desk` with `desk="shipping"`: whether the route runs normally, which way ships go
   around a closed passage, port congestion and inland waterways.
4. **Arriving and the last mile.** The shipping desk's answer on the arrival port and the last
   leg. Without it, mark the leg not checked and give the official links from Step 2.
5. **Costs.** `get_business_board` entries on fuel (`energy_commodities`) with the price and
   date the engine gives, and the shipping desk's answer on freight rates. Never quote a figure
   without its date.

For the next three months, `ask_desk` with `desk="geopolitics"` on trade measures and supply
risks for the goods and the origin countries.

## Step 2 · Before the next order

List what to settle, in order, each with its official link where one is given here. For any
other country, name the register or office without a link.

| What | Link |
|---|---|
| Swiss duty and origin rules by product code | https://www.tares.ch |
| EU duty by product code | https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp |
| Rhine gauges | https://www.pegelonline.wsv.de |
| Swiss water levels | https://www.hydrodaten.admin.ch |
| Swiss Rhine ports | https://port-of-switzerland.ch |
| Port of Rotterdam | https://www.portofrotterdam.com/en |
| A Swiss supplier's register entry | https://www.zefix.ch |
| A UK supplier's register entry | https://find-and-update.company-information.service.gov.uk |
| The daily board | https://antevo.ch/executive/strategy/ |

Turn Strategy Radar's own `responses` into steps (a price clause, a second supplier, more
stock, insurance), each with its `right_if`, as options to consider. Always add: confirm any
change of bank details on a phone number you already hold.

## Step 3 · What it means

Write one **So what** line for each finding, as an option to consider: the tariffs and curbs,
what could change the route, fuel, and `get_catalysts` with `days_ahead` 30 for dated events
that touch the origin countries or the goods (a factory survey, a tariff date).

## Join them

Two or three links, each naming the two engines it joins, for example: the tariff plans and the
end of an export-curb pause fall in the same month, so for this buyer they are one risk with
one date.

## The workspace

One artifact (an HTML page if the assistant supports artifacts), in this order: header (the
route, the goods, today's date, "Built from Antevo answers"); leg by leg; before the next order;
what it means; how the findings connect; what to watch; sources with their dates. If the
template in this plugin is available, fill a workspace file like `template/supply-chain.json`: `tries` (with
`"item": "Leg"`), `steps`, `sections` with `so_what`, `links` and `watch`.

## Rules

- Every figure keeps its date or period, as the engine gave it. Quote Antevo's answers as
  Antevo's; never name the outlets behind them.
- A quiet week is "no alerts in the sources read", never "safe". Say what was not checked.
- The options are the buyer's to decide. Not investment, legal, customs or tax advice.
