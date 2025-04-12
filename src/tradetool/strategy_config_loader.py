
import json
from confluence_engine import SweepDetector, FVGDetector, RSIDetector
from strategy_modular import ModularConfluenceStrategy

def load_config(config_path, data):
    with open(config_path, 'r') as f:
        config = json.load(f)

    # Map confluence strings naar klassen
    confluence_map = {
        "SweepDetector": SweepDetector,
        "FVGDetector": FVGDetector,
        "RSIDetector": RSIDetector
    }

    # Initialiseer confluences
    confluences = []
    for item in config.get("confluences", []):
        cls = confluence_map.get(item["type"])
        if cls:
            params = item.get("params", {})
            confluences.append(cls(data, **params) if params else cls(data))

    strategy = ModularConfluenceStrategy(
        data=data,
        settings=config.get("settings", {}),
        confluences=confluences
    )

    return strategy, config
