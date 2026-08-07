# Security Policy

Report security issues **privately** to **contact@antevo.ch**.
Please do not open public GitHub issues for vulnerabilities.

## Scope

This repository contains only the Antevo Wealth plugin manifest and Agent Skills —
**no backend code, secrets, or customer data.** The plugin points Claude at the
hosted Antevo Wealth MCP endpoints (on `https://api.vestai.ai`, OAuth 2.1).
Accessing any wealth data requires the user's own Antevo Wealth login and explicit
consent, and every change is confirmation-gated.

In scope: the plugin manifest, the skill instructions, and the documented MCP
connection. For the hosted Antevo Wealth service, see https://antevo.ch/wealth.
