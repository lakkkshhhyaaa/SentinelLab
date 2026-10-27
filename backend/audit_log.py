
import json
from datetime import datetime, timezone
from pathlib import Path

# Store logs in the backend/audit_logs folder.
LOG_DIR = Path(__file__).parent / "audit_logs"
LOG_FILE = LOG_DIR / "events.jsonl"


def write_audit_event(
    event_type: str,
    details: dict,
) -> dict:
    """Append one timestamped event to the local audit log."""

    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "details": details,
    }

    LOG_DIR.mkdir(parents=True, exist_ok=True)

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(event, ensure_ascii=False) + "\n")

    return event


def read_audit_events(limit: int = 100) -> list[dict]:
    """Read the most recent audit events from the local log."""

    if not LOG_FILE.exists():
        return []

    events = []

    with LOG_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                # Skip malformed lines rather than crashing.
                continue

    # Return only the most recent events.
    return events[-max(1, min(limit, 500)):]
