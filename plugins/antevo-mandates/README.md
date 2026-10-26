# Antevo Mandates for Claude

For external asset managers and family offices: ask Claude which clients are due a review, prepare for a client meeting from the record, or find where succession planning is incomplete across the book. It reads your firm's own client book in Antevo Mandates, with your firm's own permissions applied.

Every answer comes from the record and is dated. This is preparation support, not investment, tax or legal advice.

## What you need

An Antevo Mandates firm account. Mandates is available by arrangement with Antevo (https://antevo.ch/mandate); members of your firm then sign in with their own account the first time Claude uses the connector.

## What this plugin contains

- **One remote connector**: `https://api.antevo.ch/mcp/mandates/mcp`, run by Antevo. Nothing runs on your computer: no local server, no hooks, no scripts.
- **Three skills** that teach Claude how to use the connector well:

| Skill | What it does |
|-------|--------------|
| `reviews-due` | Overdue first, then the next thirty days by risk tier, and a review recorded only on your go |
| `meeting-prep` | One page to walk in with, from the dossier, goals, team and correspondence |
| `succession-scan` | Where succession planning is thin: clients with no checklist reported as "not started" |

## What it sends, and where

- Claude calls the connector's tools with what a question needs, such as a client's name or ID and, when you ask it to record a review, the note to file. They go to Antevo's server at api.antevo.ch, which answers from your own firm's book only.
- Answers can include client details from that book: profile and AUM, review dates, goals, the assigned team, documents, and client email with its summary and compliance flags. Your AI provider receives what the connector returns, under that provider's own terms.
- Sign-in uses OAuth 2.1 with your Antevo account. Claude holds a token for that connection; you can disconnect it at any time in Claude's connector settings.
- The connector can change records in your firm's own book: record a review, update a client, assign a team member, add a goal, file a document, or create a share link to a document that anyone holding it can download, for up to 30 days. Converting a prospect, deleting a document or creating a share link returns a plan first and runs only when it is called again with confirmation, and the skills ask before any change. A read-only sign-in refuses changes. It cannot place a trade or move money.
- Generating a full meeting brief uses credits; the meeting-prep skill asks first.
- The plugin sends nothing anywhere else.

## Privacy, terms and support

- Privacy policy: https://antevo.ch/policies/privacy-policy
- Terms of use: https://antevo.ch/policies/terms-of-use
- Connection guide: https://antevo.ch/mcp/mandates/
- Support: contact@antevo.ch, or https://antevo.ch/contact
