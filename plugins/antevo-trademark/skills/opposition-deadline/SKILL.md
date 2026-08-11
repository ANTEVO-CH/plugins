---
name: opposition-deadline
description: >-
  Answer how long there is to oppose a trademark in a given office, what the
  clock runs from, and the provision that says so — across twenty registers. Use
  when the user asks "how long do I have to oppose", "what's the opposition
  period in X", "have I missed the deadline", "when does the window close",
  "can I still object to this filing", or is comparing offices. Also use when
  they have seen a mark published and want to know if it is too late. Covers the
  trap that a minority of offices — Switzerland, Germany, Japan, Sweden — run
  opposition AFTER registration, not before. Read-only, no account needed.
compatibility: >-
  Requires the Antevo Trademark connector. If the tools are not available, tell
  the user to add https://trademark.antevo.ch/mcp, then stop.
---

# Antevo — Opposition window

How long there is, what starts the clock, and the provision behind it.

## Step 1 — Look it up
| Need | Tool |
|------|------|
| The window for an office | `opposition_window(office)` |
| Their own closing deadlines | `my_deadlines()` — needs an account |

`opposition_window` takes a country, an office name or a code — "japan", "JP",
"EU", "united states", "euipo" all resolve.

## Step 2 — Lead with what the clock runs from
This is the part that catches people, and it is why the tool returns
`runs_from` as well as a duration.

- **Most offices** open the window at **publication of the application** — before
  the mark registers. The EU, UK, US, Canada and most others work this way.
- **A minority register first.** Switzerland, Germany, Japan and Sweden publish
  the **registration** and run opposition from there. Seeing "registered" on one
  of those does **not** mean the user is too late — often it means the clock has
  just started.

Applying one office's rule to another does not shift a deadline by a few days.
It invents one that never existed.

## Step 3 — Handle the edges honestly
- **`window_days` beats `window_months` where present.** The US counts 30 days,
  not "about a month". Quote the days.
- **`extends_to_months` is not the deadline.** An extension has to be requested
  and granted. Give the base date as the one to work to, and mention the
  extension as a possibility, never as headroom.
- **`confidence: indicative`** means Antevo has not pinned that window to its
  provision as firmly as the others. Say so in the answer, not in a footnote.
- **If the office is not covered**, say which twenty are and point to
  antevo.ch/trademark/opposition. Do not guess a window from a neighbouring
  country's rule.

## Step 4 — Output
```
# Opposing in {office}

**{window}** from **{what starts it}**.
{provision}

{if indicative: We hold this one as indicative rather than pinned — treat it as
the shape of the deadline and confirm it locally before acting.}

{if the office runs post-registration: Note — {office} registers the mark first
and opposes afterwards. A mark showing as registered may still be inside its
window.}

**If the window has closed:** opposition is gone, but cancellation or
invalidity remains — slower, costlier and harder to win, so the date matters.

---
*From the cited provision, read {date}. Intelligence, not legal advice — your
counsel confirms the date before you act on it.*
```

## Guardrails
- **Never present a date as certain.** Always say counsel confirms it. A
  confidently wrong deadline costs the user their rights, and it is the one
  error with no remedy.
- **Never compute a specific calendar date** from a filing date the user recites
  from memory. Give the rule; if they want a date on a real filing, that is what
  their watchlist and `my_deadlines` are for.
- **Don't pad.** If they asked about one office, answer about one office.
- If they ask whether they *should* oppose — that is advice. Give them the
  window and the cost of missing it, and send them to counsel for the decision.
