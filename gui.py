import pickle
import os
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




#function of raeding
def read(service,id,range):
    request = service.spreadsheets().values().get(spreadsheetId=id,
                                                  range=range)
    response = request.execute()
    return response['values']


# there is a problem in append function
# def append(service,id,range,value):
#     request2 = service.spreadsheets().values().append(spreadsheetId= id,
#                                                       range=range,
#                                                       valueInputOption='USER_ENTERED',
#                                                       body=value).execute()
#     response2 = request2.execute()
#     return response2['values']


# function of writing
def update(service,id,range,value):
       sheets_file1 = service.spreadsheets().values().update(spreadsheetId=id,
                                                         body=value, range=range,
                                                        valueInputOption='USER_ENTERED').execute()
                                                        


CLIENT_SECRET_FILE = 'SmartFactoryProject-23eb59396697.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
id = '1aMyAFN41-G8ms4tvaeyJhYXroLRzSWgOe64JPN95N1A'
#range_name = 'Sheet1!A1:D2'



service = Start(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

# ------------------------------------------------------------------Reading data from GUI sheet------------------------------------------------------------------------ 

# ------------------------------------feeding_mechanism data-------------------------------------------- 
feeding_mechanism_array = read(service,id,'GUIData!C5')   
feeding_mechanism = feeding_mechanism_array[0]              # to get item from the list
# print('feeding_mechanism= ' ,feeding_mechanism)

# ------------------------------------conveyor_motor data-------------------------------------- 
conveyor_motor_array = read(service,id,'GUIData!C6')   
conveyor_motor = conveyor_motor_array[0]              # to get item from the list
# print('conveyor_motor = ',conveyor_motor)

# ------------------------------------pushing_arm data---------------------------------------------- 
pushing_arm_array = read(service,id,'GUIData!C7')   
pushing_arm = pushing_arm_array[0]              # to get item from the list
# print('pushing_arm = ' ,pushing_arm)

# ------------------------------------feeding_proximity data---------------------------------- 
feeding_proximity_array = read(service,id,'GUIData!C9')   
feeding_proximity = feeding_proximity_array[0]              # to get item from the list
# print('feeding_proximity = ',feeding_proximity)

# ------------------------------------counter_proximity data----------------------------------
counter_proximity_array = read(service,id,'GUIData!C10')   
counter_proximity = counter_proximity_array[0]              # to get item from the list
# print('counter_proximity = ' ,counter_proximity)

# ------------------------------------pick_proximity data----------------------------------
pick_proximity_array = read(service,id,'GUIData!C11')   
pick_proximity = pick_proximity_array[0]              # to get item from the list
# print('pick_proximity = ' ,pick_proximity)

#------------------------------------ type_of_control data------------------------------------- 
type_of_control_array = read(service,id,'GUIData!C13')   
type_of_control = type_of_control_array[0]              # to get item from the list
# print('type_of_control = ',type_of_control)

# ------------------------------------emergency_stop data-------------------------------------- 
emergency_stop_array = read(service,id,'GUIData!C14')   
emergency_stop = emergency_stop_array[0]              # to get item from the list
# print('emergency_stop = ', emergency_stop)

# ------------------------------------robot1_motors data--------------------------------------- 
# robot1_motors_array = read(service,id,'GUIData!E23:E26')   
# robot1_motor1 = robot1_motors_array[0]              # get data from GUI sheet for robot1_motor1
# robot1_motor2 = robot1_motors_array[1]              # get data from GUI sheet for robot1_motor2 
# robot1_motor3 = robot1_motors_array[2]              # get data from GUI sheet for robot1_motor3 
# robot1_gripper1 = robot1_motors_array[3]            # get data from GUI sheet for robot1_gripper1 
# print('robot1_motor1 = ',robot1_motor1)
# print('robot1_motor2 = ',robot1_motor2)
# print('robot1_motor3 = ',robot1_motor3)
# print('robot1_gripper1 = ',robot1_gripper1)


# ------------------------------------robot2_motors data--------------------------------------- 
# robot2_motors_array = read(service,id,'GUIData!E27:E30')   
# robot2_motor1 = robot2_motors_array[0]              # get data from GUI sheet for robot2_motor1
# robot2_motor2 = robot2_motors_array[1]              # get data from GUI sheet for robot2_motor2 
# robot2_motor3 = robot2_motors_array[2]              # get data from GUI sheet for robot2_motor3 
# robot2_gripper2 = robot2_motors_array[3]            # get data from GUI sheet for robot2_gripper2 
# # print('robot2_motor1 = ',robot2_motor1)
# # print('robot2_motor2 = ',robot2_motor2)
# # print('robot2_motor3 = ',robot2_motor3)
# # print('robot2_gripper2 = ',robot2_gripper2)


# ------------------------------------------------------------------Writting data on GUI sheet------------------------------------------------------------------------ 


# ------------------------------------feeding_mechanism_HMI data----------------------------------
feeding_mechanism_HMI_array= [['TRUE']]
data_feeding_mechanism_HMI = {
    'values' : feeding_mechanism_HMI_array
}
update(service,id,'GUIData!F5',data_feeding_mechanism_HMI)

# ------------------------------------conveyor_motor_HMI data----------------------------------
conveyor_motor_HMI_array= [['TRUE']]
data_conveyor_motor_HMI = {
    'values' : conveyor_motor_HMI_array
}
update(service,id,'GUIData!F6',data_conveyor_motor_HMI)

# ------------------------------------pushing_arm_HMI data----------------------------------
pushing_arm_HMI_array= [['TRUE']]
data_pushing_arm_HMI = {
    'values' : pushing_arm_HMI_array
}
update(service,id,'GUIData!F7',data_pushing_arm_HMI)

# ------------------------------------feeding_proximity_HMI data----------------------------------
feeding_proximity_HMI_array= [['TRUE']]
data_feeding_proximity_HMI = {
    'values' : feeding_proximity_HMI_array
}
update(service,id,'GUIData!F9',data_feeding_proximity_HMI)

# ------------------------------------counter_proximity_HMI data----------------------------------
counter_proximity_HMI_array= [['TRUE']]
data_counter_proximity_HMI = {
    'values' : counter_proximity_HMI_array
}
update(service,id,'GUIData!F10',data_counter_proximity_HMI)

# ------------------------------------pick_proximity_HMI data----------------------------------
pick_proximity_HMI_array= [['TRUE']]
data_pick_proximity_HMI = {
    'values' : pick_proximity_HMI_array
}
update(service,id,'GUIData!F11',data_pick_proximity_HMI)

# ------------------------------------type_of_control_HMI data----------------------------------
type_of_control_HMI_array= [['FALSE']]
data_type_of_control_HMI = {
    'values' : type_of_control_HMI_array
}
update(service,id,'GUIData!F13',data_type_of_control_HMI)

# -----------------------------trash counter data--------------------------
trash_counter_array= [[2]]
data_trash_counter = {
    'values' : trash_counter_array
}
update(service,id,'GUIData!F16',data_trash_counter)

# -----------------------------elements counter data--------------------------
elements_counter_array= [[4]]
data_elements_counter = {
    'values' : elements_counter_array
}
update(service,id,'GUIData!F17',data_elements_counter)

# ------------------------------------box1_elements data----------------------------------
box1_elements_array= [[2]]
data_box1_elements = {
    'values' : box1_elements_array
}
update(service,id,'GUIData!F19',data_box1_elements)

# ------------------------------------box2_elements data----------------------------------
box2_elements_array= [[5]]
data_box2_elements = {
    'values' : box2_elements_array
}
update(service,id,'GUIData!F20',data_box2_elements)

# -----------------------------box1_indicator of full capacity data-----------------------
box1_indicator_array= [['TRUE']]
data_box1_indicator = {
    'values' : box1_indicator_array
}
update(service,id,'GUIData!F21',data_box1_indicator)

# ----------------------------box2_indicator of full capacity data-------------------------
box2_indicator_array= [['TRUE']]
data_box2_indicator = {
    'values' : box2_indicator_array
}
update(service,id,'GUIData!F22',data_box2_indicator)

# ------------------------------------color_sensor_red data----------------------------------
cs_red_array= [['TRUE']]
data_cs_red = {
    'values' : cs_red_array
}
update(service,id,'GUIData!F24',data_cs_red)

# ------------------------------------color_sensor_white data----------------------------------
cs_white_array= [['TRUE']]
data_cs_white = {
    'values' : cs_white_array
}
update(service,id,'GUIData!F25',data_cs_white)

# -----------------------------feeding_mechanism_process indicator data--------------------------
feeding_mechanism_indicator_array= [['TRUE']]
data_feeding_mechanism_indicator = {
    'values' : feeding_mechanism_indicator_array
}
update(service,id,'GUIData!F27',data_feeding_mechanism_indicator)

# -----------------------------feeding_proximity_process indicator data--------------------------
feeding_proximity_indicator_array= [['TRUE']]
data_feeding_proximity_indicator = {
    'values' : feeding_proximity_indicator_array
}
update(service,id,'GUIData!F28',data_feeding_proximity_indicator)

# -----------------------------conveyor_motor_process indicator data--------------------------
conveyor_motor_indicator_array= [['TRUE']]
data_conveyor_motor_indicator = {
    'values' : conveyor_motor_indicator_array
}
update(service,id,'GUIData!F29',data_conveyor_motor_indicator)

# -----------------------------counter_proximity_process indicator data--------------------------
counter_proximity_indicator_array= [['TRUE']]
data_counter_proximity_indicator = {
    'values' : counter_proximity_indicator_array
}
update(service,id,'GUIData!F30',data_counter_proximity_indicator)

# -----------------------------pick_proximity_process indicator data--------------------------
pick_proximity_indicator_array= [['TRUE']]
data_pick_proximity_indicator = {
    'values' : pick_proximity_indicator_array
}
update(service,id,'GUIData!F31',data_pick_proximity_indicator)

# -----------------------------color_sensor_process indicator data--------------------------
color_sensor_indicator_array= [['TRUE']]
data_color_sensor_indicator = {
    'values' :color_sensor_indicator_array
}
update(service,id,'GUIData!F32',data_color_sensor_indicator)

# -----------------------------pushing_arm_process indicator data--------------------------
pushing_arm_indicator_array= [['TRUE']]
data_pushing_arm_indicator = {
    'values' :pushing_arm_indicator_array
}
update(service,id,'GUIData!F33',data_pushing_arm_indicator)

# -----------------------------robot_arm_1_process indicator data--------------------------
robot_arm_1_indicator_array= [['TRUE']]
data_robot_arm_1_indicator = {
    'values' :robot_arm_1_indicator_array
}
update(service,id,'GUIData!F34',data_robot_arm_1_indicator)

# -----------------------------robot_arm_2_process indicator data--------------------------
robot_arm_2_indicator_array= [['TRUE']]
data_robot_arm_2_indicator = {
    'values' :robot_arm_2_indicator_array
}
update(service,id,'GUIData!F35',data_robot_arm_2_indicator)