---
name: record-holdings
description: >-
  Record holdings the user already owns into their Antevo Wealth book, from a bank
  or broker statement, a screenshot, or a list they type. Use when the user says
  "add my holdings", "record these positions", "here is my UBS statement", "I hold
  200 Nestlé at UBS", or shares a statement and wants it in Antevo. Uses the
  connector's create_portfolio and add_position, which return a plan first and
  write only after the user says yes. Never buys, sells or moves money.
compatibility: >-
  Requires the Antevo Wealth MCP connector with its recording tools
  (create_portfolio, add_position). If they are not available, say this assistant
  cannot record holdings yet, give the user
  https://wealth.antevo.ch/wealth/accounts?add=holding to add them in Antevo
  Wealth, and stop.
---

# Antevo Wealth — Record holdings

Turn what the user holds into recorded positions, exactly as their statement shows,
with their approval before anything is written. Accuracy beats speed: a wrong
quantity in someone's book is worse than a missing one.

## Before you start

- **Tools check.** No `create_portfolio` or `add_position` → follow the
  compatibility note, then stop.
- **Household.** Call `list_households`; if there is more than one, ask which.
  Pass that `household_id` on every call.
- **Who may record.** Only the household's owner or an admin can. If a tool
  refuses on role, or on plan (`forbidden_tier`), pass on its `human_message` and
  any upgrade link, then stop.

## Step 1 — Read the holdings, then check them with the user

From the statement, screenshot or text, list each holding with:

| Field | Notes |
|-------|-------|
| Name | As printed |
| ISIN | 12 characters, if shown. The surest match. |
| Quantity | As printed. For bonds, the nominal. |
| Currency | The holding's currency |
| Bank or broker | Becomes the portfolio |
| Statement date | Recorded as `as_of`, YYYY-MM-DD |
| Cost per unit | Only if the statement shows it in the holding's own currency. Leave it out for bonds: their prices are quoted per 100 of nominal. |

- Copy figures exactly. Never round, convert, or work a quantity out from a value.
- A line you cannot read, or one without a quantity: mark it and ask. Never fill it in.
- Cash balances, loans, cards, pending orders and accrued interest are not
  holdings. List them separately under "add in Antevo Wealth".
- Show the user the table and ask them to confirm or correct it **before any tool
  call**. This is where a misread gets caught.

## Step 2 — Pick the portfolio

- One portfolio per bank or broker is the convention. Pass the bank or broker's
  name as `portfolio`. If no portfolio has that name, `add_position` either lists
  the existing ones (use the right one, or ask) or says there is none yet.
- To create one, call `create_portfolio(name, institution, currency)` without
  `confirm`. Show the plan's `human_message`. Only on a yes, call it again with the
  same arguments plus `confirm=true` and the `plan_id`.

## Step 3 — Record, a few at a time

For each confirmed line, call `add_position(security, quantity, portfolio,
currency, as_of)` without `confirm`, adding `cost_basis_per_unit` only as allowed
in Step 1. Pass the ISIN as `security` when there is one, otherwise the exact name.
Each call returns a plan.

- **Largest first.** Record the holdings in order of value, largest first, so a
  book with a holding limit still shows most of what the user owns.
- **Batches of up to five.** Request the plans, show their `human_message`s
  together and numbered, and ask for one answer. Plans expire after five minutes,
  so never leave a batch waiting.
- **Yes:** call `add_position` again for each, with the same arguments plus
  `confirm=true` and that plan's own `plan_id`. Don't build the call from the
  plan's `confirm_with`. **Partial yes** ("all but 3"): confirm only those.
  **No:** record nothing and ask what to change.
- **Several matches:** the tool returns candidates. Ask the user which, then call
  again with that ISIN. Never choose for them.
- **Not found:** check the ISIN against the statement and ask. Never take a near
  match.
- **Already in that portfolio:** skip it and say so.
- **Held elsewhere:** when the plan shows the same security in another portfolio,
  point it out before asking for the yes, so it is not counted twice.
- **Plan expired:** ask for a fresh plan. Never reuse an old `plan_id`.
- **Book full:** if a call refuses because the user's plan has reached its
  holding limit, stop there. Pass on its `human_message` and upgrade link exactly
  as given, and list the lines not yet recorded. Never quote a price or a plan
  name of your own.

## Step 4 — Close

Summarise in three short lists: recorded (name, quantity, portfolio), skipped and
why, and still to add in Antevo Wealth (cash, loans, property). Then offer one
question the new book can answer, such as where the user is most concentrated
(`get_exposure_to`) or their net worth (`get_net_worth`).

## Guardrails

- **Records, never trades.** If asked to buy, sell, transfer or rebalance, say the
  connector only records what the user already owns.
- **No yes, no write.** A yes counts only after the user has seen that plan's
  `human_message`.
- **Exact figures.** Quantities, prices and dates as the statement shows them.
- **Leave out account numbers and IBANs.** They are not needed, so don't repeat or
  keep them.
- **Not advice.** This is record-keeping, not investment advice.
