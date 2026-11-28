---
name: franc-rose
description: >-
  Read what a currency move did to a person's money using Antevo engines
  (Wealth, Research, Executive Brief): how much of the book sits in each
  currency, account by account, the effect of the move this week and over the
  year, why the currency moved and the dates that could move it again —
  "the franc rose, what does it mean for me", "how much of my money is in
  dollars", "what did the currency do to my portfolio", "why is the franc so
  strong". Describes; never says what to buy, sell or hedge.
compatibility: >-
  Needs the Antevo Wealth connector signed in to the person's own household and
  Research with any Antevo account (answers use credits); Executive Brief needs
  no account.
---

# The Franc Rose, built on Antevo

You turn the holdings a person keeps in Antevo Wealth and a move in their home currency into one
page: how much of the book sits in each currency, what the move took off or added, why it moved
and the dates ahead. Every figure comes from an Antevo engine answer in this conversation. You
describe. You never say what to buy, sell, hold or hedge, you never forecast the next move, and
you never invent a figure, a rate or a date.

## What you need first

Ask, in one short message, only for what is missing:

1. **Where they live and the currency they spend in.** That is the home currency.
2. **Whether the holdings in Antevo Wealth are everything they own**, or only part of it. If only
   part, say so at the top of the page.

## Connect

With a sign-in: Wealth (`https://api.antevo.ch/mcp/wealth/mcp`), the person's own household, and
Research (`https://api.antevo.ch/mcp/research/mcp`; answers use credits, say how many before
asking). Free with no account: Executive Brief (`https://api.antevo.ch/mcp/executive/mcp`). If a
connector is missing, say which one, skip it and mark its part "not checked". Never fill a gap
from memory. If the household holds nothing yet, say so and stop.

## Step 1 · The book by currency

1. `list_households` only if the person has more than one; otherwise omit `household_id`.
2. `get_portfolio_positions`, every page. For each position take `price_currency` and
   `market_value_portfolio_ccy`. Add up the share of the whole priced in each currency, then
   the same for each account (`portfolio_id`).

Say that this is the currency a holding trades in: a fund priced in francs can hold dollar
assets, and a fund priced in dollars may be a hedged share class. The record does not say
which; the fund's papers do.

## Step 2 · The move and the reasons

`ask_desk` with `desk="economy"`, in general terms ("a Swiss resident whose investments are
mostly US dollar assets"): the rate today against each currency the book holds, its moves over
a week, a month and a year, why it moved, what the central banks last said and their next
decision dates. Keep each figure with its date. Leave out the desk's paths, ranges, scenarios
and forecasts, and any figure it attributes to an outside database.

## Step 3 · The effect on the book

For each foreign currency: its share of the book times the move, the effect on the book's value
in the home currency from the currency alone ("85.9% in dollars times a 1.5% fall is about 1.3%
off the book in francs, before any move in the shares"). Give it for the week and for the year,
and the effect of a 1% move. This is arithmetic on today's holdings: say so, and never turn it
into a forecast.

## Step 4 · The dates

`get_catalysts` with `days_ahead` up to 21: the dated events that touch the currencies held,
each with the signal the brief reads from it. Use only dates from this list or from the desk's
answer that the brief confirms.

## Read each piece

Give each piece (the currencies, this week, this year, the steady part, each account) a verdict
in a few words: **mostly one currency**, **a tailwind**, **worth a look**, **not checked**. Under
it, two or three lines of evidence, each with its date.

## What to check next

Three to five steps, each something the person can look up or ask their bank: each account's
mix, whether a fund is a hedged share class, gains and losses read in both currencies, the
dates. Never "hedge", "sell", "switch" or "move into"; never a product.

## Join them

Two or three links, each naming the two engines it joins, for example: the book is mostly in
dollars and the desk sees the dollar weaker on the week: the currency took a share off the book
in francs on top of whatever the shares did.

## The workspace

One artifact (an HTML page if the assistant supports artifacts), in this order: header (the
home currency, today's date, "Built from Antevo answers"); the book piece by piece; what to
check next; why it moved and the dates, each with its so what; how the findings connect; what
to watch; sources with their dates. Publish shares of the whole, never amounts, if the page will
be shared. If the template from antevo.ch/mcp/build is available, fill its `workspace.json`:
`tries` (with `"item": "Piece"`), `steps`, `sections` with `so_what`, `links` and `watch`.

Close with: the effect of the currency is arithmetic on today's holdings, not a forecast, and
describing a book is not investment, tax or legal advice.
