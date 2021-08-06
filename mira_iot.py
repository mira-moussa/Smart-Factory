import os
import pickle
import threading
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from googleapiclient.discovery import build
import time
import numpy as np
goals='Sheet1!A1'


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


def update(cell,dat):
    service = Start(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, *SCOPES)

    sheets_file1 = service.spreadsheets().values().update(spreadsheetId='1aMyAFN41-G8ms4tvaeyJhYXroLRzSWgOe64JPN95N1A',
                                                          body=dat, range=cell,
                                                      valueInputOption='USER_ENTERED').execute()

data1=[
['name','','','','','','',''],
['','','no.','Present_pos','Speed','Voltage','Torque','Tempearture'],
['feeding mechanism_HMI','','robot1_motor1','23','2','3','4','5'],
['conveyor motor_HMI','','robot1_motor2','23','2','3','4','5'],
['pushing arm_HMI','','robot1_motor3','23','2','3','4','5'],
['','','robot1_gripper1','23','2','3','4','5'],
['feeding proximity_HMI','','robot2_motor1','23','2','3','4','5'],
['counter proximity_HMI','','robot2_motor2','23','2','3','4','5'],
['pick proximity_HMI','','robot2_motor3','23','2','3','4','5'],
['','','robot2_gripper2','23','2','3','4','5'],
['type of control_HMI','','','','','','',''],
['Emergency stop','','','','','','',''],
['','','','','','','',''],
['trash counter','','','','','','',''],
['elements counter','','','','','','',''],
['','','','','','','',''],
['box 1','','','','','','',''],
['box 2','','','','','','',''],
['box 1 full indicator','','','','','','',''],
['box 2 full indicator','','','','','','',''],
['','','','','','','',''],
['red color','','','','','','',''],
['white color','','','','','','',''],
['','','','','','','',''],
['feeding mechanism','','','','','','',''],
['feeding proximity','','','','','','',''],
['Conveyor Motor','','','','','','',''],
['Counter Proximity','','','','','','',''],
['pick proximty','','','','','','',''],
['Color_Sensor','','','','','','',''],
['pushing arm','','','','','','',''],
['Robot_arm_1','','','','','','',''],
['Robot_arm_2','','','','','','','']]






dat = {
        'values': data1
    }
start= time.perf_counter()
update(goals,dat)
update(goals,dat)
end= time.perf_counter()
print(end-start)

threads1=[]
threads2=[]
start= time.perf_counter()
for _ in range(1):
    t1= threading.Thread(target= update,args=[goals,dat])
    t2=threading.Thread(target= update,args=[goals,dat])
    threads1.append(t1)
    threads2.append(t2)
    t1.start()
    t2.start()

#t4 = threading.Thread(target= update,args=[goal[3]])
#t4.start()
for thread in threads1:
    thread.join()
for thread in threads2:
    thread.join()


#t4.join()
end= time.perf_counter()
print(end-start)