import telegram
from telegram import Bot

import auth


class PusherBot:
    telegram_bot: Bot = None

    def __init__(self):
        self.telegram_bot = self._get_bot()

    def _get_bot(self):
        if not self.telegram_bot:
            self.telegram_bot = telegram.Bot(token=auth.get_telegram_token())
            return self.telegram_bot
        else:
            return self.telegram_bot

    def push_notification(self, message, chat_id):
        bot = self._get_bot()
        return bot.send_message(text=message, chat_id=chat_id)
