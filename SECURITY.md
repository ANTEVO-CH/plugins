# Security Policy

Report security issues **privately** to **contact@antevo.ch**.
Please do not open public GitHub issues for vulnerabilities.

## Scope

This repository contains only plugin manifests and Agent Skills — **no backend
code, secrets, or customer data.** The plugins point Claude at hosted Antevo MCP
endpoints:

- **Executive** (`https://api.antevo.ch`) and **Trademark screening**
  (`https://trademark.antevo.ch`) are public: no account, and no personal data
  reachable.
- **Wealth** (`https://api.antevo.ch`, OAuth 2.1) reaches the user's own household
  only with their Antevo Wealth login and explicit consent, and every change is
  confirmation-gated.
- **Mandates** (`https://api.antevo.ch`, OAuth 2.1) reaches the signed-in firm's
  own client book. It can create and update records; irreversible actions return a
  plan first, and the skills ask before any change.

In scope: the plugin manifests, the skill instructions, and the documented MCP
connections. For the hosted services, see https://antevo.ch/mcp.
