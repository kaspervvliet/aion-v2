import unittest
from live_config_selector import LiveConfigSelector

class TestLiveConfigSelector(unittest.TestCase):
    def test_fallback(self):
        selector = LiveConfigSelector(config_dir="configs", default_config="strategy_config.json")
        config = selector.get_config_for("UNKNOWN/USD")
        self.assertTrue(config.endswith("strategy_config.json"))