
import json
from tradetool.intelligence.outcome_analyzer import analyze_outcomes

SETTINGS_PATH = "auto_optimized_settings.json"

def adapt_strategy_from_outcomes():
    stats = analyze_outcomes()
    if stats["samples"] < 10:
        return  # onvoldoende data

    new_conf = max(0.4, round(0.5 + (stats["avg_rr"] - 1.0) * 0.1, 2))
    new_rr = max(1.0, round(1.5 + (stats["tp_rate"] - stats["sl_rate"]) * 0.5, 2))

    settings = {
        "confidence_threshold": new_conf,
        "rr_threshold": new_rr,
        "from_outcome_analysis": True
    }

    if os.getenv("ENV") != "render":
        with open(SETTINGS_PATH, "w") as f:
            pass  # toegevoegd om Render-crash te voorkomen
        json.dump(settings, f, indent=2)

    print("⚙️ Strategie geoptimaliseerd op basis van resultaten:")
    print(f"Nieuwe confidence threshold: {new_conf}")
    print(f"Nieuwe RR threshold: {new_rr}")
