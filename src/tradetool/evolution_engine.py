from rolling_memory import RollingMemory

class EvolutionEngine:
    def __init__(self, config):
        self.config = config
        self.memory = RollingMemory()

    def evolve(self, performance):
        updated = self.config.copy()

        # Basislogica voor aanpassing
        if performance["profit_factor"] < 1.0:
            ct = updated["settings"].get("confidence_threshold", 0.7)
            updated["settings"]["confidence_threshold"] = min(0.95, round(ct + 0.05, 2))

        if performance["hitrate"] < 0.5:
            rr = updated["settings"].get("rr_target", 2.0)
            updated["settings"]["rr_target"] = min(3.0, round(rr + 0.2, 2))

        if performance["profit_factor"] > 2.0 and performance["hitrate"] > 0.7:
            ct = updated["settings"].get("confidence_threshold", 0.7)
            updated["settings"]["confidence_threshold"] = max(0.4, round(ct - 0.1, 2))

        # Bonus: check confluence-trends vanuit geheugen
        for conf in updated.get("confluences", []):
            name = conf["type"].replace("Detector", "")
            trend = self.memory.get_trend_for_confluence(name)
            if trend and trend["avg_winrate"] < 0.4 and trend["used_total"] > 5:
                print(f"⚠️ Confluence '{name}' presteert slecht (avg winrate: {trend['avg_winrate']})")
                conf["disabled"] = True  # vlag om te negeren

        return updated