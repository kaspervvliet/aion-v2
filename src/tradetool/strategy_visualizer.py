
import os
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

class StrategyVisualizer:
    def __init__(self, output_dir="charts"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def plot_equity_curve(self, trades, strategy_name="Strategy"):
        equity = []
        balance = 100
        for t in trades:
            rr = t.get("rr", 0)
            balance *= (1 + rr / 100)
            equity.append(balance)

        plt.figure(figsize=(10, 4))
        plt.plot(equity, label="Equity Curve")
        plt.title(f"Equity Curve - {strategy_name}")
        plt.xlabel("Trade #")
        plt.ylabel("Equity")
        plt.grid(True)
        plt.legend()
        filename = self._save_chart(f"{strategy_name}_equity")
        plt.close()
        return filename

    def plot_rr_distribution(self, trades, strategy_name="Strategy"):
        rr_values = [t.get("rr", 0) for t in trades]
        plt.figure(figsize=(6, 4))
        plt.hist(rr_values, bins=20, edgecolor='black')
        plt.title(f"RR Distribution - {strategy_name}")
        plt.xlabel("RR")
        plt.ylabel("Frequency")
        plt.grid(True)
        filename = self._save_chart(f"{strategy_name}_rr_dist")
        plt.close()
        return filename

    def _save_chart(self, name):
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        filename = f"{name}_{timestamp}.png"
        path = os.path.join(self.output_dir, filename)
        plt.savefig(path)
        return path
