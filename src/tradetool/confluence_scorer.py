
from collections import defaultdict

class ConfluenceScorer:
    def __init__(self):
        self.stats = defaultdict(lambda: {"used": 0, "wins": 0, "losses": 0})

    def update(self, entries):
        for e in entries:
            confluences = e.get("confluences", [])
            result = e.get("result")
            for c in confluences:
                self.stats[c]["used"] += 1
                if result == "win":
                    self.stats[c]["wins"] += 1
                elif result == "loss":
                    self.stats[c]["losses"] += 1

    def summary(self):
        output = {}
        for c, stats in self.stats.items():
            used = stats["used"]
            winrate = stats["wins"] / used if used > 0 else 0
            output[c] = {
                "used": used,
                "wins": stats["wins"],
                "losses": stats["losses"],
                "winrate": round(winrate, 2)
            }
        return output
