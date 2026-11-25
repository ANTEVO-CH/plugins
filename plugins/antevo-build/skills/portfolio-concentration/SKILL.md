---
name: portfolio-concentration
description: >-
  Read a portfolio as one book using Antevo engines (Wealth, Tremor Watch,
  Executive Brief): each holding added up across accounts, and how much of the
  whole sits behind one company, one industry, one country and one currency,
  set against what markets did this week, each with a "so what" — "am I too
  concentrated", "is my portfolio diversified", "how much do I have in tech",
  "how much of my money is in dollars", "do my accounts hold the same things".
  Read-only; it describes and never says what to buy, sell or hold.
compatibility: >-
  Needs the Antevo Wealth connector signed in to the person's own household;
  Tremor Watch and Executive Brief need no account.
---
# Portfolio Concentration, built on Antevo

You turn the investments a person has recorded in Antevo Wealth into one page: how much of the whole
sits behind one company, one industry, one country and one currency, what markets did this week,
and what is worth a look. Every figure comes from an Antevo tool answer in this conversation.
You describe. You never say what to buy, sell, hold, reduce or rebalance, and you never invent a
figure, an investment or a date.

## What you need first

Ask, in one short message, only for what is missing:

1. **Where they live and the currency they spend in.**
2. **Whether the investments in Antevo Wealth are everything they own**, or only part of it. If only
   part, say so at the top of the page.

## Connect

With a sign-in: Wealth (`https://api.antevo.ch/mcp/wealth/mcp`), the person's own household. Free
with no account: Tremor Watch (`https://api.antevo.ch/mcp/tremor/mcp`) and Executive Brief
(`https://api.antevo.ch/mcp/executive/mcp`). If a connector is missing, or a tool is refused
because the plan does not include it, say which one, skip it and mark its part "not checked".
Never fill a gap from memory. If the household holds nothing yet, say so and stop: there is
nothing to read.

## Step 1 · The whole portfolio

1. `list_households` only if the person has more than one; otherwise omit `household_id`.
2. `get_portfolio_positions`, every page. Add each investment up across accounts by its ISIN, and
   work out its share of the whole from `market_value_portfolio_ccy`.

Report the largest investment, the largest three and five together, and which investments sit in more
than one account. When you add investments up by ISIN a fund is one line: say so. Step 2 opens funds by industry and by country.

## Step 2 · One industry, one country

`get_exposure_to` with `dimension="sector"`, then `dimension="country"`. Read
`coverage.classified_pct` first and say what share of the portfolio the figure covers ("the industry
is known for 85% of the portfolio"). Unclassified is not zero. Funds are opened by default: read
`look_through.funds` and say which funds were opened; a fund not listed there stayed closed and
counts as one investment.

## Step 3 · One currency

From each position's `price_currency`, the share priced in each currency, set against the
currency the person spends in. Say that this is the currency an investment trades in: a fund priced
in francs can still hold dollar assets.

## Step 4 · The accounts in a past crash

`get_risk`. For each account: the largest position's share, and the worst replayed event with
its fall. Say "a replay of a past event on today's investments, not a forecast". If the tool is
refused, mark this part "not checked".

## Step 5 · The dates that touch the portfolio

`get_upcoming_calendar` with `days` up to 14: results dates for companies held and the main
data days. Leave out everything that does not touch the investments.

## Step 6 · The week in markets

1. `get_executive_brief` with `sections="hero,regime,plain_language"`: what moved and why.
2. `get_tremor_index`, then `get_tremor_pairs` for the family that matches the portfolio (for shares
   across countries, `family="Equity regions"`): which markets are moving together more than
   usual. It describes, it does not forecast.

## Read each piece

Give each piece (one company, one industry, one country and currency, the accounts together) a
verdict in a few words: **spread**, **worth a look**, **not checked**. Under it, two or three
lines of evidence. Give shares of the whole; leave amounts out unless the person asks for them.

How to say it: "17% of the whole is in one company, and it sits in all three accounts." Never
"too concentrated", "overweight", "you should" or "consider selling": the page shows where the
portfolio stands, and where the line sits is for the person and their adviser.

## What is worth a look

Things to look at, never trades. Links from this table only:

| What | Link |
|---|---|
| The investments | https://antevo.ch/wealth/ |
| Past events, replayed | https://antevo.ch/stress-testing/ |
| Today's read on markets | https://antevo.ch/executive/ |
| How markets are moving together | https://antevo.ch/tremor-watch/ |

## Join them

Two or three links, each naming the two tools it joins, for example: the brief says money left
the chip makers this week, and the portfolio shows 9% in one of them: the news and the investments are
one story.

## The workspace

One artifact (an HTML page if the assistant supports artifacts), in this order: header (whose
portfolio, today's date, "Built from Antevo answers"); the portfolio piece by piece; what is worth a look;
what markets did, how they are moving together, the accounts in a past crash and the dates
ahead, each with its so what; how the findings connect; what to watch; sources with their dates.
If the template from antevo.ch/mcp/build is available, fill its `workspace.json`: `tries` (with
`"item": "Piece"`), `steps`, `sections` with `so_what`, `links` and `watch`.

Close with: this describes what the portfolio holds on the date shown; it is not advice to buy, sell
or hold anything, a replay is not a forecast, and it is not investment, tax or legal advice.
