
import numpy as np

class MacroRegimeDetector:
    def __init__(self, price_data, window=30):
        self.price_data = price_data
        self.window = window

    def detect_trend(self):
        """
        Detecteert een trend op basis van de prijsbeweging.
        Als de prijs constant stijgt of daalt, markeer het als een trend.
        """
        recent_prices = self.price_data['close'][-self.window:]
        trend = np.polyfit(range(len(recent_prices)), recent_prices, 1)[0]
        return "uptrend" if trend > 0 else "downtrend" if trend < 0 else "sideways"

    def detect_range(self):
        """
        Detecteert of de markt zich in een zijwaartse beweging bevindt.
        """
        recent_prices = self.price_data['close'][-self.window:]
        range_threshold = np.std(recent_prices)  # Standaarddeviatie als indicatie voor range
        return "range" if range_threshold < np.mean(recent_prices) * 0.02 else "trend"

    def detect_market_regime(self):
        """
        Bepaalt het huidige marktregime: trending, range of parabool.
        """
        trend = self.detect_trend()
        range_status = self.detect_range()

        if trend == "uptrend" or trend == "downtrend":
            return "trending"
        elif range_status == "range":
            return "range"
        else:
            return "parabola"  # Voorbeeld, kan uitgebreider worden met andere market phases
