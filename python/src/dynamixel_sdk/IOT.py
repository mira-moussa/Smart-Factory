import os
import pickle
from http import client

from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2 import service_account


def Start(client_secret_file, api_name, api_version, *scopes):
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

def read(service,id,range):
    request = service.spreadsheets().values().get(spreadsheetId=id,range=range_name)
    response = request.execute()
    return response['values']

def append(service,id,range,value):
    sheets_file1 = service.spreadsheets().values().append(spreadsheetId= id,
                                                          body=value, range=range,
                                                          valueInputOption='USER_ENTERED').execute()

def update(service,id,range,value):
    sheets_file1 = service.spreadsheets().values().update(spreadsheetId= id,
                                                          body=value, range=range,
                                                         valueInputOption='USER_ENTERED').execute()


CLIENT_SECRET_FILE = 'SmartFactoryProject-23eb59396697.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
id = '1aMyAFN41-G8ms4tvaeyJhYXroLRzSWgOe64JPN95N1A'

Goal_pos = 'Sheet1!A'
Current_Pos = 'Sheet1!B'
Input_Voltage_Error = 'Sheet1!C'
Angle_Limit_Error = 'Sheet1!D'
Overheating_Error = 'Sheet1!E'
Range_Error = 'Sheet1!F'
Checksum_Error = 'Sheet1!G'
Overload_Error = 'Sheet1!H'
Instruction_Error = 'Sheet1!I'

service = Start(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, *SCOPES)
i=1
while 1:
    Goal_pos = Goal_pos + str(i)
    print(Goal_pos)
    ReadArray = read(service, id, Goal_pos)
    print(ReadArray)
    Goal_pos = 'Sheet1!A'
    i+=1



