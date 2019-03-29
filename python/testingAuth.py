from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


# The ID and range of a sample spreadsheet.
SAMPLE_RANGE_NAME = 'Sheet1!A1:B4'
newSheetID = '13d372cdvDdlft5GqOhtThB_fRGKlaAojrHBvXAJ0-WU' 
def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    creds = Credentials(token="ya29.GlvbBjyCzz2zZFZkPAbzoCZOUO4vKwZFv9pGWyiTkF2vny-faoCo9EH97eCK_AdKUgJF6sOjcGYBgmHoHzGu3IJ8x3H-bBrp-aiDRoCQVfzAJcKQCQ0LgmxxPRXZ",
                        scopes="https://www.googleapis.com/auth/spreadsheets")
    service = build('sheets', 'v4', credentials=creds)
      

    # Reading
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=newSheetID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Sl, Name:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))
if __name__ == '__main__':
    main()