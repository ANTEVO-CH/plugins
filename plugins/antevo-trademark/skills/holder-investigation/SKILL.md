---
name: holder-investigation
description: >-
  Find out who is really behind a trademark holder: an operating company, a
  shell, a serial filer. Starts from the register read, which spends no credit,
  and, only if the user agrees, runs a cited web investigation that uses a
  credit. Use when the user asks "who is behind this filing", "is this company
  real", "dig into this applicant", "investigate this holder", or wants more
  than the register shows before they talk to counsel. Nothing is spent without
  a yes, and credits are never bought in the conversation.
compatibility: >-
  Requires the Antevo Trademark connector (trademark.antevo.ch/mcp). The
  investigation and the credit tools need an Antevo sign-in, which the
  connector asks for when one of them is first used; holder_read needs none.
  If the user does not sign in, say the investigation needs it and stop.
---

# Antevo — Holder investigation

The register says how a holder files. The investigation says who they are.

## Step 1 — Start with what spends no credit
| Need | Tool | Credits |
|------|------|---------|
| How they file: lapses, class spread, leverage | `holder_read(name)` | none |
| Their whole book across every office | `company_file(name)` | none (plan permitting) |
| Credits left, and what each tool that spends costs | `get_credit_balance()` | none |
| A cited web dossier on who they are | `run_investigation(name)` | **one** |

Run `holder_read` first. It often answers the question, and it spends nothing.
Offer the investigation when the register cannot say who the holder is, or when
the user asks for it.

## Step 2 — Ask before spending
Before `run_investigation`, call `get_credit_balance` and tell the user how many
credits it uses, in their numbers. Read it from `prices` (credits per call); do
not assume it.

> An investigation of {holder} uses {credits} credit. You have {remaining} left:
> {monthly_left} included this month and {topup_balance} bought. Shall I run it?

Call it only after a clear yes. One yes covers one holder.

- The same holder again within 30 minutes returns the earlier dossier at no
  charge (`reused: true`). Say that it was reused.
- A failed run costs nothing. Say it failed; do not retry in a loop.

## Step 3 — When there are no credits
If `remaining` is 0, say so plainly, and that included credits reset each month.
Do not suggest buying.

Credits are never bought in the conversation. If the user asks how to get more,
say they are added on their Antevo desk, under Settings → Investigation credits
(https://antevo.ch/trademark/app/settings). If `run_investigation` refuses for
lack of credits, pass its message on once and do not retry. After they say they
have added credits, call `get_credit_balance` to confirm before running
anything.

## Step 4 — Present it as research
The dossier is AI-written from web sources. Relay it as research to check, not
as register fact.

- Keep the two apart: what the registers show (`holder_read`, `company_file`)
  and what the web suggests (the dossier).
- Cite the dossier's sources as it gives them.
- **Never call anyone a squatter yourself.** If the dossier uses the word, quote
  it as the dossier's finding, with its sources, and leave the conclusion to
  their counsel.
- When you quote corporate identity (organisation name, HQ, PermID) from a
  result that carries `attribution`, keep its text with it. That data is
  PermID's, CC BY 4.0.

## Step 5 — Output
```
# Who is behind {holder}

## On the registers
{how they file, from holder_read: lapses, class spread, offices, since when}

## What the web suggests
{the dossier's findings, each with its source}
{red flags, if any, as the dossier states them}

## What to take to counsel
{the two or three facts that matter for an opposition or a negotiation}

---
*Register facts from the public registers, {date}. The investigation is
AI-written research from cited web sources ({credits used}). Intelligence, not
legal advice: your counsel confirms before you act.*
```

## Guardrails
- **Never spend a credit without a yes.** Not for a "quick look", not twice on
  one yes.
- **Never sell.** Credits are bought on the desk, not here: don't suggest
  buying, and don't volunteer prices.
- **Never present the dossier as fact or advice.** It is research to check.
