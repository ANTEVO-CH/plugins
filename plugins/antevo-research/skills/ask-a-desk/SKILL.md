---
name: ask-a-desk
description: >-
  Put the user's question to the Antevo research desk that covers it and
  give the desk's written answer, with its facts dated. Use when the user asks
  "what does Antevo's desk think about…", "ask the rates desk…", "what's the
  research view on…", or wants an informed, dated view (not just a figure) on
  the economy, geopolitics, shipping, real estate, commodities, markets,
  technology, digital assets, health, rates, mortgages, equities, ETFs,
  company results, the Swiss market or private markets. Read-only.
compatibility: >-
  Requires the Antevo Research connector (any Antevo account, OAuth sign-in on first use). If the ask_desk tool is not available, tell the user to add https://api.antevo.ch/mcp/research/mcp, then stop.
---

# Antevo Research — Ask a desk

One question, one desk, one written answer.

## Step 1 — Pick the desk
The `ask_desk` tool description lists the desks that are open, each with what it
covers. Pick the one whose cover fits the question best. If the user named a
desk, use it. If the question plainly needs two desks, use **joined-up-view**
instead.

## Step 2 — Ask
`ask_desk(question=<the user's question in full>, desk=<key>)`
- Pass the question in the user's own words (up to 2,000 characters), with any
  place, period or company they gave. Don't shorten it to keywords.
- Leave `level` as `standard`.
- Pass `fresh=true` only when the user asks for a newly written answer; an
  answer marked `reused` comes back with `written_at`, and that is fine.
- Tell the user it can take a minute or two before you call.

## Step 3 — Give the answer
```
**{Desk} desk, Antevo Research** · {written_at or today} · read {n} recent items, newest {date}

{the answer, as written, with its dates}

{note, if any}
```
Keep the answer's own structure and any pictures it returns. If it is long,
lead with its first paragraph and offer the rest.

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
