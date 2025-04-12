
import os
from tradetool.data import get_latest_data
from tradetool.strategy_config_loader import load_config
from strategy_manager import StrategyManager
from entry_scorer import EntryScorer
from tradetool.gpt_validator import GPTValidator

class MultiAssetRunner:
    def __init__(self, config_dir="configs"):
        self.config_dir = config_dir
        self.asset_configs = self._load_all_configs()

    def _load_all_configs(self):
        configs = {}
        for file in os.listdir(self.config_dir):
            if file.endswith(".json"):
                symbol = file.replace(".json", "")
                configs[symbol] = os.path.join(self.config_dir, file)
        return configs

    def run_all(self):
        results = {}
        for symbol, config_path in self.asset_configs.items():
    print("Multi-asset analyse gestart")
📊 Run voor {symbol}")
            data = get_latest_data(symbol)
            strategy, config = load_config(config_path, data)

            manager = StrategyManager(data, strategy_name=config["strategy_name"])
            entries, performance = manager.run()

            if entries:
                scorer = EntryScorer()
                scored = scorer.score_entries(entries)
                validator = GPTValidator()
                explained = validator.explain_all(scored)

                high_conf = [e for e in explained if e["confidence_score"] >= config["settings"]["confidence_threshold"]]
                results[symbol] = high_conf
            else:
                results[symbol] = []
        return results
