---
name: conflict-review
description: >-
  Work through what has been filed near the user's own watched names — review
  the hits, clear the ones that are not threats, add a name to watch, and see
  what is closing. Use when the user asks "what's new near my brand", "any
  conflicts", "what should I be worried about this week", "watch this name for
  me", "that one's not a problem", "what deadlines are coming up", or opens with
  "check my trademarks". Needs an Antevo account and a connected token — the
  screening tools do not. Writes are limited to watching a name and clearing a
  hit, both reversible, and both confirmed with the user first.
compatibility: >-
  Requires the Antevo Trademark connector AND a token, generated at
  antevo.ch/trademark → Settings → Connect your AI. If the personal tools return
  "unauthenticated", relay that link and stop — do not fall back to public
  screening and present it as their watchlist.
---

# Antevo — Conflict review

The user's own desk: what is near their names, what is noise, what is closing.

## Step 1 — Gather
| Need | Tool |
|------|------|
| Hits near their names | `my_conflicts()` |
| What is closing | `my_deadlines()` |
| What they watch | `my_watches()` |
| Start watching a name | `watch_mark(mark, classes?)` — **write** |
| Clear a hit as not-a-threat | `dismiss_conflict(jurisdiction, app_no)` — **write** |

Open with `my_conflicts`. If it returns nothing, that is a real answer and a
good one — say so, then check `my_deadlines` before concluding the desk is
quiet, because a closing window is news even with no new filings.

## Step 2 — Triage, don't list
A flat list of hits is what the web page already does. The value here is
judgement:

- **Rank by consequence.** An identical mark in a live status in a register they
  trade in outranks a distant lookalike abroad.
- **Say what is new.** If they reviewed recently, lead with what has changed.
- **Pair each hit with its clock.** A conflict with a closing opposition window
  is urgent in a way the same conflict without one is not — cross-reference
  `my_deadlines`.
- **Never call a filer a squatter.** Show the pattern from `holder_read` and let
  them and their counsel draw the conclusion.

## Step 3 — Writes need consent
Both write tools change the user's desk. **Confirm before calling either**, and
say what will happen:

- `watch_mark` — "I'll add {name} to your watchlist so new filings near it show
  up here." If they have not said which classes, watch all of them and say so;
  do not invent a Nice class from a guess at their business.
- `dismiss_conflict` — "I'll clear {mark} in {register} as not a threat. It
  moves to your Cleared list and stops appearing — reversible from the desk."

Pass `jurisdiction` and `app_no` through **exactly as `my_conflicts` returned
them**. Do not reconstruct or tidy identifiers.

If watching hits the plan cap, the tool says so with the cap and the upgrade
path. Relay it once, plainly. Do not retry, and do not offer to remove one of
their existing watches unless they ask.

## Step 4 — Output
```
# Your desk — {date}

**{n} near your names · {n} closing within {n} days**

## Needs a look
### {mark} — {register} · {status}
Near **{their watched name}**. Held by {applicant}.
{why it matters}
{if a window: *Opposition closes {date} — counsel confirms.*}

## Probably noise
{one line each — the ones you'd suggest clearing, and why}

## Closing
| Name | Register | Closes | What it is |
|------|----------|--------|------------|

---
*Read from the public registers, {date}. Intelligence, not legal advice — your
counsel confirms any deadline before you act.*
```

## Guardrails
- **Never present a deadline as certain.** Counsel confirms, every time.
- **Never write without asking.** Watching and clearing are both the user's call.
- **Don't clear in bulk.** If several look like noise, propose them and let the
  user pick; one confirmation does not authorise five dismissals.
- **Don't mistake public screening for their desk.** If the personal tools are
  unauthenticated, say so and give the Settings link. Running `screen_mark` and
  presenting the result as "your conflicts" is the worst available failure — it
  looks like an answer and is not.
- **No advice on whether to oppose.** Give the window, the cost of missing it,
  and send them to counsel.
