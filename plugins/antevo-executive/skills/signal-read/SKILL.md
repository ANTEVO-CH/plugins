---
name: signal-read
description: >-
  Read Antevo's own probability layer — the engine's odds on named outcomes
  (chokepoint reopening, ceasefire, and the other bands it carries), which way
  they moved, and what the move means. Use when the user asks "what are the
  odds", "what's the probability of", "what does your model say", "is the market
  pricing this right", "what's your signal on", "how likely is", or wants the
  quantitative read rather than the narrative. This is Antevo's proprietary
  measure — not a market-implied probability and not a forecast. Universal
  market intelligence, no account, no portfolio access. Read-only.
compatibility: >-
  Requires the Antevo Executive connector (public, no sign-in). If the tools are
  not available, tell the user to add https://api.antevo.ch/mcp/executive/mcp,
  then stop.
---

# Antevo — Signal read

The engine keeps odds on named outcomes and tracks how they move. This is the
part of the brief nothing else in the market has, and the part most easily
misquoted — so the guardrails below are not optional.

## Step 1 — Pull it

```
get_executive_brief(sections="signal,plain_language")
```

You get two registers of the same thing, **both written by the desk**:

| Field | Register |
|-------|----------|
| `signal.indicator` | The precise read — which bands moved, which way, on what date |
| `signal.why_it_leads` | Why this measure leads rather than confirms, and its provenance |
| `plain_language.signal_read` | The same thing without jargon |

Add `sections="signal,plain_language,regime"` if you need the wider frame.

## Step 2 — THE GUARDRAIL: live bands only

**This is the one way to get this badly wrong, and it has happened once
already.** The desk published an expired band as a current probability on
4 August 2026 and corrected it in the open. `why_it_leads` carries that
correction and labels which bands are live.

Before quoting any number:

- **Read `why_it_leads` first, every time.** It states which bands are live —
  meaning their deadline is still ahead of us — and which are settled.
- **Never quote a settled band as a current probability.** A band whose date has
  passed is history, not an odds quote.
- **If you cannot tell whether a band is live, do not quote the number.**
  Describe the direction instead: "the reopening odds fell across every horizon"
  is true and useful; a specific percentage you can't date is not.

## Step 3 — Read the shape, not just the level

The signal's value is in the *term structure*, not any single number:

- **One band moving is news. The whole curve moving one way is a change in what
  the market thinks the situation IS.**
- **Two curves moving in opposite directions on the same day** — say, ceasefire
  odds up while reopening odds fall at every horizon — is the strongest read
  available: the market has separated two things a headline blends together.
- **Near dates vs distant dates.** A delay moves the near date. A change of mind
  moves all of them. `plain_language.decode.lesson` often says exactly this.

## Step 4 — Match the register to the question

- Asked quantitatively ("what are the odds") → lead with `signal.indicator`,
  keep the precision, state the date.
- Asked plainly ("is this likely", "what does that mean") → lead with
  `plain_language.signal_read`, which is already written for that reader.
- **Either way, quote the desk's words rather than inventing your own
  simplification.** Both registers are authored; paraphrasing a probability
  claim is how a number quietly changes meaning.

## Step 5 — Output

```
# {The outcome in question} — {date}

**The read:** {indicator, in the desk's terms}

**Which way it moved:** {direction across horizons — near vs distant}

**Why it leads:** {provenance, and what this measure is}

---
*Antevo's own probability layer, {date}. Live bands only — deadlines ahead of
us. This is Antevo's measure, not a market-implied probability, and not a
forecast. Editorial market intelligence — not investment advice.*
```

## Guardrails
- **Say whose number it is.** "Antevo's engine puts…" — never "the probability
  of X is…", which implies an objective market price.
- **Never convert a band into a bet, a position, or a recommendation.**
- **Never extrapolate a band forward.** If the engine carries August, September
  and December, those are the horizons; you do not have a January number.
- **No personal advice.** If they ask what it means for *their* holdings, that's
  the Antevo Wealth connector.
- If the brief has no `signal` for the date requested, say so — do not
  substitute the narrative and call it a signal.
