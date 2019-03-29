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
    SAMPLE_RANGE_NAME = event['range']
    newSheetID = event['sheetId']
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
    return {
        'statusCode': 200,
        'body': json.dumps('Success!')
    }
