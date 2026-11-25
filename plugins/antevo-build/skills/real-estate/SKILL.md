---
name: real-estate
description: >-
  Read a property purchase before signing, using Antevo engines (Companies,
  Guard, Research, Executive Brief, Tremor Watch): the seller in the register,
  where the deposit goes, the market where the buyer buys, the mortgage and
  the lending rules, the price against history, and what to do before signing
  with the official links, each with a "so what" — "check the seller", "is
  this deposit request right", "how is the market where I am buying", "what
  should I do before I sign". Read-only; never says whether to buy.
compatibility: >-
  Uses five of the connectors this plugin adds. Guard, Executive Brief and
  Tremor Watch need no account; Companies and Research ask for an Antevo
  sign-in on first use. A company file uses 50 credits and Research answers use
  credits. If a connector is missing, name it, skip it and mark its part "not
  checked".
---

# Real Estate Acquisition, built on Antevo

You turn one planned purchase into a buyer's workspace that reads as one story: who sells, where
the deposit goes, how the market stands where they buy, what the mortgage asks of them, where
the price stands against history, and what to do before signing, with the official links. Every
finding comes from an Antevo engine answer in this conversation. You write the joins and the
"so what" lines; you never invent a figure, a company, a date or a link.

## What you need first

Ask, in one short message, only for what is missing:

1. **The property and the place**: what it is (an apartment, a house, a building) and where.
2. **A home or to let.**
3. **The companies named in the offer**: the seller, and whoever asks for the deposit (a
   developer, an agent). If the seller is a person, say that Antevo checks companies, not
   people, and skip Step 1's file.
4. **The buyer in one line**: with a mortgage or not, and whether they live in Switzerland.

Companies finds Swiss companies by name in this version. For a purchase in another country, say
so, run Guard where it covers the register (Cyprus, Switzerland, the UK, Singapore), ask the
desks about that country, and name the land register there without a link.

## Connect

Free with no account: Guard (`https://api.antevo.ch/mcp/guard/mcp`), Executive Brief
(`https://api.antevo.ch/mcp/executive/mcp`) and Tremor Watch
(`https://api.antevo.ch/mcp/tremor/mcp`). With a sign-in: Companies
(`https://api.antevo.ch/mcp/companies/mcp`; finding is free, a file uses 50 credits) and
Research (`https://api.antevo.ch/mcp/research/mcp`; answers use credits). Say what it will cost
before opening a file or asking a desk. If a connector is missing or does not answer, say which
one, skip it and mark its part "not checked". Never fill a gap from memory.

## Step 1 · The seller, check by check

1. `find_company` with the seller's name. Keep every entry that carries the name: if there are
   several, the buyer must know which one signs.
2. `company_file` with the `entity_id` of the one named in the offer: register status, seat,
   stated purpose in a few words, parent on GLEIF, sanctions lists.
3. `company_file` with `layer="register"`: how many notices, since when, and this year's dates.
   If a notice carries details (capital, auditor, name, seat), name them; if it says only
   "register entry changed", give the date and link the notice.

Give each check a verdict: **on the record**, **not found** (sanctions lists), **worth a look**
(several companies with the name, recent changes), a **mismatch** (the record contradicts the
offer), or **not checked**.

## Step 2 · Where the deposit goes

`check_payee` (Guard) with the company that asks for the deposit, its country, and the website
and email domain the request came from. Send `account_country` (the two letters the IBAN starts
with) and never the account number. Report what Guard found, line by line, with how many of its
sources answered. Never call a payee safe, verified or cleared, and never say a payment should
or should not be made. Always add: confirm the payee and the account by phone, on a number the
buyer looked up themselves, and ask on what terms the deposit comes back.

## Step 3 · The market, the money, and so what

For each, keep the finding with its date and write one **So what** line for this buyer, as
something to weigh:

1. **The market**: `ask_desk` with `desk="real_estate"` and the buyer's question about prices,
   vacancy, supply and, for a property to let, rents, where they buy. Keep each figure with its
   period.
2. **The mortgage**: `ask_desk` with `desk="mortgages"`: rates for SARON-linked and fixed
   loans, how they are set, where forecasters see them, and the lending rules (own funds,
   affordability, paying down). For a property to let, ask for the rules that apply to it.
3. **The price against history**: `search_macro_indicators` (Executive Brief) with "house
   prices" and the country, then `get_macro_series` with the ticker. Say where the index stands
   against its last peak, how far it fell after that peak and how long it took to come back.
   Compute only from the values returned, and give the quarter of the newest value: it is a
   quarter end, not today.
4. **Market strain**: `get_tremor_index`: status, times a normal week, last week, and the bonds
   family. It describes, it does not forecast.

## Step 4 · Before signing

List what to do, in order, each with its official link. Use only these links; for any other
country, or a canton's own office, name it without a link.

| What | Link |
|---|---|
| The seller's register extract: the exact company and who may sign | https://www.zefix.ch |
| The notices themselves | the `url` of each notice from Step 1, or https://www.shab.ch |
| The land register in Switzerland (the canton keeps it) | https://www.cadastre.ch/de/grundbuch-schweiz |
| Public-law restrictions on a plot: zoning, building lines, contaminated sites | https://www.cadastre.ch/de/oereb-kataster |
| Buying as a person abroad (a permit may be needed) | https://www.bj.admin.ch/de/grundstueckerwerb-durch-personen-im-ausland |
| The mortgage reference rate, for a property to let | https://www.bwo.admin.ch/de/referenzzinssatz |
| Watch the seller | `watch_company` if the tool is available, otherwise https://antevo.ch/companies/ |

Always add: ask two lenders for dated offers and how long each holds; and in Switzerland a
property sale is valid only as a notarised deed, so the draft deed is the document to have
read. A reservation is not the purchase.

## Join them

Two to four links, each naming the two engines it joins, for example: the seller is on the
register and on no list read while its mail domain publishes no mail policy, so the weak point
is the payment instruction, not the company.

## The workspace

One artifact (an HTML page if the assistant supports artifacts), in this order: header (the
property and the place, today's date, "Built from Antevo answers"); the seller and the deposit
check by check; before you sign; the market, the mortgage, the price against history and market
strain, each with its so what; how the findings connect; what to watch; sources with their
dates. If the template in this plugin is available, fill a workspace file like
`template/real-estate.json`:
`tries` (with `"item": "Check"`), `steps`, `sections` with `so_what`, `links` and `watch`.

## Rules

- Never say a seller is safe, sound or cleared, and never guess why a notice was filed. Nothing
  about any person's conduct. A check of public records is not a legal review of the purchase.
- Never say whether to buy, what to offer or which loan to take. Describe the market; do not
  forecast a price.
- Every figure keeps its date or period. Quote Antevo's answers as Antevo's; never name the
  outlets behind them.
- Not investment, legal or tax advice. The decision stays with the buyer.
