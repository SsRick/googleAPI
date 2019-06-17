import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def lambda_handler(event, context):
    creds = Credentials(token=event['access_token'])
    
    service = build('sheets', 'v4', credentials=creds,cache_discovery=False)
    SAMPLE_RANGE_NAME = event['range']
    newSheetID = event['sheetId']
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=newSheetID,
                                range=SAMPLE_RANGE_NAME).execute()

    # print(result)
    return {
        'statusCode': 200,
        'body': result
    }
