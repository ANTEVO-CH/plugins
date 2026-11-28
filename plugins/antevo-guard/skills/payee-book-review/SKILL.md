---
name: payee-book-review
description: >-
  Work through the user's Antevo Guard payee book: what changed on the
  companies they pay, the alerts still open, and adding or removing a payee.
  Use when the user asks "what changed on my suppliers", "any alerts", "add
  this supplier to my book", "remove X", "dismiss that alert", or wants a
  review before a payment run. Saving, removing and dismissing return a
  preview first and change nothing until the user says yes. Needs an Antevo
  sign-in.
compatibility: >-
  Requires the Antevo Guard account connector. If my_payees is not available,
  tell the user to add https://api.antevo.ch/mcp/guard/me/mcp and sign in, then
  stop.
---

# Antevo Guard — Payee book review

The companies the user pays, re-read against the public record, and what changed.

## Scope (important)
An alert says a public record changed: a new registered address, a company
struck off, a domain that started resolving elsewhere. It does not say the
company did anything wrong. **Never call a change suspicious or a payee safe.**
Say what changed, from what to what, with the source and date.

## Step 1 — Read
| Need | Tool |
|------|------|
| The book, with last check and open alerts per payee | `my_payees()` |
| What changed | `my_alerts(status="open")`; `"dismissed"` or `"all"` for history |
| Credits left (for document checks) | `get_credit_balance()` |

## Step 2 — Present, most consequential first
1. Alerts on payees the user is about to pay, if they said which.
2. A company no longer active on its register, or a changed registered name.
3. Changes to the website or email domain.
4. Everything else, briefly.

For each alert: the payee, what changed, the date it was seen, the source.
Then the payees not re-read recently, if any, and why (a plan without re-checks,
or a source that did not answer).

## Step 3 — Change the book, only with a yes
Every write returns a preview with a `human_message` and changes nothing:

| Action | Tool |
|--------|------|
| Save a payee | `save_payee(company, country, ...)` (the payee-check inputs; never an account number, only `account_country` and `bank_bic`) |
| Remove a payee and its history | `remove_payee(payee_id)` |
| Mark an alert as expected | `dismiss_alert(alert_id, reason?)` |

Show the preview's `human_message`, wait for the user's yes, then call again with
`confirm=true`. A yes covers that one change only. A dismissed alert stays in the
payee's history and can be undone on the web page.

## Output
```
# Your payee book — {n} companies

## Open alerts
### {payee}
{what changed: from → to} — {source}, {date}

## Not re-read lately
- {payee}: {why}

---
*{not_included}*
```

## Guardrails
- Never save, remove or dismiss without the user's yes to that preview.
- Never call a payee or a change safe or suspicious: say what changed.
- Never send or repeat an account number.
