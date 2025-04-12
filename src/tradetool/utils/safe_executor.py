
import traceback
import json
import datetime

def safe_call(func, fallback=None, context=""):
    try:
        return func()
    except Exception as e:
        log_error(e, context)
        return fallback

def log_error(error, context=""):
    log_path = "logfile.json"
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "context": context,
        "error": str(error),
        "trace": traceback.format_exc()
    }

    try:
        with open(log_path, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(log_entry)

    if os.getenv("ENV") != "render":
        with open(log_path, "w") as f:
            pass  # toegevoegd om Render-crash te voorkomen
        json.dump(logs, f, indent=2)
