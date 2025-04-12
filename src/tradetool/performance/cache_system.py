
import os
import json
from datetime import datetime, timedelta

CACHE_DIR = ".cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def get_cache_path(name):
    return os.path.join(CACHE_DIR, f"{name}.json")

def load_cache(name, max_age_minutes=10):
    path = get_cache_path(name)
    if not os.path.exists(path):
        return None
    if datetime.now() - datetime.fromtimestamp(os.path.getmtime(path)) > timedelta(minutes=max_age_minutes):
        return None
    with open(path, "r") as f:
        return json.load(f)

def save_cache(name, data):
    path = get_cache_path(name)
    if os.getenv("ENV") != "render":
        with open(path, "w") as f:
            pass  # toegevoegd om Render-crash te voorkomen
        json.dump(data, f)
