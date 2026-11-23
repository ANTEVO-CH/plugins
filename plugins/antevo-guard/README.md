# Antevo Guard for Claude

Ask Claude whether a company you are about to pay matches the public record. Guard reads the company register, VAT validation, the company's LEI, and the website and email domain an invoice or a request came from, and reports what does not match, each line with its source and date. With an Antevo sign-in, Claude also keeps your payee book, reads an invoice or a change-of-bank-details letter against it, and watches for lookalikes of your own company name.

Guard reports what the records say. It never calls a payee safe or verified, never scores one, and never says whether a payment should be made: that decision stays with you.

## What you need

Nothing, for checking a company or a domain: those two tools are free within a daily limit. The payee book, alerts, document checks and name watches need an Antevo account: Claude asks you to sign in the first time one of those tools is used. A document check uses one credit; credits are bought on antevo.ch/account, never inside the conversation.

## What this plugin contains

- **Two remote connectors**, both run by Antevo. Nothing runs on your computer: no local server, no hooks, no scripts.
  - `https://api.antevo.ch/mcp/guard/mcp`: the two public checks, no account.
  - `https://api.antevo.ch/mcp/guard/me/mcp`: every tool, with your Antevo sign-in.
- **Four skills** that teach Claude how to use them well:

| Skill | What it does |
|-------|--------------|
| `payee-check` | One company before you pay it: register, VAT, LEI, website and email domain. What matches and what does not |
| `document-check` | An invoice or a change-of-bank-details letter read against the record and your payee book. Uses a credit, asked first |
| `payee-book-review` | What changed on the companies you pay, and the alerts still open |
| `impersonation-watch` | A daily watch for lookalike domains, companies and trademark filings near your own company name |

## What it sends, and where

- Claude sends what a check needs: a company name, its country, and where you have them its registration number, VAT number, LEI, website, the email domain the request came from, the two letters a bank account number starts with, and the bank's BIC. **Never the account number itself**: no tool accepts one, and the skills tell Claude to send only its country.
- To answer, Antevo's server reads the company registers it covers (Switzerland, the UK, Singapore and Cyprus), the EU's VIES service for VAT numbers, GLEIF for LEIs, public domain registration records, certificate logs and DNS.
- A document check sends the text of the document Claude already holds. Any account number in it is cut to its country before anything else reads it.
- Sign-in uses OAuth with your Antevo account. Claude holds a token for that connection; you can disconnect it at any time in Claude's connector settings.
- After sign-in, the connector can save or remove a payee, dismiss an alert and start a name watch. Each returns a preview first and changes nothing until you say yes.
- Your AI provider receives what the connector returns, under that provider's own terms.
- The plugin sends nothing anywhere else.

## What Guard is not

It checks companies, not people, and holds nothing about your payments. It is not a sanctions screen, an anti-money-laundering check or a know-your-customer process, and it does not replace one.

## Privacy, terms and support

- Privacy policy: https://antevo.ch/policies/privacy-policy
- Terms of use: https://antevo.ch/policies/terms-of-use
- Support: contact@antevo.ch, or https://antevo.ch/contact
