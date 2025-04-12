
from tradetool.strategy_registry import register_strategy

@register_strategy("Sweep + FVG")
def sweep_fvg_strategy(config, data):
    # Simuleer een analyse-output
    return {
        "entries": [{"asset": "SOL/USD", "confidence": 0.9, "rr": 1.8}],
        "bias": "Bullish",
        "winrate": 72.3
    }
