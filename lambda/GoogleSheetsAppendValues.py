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
    sheetID = event['sheetId']
    range_name = event['range_name']
    values = [
        [event['key'], event['value']],
        ]
    body = {
        'values': values
        }
        
    result = service.spreadsheets().values().append(
        spreadsheetId=sheetID, valueInputOption='USER_ENTERED', body=body, range=range_name).execute()
    return {
        'statusCode': 200,
        'body': json.dumps('{0} cells updated.'.format(result.get('updates').get('updatedCells')))
    }
