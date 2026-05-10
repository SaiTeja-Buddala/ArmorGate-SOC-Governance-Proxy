"""
ArmorGate — HITL Queue and Slack Approval Handler
===================================================
Module: armorgate/hitl_handler.py

Description:
    The HITL (Human-in-the-Loop) Handler manages the approval workflow for
    medium-risk actions flagged by the ArmorGate Policy Engine. It acts as
    the interface between the automated policy evaluation and human reviewers,
    ensuring that potentially impactful SOC agent actions receive explicit
    human authorization before execution.

    Responsibilities:
        - Receive medium-risk Action Requests routed from the Policy Engine.
        - Persist pending approvals in the HITL Queue.
        - Send rich approval prompts to Slack (channel or DM) with context
          (agent identity, action type, target resource, risk rationale).
        - Listen for Slack interactive callbacks (Approve / Reject).
        - On Approve  → release the action to execution and notify Audit Log.
        - On Reject   → route the action to the Deny+Block path and notify
                       the Audit Log with the human reviewer’s identity.
        - Enforce approval timeouts (auto-deny after configurable TTL).

Status: placeholder — implementation pending.
Planned integration: Slack Bolt SDK + signed-request verification.
"""

# TODO: Implement HITLQueue, SlackApprovalClient, and reject → deny routing.
