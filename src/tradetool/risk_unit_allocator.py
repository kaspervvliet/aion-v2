
class RiskUnitAllocator:
    def __init__(self, balance, risk_percent):
        self.balance = balance
        self.risk_percent = risk_percent

    def calculate_risk_amount(self):
        """
        Berekent het risico bedrag per trade op basis van de accountbalance en het ingestelde risico percentage.
        """
        risk_amount = self.balance * (self.risk_percent / 100)
        return risk_amount

    def calculate_position_size(self, entry_price, stop_loss_price):
        """
        Berekent de positie-grootte gebaseerd op het risico per trade en de afstand tussen entry en stop loss.
        """
        risk_amount = self.calculate_risk_amount()
        stop_distance = abs(entry_price - stop_loss_price)
        position_size = risk_amount / stop_distance
        return position_size
