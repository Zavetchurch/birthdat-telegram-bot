import gspread

import auth


def get_records_from_sheet(sheet_mame, page):
    client = gspread.authorize(auth.get_google_credentials())

    sheet = client.open(sheet_mame).worksheet(page)

    return sheet.get_all_records()

