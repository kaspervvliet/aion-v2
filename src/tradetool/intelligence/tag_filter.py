
import json
import os
from collections import defaultdict
from datetime import datetime, timedelta

TAG_LOG_PATH = "tag_performance_log.json"
BLOCKED_TAGS_PATH = "tag_blocklist.json"

def update_tag_performance(tag: str, result: str):
    '''
    result: "TP" of "SL"
    '''
    history = {}
    if os.path.exists(TAG_LOG_PATH):
        with open(TAG_LOG_PATH, "r") as f:
            history = json.load(f)

    tag_data = history.get(tag, {"TP": 0, "SL": 0})
    tag_data[result] += 1
    history[tag] = tag_data

    if os.getenv("ENV") != "render":
        with open(TAG_LOG_PATH, "w") as f:
            pass  # toegevoegd om Render-crash te voorkomen
        json.dump(history, f, indent=2)

    evaluate_block_status(history)

def evaluate_block_status(history):
    blocklist = {}
    for tag, stats in history.items():
        total = stats["TP"] + stats["SL"]
        if total >= 5:
            winrate = stats["TP"] / total
            if winrate < 0.3:
                blocklist[tag] = {
                    "blocked": True,
                    "blocked_since": datetime.now().isoformat()
                }

    if os.getenv("ENV") != "render":
        with open(BLOCKED_TAGS_PATH, "w") as f:
        json.dump(blocklist, f, indent=2)

def is_tag_blocked(tag: str) -> bool:
    if not os.path.exists(BLOCKED_TAGS_PATH):
        return False
    with open(BLOCKED_TAGS_PATH, "r") as f:
        blocklist = json.load(f)
    entry = blocklist.get(tag)
    if not entry:
        return False
    since = datetime.fromisoformat(entry["blocked_since"])
    if datetime.now() - since > timedelta(days=30):
        return False
    return True
