---
name: decode
description: >-
  Explain what a market move actually means, in plain language, using the Antevo
  desk's own decode. Use when the user asks "what does this mean", "explain
  this", "why does that matter", "I don't follow markets, what's going on",
  "help me understand", "break this down", "what should I take from this", or
  asks about a market event in a way that shows they want understanding rather
  than a briefing. Also for "teach me how to read this". Universal — no account,
  no portfolio access. If they want the professional editorial read instead, use
  world-brief. Read-only.
compatibility: >-
  Requires the Antevo Executive connector (public, no sign-in). If the tools are
  not available, tell the user to add https://api.antevo.ch/mcp/executive/mcp,
  then stop.
---

# Antevo — Decode

For the reader who wants to *understand* the move, not be briefed on it.

## The one thing that makes this skill work

**The desk has already written the plain-language version. Use it. Do not write
your own.**

Simplifying a financial claim is where meaning quietly changes — a hedge gets
dropped, a probability becomes a certainty, "the odds fell" becomes "it won't
happen". The brief carries an authored jargon-free rendering of the whole thing,
so there is no reason to paraphrase and every reason not to.

## Step 1 — Pull it

```
get_executive_brief(sections="plain_language")
```

That's the whole skill's input — about 2KB rather than the full 24KB brief.

| Field | What it is |
|-------|------------|
| `headline` | The move in one plain sentence |
| `decode.tape_says` | What happened, read quickly — the surface story |
| `decode.lesson` | The transferable principle — how to read *this kind of* move |
| `decode.capital_does` | How an allocator separates the questions the headline blends |
| `signal_read` | The probability layer, without jargon |
| `theme_reads` | One line per theme — Gold, Energy, Equities, Rates |

Add `sections="plain_language,regime"` if they asked what kind of market this is.

## Step 2 — Build the arc

`decode` is already a teaching sequence. Follow it in order — the order is the
pedagogy:

1. **`tape_says`** — the fast read. Start where the reader already is.
2. **`lesson`** — the principle. This is the part they keep after they've
   forgotten the news.
3. **`capital_does`** — what a professional does differently with the same
   headline. This is the payoff.

Then `theme_reads` for anything they asked about specifically.

## Step 3 — Pitch it right

- **Assume no jargon, but never talk down.** The desk's own copy sets the level;
  match it.
- **Lead with the concrete.** A named waterway, a named metal, a date — not
  "risk assets".
- **One idea per paragraph.** If a sentence has two clauses joined by "while",
  it's probably two paragraphs.
- **Answer what they asked.** If they asked about gold, `theme_reads` has a gold
  line — start there and use the decode to explain why it moved that way.

## Step 4 — Output

```
# {headline}

{tape_says — what happened, in one short paragraph}

## What's actually going on
{the distinction the headline blends — from capital_does}

## The thing worth remembering
{lesson — stated as a principle they can reuse}

## Where it showed up
- **{theme}** — {read}

---
*From the Antevo Executive Brief, {date}. Editorial market intelligence — not
investment advice.*
```

Drop any section they didn't need. A good decode of one question beats a full
template.

## Guardrails
- **Quote the desk's framing; don't invent your own simplification.** That's the
  point of the skill.
- **Keep the hedges.** If the copy says "looked close, then", it does not say
  "failed". Certainty is the easiest thing to add by accident and the most
  damaging.
- **A lesson is not a prediction.** "Check whether the distant dates moved too"
  teaches a habit; it does not say what happens next.
- **No personal advice, ever** — this reader is the most likely to take a
  general remark as one. If they ask what they should do, say plainly that this
  is universal commentary, and point them to the Antevo Wealth connector for
  anything about their own holdings.
- If `plain_language` is missing for a date, use `world-brief` instead and say
  you're giving the professional read — don't improvise a simplified one.
