# Antevo — plugins & MCP connectors

Antevo's MCP connectors and Claude plugins, in one marketplace.

| Plugin | What it is | Account |
|---|---|---|
| **`antevo-wealth`** | Your portfolios, net worth, real assets, liabilities, risk, markets, geopolitics and daily brief — plus ten private-banker skills. | Antevo Wealth account |
| **`antevo-executive`** | The Antevo Executive Brief — editorial market and world intelligence, today and back through the dated archive, plus per-sector desk reads, a world map of chokepoints and cables, and a century of macro-economic history. | **None — public** |
| **`antevo-crypto`** | Antevo's crypto reference prices — one composite daily price per major pair, a year of history and technical signals. | **None — public** |
| **`antevo-mandates`** | Your firm's client book — reviews due, meeting preparation and succession gaps, from the record. | Antevo Mandates firm account |
| **`antevo-trademark`** | Screen a brand name across the registers, read who holds a mark and how they file, and check the opposition window in twenty offices. Your own watchlist and deadlines connect separately. | **Screening: none.** Watchlist: Antevo Trademark account |

MCP is an open standard, so these work with **any MCP client** (Claude, Cursor,
VS Code/Copilot, Goose, and others). This repo packages them as one-install
Claude plugins that wire up the connector *and* the skills in a single step.

> You need an [Antevo Wealth](https://antevo.ch/wealth) account to see your own
> data. The universal market surfaces (markets brief, executive brief, signals,
> geopolitics) work on a free account; the personal surfaces (net worth, portfolio,
> real assets, liabilities, family, documents) show your household once you connect.

## Prefer a terminal?

`@antevo/cli` drives the same connectors from a shell — no assistant, scriptable,
read-only by default:

```bash
npx @antevo/cli brief     # no account, nothing installed
npx @antevo/cli tools     # every tool the server has, live
npx @antevo/cli login     # device code — works over SSH and in containers
```

It speaks MCP rather than wrapping a separate API, so it reaches tools added
after you installed it. Source: [ANTEVO-CH/cli](https://github.com/ANTEVO-CH/cli).

## Use with any MCP client

Point your client at the remote Antevo Wealth MCP servers — they advertise
OAuth 2.1, so the client walks you through sign-in (no credentials are shared with
the assistant). Each domain is its own endpoint, e.g.:

```text
https://api.antevo.ch/mcp/wealth/mcp       # everything, one sign-in
https://api.antevo.ch/mcp/executive/mcp    # public brief, no account
https://trademark.antevo.ch/mcp            # trademark — screening needs no account
https://api.antevo.ch/mcp/crypto/mcp       # crypto reference prices, no account
https://api.antevo.ch/mcp/mandates/mcp     # your firm's client book, one sign-in
```

One connection covers the whole wealth surface. Per-domain endpoints
(`/mcp/portfolio/core/mcp`, `/mcp/intelligence/geo/mcp`, …) remain available if
you want a narrower tool set.

Trademark sits on its own host rather than under `api.antevo.ch`: it runs as a
separate service, and the address difference is structural, not an oversight. It
speaks Streamable HTTP only — it never served the deprecated `/sse` transport.

## Install in Claude

```text
# 1. add the marketplace (once)
/plugin marketplace add ANTEVO-CH/plugins

# 2. install what you need
/plugin install antevo-executive@antevo    # public — nothing to sign in to
/plugin install antevo-trademark@antevo    # screening public; watchlist needs a token
/plugin install antevo-wealth@antevo       # your account — OAuth on first use
/plugin install antevo-crypto@antevo       # public — nothing to sign in to
/plugin install antevo-mandates@antevo     # your firm — OAuth on first use
```

Works in Claude Code, Claude.ai (web) and Claude Desktop.

### Try it without an account

`antevo-executive` needs no sign-in — add it and ask:

```text
https://api.antevo.ch/mcp/executive/mcp
```

**The day:**
> *"What's happening in the markets?"* · *"What could go wrong from here?"* ·
> *"What's coming up this week?"* · *"What did the brief say on 9 August?"* ·
> *"How did the energy story develop?"*

**The desk's own view, one sector at a time:**
> *"What's Antevo's read on shipping?"* · *"How do you see aviation right now?"* ·
> *"Your view on succession planning?"* · *"What does the desk say about art?"* ·
> *"Give me the institutional read on commodities."*

**Where it is happening:**
> *"What's going on at the Strait of Hormuz?"* ·
> *"Which submarine cables run through the Red Sea?"* ·
> *"Where is displacement rising?"* · *"What disasters are active right now?"* ·
> *"Any new sanctions this month?"*

**The long run — around 180 countries, some series back to 1920:**
> *"What has Swiss inflation done since 2020?"* ·
> *"Compare house prices in France and Italy."* ·
> *"What were UK policy rates through the seventies?"* ·
> *"Show me industrial production for Germany."* ·
> *"What did Japanese CPI do after 1990?"*

`antevo-trademark`'s screening tools are open too — no account, no token:

```text
https://trademark.antevo.ch/mcp
```

> *"Has anyone filed anything close to my brand name?"* ·
> *"How long do I have to oppose an EU trademark?"* ·
> *"Does Japan run opposition before or after registration?"*

`antevo-crypto` needs no sign-in either:

```text
https://api.antevo.ch/mcp/crypto/mcp
```

> *"What's bitcoin worth?"* · *"How has ETH done this quarter?"* ·
> *"Is SOL above its 200-day?"* · *"Compare BTC and ETH since June."*

One composite reference price per pair — whole UTC days, not a live or tradable
quote. Antevo publishes the price, not its sources.

## What's inside

| Component | What it is |
|-----------|------------|
| **MCP connector** (`.mcp.json`) | The Antevo Wealth MCP servers (remote Streamable HTTP, OAuth 2.1, on `api.antevo.ch`) — portfolio & net worth (cash-inclusive AUM), risk, credit/leverage, real assets, markets & daily brief, **equity & technical analysis**, **geopolitics**, **watchlist**, **goals**, family and documents. One connection (`/mcp/wealth/mcp`) covers all of it; per-domain endpoints remain available for a narrower tool set. |
| **Skill: `daily-brief`** | The morning note — what matters today, what needs you: brief, alerts, open breaches, drift and the upcoming calendar in one read. |
| **Skill: `wealth-portfolio-review`** | Banker-grade review → net worth, allocation/concentration, risk & drift, leverage, real-asset yield, market backdrop → a dated memo. |
| **Skill: `portfolio-stress-radar`** | "Where could I get hurt?" — traces a shock across concentration → risk → leverage/covenants → liquidity into a consequence, with pre-emptions. |
| **Skill: `concentration-and-drift`** | Concentration map (name/class/currency/region) + drift vs target + ranked trim/rebalance candidates. |
| **Skill: `liquidity-and-leverage`** | Liquidity ladder (raisable in days / weeks / months+), leverage, and covenant headroom with distance to margin-call / DSCR / ICR triggers. |
| **Skill: `market-signals-period`** | Time-series read over a look-back window — what trended, what's new, how correlations shifted. |
| **Skill: `security-analysis`** | One instrument, both lenses — fundamentals (valuation, growth, margins, peers) + technicals (signal consensus, backtest). |
| **Skill: `geopolitical-risk`** | World risk read tied to your exposure — conflict, chokepoints, sanctions, cyber, narrative; cross-references where your capital sits. |
| **Skill: `watchlist-review`** | Your tracked instruments — movers, buy/sell signals, regime & volatility; hands off to `security-analysis`. |
| **Skill: `goals-review`** | Funding progress vs targets, the gap to plan, what's on track vs at risk. |

### `antevo-executive` — public, no account

| Component | What it is |
|-----------|------------|
| **MCP connector** | `https://api.antevo.ch/mcp/executive/mcp` — fifteen tools: the published Executive Brief, its risk radar and forward calendar, the dated archive, market snapshot and indices, a nine-layer world-events map, fourteen per-sector desk reads, and ~80,000 macro-economic series. Read-only, rate-limited, no personal data reachable. |
| **Skill: `world-brief`** | What's happening in markets and the world — the editorial read, grounded in the numbers. |
| **Skill: `risk-radar`** | What could go wrong from here — each risk graded by trend, impact and probability, paired with the reading that would settle it, plus the dated forward calendar. |
| **Skill: `emerging-risks`** | How the risk board has moved over weeks — what's newly on it, what has escalated, what is entrenched, what has left. |
| **Skill: `signal-read`** | Antevo's own probability layer — the odds it carries on named outcomes, which way they moved, and what the shape of the move means. Live bands only. |
| **Skill: `decode`** | What a move actually means, in plain language — the desk's own decode: what the tape says, the transferable lesson, and what an allocator does differently. |
| **Skill: `story-timeline`** | How a story developed — reconstructs the arc from the dated archive, including where the view shifted. |
| **Skill: `desk-read`** | Antevo's written view on ONE area — shipping, aviation, yachts, energy, infrastructure, real estate, commodities, geopolitics, AI, energy transition, demographics, generational wealth, succession, art. Retail or institutional; both are dated. |
| **Skill: `world-map`** | Where it is happening — shipping chokepoints, submarine cables, armed conflicts, disasters, displacement, sanctions, cyber and regulatory actions. Ask for the layers you need; narrowing buys depth. |
| **Skill: `macro-history`** | The long run — consumer prices, policy and market rates, house prices, industrial production and commodities for ~180 countries, some back to 1920. Quarterly published levels, always dated. |

### `antevo-trademark` — screening public, watchlist on a token

| Component | What it is |
|-----------|------------|
| **MCP connector** | `https://trademark.antevo.ch/mcp` — eleven tools. Three need no account: screen a name across the registers, read a holder's filing pattern, look up an opposition window. The rest reach the user's own desk and need a token from **antevo.ch/trademark → Settings → Connect your AI**. |
| **Skill: `clearance-check`** | "Is this name taken?" — screens the registers, then reads whoever holds the closest hits. Reports what exists and which registers were searched; it never clears a name for use. |
| **Skill: `opposition-deadline`** | "How long do I have?" — the window for any of twenty offices, what starts the clock, and the provision behind it. Leads with the trap: a minority of offices (Switzerland, Germany, Japan, Sweden) run opposition *after* registration, so "registered" does not mean too late. |
| **Skill: `conflict-review`** | The desk loop — what has been filed near the user's watched names, ranked by consequence and paired with its closing window; clear the noise, add a name to watch. Both writes are reversible and confirmed first. |

> Two things these skills will not do, by design: **clear a name** (a register
> search says what exists, not whether a name may be used — that turns on goods,
> territory and unregistered rights) and **call anyone a squatter** (a legal
> conclusion, and defamatory if wrong). They show the evidence and leave the
> conclusion to the reader and their counsel.

### `antevo-crypto` — public, no account

| Component | What it is |
|-----------|------------|
| **MCP connector** | `https://api.antevo.ch/mcp/crypto/mcp` — four tools: every covered pair with its latest reference price, one pair's price, up to 365 days of daily history, and technical signals. One composite daily price per pair across major exchanges, outlying quotes excluded. Read-only, rate-limited, no personal data reachable. |
| **Skill: `price-check`** | "What is bitcoin worth?" — the reference price for one pair or many, always dated, never passed off as a live quote. |
| **Skill: `crypto-performance`** | How a pair moved over a window — return, range and worst drawdown from the daily bars, with the exact dates used, and pairs compared on percentage moves. |
| **Skill: `technical-read`** | Moving averages, MACD, RSI, Bollinger and ATR on the reference price — the readings and the vote counts, translated into words and never into a trading recommendation. Stablecoin pegs are refused. |

### `antevo-mandates` — your firm's book, OAuth

| Component | What it is |
|-----------|------------|
| **MCP connector** | `https://api.antevo.ch/mcp/mandates/mcp` — the signed-in firm's client book: clients and dossiers, reviews, goals, team, documents, meeting briefs, succession and client email. **Not read-only:** it can create and update records; irreversible actions return a plan first. |
| **Skill: `reviews-due`** | The review list in the order it needs working — overdue first, then the next thirty days by risk tier — and, on an explicit go, a review recorded as done. |
| **Skill: `meeting-prep`** | One page to walk into a client meeting with, from the dossier, goals, team and correspondence. Offers the full generated brief, and says first that it uses credits. |
| **Skill: `succession-scan`** | Where succession planning is thin across the book — with clients who have no checklist at all reported as "not started", not as low urgency. |

> Every Mandates client-book tool takes a `firm_id`, and the connector has no tool
> that looks it up yet: the skills ask for it once and reuse it.

Invoke a skill explicitly with `/antevo-wealth:<skill>` (e.g.
`/antevo-wealth:portfolio-stress-radar`), or just ask in plain language — the skills
auto-trigger on the questions below.

## Critical questions you can ask

Once connected, fire these directly — each routes to a skill and drills straight
into the detail:

**Start the day**
- "What's my brief?" · "Anything I should know today?" · "What needs my attention?"

**Where am I exposed**
- "Where could I get hurt this week?" · "Stress my book against an oil shock / equity −20% / rates +50bp."
- "Am I over-leveraged? What's my margin-call risk?"

**Concentration & allocation**
- "Am I too concentrated? What's my single-name risk?"
- "Have I drifted from my target allocation — what should I trim?"

**Liquidity & leverage**
- "How fast could I raise cash? Could I meet a capital call without forced sales?"
- "What's my blended LTV and covenant headroom?"

**Markets over a period**
- "Summarise the signals over the last 3 months." · "How have correlations shifted this quarter?"
- "What's been trending — and what rolled off?"

**Analyse a security**
- "Analyse NVDA." · "Is Apple expensive?" · "Technicals on the S&P 500."

**Geopolitics**
- "What are the geopolitical risks right now?" · "How exposed am I to the Strait of Hormuz / China?"

**Watchlist & goals**
- "What's on my watchlist — anything signalling?" · "How am I tracking against my goals?"

**The whole picture**
- "Review my portfolio." · "How am I doing?" · "Give me a net-worth breakdown."

**Trademark — screening needs no account**
- "Is this name taken?" · "Has anyone filed anything close to my brand?"
- "Who owns this trademark, and how do they file?"
- "How long do I have to oppose an EU trademark?" · "Have I missed the window in Japan?"
- "What's near my brands this week?" · "Watch this name for me." *(token)*

**The public brief — no account needed**
- "What's happening in the markets?" · "What could go wrong from here?"
- "What new risks have emerged this month?" · "What's coming up this week?"
- "How did the energy story develop?" · "What did the brief say on 9 August?"
- "What are the odds the strait reopens?" · "What does your model say?"
- "Explain that move to me." · "I don't follow markets — what's going on?"

> Period analytics that span the *household over time* (net-worth trajectory, risk
> radar across 6 months, drawdown/VaR history) need connector history tools that
> aren't exposed yet — on the roadmap. Market-signal trends over a window work today.

Read-only: the connector surfaces recommendations and only makes a change after you
approve a plan. AI outputs are informational support only — not investment, tax, or
legal advice.

## Structure

```
.claude-plugin/marketplace.json              # the catalog
plugins/antevo-crypto/
├── .claude-plugin/plugin.json
├── .mcp.json                                # public crypto reference prices (no auth)
└── skills/
    ├── price-check/SKILL.md
    ├── crypto-performance/SKILL.md
    └── technical-read/SKILL.md
plugins/antevo-executive/
├── .claude-plugin/plugin.json
├── .mcp.json                                # public Executive connector (no auth)
└── skills/
    ├── world-brief/SKILL.md
    ├── risk-radar/SKILL.md
    ├── emerging-risks/SKILL.md
    ├── signal-read/SKILL.md
    ├── decode/SKILL.md
    └── story-timeline/SKILL.md
plugins/antevo-mandates/
├── .claude-plugin/plugin.json
├── .mcp.json                                # the firm's client book (OAuth 2.1)
└── skills/
    ├── reviews-due/SKILL.md
    ├── meeting-prep/SKILL.md
    └── succession-scan/SKILL.md
plugins/antevo-trademark/
├── .claude-plugin/plugin.json
├── .mcp.json                                # trademark.antevo.ch — its own host
└── skills/
    ├── clearance-check/SKILL.md
    ├── opposition-deadline/SKILL.md
    └── conflict-review/SKILL.md
plugins/antevo-wealth/
├── .claude-plugin/plugin.json               # plugin manifest
├── .mcp.json                                # one-connect Antevo Wealth MCP connector
└── skills/
    ├── daily-brief/SKILL.md
    ├── wealth-portfolio-review/SKILL.md
    ├── portfolio-stress-radar/SKILL.md
    ├── concentration-and-drift/SKILL.md
    ├── liquidity-and-leverage/SKILL.md
    ├── market-signals-period/SKILL.md
    ├── security-analysis/SKILL.md
    ├── geopolitical-risk/SKILL.md
    ├── watchlist-review/SKILL.md
    └── goals-review/SKILL.md
```

## Links
- Connectors: https://antevo.ch/mcp · Wealth: https://antevo.ch/wealth · Executive: https://antevo.ch/executive · Trademark: https://antevo.ch/trademark · Mandates: https://antevo.ch/mandate
- Privacy: https://antevo.ch/policies/privacy-policy · Terms: https://antevo.ch/policies/terms-of-use
- Contact: contact@antevo.ch

---
*This repo contains only plugin manifests, skills, and pointers to the hosted
Antevo MCP endpoints — no backend code.*
