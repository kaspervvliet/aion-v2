
import random

class ExecutionAwareSimulator:
    def __init__(self, slippage_range=0.01, latency_range=0.1):
        self.slippage_range = slippage_range
        self.latency_range = latency_range

    def simulate_slippage(self, price):
        """
        Simuleer slippage door een percentage verandering op de prijs toe te passen
        gebaseerd op een willekeurige waarde binnen het opgegeven bereik.
        """
        slippage = random.uniform(-self.slippage_range, self.slippage_range)
        return price * (1 + slippage)

    def simulate_latency(self, price):
        """
        Simuleer latentie-effecten door een willekeurige vertraging toe te voegen aan de prijs.
        """
        latency = random.uniform(-self.latency_range, self.latency_range)
        return price * (1 + latency)

    def simulate_execution(self, entry_price, stop_loss, take_profit):
        """
        Simuleer de uitvoering van een trade, rekening houdend met slippage en latentie
        bij de entry, stop loss en take profit prijzen.
        """
        simulated_entry = self.simulate_slippage(entry_price)
        simulated_sl = self.simulate_slippage(stop_loss)
        simulated_tp = self.simulate_slippage(take_profit)

        # Bereken of de slippage en latentie impact hebben op de uitkomst van de trade
        if simulated_entry <= simulated_sl:
            return "loss", simulated_entry, simulated_sl
        elif simulated_entry >= simulated_tp:
            return "win", simulated_entry, simulated_tp
        else:
            return "ongoing", simulated_entry, simulated_tp
