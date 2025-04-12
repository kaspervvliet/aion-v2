
import json
import os
from collections import defaultdict

OUTCOME_LOG = "entry_outcomes.json"

def analyze_outcomes():
    if not os.path.exists(OUTCOME_LOG):
        return {"avg_rr": 0.0, "tp_rate": 0.0, "sl_rate": 0.0, "samples": 0}

    with open(OUTCOME_LOG, "r") as f:
        entries = json.load(f)

    tp = [e for e in entries if e["result"] == "TP"]
    sl = [e for e in entries if e["result"] == "SL"]
    all_rr = [e["realized_rr"] for e in entries]

    if not entries:
        return {"avg_rr": 0.0, "tp_rate": 0.0, "sl_rate": 0.0, "samples": 0}

    return {
        "avg_rr": sum(all_rr) / len(all_rr),
        "tp_rate": len(tp) / len(entries),
        "sl_rate": len(sl) / len(entries),
        "samples": len(entries)
    }
