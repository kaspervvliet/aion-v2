from tradetool.utils.safe_executor import safe_call

import os
import requests

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(entry):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram credentials not set.")
        return

    message = (
    print("Telegram alert verzonden")
"
        f"Asset: {entry.asset}
"
        f"Richting: {entry.direction}
"
        f"Confidence: {entry.confidence:.2f}
"
        f"RR: {entry.rr:.2f}
"
        f"Reden: {entry.reason}
"
        f"⏰ Tijd: {entry.timestamp}"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Telegram alert failed: {e}")
