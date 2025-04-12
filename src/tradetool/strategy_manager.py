
import logging
from datetime import datetime
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s [%(name)s] %(message)s')
logger = logging.getLogger(__name__)


from strategy_class_based import SweepFVGStrategyV1

class StrategyManager:
    def __init__(self, data, strategy_name="SweepFVGStrategyV1", settings=None):
        self.data = data
        self.strategy_name = strategy_name
        self.settings = settings or {}
        self.strategy = self._load_strategy()

    def _load_strategy(self):
        if self.strategy_name == "SweepFVGStrategyV1":
            return SweepFVGStrategyV1(self.data, self.settings)
        else:
            raise ValueError(f"Strategie {self.strategy_name} niet gevonden.")

    def run(self):
        logger.info(f'Strategie {self.strategy_name} gestart')
        entries = self.strategy.find_entries()
        performance = self.strategy.calculate_performance(entries)
        return entries, performance
