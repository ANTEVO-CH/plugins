---
name: world-map
description: >-
  Answer questions about physical and infrastructure exposure from Antevo's
  world-events layers — shipping waterways and chokepoints, submarine
  communications cables, armed conflicts, natural disasters, displacement,
  sanctions, cyber incidents, regulatory actions and watch hotspots. Use when
  the user asks "what's happening at Hormuz / Suez / Panama", "which cables run
  through there", "where are people being displaced", "what disasters are
  active", "who has been sanctioned lately", "what cyber incidents are there",
  or any question about WHERE something is happening rather than what a market
  did. Ask for the specific layers you need, never all of them. Read-only, no
  account.
compatibility: >-
  Requires the Antevo Executive connector (public, no sign-in). If the tools are
  not available, tell the user to add https://api.antevo.ch/mcp/executive/mcp,
  then stop.
---

# Antevo — World map

Nine layers of physical and infrastructure events, each with its own geometry.
This is the "where" surface: chokepoints, cables, conflicts, disasters.

## Step 1 — Choose your layers FIRST
| Layer | What it carries |
|---|---|
| `waterways` | shipping lanes and chokepoints — Hormuz, Suez, Panama, Malacca |
| `submarine_cables` | subsea communications cables and their landing points |
| `armed_conflicts` | active conflict events |
| `disasters` | natural disasters |
| `displacement` | population displacement |
| `sanctions` | sanctions actions |
| `cyber` | cyber incidents |
| `regulatory` | regulatory actions |
| `hotspots` | the desk's watch points |

```
get_world_events(layers="waterways,submarine_cables", days_back=30)
```

**Narrowing earns depth, and this is the whole point of the argument.** All
layers together already run to roughly 40,000 tokens with two of them truncated.
Ask for one or two and the row budget the others were spending is yours — you
get materially more of what you actually asked for. Asking for everything is
almost always the wrong call: it is slower, it is truncated, and the answer is
buried.

Omitting `layers` returns the six default layers. That is a fallback, not a
default worth choosing.

## Step 2 — Check what came back
The response echoes `layers_requested` and `layers_available`. If you asked for
a name that is not a layer, it comes back in **`layers_unknown`** — read it. A
payload that looks complete but silently dropped your selection is the failure
mode this field exists to prevent.

`row_limits` states where a layer was capped. If a layer you are relying on was
truncated, say so rather than presenting a partial list as the full picture.

## Step 3 — Answer geographically
- **Name the place, then the event.** This layer's value is location.
- **`snapshot_time` dates the whole payload.** Give it. These are live-ish
  feeds, not a dated editorial note.
- **Do not infer market impact from a map.** A conflict event near a waterway is
  not the same as a disrupted waterway. If the user wants the read, that is
  **world-brief** or **risk-radar**; this skill supplies the geography.
- **Do not aggregate counts into a trend.** More rows this week than last can be
  reporting coverage, not escalation.

## Worked shape
> **"What's the risk to shipping through Hormuz right now?"**
>
> `get_world_events(layers="waterways", days_back=30)` for the chokepoint
> itself, then `get_coverage(area="real-assets-shipping")` for Antevo's written
> read, and `get_risk_radar()` if they want the graded downside.
>
> The map says what is there; the desk says what it means. Keep them separate
> and attribute each.

## Hand-offs
- What it means → **world-brief** or **desk-read**
- Graded downside → **risk-radar**
- How it developed → **story-timeline**
