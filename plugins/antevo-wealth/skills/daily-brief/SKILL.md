---
name: daily-brief
description: >-
  The household's morning note — what matters today and what needs attention.
  Use whenever the user asks "what's my brief", "what's happening today", "good
  morning", "anything I should know", "what needs my attention", "what changed",
  "any alerts / breaches", "what's coming up", "catch me up", or opens the day
  with a general check-in on their wealth. Composes the Antevo Wealth today
  surface — the daily brief, unread alerts, open compliance breaches, allocation
  drift and the upcoming calendar — into one executive read. Read-only.
compatibility: >-
  Requires the Antevo Wealth MCP connector (wealth.today; optionally
  markets.core). If the tools are not available, tell the user to connect Antevo
  Wealth, then stop.
---

# Antevo Wealth — Daily brief

The single most-used surface: **what matters today, and what wants a decision.**
Your job is to lead with the answer, not to dump five tool outputs.

## Before you start
- **Connector check.** No `get_today_brief` tool → ask the user to connect Antevo Wealth, then stop. Never invent events.
- **Household.** Resolve a `household_id` (ask if more than one).
- **Read-only.** You surface and recommend; the user acts.

## Step 1 — Gather (in this order)
| Layer | Tool |
|-------|------|
| The brief — what matters now | `get_today_brief` |
| Attention — anything unread | `get_unread_alerts` |
| Policy — anything in breach | `get_open_breaches` |
| Position — drifted from plan? | `get_drift_snapshot` |
| Ahead — dividends, earnings, macro | `get_upcoming_calendar` |
| Backdrop (optional) | `get_market_brief` — only the lines that touch this book |

Call all of them for a general "what's my brief"; for a narrow ask ("any
breaches?") call just what's needed.

## Step 2 — Triage (the value you add)
Rank ruthlessly — a principal reads the first two lines.

1. **Hard first.** An open breach with a cure date, or a critical alert, outranks everything.
2. **Then the money.** Drift beyond threshold, a concentration that grew, a facility nearing a covenant.
3. **Then the diary.** Calendar items in the next days that need a decision (not every dividend).
4. **Then context.** One or two market lines *only if they bear on this book*.
5. **Say when it's quiet.** A clean morning is a real answer — state it plainly ("nothing needs you today; concentration, leverage and the regime are within band"). Don't manufacture urgency.

## Step 3 — Write the note
```
# {Good morning / afternoon} — {household} · {date}

**{The one thing.}** {Single sentence: the most important item, or "nothing needs you today".}

## Needs you
- {breach / alert} — {what and by when}

## On the book
- {drift, concentration, leverage changes worth a look}

## Coming up
- {date} — {event} · {why it matters}

## Backdrop
- {1–2 lines, only if they touch this book}

---
*Read-only brief from your Antevo Wealth data as of {dates}. Informational only —
not investment, tax, or legal advice.*
```

## Guardrails
- **Lead with the verdict**, then the evidence. Never open with a list of tool names.
- **Cite with dates.** Empty is data ("no open breaches"), never a gap to fill.
- **No manufactured urgency.** If the book is calm, say so — that's the premium answer.
- **Hand off.** Offer the deeper skill when relevant ("want the full stress read?" → `portfolio-stress-radar`; "look at that name?" → `security-analysis`).
- Not advice; the user decides and confirms every change in Antevo Wealth.
