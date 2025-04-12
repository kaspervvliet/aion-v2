
import os
from dotenv import load_dotenv

def safe_load_env(required_keys=None):
    load_dotenv()
    errors = []
    config = {}

    if required_keys:
        for key in required_keys:
            value = os.getenv(key)
            if not value:
                errors.append(f"⚠️ Missende env key: {key}")
            config[key] = value

    return config, errors
