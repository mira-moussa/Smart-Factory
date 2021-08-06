#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Copyright 2017 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

# Author: Ryu Woon Jung (Leon)

#
# *********     Read and Write Example      *********
#
#
# Available DXL model on this example : All models using Protocol 1.0
# This example is tested with a DXL MX-28, and an USB2DYNAMIXEL
# Be sure that DXL MX properties are already set as %% ID : 1 / Baudnum : 34 (Baudrate : 57600)
#

import pickle #it serializes objects so they can be saved to a file, and loaded in a program again later on
import os


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

from dynamixel_sdk import *                     # Uses Dynamixel SDK library
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
    request = service.spreadsheets().values().get(spreadsheetId=id,range=Goal_pos)
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
# Control table address
ADDR_MX_TORQUE_ENABLE = 24  # Control table address is different in Dynamixel model
ADDR_MX_GOAL_POSITION = 30
ADDR_MX_PRESENT_POSITION = 36

# Protocol version
PROTOCOL_VERSION = 1.0  # See which protocol version is used in the Dynamixel

# Default setting
DXL_ID = 1  # Dynamixel ID : 1
BAUDRATE = 57600  # Dynamixel default baudrate : 57600
DEVICENAME = 'COM4'  # Check which port is being used on your controller
# ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE = 1  # Value for enabling the torque
TORQUE_DISABLE = 0  # Value for disabling the torque
DXL_MINIMUM_POSITION_VALUE = 10  # Dynamixel will rotate between this value
DXL_MAXIMUM_POSITION_VALUE = 1000  # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
#DXL_MOVING_STATUS_THRESHOLD = 20  # Dynamixel moving status threshold

index = 0
dxl_goal_position = [DXL_MINIMUM_POSITION_VALUE, DXL_MAXIMUM_POSITION_VALUE]  # Goal position

# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
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
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel has been successfully connected")
i=1

while 1:
    import time

    Goal_pos = Goal_pos + str(i)


    ReadArray = read(service, id, Goal_pos)
    print(ReadArray)
    Goal_pos = 'Sheet1!A'
    goal = int(ReadArray[0][0])
    goal = int(goal*1023/300)

    # Write goal position
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_MX_GOAL_POSITION,goal)

    time.sleep(1)

    # Read present position
    dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL_ID, ADDR_MX_PRESENT_POSITION)
    current = [[str(dxl_present_position*300/1023)]]
    data3 = {
        'values': current
    }
    print(data3)

    Current_Pos = Current_Pos + str(i)
    Input_Voltage_Error = Input_Voltage_Error+ str(i)
    Angle_Limit_Error = Angle_Limit_Error+str(i)
    Overheating_Error = Overheating_Error +str(i)
    Range_Error = Range_Error +str(i)
    Checksum_Error = Checksum_Error +str(i)
    Overload_Error = Overload_Error +str(i)
    Instruction_Error = Instruction_Error +str(i)

    update(service, id, Current_Pos, data3)

    Goal_pos = 'Sheet1!A'
    Current_Pos = 'Sheet1!B'
    Input_Voltage_Error = 'Sheet1!C'
    Angle_Limit_Error = 'Sheet1!D'
    Overheating_Error = 'Sheet1!E'
    Range_Error = 'Sheet1!F'
    Checksum_Error = 'Sheet1!G'
    Overload_Error = 'Sheet1!H'
    Instruction_Error = 'Sheet1!I'
    i += 1


# Disable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

# Close port
portHandler.closePort()
