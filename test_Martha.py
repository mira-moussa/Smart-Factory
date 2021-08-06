import os
import pickle
import threading
import concurrent.futures
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from googleapiclient.discovery import build
import time
"""
dat = {
        'values': [[1]]
}
goal = ['Sheet1!A1', 'Sheet1!A2', 'Sheet1!A3', 'Sheet1!A4', 'Sheet1!A5', 'Sheet1!A6']
"""
goal=[0]*20
for i in range (20):
    goal[i] = 'Sheet1!A{}'.format(i+1)
n=[1,2,3,4,5,6,7,8,9,10]

CLIENT_SECRET_FILE = 'SmartFactoryProject-23eb59396697.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
id = '1aMyAFN41-G8ms4tvaeyJhYXroLRzSWgOe64JPN95N1A'

def doo(x):
    print('hi{}'.format(x))
    time.sleep(3)
    return 'done{}'.format(x)
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
    request = service.spreadsheets().values().get(spreadsheetId=id,range=range)
    response = request.execute()
    return response['values']


def update(service,id,range,value):
    time.sleep(0.2)
    sheets_file1 = service.spreadsheets().values().update(spreadsheetId= id,
                                                          body=value, range=range,
                                                         valueInputOption='USER_ENTERED').execute()

def UPDATE(Goal):
    dat = {
        'values': [[1]]
    }
    update(service, id, Goal, dat)
    rd = read(service, id, Goal)

    while(1):
        if rd[0][0] == dat:
            break
    return rd
service = Start(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, *SCOPES)
"""
start = time.perf_counter()
update(service,id,'Sheet1!D1',dat)
update(service,id,'Sheet1!D2',dat)
reading=read(service,id,'Sheet1!D1')
print(reading)
reading=read(service,id,'Sheet1!D2')
print(reading)
end= time.perf_counter()
print(end-start)
"""

start = time.perf_counter()

"""
start= time.perf_counter()
update('Sheet1!A1')
update('Sheet1!B1')
update('Sheet1!C1')

end= time.perf_counter()
print(end-start)



threads = []
for i in range(4):
    t = threading.Thread(target= update,args=[goal[i]])
    t.start()
    threads.append(t)
for th in threads:
    th.join()
"""
"""
t1 = threading.Thread(target= update,args=['Sheet1!D1'])
t1.start()
t2 = threading.Thread(target= update,args=['Sheet1!E1'])
t2.start()
t3 = threading.Thread(target= update,args=['Sheet1!F1'])
t3.start()
t4 = threading.Thread(target= update,args=['Sheet1!G1'])
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
"""
"""
with concurrent.futures.ThreadPoolExecutor() as executor:
    goal = ['Sheet1!A1', 'Sheet1!A2', 'Sheet1!A3', 'Sheet1!A4', 'Sheet1!A5', 'Sheet1!A6']
    dat = {
        'values': [[1]]
    }
    results = [executor.map(update,service, id, g, dat )for g in goal]
    for r in results:
        print(r)
"""
#goal = ['Sheet1!A1', 'Sheet1!A2', 'Sheet1!A3', 'Sheet1!A4', 'Sheet1!A5', 'Sheet1!A6']
dat = {
    'values': [['']]*2000
}
"""
threads = []
for i in range(6):
    t = threading.Thread(target= update,args=[service, id, goal[i], dat])
    t.start()
    threads.append(t)
for th in threads:
    th.join()

t1 = threading.Thread(target= update,args=(service, id, goal[0], dat))
t1.start()
t2 = threading.Thread(target= update,args=(service, id, goal[1], dat))
t2.start()
time.sleep(1)

t3 = threading.Thread(target= update,args=(service, id, goal[2], dat))
t3.start()
t4 = threading.Thread(target= update,args=(service, id, goal[3], dat))
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()


for i in range(20):
    update(service, id, 'Sheet1!A', dat)
"""
t1=threading.Thread(target=update,args=(service, id, 'Sheet1!C1', dat))
t2=threading.Thread(target=update,args=(service, id, 'Sheet1!B1', dat))
#t3=threading.Thread(target=update,args=(service, id, 'Sheet1!C1', dat))

t1.start()
t2.start()
#t3.start()
t1.join()
t2.join()
#t3.join()

#rd = read(service, id, 'Sheet1!A1:A2000')
#print(rd)

end= time.perf_counter()
print(end-start)