import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def lambda_handler(event, context):
    creds = Credentials(token=event['access_token'],
                        refresh_token=event['refresh_token'],
                        client_id=event['client_id'],
                        token_uri=event['token_uri'],
                        client_secret=event['client_secret'],
                        scopes=event['scope'])
    service = build('sheets', 'v4', credentials=creds,cache_discovery=False)
    spreadsheet = {
        'properties': {
        'title': event['spreadsheetName']
        }
    }
    spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                    fields='spreadsheetId').execute()
    # print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))
    return {
        'statusCode': 200,
        'body': spreadsheet.get('spreadsheetId')
    }
