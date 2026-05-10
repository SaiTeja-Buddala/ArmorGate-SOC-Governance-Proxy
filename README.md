# ArmorGate

> Policy-enforced governance proxy for autonomous SOC agents.

## Overview

ArmorGate is an agentic governance proxy that intercepts machine-to-machine traffic between autonomous SOC agents and production environments. It enforces deterministic security policies aligned with ARMOR resilience controls and OWASP LLM Top 10 (Excessive Agency) before any high-impact action reaches production systems.

## Architecture

The ArmorGate flow operates as follows:

1. **SOC Agent** submits an Action Request to the ArmorGate Policy Engine.
2. **ArmorGate Policy Engine** (backed by a Policy Store) evaluates the request and routes it to one of three paths:
   - **Auto-Approve** — for low-risk actions that pass policy checks automatically.
      - **HITL Queue with Slack Approval** — for medium-risk actions requiring human review before execution.
         - **Deny + Block** — for high-risk policy violations that are immediately rejected.
         3. All three paths terminate in a centralized **Audit Log**.
         4. Rejected HITL approvals route back to the **Deny + Block** path.
         5. The **Audit Log** feeds back to the **Policy Store** for adaptive policy refinement over time.

         ## Key Features

         - Deterministic policy enforcement on agentic workflows
         - Human-in-the-Loop (HITL) approval via Slack integration
         - Excessive Agency risk mitigation per OWASP LLM Top 10
         - Centralized audit layer for previously invisible agentic actions
         - ARMOR-aligned resilience controls
         - Bidirectional Policy Store with adaptive learning from audit feedback

         ## Tech Stack

         - **Python** — core language
         - **FastAPI or Flask** — proxy engine framework
         - **Slack API** — HITL approval workflow
         - **JSON or YAML** — policy definitions
         - **SQLite or PostgreSQL** — audit logging
         - **Docker** — containerization (planned)

         ## Project Status

         **Active development — May 2026 to Present.**

         Currently in architecture and design phase. Core policy engine and HITL workflow in progress.

         ## Motivation

         Modern AI-driven SOC deployments create an agentic visibility gap — autonomous agents take high-impact actions with no human checkpoint. ArmorGate addresses this by sitting as a governance proxy between the agent and production, enforcing policy before damage occurs.

         ## References

         - [OWASP LLM Top 10 — LLM08: Excessive Agency](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
         - [MITRE ATLAS — Adversarial Threat Landscape for AI Systems](https://atlas.mitre.org/)
         
