---
name: document-check
description: >-
  Read an invoice or a change-of-bank-details letter the user has shared and
  compare the company details on it with the public record and their payee
  book. Use when the user attaches or pastes an invoice, a "we have changed our
  bank" letter, or a payment request email and asks whether it looks right.
  Spends one Antevo credit: always ask first. Needs an Antevo sign-in.
compatibility: >-
  Requires the Antevo Guard account connector. If check_document is not
  available, tell the user to add https://api.antevo.ch/mcp/guard/me/mcp and
  sign in, then stop. Without an account, payee-check covers the company itself.
---

# Antevo Guard — Document check

The company details on a document, read against the public record and, when the
company is in the user's payee book, against what was saved for it.

## Scope (important)
Same rules as **payee-check**: never call a document genuine, a payee safe or
verified, and never say whether to pay. Say what was read, what was compared and
what does not match.

## Step 1 — Ask before spending
`check_document` uses **one credit** (none if no company could be read from the
text). Say so and wait for a yes. If the user is unsure, `get_credit_balance`
shows what they have. Credits are bought on antevo.ch/account, never here: if
the balance is empty, point there.

## Step 2 — Send the text, not the account number
- Pass the document's text as `document_text`, up to 20,000 characters. Guard
  cuts any account number in it to its country before reading further, but do
  not quote the number in your own answer.
- If the user named the payee, or it is in `my_payees`, pass its `payee_id`, so
  the document is compared with what was saved: a new bank country or a new
  email domain on a saved payee is exactly what this is for.
- Pass `country` if the document does not make it clear.

## Step 3 — Read the result
The result has the same shape as a payee check, plus what was read from the
document (`document.fields`) and, with a payee, findings on what differs from
the saved record.

- **Lead with differences from the saved payee**, then mismatches with the
  public record. Quote each `statement` as written, with its source and date.
- If no company could be read, say so; no credit was spent.
- `not_checked` sources are not clean: name them with their reason.
- Keep the `not_included` sentence.

## Step 4 — Output
```
# {document type} from {company}

**Read from the document:** {company}, {country}, {registration / VAT / domain},
bank in {account_country}

## Different from what you saved
- {statement}

## Does not match the public record
- {statement} — {source}, {date}

**Not checked:** {source} ({reason})

---
*{not_included}*
```

When bank details changed, suggest the user confirms the change by calling the
company on a number they already had, not one on this document.

## Guardrails
- Ask before every call: each spends a credit.
- Never repeat a full account number.
- Never call the document genuine or fake: say what matched and what did not.
