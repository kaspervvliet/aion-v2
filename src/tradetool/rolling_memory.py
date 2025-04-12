import json
import os
from datetime import datetime

class RollingMemory:
    def __init__(self, path=None):
        base_dir = os.path.dirname(__file__)
        self.path = path or os.path.join(base_dir, "..", "data", "memory_log.json")
        self.memory = []
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                self.memory = json.load(f)

    def log_session(self, performance, confluence_summary, bias=None):
        self.memory.append({
            "timestamp": datetime.utcnow().isoformat(),
            "performance": performance,
            "confluence_summary": confluence_summary,
            "bias": bias
        })
        with open(self.path, 'w') as f:
            json.dump(self.memory, f, indent=2)

    def get_last_n_sessions(self, n=5):
        return self.memory[-n:]

    def get_trend_for_confluence(self, name):
        history = [entry["confluence_summary"].get(name) for entry in self.memory if name in entry["confluence_summary"]]
        if not history:
            return None
        winrates = [h["winrate"] for h in history]
        return {
            "avg_winrate": round(sum(winrates) / len(winrates), 2),
            "used_total": sum(h["used"] for h in history),
            "last_winrate": winrates[-1]
        }

    def get_bias_performance(self):
        bias_perf = {}
        for entry in self.memory:
            bias = entry.get("bias", "unknown")
            if bias not in bias_perf:
                bias_perf[bias] = {"count": 0, "hitrate_total": 0.0}
            bias_perf[bias]["count"] += 1
            bias_perf[bias]["hitrate_total"] += entry["performance"].get("hitrate", 0)

        result = {}
        for bias, stats in bias_perf.items():
            result[bias] = {
                "runs": stats["count"],
                "avg_hitrate": round(stats["hitrate_total"] / stats["count"], 2)
            }
        return result