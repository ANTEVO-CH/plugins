---
name: succession-readiness
description: >-
  Answer "if something happened to me tomorrow, what's missing?" from an Antevo
  Wealth household's own succession data. Use when the user asks how ready their
  succession or estate plan is, what their family would need if they died or
  could not act, what to sort out before seeing their lawyer or notary, or which
  Legacy checklist items are still open. Orchestrates the Antevo Wealth MCP
  connector's succession tools (readiness, checklist) with family, documents and
  goals. People appear by role, never by name. Read-only; not legal or tax advice.
compatibility: >-
  Requires the Antevo Wealth MCP connector with get_succession_readiness and
  get_succession_checklist. If they are not available, or a call says the
  connection doesn't include succession readiness yet, tell the user to
  disconnect Antevo Wealth and connect it again, then stop.
---

# Antevo Wealth — Succession readiness

Turn the household's succession data into one answer a family can act on: where
it stands, the biggest gaps, and who to involve for each.

## Before you start
- **Connector check.** No `get_succession_readiness` tool → ask the user to connect Antevo Wealth, then stop. A result saying the connection doesn't include succession readiness → pass that on (disconnect and connect again), then stop.
- **Plan or role.** A result saying succession readiness isn't available on this account, or is shared with the household's principals only → pass on its message as it stands and stop. Don't guess why.
- **Household.** Omit `household_id` unless the user belongs to more than one; then ask which.

## Step 1 — Gather
- `get_succession_readiness(household_id)` — readiness band (present / total), urgency, material gaps, signals with weights and recommendations, people and structures by role, jurisdictions.
- `get_succession_checklist(household_id)` — each Legacy checklist item with its group and status (confirmed / open / not relevant).
- Context, only as needed:
  - `list_documents(household_id)` — whether a will, power of attorney, healthcare directive, letter of wishes or property deeds are in the vault.
  - `list_family(household_id)` — roles and structures only. It returns real names: **refer to people by the roles the readiness tool uses (Principal, Spouse, Child A, Trust 1), never by name**, unless the user names them first.
  - `list_goals(household_id)` — a legacy or education goal that the plan should serve.

## Step 2 — Analyse
- **Where it stands.** The readiness band with its count (e.g. 4 of 7 material inputs), and the urgency label as returned.
- **Missing data vs planning gaps.** A material gap is an input not yet recorded (no will on file, no date of birth); a signal is a planning issue in what is recorded (sole director, forced heirship, a trust ending soon). Keep them apart.
- **The top three.** Rank by the signal weights and the material gaps the tool returns; never re-score.
- **Open checklist items.** By group; skip items marked not relevant.
- **Who to involve.** For each gap, the kind of professional who handles it — your lawyer or notary (will, powers of attorney, guardianship), your tax adviser (cross-border, forced heirship), your trustee (trust wind-down, letter of wishes), your bank (account access). Kinds, never named firms.

## Step 3 — Output
```
# Succession readiness — {household} · {as-of}

**Read.** {1–2 lines: the band with its count, and the single most important gap.}

## The three things to sort out first
1. {gap or signal} — {what it needs} · {who to involve}
2. …
3. …

## Checklist still open
- {group}: {item}, {item}

## Documents to add to the vault
- {document} — {why it matters here}

*Based on your Antevo data as of {as-of}. Information, not legal or tax advice;
review with your lawyer, notary or tax adviser.*
```

## Guardrails
- **No names.** Use the roles the tools return. Never ask for, guess or reconstruct a real name, date of birth, address or account number.
- **No notes, no secrets.** The checklist never returns notes; never ask the user where seed phrases, passwords or keys are kept.
- **Figures as returned.** Quote the band, counts and urgency exactly; never estimate a tax or duty amount.
- **Information, not legal or tax advice.** Say so. No regulated titles for yourself or Antevo; no named firms or products.
- **Empty is data.** `no_family_record` → say there is nothing to assess yet and pass on its next step (add the family on the Legacy page). It is not a clean bill of health.
- **Read-only.** This skill does not tick checklist items or change records; point the user to the Legacy page for that.
