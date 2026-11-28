---
name: banks-on-one-page
description: >-
  Put everything a person or family holds at several banks on one page, using
  Antevo Wealth: what each bank holds, the total, shares against bonds, and each
  company or fund that sits at more than one bank or in more than one portfolio,
  added up — "what do we own in total", "add up my accounts", "all my banks on
  one page", "which bank holds what", "do I hold the same thing twice". Read-
  only; it describes what is held and where, never what to buy or sell.
compatibility: >-
  Uses the Wealth connector this plugin adds, which asks for an Antevo sign-in
  on first use and reads the person's own household. If the connector is missing
  or a tool is refused, name it, skip it and mark its part "not checked".
---
# All your banks on one page, built on Antevo

You add up what a person or a family holds at every bank and show what no single statement
shows. You describe; you never say what to buy, sell or move. Every figure comes from an Antevo
Wealth answer read in this conversation, with its date.

## What you need first

Ask, in one short message, only for what is missing:

1. **How many banks or brokers** hold their investments.
2. **Whether what they recorded in Antevo Wealth is everything**, or only part of it.

## Connect

Antevo Wealth (`https://api.antevo.ch/mcp/wealth/mcp`), with a sign-in: the person's own
household. If the household holds nothing yet, say so and stop: there is nothing to add up. If
a tool is refused because the plan does not include it, say which one and mark that part "not
checked". Never fill a gap from memory.

## Step 1 · The banks

`list_households` only if the person has more than one; otherwise omit `household_id`.
`list_accounts`: each account with its `institution_name` (the bank) and its `account_id`. An
account with no bank named: say so, and call it by its account name.

## Step 2 · Each holding, with its bank

`get_portfolio_positions`, every page. Each holding carries `account_id`: match it to the
account from step 1. Use `market_value_portfolio_ccy` (the household's own currency) for every
sum. Add up per bank, and the total.

Check the total against `get_net_worth` with `scope="aum"`. If the two differ by more than a
rounding, say so and show both.

## Step 3 · Shares, bonds and the rest

`get_net_worth` with `scope="allocation"`: the split by kind of holding, as shares of the total.

## Step 4 · The same thing in more than one place

Add each holding up by its ISIN across every account and portfolio. Report:

- the largest holding and its share of everything,
- the largest three together,
- every holding that sits at more than one bank or in more than one portfolio.

A fund is one line here. Say that this page does not look inside funds, and that
`get_exposure_to` does (the build "What is inside your funds").

## Step 5 · What is not there

`get_net_worth` with `scope="estate"`: property and loans, if any are recorded. If none are,
say "no property and no loans recorded", not "none owned".

## Read each line

Give each line a verdict in a few words: **added up**, **worth a look**, **not checked**. Under
it, two or three lines of evidence with the amounts and the shares.

How to say it: "One company sits in three portfolios: added up, 14% of everything." Never "too
much", "overweight", "you should" or "consider selling".

## The workspace

One artifact, in this order: header; the banks and the total; shares against bonds; what sits
in more than one place; what is worth asking, with links; what is not on the page; sources.

If the template from antevo.ch/mcp/build is available, fill its `workspace.json`: `tries` (one
item per line: `name`, `verdict`, `level`, `evidence`), `steps`, `sections` (with `so_what`),
`links` and `watch`.

Links from this table only:

| What | Link |
|---|---|
| Record an account | https://antevo.ch/wealth/ |
| Inside the funds | https://antevo.ch/mcp/build/inside-your-funds/ |
| Today's risks, in francs | https://antevo.ch/mcp/build/risks-in-francs/ |
| The family file | https://antevo.ch/family-file/ |

## Rules

- Plain words. Amounts in the household's own currency, with the date of the prices.
- The page covers only what has been recorded. Say so every time.
- Describe companies if the person asks for a page to share; name them if it is only for them.
- Never advice: nothing about what to buy, sell, move or how much is too much. That is for the
  person and their adviser.
