---
name: joined-up-view
description: >-
  A question that crosses desks — e.g. what a Red Sea closure means for
  shipping, oil and European rates, or how a US tariff touches Swiss
  equities and the franc. Ask each desk involved, or the strategy desk for
  the joined-up view, and set the answers side by side with where they agree
  and where they differ. Use when the user asks "how does X ripple through…",
  "what does this mean across markets", "give me the joined-up view", or names
  two or more areas at once. Read-only.
compatibility: >-
  Requires the Antevo Research connector (any Antevo account, OAuth sign-in on first use). If the ask_desk tool is not available, tell the user to add https://api.antevo.ch/mcp/research/mcp, then stop.
---

# Antevo Research — The joined-up view

When one desk can't answer alone.

## Step 1 — Decide the route
- **Two or three named areas** (e.g. shipping and commodities): ask each desk.
- **A broad "what does this mean overall"**: ask `strategy`, which joins the
  desks' reading up, if it is listed.
- Never more than three desks for one question; say which you chose and why in
  one line.

## Step 2 — Ask
For each desk: `ask_desk(question=<the user's question, framed for that desk>,
desk=<key>)`. Keep the user's wording and add one clause saying which part you
want from that desk ("…from the shipping side"). Leave `level` as `standard`.
Answers take a minute or two each; tell the user before you start.

## Step 3 — Set them side by side
```
# {the question, short}
Antevo Research · {date}

**Where the desks agree**
- …

**Where they differ**
- {desk}: … / {desk}: …

**By desk**
### {Desk} desk · read {n} items, newest {date}
{answer}
…
```
"Agree" and "differ" must come from the answers themselves. If they don't
touch, say so rather than inventing a link.

## Guardrails
- **Antevo's view, quoted as such.** Say which desk answered; keep its dates and
  pass on its `note` when it found no recent research. Don't add facts or
  figures from memory to its answer.
- **Never advice.** Don't turn an answer into a recommendation to buy, sell or
  hold, a rating or a price target, and never give a price level a market is
  expected to reach.
- **No sources passed out.** Credit only "Antevo Research" and the desk; don't
  name outlets, banks or research houses, or add links.
- **Not their money.** The desks can't see the user's holdings. For what
  something means for their own portfolio, point to Antevo Wealth.
- **Refusals are answers.** If the tool answers `insufficient_credits`,
  `not_available` or `bad_input`, pass on its message and its next step in one
  line; don't retry with a different desk to get round it.
