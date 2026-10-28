---
name: episode-compare
description: >-
  Compare this week's Antevo Tremor Index with past episodes — 2008, March
  2020, 2022 or any period since 1997 — and show how the reading moved over a
  stretch of weeks. Use when the user asks "how does this compare with 2008",
  "is this like COVID", "when was it last this bad", "show me the last year",
  "how did it look during the 2022 rate shock", or wants the index over time.
  Descriptive, not a forecast. Read-only.
compatibility: >-
  Requires the Antevo Tremor Watch connector (public, no sign-in). If the tools
  are not available, tell the user to add https://api.antevo.ch/mcp/tremor/mcp,
  then stop.
---

# Antevo — Then and now

This week's reading set against the record since 1997.

## Step 1 — Gather
| Need | Tool |
|------|------|
| Now | `get_tremor_index()` — includes `worst_on_record` |
| A named episode | `get_tremor_history(weeks=78, until="2009-06-30")` for 2008; `weeks=40, until="2020-09-30"` for 2020 |
| The last year | `get_tremor_history(weeks=52)` |
| The whole record | `get_tremor_history(weeks=1600)` — answered by quarter |
| The pairs of a past week | `get_tremor_pairs(week="2008-10-10")` |

`until` ends the window in that week; `weeks` is how many Fridays it covers.
More than 160 readings step up to months, then quarters (the answer says so).

## Step 2 — Compare like with like
- **Compare `times_normal`**, the multiple of a normal Friday. It is the same
  scale for every week since 1997.
- **Use each window's `peak`** for the episode's worst week, with its date and
  status.
- **Say how long it lasted**: count the weeks at High or Severe in the window.
- **Place now on the record**: `rank_since_2001` and `worst_on_record` from the
  index.

## Step 3 — Output
```
# Then and now

**Now (week ending {week}):** {times_normal}× a normal Friday, {status}.
**{Episode} peak ({date}):** {times_normal}× — {status}; {n} weeks at High or
Severe.
**Worst on record:** {date}, {times_normal}×.

{One or two sentences on what that comparison says about scale — not about
what comes next.}

---
*Antevo Tremor Index, weeks of {dates}. Descriptive, not a forecast, and not
investment advice.*
```

## Guardrails
- **A comparison is not a prediction.** Never say that because a week resembles
  2008, a 2008-style outcome follows.
- **Quote the dates the tool returned**, not remembered dates for events.
- **No price levels** or market returns from memory; the index has none.
- **No personal advice.**
