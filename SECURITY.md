# Security Policy

Report security issues **privately** to **security@vestai.ai** (or support@vestai.ai).
Please do not open public GitHub issues for vulnerabilities.

## Scope

This repository contains only the VestAI plugin manifest and Agent Skills — **no
backend code, secrets, or customer data.** The plugin points Claude at the hosted
VestAI MCP endpoint (`https://api.vestai.ai/mcp/sse`), which is protected by
OAuth 2.1. Accessing any wealth data requires the user's own VestAI login and
explicit consent, and every change is confirmation-gated.

In scope: the plugin manifest, the skill instructions, and the documented MCP
connection. For the hosted VestAI service, see https://vestai.ai.
