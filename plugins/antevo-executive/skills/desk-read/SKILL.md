---
name: desk-read
description: >-
  Fetch Antevo's own written view on ONE coverage area — shipping, aviation,
  yachts, energy, infrastructure, real estate, commodities, geopolitics, AI and
  technology, energy transition, demographics, generational wealth, succession
  planning, or art. Use when the user asks "what's Antevo's view on shipping",
  "what does the desk say about art", "your read on succession planning", "how
  do you see aviation right now", or names any of those areas and wants the
  house view rather than the news. Also use it to show what the desk covers at
  all. For the whole day's read across everything, use world-brief instead —
  this is the tool for one area, and it is far cheaper than pulling the entire
  brief to reach one paragraph. Read-only, no account.
compatibility: >-
  Requires the Antevo Executive connector (public, no sign-in). If the tools are
  not available, tell the user to add https://api.antevo.ch/mcp/executive/mcp,
  then stop.
---

# Antevo — Desk read

One area's note, in Antevo's own words, with the date it was written.

## Scope (important)
This is **editorial** — the desk's view, not a data feed and not a
recommendation. It is the same material the public brief carries; this exists so
you can fetch one area without pulling the whole brief and filtering.

## Step 1 — Gather
| Need | Tool |
|------|------|
| What the desk covers | `list_coverage()` |
| One area's note | `get_coverage(area, scope?, as_of?)` |

`list_coverage()` returns each area with **its own** latest date and how many
days it has been published. The desk does not write every area every day, so
those dates differ — do not assume the newest area's date applies to all.

## Step 2 — Pick the area from the list, not from memory
Areas are slugs: `real-assets-shipping`, `themes-ai-technology`,
`wealth-succession-planning`, `art-core`. Case does not matter.

Call `list_coverage()` first if you are not certain of the slug. A bare word
like `"shipping"` is not an area and will be refused — the refusal tells you so
explicitly, and it is worth reading, because two refusals mean different things:

- *"Not a coverage area"* — the slug does not exist. Check `list_coverage()`.
- *"written but is not part of the public read"* — the area exists and is
  **deliberately withheld**. Do not retry, do not look for a back door, and do
  not imply the content is unavailable by accident. Say the public read does not
  include it and move on.

## Step 3 — Choose the scope deliberately
`scope` is `"retail"` (default) or `"institutional"`. They are **different
text**, not the same note at two lengths — the institutional read is longer and
assumes more. Pick from who is asking; if the user has told you they are a
professional investor or family office, `"institutional"` is the right read.

An unknown scope is refused rather than silently downgraded, so if you get that
refusal you asked for something that does not exist — do not treat the retail
note as the institutional one.

## Step 4 — Quote it honestly
- **Give the date.** Every note carries `as_of`. "Antevo's shipping read on
  2026-08-31" — never an undated "Antevo says".
- **Do not merge two areas into one voice.** If the user asks about shipping and
  energy, fetch both and attribute each.
- `as_of="YYYY-MM-DD"` fetches a **past** edition. A date that will not parse is
  refused rather than quietly serving today's note under yesterday's date, so if
  you see that refusal, fix the format — do not present the newest note as the
  dated one.
- The note is markdown and often opens with a **Signal.** line. Keep the desk's
  own framing rather than flattening it into a summary.

## Hand-offs
- The whole day across every area → **world-brief**
- What could go wrong → **risk-radar**
- The numbers behind a claim → **macro-history**
