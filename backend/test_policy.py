
from policy import evaluate_action


def test_read_only_action_is_allowed():
    result = evaluate_action("read_email")

    assert result["decision"] == "allowed"
    assert result["executed"] is False


def test_delete_email_is_blocked():
    result = evaluate_action("delete_email")

    assert result["decision"] == "blocked"
    assert result["executed"] is False


def test_export_credentials_is_blocked():
    result = evaluate_action("export_credentials")

    assert result["decision"] == "blocked"
    assert result["executed"] is False


def test_send_email_requires_approval():
    result = evaluate_action("send_email", approved=False)

    assert result["decision"] == "approval_required"
    assert result["executed"] is False


def test_unknown_action_is_blocked():
    result = evaluate_action("run_arbitrary_code")

    assert result["decision"] == "blocked"
    assert result["executed"] is False


def test_action_name_is_normalized():
    result = evaluate_action("  READ_EMAIL  ")

    assert result["action"] == "read_email"
    assert result["decision"] == "allowed"

def test_approved_send_email_is_allowed_by_policy():
    result = evaluate_action("send_email", approved=True)

    assert result["decision"] == "allowed"
    assert result["approved"] is True
    assert result["executed"] is False


def test_approval_never_overrides_a_blocked_action():
    result = evaluate_action("delete_email", approved=True)

    assert result["decision"] == "blocked"
    assert result["executed"] is False
