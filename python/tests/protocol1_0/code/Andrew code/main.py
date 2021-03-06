import pickle
import os
from google.oauth2.service_account import IDTokenCredentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2 import service_account
#

def Create_Service(client_secret_file, api_name, api_version, *scopes):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "SmartFactoryProject-23eb59396697.json"
    print(client_secret_file, api_name, api_version, scopes, sep='-')
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    print(SCOPES)

    cred = None

    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
    # print(pickle_file)

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = service_account.Credentials.from_service_account_file(
                CLIENT_SECRET_FILE, scopes=SCOPES)



        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None





CLIENT_SECRET_FILE = 'SmartFactoryProject-23eb59396697.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

range_name = 'Sheet1!A1:D2'

service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)



spreadsheetid = '1aMyAFN41-G8ms4tvaeyJhYXroLRzSWgOe64JPN95N1A'


#def Read (spreessheetid,Range)
sheet_ID = spreadsheetid 




request = service.spreadsheets().values().get(spreadsheetId=spreadsheetid, range = range_name)
response = request.execute()
request = service.spreadsheets().values()
print (response['values'])
response['values'][0][0]= 'ibrahim'





data = {
    'values' : response['values']
}
for i in range(10):
    sheets_file1 = service.spreadsheets().values().append(spreadsheetId=spreadsheetid, body=data, range = range_name ,valueInputOption='USER_ENTERED').execute()