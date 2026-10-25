# Antevo Trademark for Claude

Ask Claude whether a name is already on the registers before you launch it. Screen a brand name, or a whole shortlist with the companies and domains already registered under each name, across 50+ registers; find the Nice classes a business like yours files in; read who holds a mark and how they file; and check the opposition window in any of twenty offices, including the ones that run it after registration. With an Antevo sign-in, Claude also works through your own watchlist, conflicts and deadlines, and can investigate who is behind a holder.

Every answer is dated and names the registers it read. A screen is not a clearance: this is intelligence, not legal advice, and your counsel advises on use.

## What you need

Nothing, for screening, class suggestions, holder reads and opposition windows. Your watchlist, conflicts, deadlines and holder investigations need an Antevo Trademark account: Claude asks you to sign in the first time one of those tools is used. Some reads depend on your plan; Claude says when one isn't included.

## What this plugin contains

- **One remote connector**: `https://trademark.antevo.ch/mcp`, run by Antevo. Nothing runs on your computer: no local server, no hooks, no scripts.
- **Four skills** that teach Claude how to use the connector well:

| Skill | What it does |
|-------|--------------|
| `clearance-check` | What is on the registers near a name, and for a shortlist the companies and domains under it, and who holds it. Never a clearance |
| `opposition-deadline` | How long there is to oppose in a given office, what starts the clock, and the provision |
| `conflict-review` | New filings near your watched names, ranked by consequence, with your sign-in |
| `holder-investigation` | Who is behind a holder: the register read first, then a cited web dossier that uses a credit, asked first |

## What it sends, and where

- Claude calls the connector's tools with what a question needs: a name or a shortlist, Nice classes, countries, an office, a holder's name or a short description of a business. They go to Antevo's Trademark server at trademark.antevo.ch.
- To answer, that server reads Antevo's copy of the trademark registers, and EUIPO's search for EU marks. For a shortlist it also looks each name up in the Swiss commercial register (and the UK and Singapore company registers when you ask for those countries) and in the .ch and .com domain registries (and .sg for Singapore).
- A holder investigation sends the holder's name to an AI model with web search (Anthropic's Claude API), run by Antevo, which writes a dossier that cites its sources. It uses one of your credits, and Claude asks before running it.
- Sign-in uses OAuth with your Antevo account. Claude holds a token for that connection; you can disconnect it at any time in Claude's connector settings.
- After sign-in, the connector can add a name to your watchlist, follow a filer, or clear a conflict as not a threat, which you can undo. The skills ask before they change anything. It cannot file, oppose or renew a mark, and credits are never bought inside the conversation: they are bought on your Antevo desk.
- Your AI provider receives what the connector returns, under that provider's own terms.
- The plugin sends nothing anywhere else.

## Privacy, terms and support

- Privacy policy: https://antevo.ch/policies/privacy-policy
- Terms of use: https://antevo.ch/policies/terms-of-use
- Data sources: https://antevo.ch/trademark/data-sources
- Support: contact@antevo.ch, or https://antevo.ch/contact
