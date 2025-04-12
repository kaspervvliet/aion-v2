import unittest
from telegram_notifier import TelegramNotifier

class TestTelegramNotifier(unittest.TestCase):
    def test_init(self):
        bot = TelegramNotifier(bot_token="dummy", chat_id="123")
        self.assertIsInstance(bot, TelegramNotifier)