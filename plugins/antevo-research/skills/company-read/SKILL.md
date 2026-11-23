---
name: company-read
description: >-
  A named listed company read across Antevo's desks: the equities desk
  for the business and valuation figures, the results desk for the latest
  results against expectations and what the call said, and, on request, the
  technical desk for how the shares have moved (in percentages and words,
  never a price level). For a Swiss company the swiss desk adds the SMI and
  the Swiss results season. Use when the user asks "what's the read on
  Nestlé", "how did Roche's results go", "is UBS's chart breaking down" or
  wants a company file. Read-only; never a rating or advice.
compatibility: >-
  Requires the Antevo Research connector (any Antevo account, OAuth sign-in on first use). If the ask_desk tool is not available, tell the user to add https://api.antevo.ch/mcp/research/mcp, then stop.
---

# Antevo Research — A company read

## Step 1 — Which desks
| The user wants | Desk |
|------|------|
| The business, figures, valuation at the latest close | `equities` |
| The latest results, beats or misses, what the call said, the season | `results` |
| How the shares or a market have moved, trend and momentum | `technical` |
| A Swiss company in its home market | add `swiss` |
| A fund rather than a company | `etfs` |

Default to `equities` plus `results`. Add `technical` only when the user asks
about the chart or the price move.

## Step 2 — Ask
`ask_desk(question=<the user's question naming the company>, desk=<key>)` for
each desk chosen. Name the company the way the user did and add the exchange if
they gave one. If a desk answers that it could not find the company, pass that
on; never say the company has no data when a lookup failed or timed out.

## Step 3 — The read
```
# {Company}
Antevo Research · {date}

**Business and figures** — equities desk
…
**Latest results** — results desk
…
**How the shares have moved** — technical desk (if asked)
…
```
The technical desk sends a picture per instrument; show it. Its price axis has
no numbers by design — don't add any.

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
