import gspread

import auth


def get_records_from_sheet(sheet_name: str, page: str) -> list:
    client = gspread.authorize(auth.get_google_credentials())

    sheet = client.open(sheet_name).worksheet(page)

    return sheet.get_all_records()
