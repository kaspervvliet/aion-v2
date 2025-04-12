
import numpy as np
import matplotlib.pyplot as plt

class ConfidenceIntervalAnalyzer:
    def __init__(self, trades):
        self.trades = trades

    def analyze(self):
        """
        Analyseert de performance en berekent het interval van verwachte winrate en RR op basis van de trades.
        """
        winrates = [1 if trade['result'] == 'win' else 0 for trade in self.trades]
        rrs = [trade['rr'] for trade in self.trades]

        winrate_mean = np.mean(winrates)
        rr_mean = np.mean(rrs)
        winrate_std = np.std(winrates)
        rr_std = np.std(rrs)

        # Bereken confidence interval (95% confidence)
        winrate_ci = (winrate_mean - 1.96 * (winrate_std / np.sqrt(len(winrates))),
                      winrate_mean + 1.96 * (winrate_std / np.sqrt(len(winrates))))
        rr_ci = (rr_mean - 1.96 * (rr_std / np.sqrt(len(rrs))),
                 rr_mean + 1.96 * (rr_std / np.sqrt(len(rrs))))

        # Plot de verdeling van winrates en RRs
        fig, ax = plt.subplots(1, 2, figsize=(12, 6))

        # Winrate verdeling
        ax[0].hist(winrates, bins=2, color='green', alpha=0.6)
        ax[0].set_title("Winrate Distributie")
        ax[0].set_xlabel("Winrate")
        ax[0].set_ylabel("Aantal Trades")

        # RR verdeling
        ax[1].hist(rrs, bins=30, color='blue', alpha=0.6)
        ax[1].set_title("RR Distributie")
        ax[1].set_xlabel("Risk/Reward (RR)")
        ax[1].set_ylabel("Aantal Trades")

        plt.tight_layout()
        plt.show()

        return winrate_mean, rr_mean, winrate_ci, rr_ci
