---
name: clearance-check
description: >-
  Screen a brand, product or company name against the trademark registers, and
  for a shortlist also the company registers and domains, and read who already
  holds anything close. Use when the user asks "is this name taken", "is this
  name free everywhere", "can I use this name", "is my brand trademarked", "has
  anyone registered X", "check this name before I launch", "who owns this
  trademark", or is choosing between candidate names. Also use when they have just been sent
  a cease-and-desist and want to know who is behind the mark. This is a search
  of public registers, not a legal opinion — it never clears a name for use.
  Read-only, no account needed.
compatibility: >-
  Requires the Antevo Trademark connector. If the tools are not available, tell
  the user to add https://trademark.antevo.ch/mcp, then stop.
---

# Antevo — Clearance check

What is already on the registers near a name — trademarks, and for a shortlist the
companies and domains registered under it — and who is behind it.

## Scope (important)
This is a **register search**. It tells the user what exists; it does not tell
them whether they may use a name. That judgement depends on their goods and
services, their territory, their intended use and prior rights that never reach
a register at all. **Never say a name is "clear", "free", "available" or "safe
to use".** Say what was found and what was searched. An unregistered domain is not
reserved for them, and a company register with nothing near the name is not a
clearance either.

## Step 1 — Screen
| Need | Tool |
|------|------|
| Several candidate names, or "is it free everywhere" | `check_names(names, classes?, countries?)` |
| The detail on one name's nearby marks | `screen_mark(mark)` |
| Which classes to pass | `suggest_classes(description)` |
| Who a holder is | `holder_read(name)` |
| A holder's whole book across offices | `company_file(name)` — needs an account |

When the user has more than one candidate, or wants to know whether a name is free
beyond trademarks, start with `check_names`. One call takes up to 15 names and
returns, for each:
- a trademark **verdict** on what is on file (`none_found`, `similar`, `close`,
  `identical`), the near-mark count and the three closest;
- **companies** registered under the same or a similar name, per country: name and
  legal form only. Switzerland is always checked; pass `countries: ["UK", "SG"]`
  when the business trades there;
- **domains**: `<name>.ch` and `.com` (and `.sg`), each `registered`,
  `appears_free` or `not_checked`.

If the user described what they sell, run `suggest_classes` first and pass the
classes. If `check_names` is not available on their server, run `screen_mark` once
per name instead. For one name's full list of nearby marks, use `screen_mark`; its
`registers` field lists where those marks are filed, not every register searched.

## Step 2 — Read the tiers as computed, not as verdicts
Each hit carries a similarity tier. It is a **string-and-phonetic comparison**,
not an assessment of legal confusability. A tier says the names look or sound
alike; whether that matters depends on the goods and the market.

- **Lead with the closest hits.** An identical mark in a live status is the story.
- **Say what was searched.** `sources` in a `check_names` answer cites each
  register; coverage is not universal, and a reader who assumes it is will be
  misled by an absence.
- **An absence is not a clearance.** If nothing came back, say "nothing found in
  the registers we searched" — never "the name is available".
- **`not_checked` is not nothing found.** A register or registry that did not
  answer says so, with a reason (`skipped` explains the ones never asked, such as
  `.co.uk`). Say it was not checked; never fill the gap with a guess.
- **`appears_free` is today only.** The registry had no record when asked; anyone
  can register the domain a minute later.

## Step 3 — Read the holder, where it matters
If a close hit has a named applicant, `holder_read` shows how that holder files:
how much of their book they let lapse, whether their marks cluster where they
trade or spray across unrelated classes.

**Never call anyone a squatter, a troll, or bad-faith.** Those are legal
conclusions, and asserting one about a named party is defamatory if wrong.
Present the pattern — "forty marks, none in the sector they trade in, most
lapsed" — and let the reader and their counsel draw it.

## Step 4 — Output
```
# {name} — what's on the register

**Searched:** {n} registers — {list}
**Found:** {n} marks near this name

## Closest
### {mark} — {register} · {status}
Held by {applicant}. {similarity tier} to "{name}".
{one line on why it matters, if it does}

## The holder behind it
{what their filing pattern shows, evidence first}

---
*Read from the public registers on {date}. Intelligence, not legal advice — a
search is not a clearance, and your counsel advises on use.*
```

If several candidate names are in play, `check_names` already ranks them, fewest
conflicts first — that is the question behind "which of these should I pick", and a
table beats prose: one row per name, with the trademark verdict, the companies on
file and the domains taken. Then offer to watch the one they keep (hand off to
**conflict-review**).

## Guardrails
- **Never clear a name.** No "you're fine", no "safe to proceed".
- **Never call anyone a squatter.** Evidence, not labels.
- **Name the coverage.** Say which registers were searched, every time.
- **Don't infer classes.** If the user has not said what they sell, ask rather
  than assuming a Nice class.
- **Point to counsel** for anything that turns on use, risk or infringement.
- If the user wants to be told when something new appears near their name, hand
  off to **conflict-review** — watching is a different job from screening.
