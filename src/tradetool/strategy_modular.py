
from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    def __init__(self, data, settings=None, confluences=None):
        self.data = data
        self.settings = settings or {}
        self.confluences = confluences or []

    @abstractmethod
    def find_entries(self):
        pass

    @abstractmethod
    def calculate_performance(self, trades):
        pass


class ModularConfluenceStrategy(BaseStrategy):
    def find_entries(self):
        entries = []
        for i in range(len(self.data)):
            if all(c.check(i) for c in self.confluences):
                entries.append({
                    "index": i,
                    "price": self.data[i]["close"],
                    "type": "long",
                    "result": "win" if i % 2 == 0 else "loss",  # simulatie
                    "rr": 2.0 if i % 2 == 0 else -1.0
                })
        return entries

    def calculate_performance(self, trades):
        total = len(trades)
        wins = sum(1 for t in trades if t["result"] == "win")
        losses = sum(1 for t in trades if t["result"] == "loss")
        rr_list = [t.get("rr", 0) for t in trades]

        hitrate = wins / total if total else 0
        avg_rr = sum(rr_list) / total if total else 0
        profit_factor = sum(t["rr"] for t in trades if t["rr"] > 0) / abs(
            sum(t["rr"] for t in trades if t["rr"] < 0) or 1
        )
        expectancy = (hitrate * avg_rr) + ((1 - hitrate) * -1)
        max_consec_wins = max_consec_losses = streak = 0
        last_result = None

        for t in trades:
            if t["result"] == last_result:
                streak += 1
            else:
                streak = 1
            if t["result"] == "win":
                max_consec_wins = max(max_consec_wins, streak)
            elif t["result"] == "loss":
                max_consec_losses = max(max_consec_losses, streak)
            last_result = t["result"]

        return {
            "total_trades": total,
            "wins": wins,
            "losses": losses,
            "hitrate": round(hitrate, 2),
            "avg_rr": round(avg_rr, 2),
            "expectancy": round(expectancy, 2),
            "profit_factor": round(profit_factor, 2),
            "max_consec_wins": max_consec_wins,
            "max_consec_losses": max_consec_losses
        }
