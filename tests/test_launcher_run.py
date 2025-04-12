
import unittest
from tradetool.strategy_config_loader import load_config
from tradetool.auto_mode_launcher import run_auto_mode

class LauncherTest(unittest.TestCase):
    def test_launcher_runs(self):
        config = load_config("src/tradetool/strategy_config.json")
        try:
            run_auto_mode(config)
        except Exception as e:
            self.fail(f"Launcher failed with error: {e}")
