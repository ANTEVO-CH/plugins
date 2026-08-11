---
name: clearance-check
description: >-
  Screen a brand, product or company name against the live trademark registers
  and read who already holds anything close. Use when the user asks "is this
  name taken", "can I use this name", "is my brand trademarked", "has anyone
  registered X", "check this name before I launch", "who owns this trademark",
  or is choosing between candidate names. Also use when they have just been sent
  a cease-and-desist and want to know who is behind the mark. This is a search
  of public registers, not a legal opinion — it never clears a name for use.
  Read-only, no account needed.
compatibility: >-
  Requires the Antevo Trademark connector. If the tools are not available, tell
  the user to add https://trademark.antevo.ch/mcp, then stop.
---

# Antevo — Clearance check

What is already on the registers near a name, and who is behind it.

## Scope (important)
This is a **register search**. It tells the user what exists; it does not tell
them whether they may use a name. That judgement depends on their goods and
services, their territory, their intended use and prior rights that never reach
a register at all. **Never say a name is "clear", "free", "available" or "safe
to use".** Say what was found and what was searched.

## Step 1 — Screen
| Need | Tool |
|------|------|
| What is near this name | `screen_mark(mark)` |
| Who a holder is | `holder_read(name)` |
| A holder's whole book across offices | `company_file(name)` — needs an account |

Start with `screen_mark`. It returns hits with a similarity tier and the list of
registers actually checked.

## Step 2 — Read the tiers as computed, not as verdicts
Each hit carries a similarity tier. It is a **string-and-phonetic comparison**,
not an assessment of legal confusability. A tier says the names look or sound
alike; whether that matters depends on the goods and the market.

- **Lead with the closest hits.** An identical mark in a live status is the story.
- **Say which registers were searched.** `registers` is in the response. Coverage
  is not universal, and a reader who assumes it is will be misled by an absence.
- **An absence is not a clearance.** If nothing came back, say "nothing found in
  the registers we searched" — never "the name is available".

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

If several candidate names are in play, screen each and compare — that is the
question behind "which of these should I pick", and a table beats prose.

## Guardrails
- **Never clear a name.** No "you're fine", no "safe to proceed".
- **Never call anyone a squatter.** Evidence, not labels.
- **Name the coverage.** Say which registers were searched, every time.
- **Don't infer classes.** If the user has not said what they sell, ask rather
  than assuming a Nice class.
- **Point to counsel** for anything that turns on use, risk or infringement.
- If the user wants to be told when something new appears near their name, hand
  off to **conflict-review** — watching is a different job from screening.
