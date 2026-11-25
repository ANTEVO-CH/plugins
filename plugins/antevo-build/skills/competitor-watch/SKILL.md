---
name: competitor-watch
description: >-
  Read a company's rivals on the public record using Antevo engines
  (Companies, Trademark, Strategy Radar): register changes, mergers and
  signatory turnover, where and in which classes each files trademarks,
  sanctions-list checks and what changed for the sector today, each with a
  "so what" — "what are our competitors up to", "watch our rivals", "has a
  competitor changed anything", "where is our rival filing trademarks".
  A rival's name goes to Antevo when it is looked up; ask first.
compatibility: >-
  Companies needs any Antevo account (50 credits per file, first opening in 30
  days); Trademark and Strategy Radar need no account.
---

# Competitor Watch, built on Antevo

You turn a company's list of rivals into one page: what changed in each rival's register, where
and in which classes it files trademarks, any sanctions-list finding, what changed for the sector
today, and what to watch next. Every finding comes from an Antevo engine answer in this
conversation. You write the "so what" lines; you never invent a figure, a date or a plan, and you
never claim to know a rival's intentions from its filings.

## What you need first

Ask, in one short message, only for what is missing:

1. **The company and what it makes**, in a line.
2. **Two to five rivals**, by their registered names if known.

Say first that looking a rival up sends its name to Antevo, and go ahead only if they agree.
The company's own name is never needed.

## Connect

With a sign-in: Companies (`https://api.antevo.ch/mcp/companies/mcp`; 50 credits the first time
a file is opened in 30 days, sections free after that; say the total before opening). Free with
no account: Trademark (`https://trademark.antevo.ch/mcp`) and Strategy Radar
(`https://api.antevo.ch/mcp/strategy/mcp`). If a connector is missing, say which one, skip it and
mark its part "not checked". Never fill a gap from memory.

## Step 1 · Find each rival

`find_company` with each name (free). If more than one candidate comes back, pick the operating
company by its purpose and seat, and say which one you chose; ask only if it is unclear. Names
find Swiss companies only; for a rival outside Switzerland, mark the company file "not covered"
and go on with the trademark read.

## Step 2 · The company files

`company_file` with each `entity_id`, then `layer="history"`. Report the dated events by kind:
name and purpose changes, mergers (a call to creditors after a merger means it took over
another company; the same call is published three times, so count it once), signatory changes as counts, the sanctions-list result in its own words. A
notice that says only "register entry changed" shows that something changed, not what: say so
and point to the notice text on the official gazette. Never name the people in a notice.

## Step 3 · The trademark books

`holder_read` with each registered name, including its legal form (`AG`, `GmbH`, `Ltd`). Report
the marks held, the offices, the classes, how many reached the register, and the first and last
filing dates. Explain a class in words (7 machines, 9 software and electronics, 37 installation
and repair, 42 engineering and software services). A filing country shows where a company
protects a name, not what it plans: say "files in", never "is expanding into". If the holder is
not found, say there are no filings under that name and that marks may sit with another group
company.

## Step 4 · The sector today

`get_business_board`. Keep the entries that touch the field the rivals sell in. Give impact,
likelihood and trend in the board's words, and credit "Antevo Executive Brief" with its date.

## Read each rival

Give each rival a verdict in a few words: **a busy record**, **worth a look**, **a quiet record**,
**not covered**. Under it, two or three lines of evidence, each with its date.

## What to watch next

Three to five steps, each with a link from this table only:

| What | Link |
|---|---|
| Follow a filer's next filings | https://antevo.ch/trademark/app/filers |
| Watch a company file | https://antevo.ch/companies/ |
| The notice text, official gazette | https://www.shab.ch/ |
| The Swiss company register | https://www.zefix.ch/ |

Offer, once, to follow each rival with `follow_filer` and to watch each file with
`watch_company` if those tools are available.

## Join them

Two or three links, each naming the two engines it joins, for example: the register shows a
merger and the trademark book shows first filings abroad soon after: one story of a company
rebuilding its offer.

## The workspace

One artifact (an HTML page if the assistant supports artifacts), in this order: header (today's
date, "Built from Antevo answers"); the rivals one by one; what to watch next; the findings,
each with its so what; how the findings connect; what to watch; sources with their dates. If the
template from antevo.ch/mcp/build is available, fill its `workspace.json`: `tries` (with
`"item": "Rival"`), `steps`, `sections` with `so_what`, `links` and `watch`.

Close with: the findings come from the public record, a register notice shows that something
changed, a trademark book is not a plan, a sanctions-list check is not a compliance screen, and
none of this is legal advice.
