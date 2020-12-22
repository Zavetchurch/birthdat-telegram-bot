import json
from datetime import datetime
from typing import List, Dict

import logging

import spreadsheet
import s3
from pusher import PusherBot

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

BIRTHDAY_KEY = 'Дата рождения'
NAME_KEY = 'ФИО'


def get_telegram_chats() -> dict:
    config_object = s3.get_object('telegram-chats.json')
    return json.loads(config_object)


def is_birthday(record: Dict) -> bool:
    try:
        birthday_date = datetime.strptime(record[BIRTHDAY_KEY], '%Y-%m-%d')
        return birthday_date.day == datetime.today().day and birthday_date.month == datetime.today().month
    except Exception as e:
        logger.error(f"Error found when trying to check {record[NAME_KEY]}'s birthday: {e}")
        return False


def lambda_handler(request, context):
    pusher: PusherBot = PusherBot()
    chats = get_telegram_chats()

    for chat in filter(lambda chat1: chat1['enabled'] is True, chats['chats']):
        records: List = spreadsheet.get_records_from_sheet(chat['sheetname'], chat['page'])
        birthdays = filter(is_birthday, records)
        for birthday in birthdays:
            pusher.push_notification(chat['celebratePattern'].format(birthday[NAME_KEY]), chat['id'])
