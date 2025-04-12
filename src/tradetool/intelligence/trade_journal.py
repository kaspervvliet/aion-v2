
import os
import json

JOURNAL_PATH = "trade_journal.json"

def log_entry(entry_result, annotation):
    entry_dict = entry_result.__dict__
    entry_dict["annotation"] = annotation

    journal = []
    if os.path.exists(JOURNAL_PATH):
        with open(JOURNAL_PATH, "r") as f:
            journal = json.load(f)

    journal.append(entry_dict)

    if os.getenv("ENV") != "render":
        with open(JOURNAL_PATH, "w") as f:
            pass  # toegevoegd om Render-crash te voorkomen
        json.dump(journal, f, indent=2)
