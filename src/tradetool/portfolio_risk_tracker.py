
class PortfolioRiskTracker:
    def __init__(self):
        self.active_trades = []

    def add_trade(self, symbol, position_size, entry_price, stop_loss, take_profit):
        trade = {
            "symbol": symbol,
            "position_size": position_size,
            "entry_price": entry_price,
            "stop_loss": stop_loss,
            "take_profit": take_profit
        }
        self.active_trades.append(trade)

    def remove_trade(self, symbol):
        self.active_trades = [trade for trade in self.active_trades if trade["symbol"] != symbol]

    def calculate_total_exposure(self):
        total_exposure = sum([trade['position_size'] for trade in self.active_trades])
        return total_exposure

    def display_active_trades(self):
        return self.active_trades

    def display_risk_summary(self):
        total_exposure = self.calculate_total_exposure()
        summary = f"Total Exposure: {total_exposure} units across {len(self.active_trades)} trades."
        return summary
