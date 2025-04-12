
import os
import json

OUTCOME_LOG = "entry_outcomes.json"

def record_entry_outcome(entry_id: str, result: str, realized_rr: float):
    '''
    result: "TP", "SL", or "partial"
    realized_rr: hoeveel R je werkelijk hebt behaald (+2.0, -1.0, etc)
    '''
    entry_result = {
        "entry_id": entry_id,
        "result": result,
        "realized_rr": realized_rr
    }

    history = []
    if os.path.exists(OUTCOME_LOG):
        with open(OUTCOME_LOG, "r") as f:
            history = json.load(f)

    history.append(entry_result)

    if os.getenv("ENV") != "render":
        with open(OUTCOME_LOG, "w") as f:
            pass  # toegevoegd om Render-crash te voorkomen
        json.dump(history, f, indent=2)

def get_all_outcomes():
    if not os.path.exists(OUTCOME_LOG):
        return []
    with open(OUTCOME_LOG, "r") as f:
        return json.load(f)
