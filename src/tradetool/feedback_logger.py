
import logging
from datetime import datetime
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s [%(name)s] %(message)s')
logger = logging.getLogger(__name__)


import os
import json
from datetime import datetime

class FeedbackLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def log_entry_feedback(self, strategy_name, entries, performance):
        logger.info(f'Logging feedback voor {strategy_name}')
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "strategy": strategy_name,
            "entries": entries,  # entries bevatten nu ook gpt_explanation
            "performance": performance
        }
        filename = f"{strategy_name}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
        path = os.path.join(self.log_dir, filename)
        with open(path, 'w') as f:
            json.dump(log_data, f, indent=2)
        return path
