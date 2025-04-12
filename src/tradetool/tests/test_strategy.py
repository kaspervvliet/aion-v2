
import unittest
from strategy_class_based import SweepFVGStrategyV1

class TestStrategy(unittest.TestCase):
    def test_entry_generation(self):
        dummy_data = [{'low': 99, 'high': 101, 'close': 100}] * 10
        strat = SweepFVGStrategyV1(dummy_data)
        entries = strat.find_entries()
        self.assertIsInstance(entries, list)
        self.assertTrue(all("price" in e for e in entries))

    def test_performance_metrics(self):
        dummy_trades = [{"result": "win", "rr": 2}, {"result": "loss", "rr": -1}]
        strat = SweepFVGStrategyV1([])
        perf = strat.calculate_performance(dummy_trades)
        self.assertIn("hitrate", perf)
        self.assertIn("avg_rr", perf)
