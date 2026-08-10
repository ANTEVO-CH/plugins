---
name: story-timeline
description: >-
  Trace how a story developed over time using the Antevo Executive Brief
  archive. Use when the user asks "how did X develop", "what did you say about X
  back then", "what was the read in {month/date}", "how has the view on X
  changed", "when did X start", "show me the history of this story", or asks
  about a PAST date rather than today. Reads the dated archive of published
  briefs and reconstructs the arc — what was said when, and how the view
  shifted. Read-only, no account required.
compatibility: >-
  Requires the Antevo Executive connector (public, no sign-in). If the tools are
  not available, tell the user to add https://api.antevo.ch/mcp/executive/mcp,
  then stop.
---

# Antevo — Story timeline

The archive's real value: not "what's the news" but **"how did this story
actually develop, and where was the view wrong or early?"**

## Step 1 — Find the dates
- `list_executive_notes(limit)` — the archive, newest first, each with date, title, subtitle and hero line.
- Scan those lines for the theme the user named. The subtitle/hero is usually enough to spot relevance — you don't need to open every note.
- If they gave a specific date, skip straight to `get_executive_note(as_of=…)`.

## Step 2 — Read the relevant days
- `get_executive_note(as_of="YYYY-MM-DD")` for each date that matters — typically 3–6, not twenty.
- Pick the **turning points**, not every mention: when the theme first appeared, when the view changed, where it stands now.

## Step 3 — Build the arc
- **Chronological**, oldest → newest, so the development is visible.
- For each point: the date, what was said, and what had changed since the last one.
- **Call out the shift.** "Early on the read was X; by {date} it had turned to Y because Z" is the insight — a list of quotes is not.
- **Close with where it stands** (pull today's brief if useful) and what would move it next.
- **Be honest about the record** — if the view was early, late or wrong, say so. That's what makes an archive worth having.

## Step 4 — Output
```
# {Theme} — how it developed

**The arc.** {one sentence: from what, to what.}

## Timeline
- **{date}** — {what was said} · {what changed}
- **{date}** — …

## Where it stands
{today's read, and what would move it next}

---
*Reconstructed from the Antevo Executive Brief archive ({earliest date} →
{latest date}). Editorial market intelligence — not investment advice.*
```

## Guardrails
- **Every claim gets its date.** This is a historical record; undated assertions defeat the purpose.
- **Don't fabricate coverage.** If the archive doesn't cover the theme (or the window), say so plainly and show what it *does* cover.
- Distinguish **what was said then** from **what is true now** — never present an old read as current.
- Not investment advice.
