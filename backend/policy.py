
from datetime import datetime, timezone

# SentinelLab policy engine.
# This module evaluates simulated actions only.
# It does not access real email, calendars, or accounts.

ALLOWED_ACTIONS = {
    "inspect_inbox",
    "read_email",
    "view_calendar",
}

APPROVAL_REQUIRED_ACTIONS = {
    "archive_email",
    "create_calendar_event",
    "send_email",
}

BLOCKED_ACTIONS = {
    "delete_email",
    "export_credentials",
    "send_passwords",
    "change_security_policy",
}


def evaluate_action(action: str, approved: bool = False) -> dict:
    """
    Evaluate an action independently of the AI model.

    Returns a policy decision. This function does not execute
    the requested action.
    """
    action = action.strip().lower()

    if action in BLOCKED_ACTIONS:
        decision = "blocked"
        reason = "This action is prohibited by SentinelLab policy."

    elif action in ALLOWED_ACTIONS:
        decision = "allowed"
        reason = "This read-only simulated action is permitted."

    elif action in APPROVAL_REQUIRED_ACTIONS and not approved:
        decision = "approval_required"
        reason = "This action requires explicit human approval."

    elif action in APPROVAL_REQUIRED_ACTIONS and approved:
        decision = "allowed"
        reason = "Approval was supplied for this simulated action."

    else:
        decision = "blocked"
        reason = "Unknown actions are denied by default."

    return {
        "action": action,
        "decision": decision,
        "reason": reason,
        "approved": approved,
        "executed": False,
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
    }
