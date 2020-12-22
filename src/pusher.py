import telegram
import typing
import auth


class PusherBot:
    telegram_bot: telegram.Bot = None

    def __init__(self):
        self.telegram_bot = self._get_bot()

    def _get_bot(self) -> telegram.Bot:
        if not self.telegram_bot:
            self.telegram_bot = telegram.Bot(token=auth.get_telegram_token())
            return self.telegram_bot
        else:
            return self.telegram_bot

    def push_notification(self, message: str, chat_id: typing.Union[str, int]) -> telegram.Message:
        bot = self._get_bot()
        return bot.send_message(text=message, chat_id=chat_id)
