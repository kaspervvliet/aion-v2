import unittest
from rolling_memory import RollingMemory

class TestRollingMemory(unittest.TestCase):
    def test_log_session(self):
        rm = RollingMemory(path="test_memory.json")
        rm.log_session({"hitrate": 1.0}, {"Sweep": {"used": 1, "wins": 1, "losses": 0, "winrate": 1.0}})
        latest = rm.get_last_n_sessions(1)[0]
        self.assertIn("performance", latest)