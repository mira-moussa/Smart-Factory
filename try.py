import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from googleapiclient.discovery import build
import time
import concurrent.futures
import threading

threadsQueue = []
goal=['Sheet1!A1','Sheet1!B1','Sheet1!C1','Sheet1!D1','Sheet1!E1','Sheet1!F1','Sheet1!G1','Sheet1!H1','Sheet1!I1','Sheet1!J1','Sheet1!K1']


CLIENT_SECRET_FILE = 'SmartFactoryProject-23eb59396697.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
id = '1aMyAFN41-G8ms4tvaeyJhYXroLRzSWgOe64JPN95N1A'

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


service = Start(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, *SCOPES)
dat = {
    'values': [['n']]*20

}
def update(cell):

    sheets_file1 = service.spreadsheets().values().update(spreadsheetId='1aMyAFN41-G8ms4tvaeyJhYXroLRzSWgOe64JPN95N1A',
                                                          body=dat, range=cell,
                                                      valueInputOption='USER_ENTERED').execute()

start= time.perf_counter()
'''
if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:

         results = executor.map(update, goal)
'''
up = threading.Thread(target=update,args= [goal[0]])
da = threading.Thread(target=update,args= [goal[1]])
#te = threading.Thread(target=update,args= [goal[2]])


threadsQueue.extend([up, da])

# Start the threads.
for th in threadsQueue:
    th.start()

# Wait the threads to complete their tasks.
for th in threadsQueue:
    th.join()
end= time.perf_counter()
print(end-start)