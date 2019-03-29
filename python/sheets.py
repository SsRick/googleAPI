from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

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
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'cred.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    # Creating
    # spreadsheet = {
    #     'properties': {
    #     'title': "checkFile"
    #     }
    # }
    # spreadsheet = service.spreadsheets().create(body=spreadsheet,
    #                                 fields='spreadsheetId').execute()
    # print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))
    # newSheetID = format(spreadsheet.get('spreadsheetId'))
    
    # newSheetID = '1nMNgmb8rTmV8di54svKZGVgtzVOjZxtjfRaVMiSg4KU'
    newSheetID = '13d372cdvDdlft5GqOhtThB_fRGKlaAojrHBvXAJ0-WU'
    # Writing
    range_name = 'Sheet1!A2:B2'
    values = [
        [
        "8", "happen"
        ],
        # APIdditional rows ...
    ]
    body = {
        'values': values
    }
    # result = service.spreadsheets().values().update(
    #     spreadsheetId=newSheetID, range=range_name,
    #     valueInputOption='USER_ENTERED', body=body).execute()
    # print('{0} cells updated.'.format(result.get('updatedCells')))

    result = service.spreadsheets().values().append(
        spreadsheetId=newSheetID, valueInputOption='USER_ENTERED', body=body, range='Sheet1!A1:E12').execute()
    print('{0} cells updated.'.format(result.get('updates').get('updatedCells')))

    # Reading
    # sheet = service.spreadsheets()
    # result = sheet.values().get(spreadsheetId=newSheetID,
    #                             range=SAMPLE_RANGE_NAME).execute()
    # values = result.get('values', [])

    # if not values:
    #     print('No data found.')
    # else:
    #     print('Sl, Name:')
    #     for row in values:
    #         # Print columns A and E, which correspond to indices 0 and 4.
    #         print('%s, %s' % (row[0], row[1]))

    # spreadsheet = service.spreadsheets().get(spreadsheetId=newSheetID).execute()
    # print(spreadsheet)
    # Deleting the sheet
    # requests = []
    # requests.append({
    #     'deleteSheet': {'sheetId' : 1273582596}
    # })
    # body = {
    #     'requests': requests
    # }
    # response = service.spreadsheets().batchUpdate(
    #     spreadsheetId=newSheetID,
    #     body=body).execute()
if __name__ == '__main__':
    main()