
import os
import pickle
import threading
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from googleapiclient.discovery import build

"""
goal = [0]*10
for i in range (10):
    goal[i] = 'Sheet1!A{}'.format(i)
#data = [0]*10
"""

goal='Sheet1!A1'
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


def read(service,id,rang):
    request = service.spreadsheets().values().get(spreadsheetId=id,range=rang)
    response = request.execute()
    return response['values']


def update(service,id,range,value):
    sheets_file1 = service.spreadsheets().values().update(spreadsheetId= id,
                                                          body=value, range=range,
                                                         valueInputOption='USER_ENTERED').execute()

dat = {
        'values': [['martha']]
}


def UPDATE(goal,data):
    dat = {
        'values': [[data]]
    }

    update(service, id, goal, dat)
    rd = read(service, id, goal)

    while(1):
        if rd[0][0] == dat:
            print('hello')
            break
    return rd


CLIENT_SECRET_FILE = 'SmartFactoryProject-23eb59396697.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
id = '1aMyAFN41-G8ms4tvaeyJhYXroLRzSWgOe64JPN95N1A'

service = Start(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, *SCOPES)
update(service, id, goal,dat)
x=read(service, id, goal)
print(x)
"""
with concurrent.futures.ProcessPoolExecutor() as executor:
    results= executor.map(UPDATE,goal)
"""
"""
th=[]
for i in range (10):
    thrd= threading.Thread(target=UPDATE(goal[i],data[i]) )
    thrd.start()
    th.append(thrd)

"""

"""
start = time.perf_counter()
UPDATE1(data1)
UPDATE2(data2)
print('hi')
finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)')



start = time.perf_counter()
fth=threading.Thread(target=UPDATE1(data3),name='thread1')
sth=threading.Thread(target=UPDATE2(data4),name='thread2')

fth.start()
sth.start()
print('hi')
finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)')
"""