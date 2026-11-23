---
name: impersonation-watch
description: >-
  Watch for lookalikes of the user's OWN company name: newly registered domains,
  companies and trademark filings close to it, the kind used to send invoices in
  their name. Use when the user asks "is anyone pretending to be us", "watch for
  fake domains of our company", "a customer got an invoice that wasn't from us",
  or "check if someone registered a domain like ours". Starting a watch returns
  a preview first. Needs an Antevo sign-in for the watch; a one-off domain check
  needs none.
compatibility: >-
  Requires the Antevo Guard connector. For a one-off check, check_domain on
  https://api.antevo.ch/mcp/guard/mcp is enough. For a watch, the account
  connector https://api.antevo.ch/mcp/guard/me/mcp with a sign-in.
---

# Antevo Guard — Impersonation watch

New domains, companies and trademark filings that look like the user's own name.

## Scope (important)
Only the user's **own** company names. Do not start a watch on a name the user
does not own or represent; say Guard watches your own name, and for a supplier
use **payee-check** instead.

A lookalike is a string comparison on public records. **Never say a domain or a
company is a fraud, a scam or run by criminals**: say how close it is to the
user's name, when it was registered, and whether it has mail servers. Whether to
act, and how, is the user's call and their counsel's.

## Step 1 — One-off check
If the user has a specific domain in hand ("a customer got an email from
acme-billing.co"), run `check_domain(domain, expected_domain=<their own
domain>)` and report: registration date, first certificate logged, mail records,
and the lookalike comparison. Quote statements as written, with source and date.

## Step 2 — Start a watch
`watch_name(name, domains=[their own domains])` returns a preview with a
`human_message` and starts nothing. Show it, wait for a yes, then call again with
`confirm=true`. Each watch counts against the user's plan; if the plan's watches
are used up, the answer says so.

The watch runs daily. New lookalikes arrive as alerts: read them with
`my_alerts()` (hand off to **payee-book-review** for working through them).

## Output for a one-off check
```
# {domain} next to {their domain}

**Lookalike:** {comparison}
**Registered:** {date} · **First certificate:** {date}
**Mail:** {mail records and policy}

---
*{not_included}*
```

## Guardrails
- Own names only.
- Never label anyone a fraudster: give the record, not the conclusion.
- Never start a watch without the user's yes to the preview.
- Guard cannot take a domain down. For that, point to the registrar's abuse
  contact or their counsel.
