# This just deletes a sheet within the spreadsheet. 
# To delete an entire spreadsheet, use the Drive API
import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def lambda_handler(event, context):
    creds = Credentials(token=event['access_token'])
    
    service = build('sheets', 'v4', credentials=creds,cache_discovery=False)
    sheetID = event['sheetId']
    
    request = []
    
    request.append({
        "deleteSheet" : {
            "sheetId": event['sheetId']
        }
    })
    
    body = {
        "requests":request
    }
    
    sheet = service.spreadsheets()
    result = sheet.batchUpdate(spreadsheetId=event['spreadsheetId'], body = body).execute()

    # print(result)
    return {
        'statusCode': 200,
        'body': result
    }
