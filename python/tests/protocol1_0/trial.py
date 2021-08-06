import os
import pickle
from dynamixel_sdk import *
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2 import service_account


if os.name == 'nt':
    import msvcrt


    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)


    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch



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
    request = service.spreadsheets().values().get(spreadsheetId=id,range=Goal)
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
PRESENT_VOLTAGE = 'Sheet1!C'
PRESENT_TEMPERATURE = 'Sheet1!D'
PRESENT_LOAD = 'Sheet1!E'
PRESENT_SPEED = 'Sheet1!F'
i=1                            #num of iterations

service = Start(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, *SCOPES)

# Control table address
ADDR_RX_TORQUE_ENABLE = 24
ADDR_RX_PRESENT_POSITION = 36
ADDR_RX_PRESENT_SPEED = 38
ADDR_RX_PRESENT_LOAD = 40
ADDR_RX_PRESENT_TEMPERATURE = 43
ADDR_RX_PRESENT_VOLTAGE = 42
ADDR_RX_GOAL_POSITION = 30

# Protocol version
PROTOCOL_VERSION = 1.0

# Default setting
DXL_ID = 1
BAUDRATE = 57600
DEVICENAME = 'COM4'  # make sure to check the com in your devices manager please.

TORQUE_ENABLE = 1  # Value for enabling the torque
TORQUE_DISABLE = 0  # Value for disabling the torque
DXL_MINIMUM_POSITION_VALUE = 0  # Dynamixel will rotate between this value
DXL_MAXIMUM_POSITION_VALUE = 1023  # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)

index = 0


# Set the port path
portHandler = PortHandler(DEVICENAME)

# Set the protocol version
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()

# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()

# Enable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_RX_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("RX-64 has been successfully connected!")


while 1:
    import time
    Goal = Goal_pos + str(i)
    ReadArray = read(service, id, Goal)
    goal = int(ReadArray[0][0])
    goal = int(goal * 1023 / 300)

    print("Press any key to continue! (or press ESC to quit!)")
    # if getch() == chr(0x1b):
    # break

    # Write goal position
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_RX_GOAL_POSITION, goal)
    time.sleep(0.15)
    dxl_present_load, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID,
                                                                               ADDR_RX_PRESENT_LOAD)


    dxl_present_speed, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID,
                                                                                ADDR_RX_PRESENT_SPEED)
    print("          Present Speed is :%03d m/s" % dxl_present_speed)
    current5 = [[str(dxl_present_speed)]]

    data5 = {
        'values': current5
    }
    SPEED = PRESENT_SPEED + str(i)
    update(service, id, SPEED, data5)
    # print(data3)
    print("          Present Load is :%03d Nm" % dxl_present_load)
    current4 = [[str(dxl_present_load)]]

    data4 = {
        'values': current4
    }
    LOAD = PRESENT_LOAD + str(i)
    update(service, id, LOAD, data4)
    # print(data3)
    
    # Read present voltage, speed, load,position and temperature.

    # read current POSITION
    dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID,
                                                                                   ADDR_RX_PRESENT_POSITION)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    print("[ID:%03d]  Present Position is :%03d" % (DXL_ID, dxl_present_position))
    current1 = [[str(dxl_present_position * 300 / 1023)]]
    data1 = {
        'values': current1
    }
    Pos = Current_Pos + str(i)
    update(service, id, Pos, data1)
    #print(data3)

    # VOLTAGE
    dxl_present_voltage, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL_ID,
                                                                                  ADDR_RX_PRESENT_VOLTAGE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    print("          Present Voltage is : %f Volt." % (dxl_present_voltage / 10))
    current2 = [[str(dxl_present_voltage / 10)]]
    data2 = {
        'values': current2
    }
    VOLTAGE = PRESENT_VOLTAGE + str(i)
    update(service, id, VOLTAGE, data2)
    # print(data3)


    # Temperature
    dxl_present_temperature, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL_ID,
                                                                                      ADDR_RX_PRESENT_TEMPERATURE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    print("          Present Temperature is %f degrees celesius." % float(dxl_present_temperature))
    current3 = [[str(float(dxl_present_temperature))]]

    data3 = {
        'values': current3
    }
    TEMPERATURE = PRESENT_TEMPERATURE + str(i)
    update(service, id,TEMPERATURE, data3)
    #print(data3)

    # LOAD


    # SPEED

    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))



    i += 1
    if i==7:
        quit()

# Disable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_RX_TORQUE_ENABLE,
                                                              TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

# Close port
portHandler.closePort()
quit()
