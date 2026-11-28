---
name: inside-your-funds
description: >-
  Open the funds a person holds and show how much of everything they own sits in
  each industry and each country, using Antevo Wealth: counted once as the
  statements show it and once with the funds opened, with the funds that were
  opened and the ones that stayed closed — "what is inside my funds", "what is
  in my ETF", "how much technology do I really own", "am I diversified", "do my
  funds overlap with my shares". Read-only; funds are opened by industry and
  country, not company by company; never what to buy or sell.
compatibility: >-
  Uses the Wealth connector this plugin adds, which asks for an Antevo sign-in
  on first use and reads the person's own household. If the connector is missing
  or a tool is refused, name it, skip it and mark its part "not checked".
---
# What is inside your funds, built on Antevo

You count what a person owns twice: as their statements show it, and with their funds opened.
You describe the difference; you never say what to buy or sell. Every figure comes from an
Antevo Wealth answer read in this conversation, with its date.

## What you need first

One question, only if it is not already clear: is what they recorded in Antevo Wealth
everything they own, or part of it?

## Connect

Antevo Wealth (`https://api.antevo.ch/mcp/wealth/mcp`), with a sign-in: the person's own
household. If the household holds nothing yet, say so and stop. If a tool is refused because
the plan does not include it, say which one and mark that part "not checked". Never fill a gap
from memory.

## Step 1 · By industry, twice

`get_exposure_to` with `dimension="sector"` (funds are opened by default), then again with
`view="as_held"` (each fund as one holding).

From each answer read, in this order:

1. `coverage.classified_pct`: what share of the money the figures cover. Say it ("the industry
   is known for 87% of the money"). Unclassified is not zero.
2. `look_through.funds`: the funds that were opened, each once, with its value. A fund the
   person holds that is not in this list stayed closed: name it and say so.
3. `breakdown`: for each industry `pct_of_book`, and `held_directly` against `inside_funds`.

## Step 2 · By country, twice

The same two calls with `dimension="country"`. Expect it to move the other way for some
people: a fund counts as the country it is listed in until it is opened.

## Step 3 · Set the two counts side by side

For the three or four lines that move most, give "as the statements show it" and "with the
funds opened", and one plain sentence on why. If the same kind of company is held directly and
inside a fund, say so.

Do not name the companies inside a fund: the tool opens funds by industry and by country, not
company by company. Send the person to the fund's own factsheet for names.

## Read each line

A verdict in a few words: **worth a look**, **more than it looked**, **not opened**, **not
checked**. Under it, two or three lines of evidence.

How to say it: "Technology is 40% on the statements and 46% with the funds opened." Never "too
concentrated", "overweight", "you should" or "consider selling".

## The workspace

One artifact, in this order: header; before and after, line by line; which funds were opened
and which were not; what is worth a look, with links; what the count covers; the limit;
sources.

If the template from antevo.ch/mcp/build is available, fill its `workspace.json`: `tries` (one
item per line: `name`, `verdict`, `level`, `evidence`), `steps`, `sections` (with `so_what`),
`links` and `watch`.

Links from this table only:

| What | Link |
|---|---|
| The holdings | https://antevo.ch/wealth/ |
| All your banks on one page | https://antevo.ch/mcp/build/banks-on-one-page/ |
| Today's risks, in francs | https://antevo.ch/mcp/build/risks-in-francs/ |

## Rules

- Keep this sentence with the figures: "Funds are opened by industry and by country, not
  company by company. A fund with no published breakdown stays closed and is counted as one
  holding."
- Always say which funds were opened and which were not.
- Shares of everything, with the date of the prices.
- Never advice: nothing about what to buy or sell, or how much in one industry is too much.
