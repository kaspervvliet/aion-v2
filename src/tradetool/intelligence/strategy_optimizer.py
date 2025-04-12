
import json
import os

JOURNAL_PATH = "trade_journal.json"
SETTINGS_PATH = "auto_optimized_settings.json"

def optimize_strategy_thresholds(min_trades=10):
    if not os.path.exists(JOURNAL_PATH):
        return {"confidence_threshold": 0.5, "rr_threshold": 1.5}

    with open(JOURNAL_PATH, "r") as f:
        journal = json.load(f)

    if len(journal) < min_trades:
        return {"confidence_threshold": 0.5, "rr_threshold": 1.5}

    rr_values = [e["rr"] for e in journal]
    conf_values = [e["confidence"] for e in journal]

    avg_rr = sum(rr_values) / len(rr_values)
    avg_conf = sum(conf_values) / len(conf_values)

    # Optimalisatie: iets onder gemiddelde gaan zitten om meer signalen te vangen
    new_conf = round(max(0.3, avg_conf - 0.05), 2)
    new_rr = round(max(1.0, avg_rr - 0.2), 2)

    settings = {
        "confidence_threshold": new_conf,
        "rr_threshold": new_rr
    }

    if os.getenv("ENV") != "render":
        with open(SETTINGS_PATH, "w") as f:
            pass  # toegevoegd om Render-crash te voorkomen
        json.dump(settings, f, indent=2)

    return settings
