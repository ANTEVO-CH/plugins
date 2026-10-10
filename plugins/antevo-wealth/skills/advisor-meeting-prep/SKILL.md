---
name: advisor-meeting-prep
description: >-
  Prepare the user for a meeting with their own banker, relationship manager or
  wealth manager: a one-page brief on where their book stands with that bank, what
  needs attention, and the questions worth asking. Use when the user says "I'm
  meeting my banker", "prepare me for my UBS review", "what should I ask my
  advisor", "annual review with my relationship manager", or similar. Read-only:
  it informs the user, it never contacts the bank.
compatibility: >-
  Requires the Antevo Wealth MCP connector. If the Antevo Wealth tools are not
  available, tell the user to connect Antevo Wealth, then stop.
---

# Antevo Wealth — Before you meet your advisor

Send the user into the meeting knowing their own numbers, with sharp questions.
This is not the general portfolio review: it centres on the bank they are meeting,
sets that against the whole book, and ends in questions rather than conclusions.

## Before you start

- **Connector check.** No Antevo Wealth tools → ask the user to connect Antevo
  Wealth, then stop.
- **Household.** Call `list_households`; if there is more than one, ask which.
  Pass that `household_id` on every call.
- **Which bank, which meeting.** If the user hasn't said, ask once who they are
  meeting and whether it covers everything or one account. With no answer, cover
  the whole book.

## Step 1 — Gather (call tools, don't guess)

| What | Tool |
|------|------|
| Accounts and the bank behind each | `list_accounts` |
| Portfolios: id, name, base currency, value; household risk | `get_risk()` (no `portfolio_id`) |
| Holdings | `get_portfolio_positions(limit=100)`, following `next_cursor` to the end |
| The investable book, for scale | `get_net_worth(scope='aum')` |
| Allocation, cost basis, unrealised P&L | `get_net_worth(scope='allocation')` |
| Country and sector exposure | `get_exposure_to` |
| Risk for one portfolio at that bank | `get_risk(portfolio_id=…)` |
| Drift against target | `get_portfolio_drift(household_id, portfolio_id)` |
| Credit | `list_facilities`, then `get_facility` for its terms and collateral |
| Open items | `get_open_breaches`, `get_unread_alerts` |
| Goals against plan | `list_goals` |
| Dates in the next month | `get_upcoming_calendar(days=30)` |

- **Find the bank's share of the book.**
  - Portfolios: match each to the bank by its name.
  - Holdings: keep the positions whose `portfolio_id` is one of that bank's.
  - Credit: match each facility through its `account_id` to the account's
    institution in `list_accounts`.
  - If a match is unclear, ask rather than guess.
- **Empty book.** When a result carries `empty_book: true`, say nothing has been
  added yet, pass on its `next_step`, and stop.

## Step 2 — Find what matters for this meeting

- **Their share.** What this bank holds, and its share of the investable book.
  Work out a share only when both figures are in the same currency. Otherwise
  show both values with their currencies.
- **Concentration.** The largest holdings at this bank and their weight. Flag any
  that are also large across the whole book.
- **Antevo's checks.** Open breaches are Antevo's own concentration checks, not
  the bank's mandate limits. Say "Antevo's concentration check flags…". Drift that
  comes back `no_targets` means "no target set", not "on target".
- **Credit.** Utilisation, rate and maturity. Quote the margin-call loan-to-value
  only if the facility's `terms` give it; otherwise make headroom a question.
- **Goals.** List the goals behind plan. Never say which bank funds one: the
  tools don't link them.
- **Dates.** A review due, a document expiring, a promised follow-up.
- **What Antevo cannot see.** Fees and performance against a benchmark are not in
  these tools. Turn them into questions; never estimate them.

## Step 3 — Write the brief

```
# Meeting brief — {bank or adviser} · {date}

**Where you stand.** {2–3 lines: what this bank holds, its share of the book, the
one thing to raise.}

## Your book with {bank}
- {value, currency, as-of}; {share of investable book, or both values}
- Largest holdings: {name, weight}; allocation: {classes}
- Antevo's concentration checks: {flags or "none"}; drift: {status or "no target set"}

## Credit with {bank}           (omit if none)
- {facility}: {drawn}/{limit}, {rate}, matures {date}; {headroom, or "ask"}

## Goals and dates
- Goals behind plan: {goal, gap}
- Coming up: {review or expiry dates}

## Questions to ask
1. {tied to a finding: "X is {n}% of what you manage for me. Is that intended?"}
2. What did I pay in total this year: management fee, custody, product costs, and
   any retrocessions?
3. How has each mandate done against the benchmark we agreed?
4. …

---
*From your Antevo Wealth data as of {dates}. Informational only, not investment,
tax or legal advice.*
```

## Guardrails

- **Questions, not verdicts.** Never tell the user to buy, sell, move money or
  change banks. Raise the point; the decision is theirs and their adviser's.
- **Cite, don't invent.** Every figure from a tool result, with its date. Fees,
  returns and benchmarks Antevo doesn't hold are questions, never numbers.
- **No probabilities.** Don't put odds on markets or outcomes.
- **Read-only.** This skill never writes, and never sends anything to the bank.
