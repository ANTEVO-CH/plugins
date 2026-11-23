---
name: payee-check
description: >-
  Check a company against the public record before paying it: the company
  register, its VAT number, its LEI, and the website and email domain an invoice
  or a payment request came from. Use when the user asks "is this supplier
  real", "does this invoice look right", "should I worry about this payment
  request", "a supplier changed their bank details", "is this email domain
  theirs", or pastes a company's details before a payment. Reports what matches
  and what does not, each with its source and date. Never says whether to pay.
  No account needed.
compatibility: >-
  Requires the Antevo Guard connector. If the tools are not available, tell the
  user to add https://api.antevo.ch/mcp/guard/mcp, then stop.
---

# Antevo Guard — Payee check

What the public record says about a company the user is about to pay, and where
the details they were given do not match it.

## Scope (important)
This is a **comparison with public records**, not a judgement on the payee.
**Never call a payee safe, verified, legitimate, trusted or cleared, and never
say a payment should or should not be made.** Say what was checked and what was
found. It checks companies, not people: if the user asks about a director or an
individual, say Guard does not cover people.

## Never send an account number
No tool takes one. If the user gives an IBAN or account number, send only
`account_country`, the two letters it starts with, and `bank_bic` if the invoice
prints the bank's BIC. Do not repeat the full number back in your answer either.

## Step 1 — Gather what the user has
| Input | Where it usually is |
|-------|---------------------|
| `company`, `country` | The invoice header. Ask for the country if it is not clear |
| `registration_number` | Footer of the invoice, or the letterhead |
| `vat_number` | The invoice, for EU suppliers |
| `lei` | Larger companies' invoices and contracts |
| `domain` | The website printed on the invoice |
| `email_domain` | The part after @ in the address the request came from |
| `account_country`, `bank_bic` | The payment block: two letters and the BIC only |

Send what the user has; nothing is required beyond the company and its country.
The more fields, the more there is to compare.

## Step 2 — Check
- `check_payee(...)` for the company.
- `check_domain(domain, expected_domain?)` when the question is only about a
  website or email address, for example "is supp1ier-ltd.com theirs?": pass the
  domain they know as `expected_domain` to get the lookalike comparison.

## Step 3 — Read the result as given
Every result has a `summary` (its `headline` and the counts by level), the
`findings`, the `sources` and a `not_included` sentence.

- **Lead with mismatches.** Each one has a `statement` written by Guard: quote it
  as written, with its source and date. Do not soften or strengthen it.
- **`note`** findings are context worth knowing (a young domain, no mail policy).
  Give them after the mismatches.
- **`on_record`** findings say what matched. Mention them briefly.
- **`not_checked` is not a clean result.** A source that did not answer carries a
  `reason`. Say that source was not checked and why; never fill the gap.
- **No score.** Do not add one, rank the payee, or say "low risk".
- **Keep the `not_included` sentence** with what you quote.

## Step 4 — Output
```
# {company} — compared with the public record

**{headline}**

## What does not match
- {statement} — {source}, {date}

## Worth knowing
- {statement} — {source}, {date}

## What matched
{one line}

**Not checked:** {source} ({reason})

---
*{not_included}*
```

If anything does not match, suggest the user confirms the details with the
company through a contact they already had before this request, not one printed
on the invoice or in the email. That is a suggestion about how to confirm, not a
verdict.

## Next steps
- The user pays this company regularly: offer to save it to their payee book
  (**payee-book-review**; needs a sign-in).
- The user has the invoice or letter itself: **document-check** reads it whole.
