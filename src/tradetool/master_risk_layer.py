
class MasterRiskLayer:
    def __init__(self, balance, confidence_score, max_exposure=0.1):
        self.balance = balance
        self.confidence_score = confidence_score
        self.max_exposure = max_exposure

    def calculate_adaptive_exposure(self):
        """
        Berekent de dynamische exposure op basis van de huidige confidence score en de balans.
        """
        exposure_factor = self.confidence_score / 100
        adaptive_exposure = min(self.balance * exposure_factor, self.balance * self.max_exposure)
        return adaptive_exposure

    def apply_risk_adjustment(self, position_size):
        """
        Pas de position size aan op basis van de berekende exposure.
        """
        exposure = self.calculate_adaptive_exposure()
        adjusted_position_size = min(position_size, exposure)
        return adjusted_position_size

    def display_risk_summary(self):
        """
        Toont de samenvatting van het risiconiveau en de aanbevolen exposure.
        """
        adaptive_exposure = self.calculate_adaptive_exposure()
        return f"Max Exposure: {self.max_exposure * 100}% | Adaptive Exposure: {adaptive_exposure:.2f}"
