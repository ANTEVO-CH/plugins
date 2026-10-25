# Antevo Executive Brief for Claude

Ask Claude what is happening in markets and the world, and get the Antevo Executive Brief's answer: today's editorial read, the risk radar and how it has changed, the forward calendar, Antevo's own probability layer, per-sector desk reads from shipping to art, a world map of chokepoints, conflicts and disasters, and macro-economic history back to 1920.

Every answer is dated and names its source. This is editorial market intelligence, not investment advice.

## What you need

Nothing. The connector is public: no account and no sign-in. It holds no personal data and cannot see anyone's portfolio. For questions about your own holdings, use the Antevo Wealth plugin.

## What this plugin contains

- **One remote connector**: `https://api.antevo.ch/mcp/executive/mcp`, run by Antevo. Nothing runs on your computer: no local server, no hooks, no scripts.
- **Nine skills** that teach Claude how to use the connector well:

| Skill | What it does |
|-------|--------------|
| `world-brief` | What's happening in markets and the world: the editorial read, grounded in the numbers |
| `risk-radar` | What could go wrong from here: each risk graded as published, paired with the reading that would settle it |
| `emerging-risks` | How the risk board has moved over weeks: new, escalating, entrenched, gone |
| `signal-read` | Antevo's own probability layer: live bands only, dated |
| `decode` | What a move actually means, in the desk's own plain language |
| `story-timeline` | How a story developed, from the dated archive, including where the view shifted |
| `desk-read` | Antevo's written view on one area, from shipping and aviation to succession and art |
| `world-map` | Chokepoints, conflicts, disasters, displacement, sanctions, cyber and regulatory events, by place |
| `macro-history` | The long run: prices, rates, house prices and production for about 180 countries |

## What it sends, and where

- Claude calls the connector's tools with the arguments a question needs, such as a date, a coverage area, a map layer, a country or a series ticker. They go to Antevo's server at api.antevo.ch, which answers from Antevo's published brief, its dated archive and its reference data.
- No tool takes an account, a name or a portfolio. There is no sign-in, so Claude holds no token for this connection.
- Every tool only reads. Nothing is changed, bought, sold or moved.
- Your AI provider receives what the connector returns, under that provider's own terms.
- The plugin sends nothing anywhere else.

## Privacy, terms and support

- Privacy policy: https://antevo.ch/policies/privacy-policy
- Terms of use: https://antevo.ch/policies/terms-of-use
- Support: contact@antevo.ch, or https://antevo.ch/contact
