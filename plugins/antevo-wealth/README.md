# Antevo Wealth for Claude

Ask Claude about your own wealth, held in your Antevo Wealth account: net worth across accounts, real assets and liabilities; positions, allocation and concentration; today's brief for your household; risk, drift and stress; credit, goals and your calendar. Tell Claude what you hold and it can record it for you, after you approve each change.

Every answer is dated and names its source. This is information, not investment, tax or legal advice.

## What you need

An Antevo Wealth account. You sign in with it the first time Claude uses the connector, and you approve the connection on an Antevo screen. Some sections, such as risk analysis, real assets and credit, depend on your plan; Claude says when a section isn't included.

## What this plugin contains

- **One remote connector**: `https://api.antevo.ch/mcp/wealth/mcp`, run by Antevo. Nothing runs on your computer: no local server, no hooks, no scripts.
- **Twelve skills** that teach Claude how to use the connector well:

| Skill | What it does |
|-------|--------------|
| `record-holdings` | Records what you already hold, from a statement or a list, after you approve each plan |
| `advisor-meeting-prep` | Before you meet your banker: your book with that bank, what needs attention, the questions to ask |
| `daily-brief` | Your household's morning note: what matters today and what needs you |
| `wealth-portfolio-review` | A dated review: net worth, allocation, risk and drift, leverage, real assets |
| `portfolio-stress-radar` | Where you could get hurt, traced through concentration, risk, leverage and liquidity |
| `concentration-and-drift` | Concentration by name, class, currency and region, and drift against target |
| `liquidity-and-leverage` | What can be raised in days, weeks or months, and the headroom to covenant triggers |
| `market-signals-period` | What trended over a window, what's new, where correlations stand |
| `security-analysis` | One instrument through both lenses: fundamentals and technicals |
| `geopolitical-risk` | The world's risks tied to your exposure |
| `watchlist-review` | Your tracked instruments, what moved and why |
| `goals-review` | Funding progress against targets, and the gap to plan |

## What it sends, and where

- Claude calls the connector's tools with the arguments a question needs, such as a household, a portfolio, a country or a security. The connector answers from your own household's data only.
- Sign-in uses OAuth 2.1 with your Antevo account. Claude holds a token for that connection; you can disconnect it at any time in Antevo Wealth under Settings, Agent Access.
- Two tools change your records: `create_portfolio` and `add_position`. Each returns a plan first and writes nothing until you say yes. Nothing is ever bought, sold or moved.
- The plugin sends nothing anywhere else.

## Privacy, terms and support

- Privacy policy: https://antevo.ch/policies/privacy-policy
- Terms of use: https://antevo.ch/policies/terms-of-use
- Support: contact@antevo.ch, or https://antevo.ch/contact
