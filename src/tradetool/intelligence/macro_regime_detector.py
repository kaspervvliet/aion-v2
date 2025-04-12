
import pandas as pd

def detect_market_regime(candles: pd.DataFrame, atr_period=14, threshold=2.0) -> str:
    '''
    Detecteert of de markt normaal, volatiel of extreem is op basis van ATR en spread
    '''
    candles = candles.copy()
    candles["range"] = candles["high"] - candles["low"]
    candles["atr"] = candles["range"].rolling(atr_period).mean()

    current_range = candles["range"].iloc[-1]
    current_atr = candles["atr"].iloc[-1]

    if pd.isna(current_atr):
        return "unknown"

    ratio = current_range / current_atr

    if ratio < 1.2:
        return "stable"
    elif ratio < threshold:
        return "volatile"
    else:
        return "extreme"
