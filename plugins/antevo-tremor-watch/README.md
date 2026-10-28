# Antevo Tremor Watch for Claude

Ask Claude whether markets are under strain and get the Antevo Tremor Index's answer: every week, how many of 753 relationships between markets stopped behaving, across equity regions, US sectors, credit, bonds, commodities, FX and crypto, and volatility. A pair has stopped behaving when its correlation is two standard deviations away from its own previous two years. This week is read against a normal Friday since 2001, family by family, with the new breaks of the last four weeks, any week's pairs, and every reading since 1997.

Every answer names its week and how to cite it. Derived statistics only, never price or index levels. Descriptive, not a forecast, and not investment advice.

## What you need

Nothing. The connector is public: no account and no sign-in. It holds no personal data and cannot see anyone's portfolio. For questions about your own holdings, use the Antevo Wealth plugin.

## What this plugin contains

- **One remote connector**: `https://api.antevo.ch/mcp/tremor/mcp`, run by Antevo. Nothing runs on your computer: no local server, no hooks, no scripts.
- **Three skills** that teach Claude how to use the connector well:

| Skill | What it does |
|-------|--------------|
| `market-strain` | This week's reading: how many times a normal Friday, its status and rank, and where the breaks gather |
| `what-broke` | The pairs that stopped behaving, coming apart or moving closer, and what is newly broken |
| `episode-compare` | This week set against 2008, 2020 or any period since 1997 |

## What it sends, and where

- Claude calls the connector's four tools with the arguments a question needs, such as a week, a family or a market name. They go to Antevo's server at api.antevo.ch, which answers from Antevo's weekly Tremor index.
- No tool takes an account, a name or a portfolio. There is no sign-in, so Claude holds no token for this connection.
- Every tool only reads. Nothing is changed, bought, sold or moved.
- Your AI provider receives what the connector returns, under that provider's own terms.
- The plugin sends nothing anywhere else.

## Privacy, terms and support

- Privacy policy: https://antevo.ch/policies/privacy-policy
- Terms of use: https://antevo.ch/policies/terms-of-use
- Support: contact@antevo.ch, or https://antevo.ch/contact
- The index and its method: https://antevo.ch/tremor-watch/
