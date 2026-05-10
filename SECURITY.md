# Security Policy

## Project Status

ArmorGate is in active architecture and design phase (May 2026 — Present).
There is no executable code or deployed instance yet. The current repo
contains design documentation, placeholder modules, and infrastructure stubs.

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |

## Reporting a Vulnerability

If you believe you have found a security vulnerability in ArmorGate —
including in the design, the placeholder code, or the documented
architecture — please report it privately rather than opening a public
issue.

Preferred channel: **GitHub Security Advisories** for this repository.

1. Navigate to the **Security** tab of this repo.
2. Click **Report a vulnerability**.
3. Provide a description, reproduction steps (if applicable), and impact.

You can expect:

- Acknowledgement within **5 business days**.
- A triage decision and severity assessment within **10 business days**.
- Coordinated disclosure once a fix or mitigation is in place.

## Out of Scope

- Findings in dependencies not yet pinned by this repo.
- Theoretical issues in the placeholder modules that contain no
  executable logic.
- Social-engineering attacks against project maintainers.

## Secrets Handling

This repository must never contain real credentials, tokens, or keys.
All sensitive values are referenced via environment variables (see
`docker-compose.yml`). The `.gitignore` excludes `.env`, `secrets/`,
`*.secret`, and local audit databases. If you discover a committed
secret, please report it through the channel above so it can be rotated
and purged from history.
