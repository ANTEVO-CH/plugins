---
name: a-banks-monday
description: >-
  Prepare a bank's or wealth manager's week from Antevo's tools: today's risks,
  what each what-if would do to the firm's own income, to a client household and
  to the loans against its portfolios, and which business clients today's
  developments touch, ending in notes for each client meeting — "what does this
  do to our book", "which clients are affected", "how close are our Lombard loans
  to their limits", "prepare my client meetings", "what would a market shock do
  to our revenues". Read-only; Antevo's figures and the bank's own are kept
  apart, a what-if is not a forecast, and it never says a margin call will happen.
compatibility: >-
  Uses four of the connectors this plugin adds. Wealth asks for an Antevo sign-in
  on first use and reads the client household the person is signed in to.
  Executive Brief, Tremor Watch and Strategy Radar need no account. If a
  connector is missing or a tool is refused, name it, skip it and mark its part
  "not checked".
---

# A bank's Monday, built on Antevo

You prepare a bank's week from Antevo's answers and the bank's own figures. You keep the two
apart, show the arithmetic between them, and never forecast, advise or say a margin call will
happen. Every Antevo figure comes from an answer read in this conversation, with its date.

## What you need first

Three things from the person, in their own words. Do not invent any of them.

1. How their client assets split between cautious, balanced and growth mandates (shares that
   add to 100%).
2. How their income splits between fees charged on client assets, dealing (transactions) and
   interest, and their own assumptions for dealing and interest in a market shock (for example
   "dealing up 5%, interest down 8%"). If they give none, leave those two lines unchanged and
   say so.
3. The business clients to check, each in a few words: what it sells, to whom, where it buys.

## Connect

Free, no account: Executive Brief (`https://api.antevo.ch/mcp/executive/mcp`), Tremor Watch
(`https://api.antevo.ch/mcp/tremor/mcp`), Strategy Radar (`https://api.antevo.ch/mcp/strategy/mcp`).
With a sign-in: Antevo Wealth (`https://api.antevo.ch/mcp/wealth/mcp`), for a client household
the person has access to. If a tool is refused, say which one and mark that part "not checked".
Never fill a gap from memory.

## Step 1 · What is unfolding

**Executive Brief** `get_risk_radar`: today's risks. For each: `title`, `trend`, `impact`,
`mornings_on_radar`, `watch_indicator`. **Tremor Watch** `get_tremor_index`: `status` and
`times_normal` for the week, and last week's. Say the week's date. It describes; it does not
forecast.

## Step 2 · The bank's own plan

**Wealth** `get_today_brief` on a household whose portfolios stand for the three mandate types
(the person's own model portfolios, or Antevo's example household). In `risk_scenarios`, each
risk with a `scenario` has `by_portfolio`: the fall of each portfolio under that what-if.

For each such risk:

- client assets = each mandate's share × that mandate's fall, added up;
- fees on assets move by the same percentage;
- dealing and interest move by the bank's own assumptions, marked as the bank's;
- income = each income line's share × its change, added up. Show the line of arithmetic.

A risk with no what-if gets no figure: say so. Never pair a risk with a what-if yourself.

## Step 3 · One client, and the loan

For each client household the person is signed in to, from the same `get_today_brief`:

- `loans`: each loan with something pledged. `today` gives the loan as a share of what is
  pledged (`loan_to_value`), the agreed limit (`max_ltv`), the second level
  (`margin_call_ltv`), and how far the pledged holdings can fall before each
  (`fall_to_limit`, `fall_to_margin_call`). `across_scenarios` says how many what-ifs take the
  loan past each level and which takes it furthest.
- in `risk_scenarios`, each risk's `loans`: where the loan would stand under that what-if
  (`loan_to_value_after`, `status_after`) and what would bring it back to the limit
  (`repay_to_limit`, `pledge_more_to_limit`).

`get_facility` gives one loan in full, with each pledged holding and its value. If a loan has
no agreed limit recorded, say so and give no verdict. `list_accounts` and
`get_exposure_to` show what the client holds at other banks and inside its funds.

Say "the level where the bank may ask for more security", not "margin call". What a bank does
at each level is set by the loan agreement.

## Step 4 · The business clients

**Strategy Radar** `get_business_board`: today's lines. For each business client, name the
lines whose `tags` and `who_it_touches` fit what the person told you about it, with the line's
`act_when`. If none fits, say none fits. Do not stretch a line to make it fit.

## Step 5 · Notes for each meeting

For each client, five lines at most: what moved; the figure and the what-if's name; what to
ask the client; what to bring. No recommendation, no product.

## The workspace

One artifact, in this order: header; the same morning from each seat (the chief executive, the
bank's own plan, each client, each business client); what is worth a look, with links; the
loan against every what-if; the bank's client assets risk by risk; what the bank does not see;
sources.

If the template from antevo.ch/mcp/build is available, fill its `workspace.json`: `tries` (one
item per seat: `name`, `verdict`, `level`, `evidence`), `steps`, `sections` (with `so_what`),
`links` and `watch`.

Links from this table only:

| What | Link |
|---|---|
| How the what-ifs work | https://antevo.ch/stress-testing/ |
| Today's risks, in francs | https://antevo.ch/mcp/build/risks-in-francs/ |
| All your banks on one page | https://antevo.ch/mcp/build/banks-on-one-page/ |
| Strategy desk | https://antevo.ch/mcp/build/strategy-desk/ |
| Today's read | https://antevo.ch/executive/ |

## Rules

- Keep this with the figures, every time: "A what-if is not a forecast: the risk may play out
  differently, or not at all."
- Mark every figure as Antevo's answer or the bank's own. Never present the bank's assumption
  as an Antevo answer, and never invent an assumption the person did not give.
- A loan is measured only against the limit recorded for it. Never say a margin call will
  happen, and never say what the bank or the client should do.
- Never pair a risk with a what-if yourself, and never give a figure the tool did not give.
- Client names stay in the conversation. Do not put a real client's name in anything shared.
- Never advice: nothing about what to buy, sell or hedge.
