# Antevo Strategy Radar for Claude

Ask Claude what changed today for your company's strategy and get Antevo's answer: every morning Antevo's desk writes a business board of risks and opportunities for companies — trade and tariffs, regulation, supply and inputs, shipping, energy, demand, currencies, funding and rates, labour, technology, cyber, geopolitics and climate. Each entry carries its theme and the exposures it touches, its impact, likelihood and trend in words, why it matters with a date, what to watch, the event that would make a response right, and two or three possible responses with their reasons.

Claude matches that board to your company. Five short questions — about three minutes, no figures — become a profile of exposure tags and objectives that stays with Claude. Possible responses with reasons, never advice.

## What you need

Nothing. The connector is public: no account and no sign-in. It holds no personal data and no company data.

## What this plugin contains

- **One remote connector**: `https://api.antevo.ch/mcp/strategy/mcp`, run by Antevo. Nothing runs on your computer: no local server, no hooks, no scripts.
- **Three skills** that teach Claude how to use the connector well:

| Skill | What it does |
|-------|--------------|
| `strategy-setup` | Five questions become your company profile, then today's board matched to it at once |
| `strategy-today` | What changed for your strategy today — linked risks and opportunities, each tied to the objective it touches |
| `board-read` | The whole board, today's or any morning in the last 400 days, by theme or exposure, or two mornings compared |

## What it sends, and where

- Claude calls the connector's two tools. `get_strategy_radar_setup` takes nothing; `get_business_board` takes only a date. They go to Antevo's server at api.antevo.ch.
- **Your company's answers, objectives and tags never go to Antevo.** No tool takes them. They stay in your conversation, or in a morning task you choose to save, with your AI provider under its own terms.
- Antevo sees that the board was read, like any web request.
- Every tool only reads. Nothing is changed, bought, sold or moved.
- The plugin sends nothing anywhere else.

## Privacy, terms and support

- Privacy policy: https://antevo.ch/policies/privacy-policy
- Terms of use: https://antevo.ch/policies/terms-of-use
- Support: contact@antevo.ch, or https://antevo.ch/contact
- The board and how it is made: https://antevo.ch/executive/strategy/
