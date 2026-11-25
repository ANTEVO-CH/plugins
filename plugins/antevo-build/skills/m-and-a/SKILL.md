---
name: m-and-a
description: >-
  Map a niche and read a shortlist of companies before any approach, using
  Antevo engines (Companies, Trademark, Strategy Radar, Tremor Watch,
  Research): who is registered in the niche, each shortlisted company's
  register, notices and brands, what to check before a first approach with the
  official links, and the deal climate (financing, currency, demand, market
  strain) with a "so what" for each — "who is in this niche", "read these
  companies before we call them", "is now a good climate for a deal".
  Read-only; never says a company is for sale.
compatibility: >-
  Uses five of the connectors this plugin adds. Trademark, Strategy Radar and
  Tremor Watch need no account; Companies and Research ask for an Antevo
  sign-in on first use. A company file uses 50 credits and Research answers use
  credits. If a connector is missing, name it, skip it and mark its part "not
  checked".
---

# M&A Intelligence, built on Antevo

You turn one niche into a buyer's workspace that reads as one story: who is registered in it,
the shortlist read company by company, what to check before a first approach with the official
links, the deal climate with what each finding means, and what to watch. Every finding comes
from an Antevo engine answer in this conversation. You write the joins and the "so what" lines;
you never invent a figure, a company, a date or a link.

## What you need first

Ask, in one short message, only for what is missing:

1. **The niche**: a word that appears in company names (for example "robotics"), or a list of
   company names.
2. **The country.** Companies finds Swiss companies by name in this version; for another
   country, say so and work from names and registers the buyer gives.
3. **How many to read closely**: two to five. Each company file uses 50 credits; re-reading it
   is free for 30 days.
4. **The buyer in one line**: what it sells, in which currency, and whether a deal would need
   debt.

## Connect

Free with no account: Trademark (`https://trademark.antevo.ch/mcp`), Strategy Radar
(`https://api.antevo.ch/mcp/strategy/mcp`) and Tremor Watch
(`https://api.antevo.ch/mcp/tremor/mcp`). With a sign-in: Companies
(`https://api.antevo.ch/mcp/companies/mcp`; finding is free, a file uses 50 credits) and
Research (`https://api.antevo.ch/mcp/research/mcp`; answers use credits). Say what it will cost
before opening files or asking a desk. If a connector is missing or does not answer, say which
one, skip it and mark its part "not checked". Never fill a gap from memory.

## Step 1 · Map the niche

`find_company` with the niche word, and one or two variants if the buyer agrees. It returns
about ten at a time; `"complete": false` means more exist, so say how many were read. Keep
names, legal forms and seats, and count them. Do not open files at this step.

## Step 2 · The shortlist, company by company

Agree the shortlist with the buyer, say the credits, then for each company:

1. `company_file` with its `entity_id`: register status, seat (say so if it differs from the
   search), stated purpose in a few words, parent on GLEIF, sanctions lists, and the news
   section.
2. `company_file` with `layer="register"`: how many notices, since when, and this year's dates.
   If a notice carries details (capital, auditor, name, seat, signatories), name them; if it
   says only "register entry changed", give the date and link the notice.
3. `holder_read` (Trademark) with the legal name: how many marks, which offices and classes,
   their status. "No filings in the registers Antevo reads" is a finding, not a fault.

Give each a verdict: **a quiet record**, **worth a look** (recent changes, thin protection), a
**mismatch** (the record contradicts what the buyer was told), or **not checked**.

## Step 3 · Before a first approach

List what to check, in order, each with its official link. Use only these links; for any other
country, name the register without a link.

| What | Link |
|---|---|
| Today's register extract, purpose, capital, who may sign | https://www.zefix.ch |
| The notices themselves | the `url` of each notice from Step 2, or https://www.shab.ch |
| Patents, designs and Swiss trademarks | https://www.swissreg.ch |
| The company's UID | https://www.uid.admin.ch |
| Watch a company | `watch_company` if the tool is available, otherwise https://antevo.ch/companies/ |
| Follow a holder's filings | `follow_filer` if the tool is available, otherwise the link `holder_read` gives |

Always add: owners who are people are not public in Switzerland, so ask who owns the company
under a confidentiality agreement.

## Step 4 · The deal climate, and so what

For each, keep the finding with its date and write one **So what** line for this buyer, as an
option to consider:

1. **Financing and the currency**: `ask_desk` with `desk="economy"` and the buyer's question
   about policy rates, the cost of debt, the currency and the customers' economy. Keep each
   figure with its period.
2. **Market strain**: `get_tremor_index`: status, times a normal week, last week, which
   families are breaking. It describes, it does not forecast.
3. **The niche's market**: `get_business_board`: only entries that touch the niche or its
   customers, with impact, likelihood and trend.

## Join them

Two or three links, each naming the two engines it joins, for example: two of three companies
have no trademark filings, so what a buyer pays for may sit in patents or know-how, and that is
the first question.

## The workspace

One artifact (an HTML page if the assistant supports artifacts), in this order: header (the
niche, today's date, "Built from Antevo answers"); the shortlist company by company; before a
first approach; the niche and the deal climate; how the findings connect; what to watch;
sources with their dates. If the template in this plugin is available, fill a workspace file like
`template/m-and-a.json`: `tries` (with `"item": "Company"`), `steps`, `sections` with `so_what`,
`links` and `watch`.

## Rules

- Never say or suggest that a company is for sale, in difficulty, or a target, and never guess
  why a notice was filed. Nothing about any person's conduct.
- Every figure keeps its date or period. Quote Antevo's answers as Antevo's; never name the
  outlets behind them.
- Not investment, legal or tax advice. Whether and whom to approach stays with the buyer.
