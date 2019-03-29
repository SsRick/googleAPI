from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1nMNgmb8rTmV8di54svKZGVgtzVOjZxtjfRaVMiSg4KU'
SAMPLE_RANGE_NAME = 'Sheet1!A1:B4'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    creds = Credentials(token="ya29.GlvbBqzdnKtp0v1ZCxgZLtweMASSRT8_sTYi3c7py8q-YC1KpuYzydpez-Iswu41oEAblFGbAozvOGwQxvfwqCpYO3ch8xIV4P-JL6suT-vG3Z1Zc_M72N6LuJ4Z",
                        id_token="eyJhbGciOiJSUzI1NiIsImtpZCI6ImE0MzEzZTdmZDFlOWUyYTRkZWQzYjI5MmQyYTdmNGU1MTk1NzQzMDgiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI4ODc1OTc4Mjg1OTctajRjODE1aGdsamwybG1xdXNsczgxOTliYXN1Zm01YjkuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI4ODc1OTc4Mjg1OTctajRjODE1aGdsamwybG1xdXNsczgxOTliYXN1Zm01YjkuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTQzODY2MDg4OTk0OTQzNzY5MjkiLCJhdF9oYXNoIjoiYlVoWnpBNVVoVlBudThVUTNTeVNPZyIsIm5hbWUiOiJTSEFOS0hBIFNIVUJIUkEiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDYuZ29vZ2xldXNlcmNvbnRlbnQuY29tLy0xLVBUX1Atc2NqYy9BQUFBQUFBQUFBSS9BQUFBQUFBQUFBQS9BQ0hpM3Jlcjl5NjJXb1drUld5TkV1YkR2b1VxMHpLSHpRL3M5Ni1jL3Bob3RvLmpwZyIsImdpdmVuX25hbWUiOiJTSEFOS0hBIiwiZmFtaWx5X25hbWUiOiJTSFVCSFJBIiwibG9jYWxlIjoiZW4iLCJpYXQiOjE1NTM4NDIyOTksImV4cCI6MTU1Mzg0NTg5OX0.RGy5TZUmaz91y2PygRma_lR7Rw3WqQ1cEWsMxrnNe5lfnDDhkOvxY-JSq8sZK_ruwUGVjw9uymBflKGJKmiVFjGaQOuPbemRFhHAEN8nXxHqwyXq0Z6WfURy7OKLtOOBfR9nBH48nt4jufYhBwS3jyRtYQ-T_omMw5aJJrPlBcV4RJXcxuxv2P5dylReiDoWz6Za-WCfDEovuwoHSlfUeBmp3_9ze--mMo4leBJ5LdOq-CO25jQMRNtP_6UCROxMdDbwf_qV9gL0peTrJS4957eu2MrgQ8ZZ2a0F4PMlEhxLK13tIoLET_fHOsUvDQVliDmOa2Tp21yQc7h3TmDegQ",
                        scopes="https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/contacts.readonly https://www.googleapis.com/auth/contacts")
    service = build('sheets', 'v4', credentials=creds)
    
    newSheetID = '13d372cdvDdlft5GqOhtThB_fRGKlaAojrHBvXAJ0-WU'
    

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