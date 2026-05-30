import json
from pathlib import Path

STATE_FILE = Path("data/suppression_state.json")


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))


def is_suppressed(state, target_name):
    return state.get(target_name, {}).get("suppressed", False)


def record_failure(state, target_name, error):
    if target_name not in state:
        state[target_name] = {
            "failed_count": 0,
            "suppressed": False,
            "last_error": "",
            "url": ""
        }

    state[target_name]["failed_count"] += 1
    state[target_name]["last_error"] = str(error)

    return state


def should_suppress(state, target_name, retries):
    return state[target_name]["failed_count"] >= retries


def suppress_target(state, target_name):
    state[target_name]["suppressed"] = True
    return state


def reset_target(state, target_name):
    state[target_name] = {
        "failed_count": 0,
        "suppressed": False,
        "last_error": ""
    }
    return state