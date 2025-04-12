
import os
import json

class LiveConfigSelector:
    def __init__(self, config_dir="configs", default_config="strategy_config.json"):
        self.config_dir = config_dir
        self.default_config = default_config
        self.cache = {}

    def get_config_for(self, symbol):
        if symbol in self.cache:
            return self.cache[symbol]

        clean = symbol.replace("/", "_").replace("-", "_")
        config_file = os.path.join(self.config_dir, f"{clean}.json")
        if os.path.exists(config_file):
            self.cache[symbol] = config_file
        else:
            self.cache[symbol] = self.default_config

        return self.cache[symbol]

    def preview_all(self):
        return {symbol: path for symbol, path in self.cache.items()}
