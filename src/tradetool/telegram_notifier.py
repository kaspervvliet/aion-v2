
import requests
import os

class TelegramNotifier:
    def __init__(self, bot_token=None, chat_id=None):
        self.bot_token = bot_token or os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = chat_id or os.getenv("TELEGRAM_CHAT_ID")

    def send(self, message):
        if not self.bot_token or not self.chat_id:
            print("⚠️ Telegram credentials ontbreken.")
            return

        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        data = {"chat_id": self.chat_id, "text": message}
        response = requests.post(url, data=data)

        if response.status_code == 200:
            print("📨 Telegram signaal verzonden.")
        else:
            print(f"❌ Telegram fout: {response.status_code} - {response.text}")
