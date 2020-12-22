import json

from oauth2client.service_account import ServiceAccountCredentials

import s3


def get_telegram_token():
    telegram_credentials = json.loads(s3.get_object('telegram-creds.json'))
    return telegram_credentials['credentials']
    
    
def get_google_credentials() -> ServiceAccountCredentials:
    google_creds_json = json.loads(s3.get_object('zavetchurch-google-creds.json'))

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(google_creds_json, scope)
    return credentials
