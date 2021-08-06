import concurrent.futures
import threading
from dynamixel_sdk import *  # Uses Dynamixel SDK library
import time  # for trajectory timing
from Trajectory1 import *  # trajectory functions
import numpy as np


status = 'stop'
ADDR_RX_TORQUE_ENABLE = 24
ADDR_RX_PRESENT_POSITION = 36
ADDR_RX_PRESENT_SPEED = 38
ADDR_RX_PRESENT_LOAD = 40
ADDR_RX_PRESENT_TEMPERATURE = 43
ADDR_RX_PRESENT_VOLTAGE = 42
ADDR_RX_GOAL_POSITION = 30
ADDR_AX_GOAL_SPEED_L = 32
ADDR_Movement_Status = 46

LEN_RX_GOAL_POSITION = 4

PROTOCOL_VERSION = 1.0  # Protocol version
BAUDRATE = 57600  # Dynamixel default baudrate : 57600
DEVICENAME = 'COM5'  # Check which port is being used on your controller
# DEVICENAME = '/dev/ttyUSB0'

TORQUE_ENABLE = 1  # Value for enabling the torque
TORQUE_DISABLE = 0  # Value for disabling the torque
ID_INDEX = 0  # index for iteration of different dxl Id
SPEED_INDEX = 0  # index for looping over different speeds

DXL_MORAD_ID = [1, 2, 3]  # used dxl ID
DXL_ZIKAS_ID = [5, 6, 7]  # used dxl ID
DXL_AX_ID = [4, 8]
DXL_ALL_IDS = [1, 2, 3, 4, 5, 6, 7, 8]  # used dxl ID
ax_goal_speed = 100  # AX_speed
MORAD_AX_GOAL_POS = [880, 980]  # pick and place thetas for ax 7
ZIKAS_AX_GOAL_POS = [580, 645]  # pick and place thetas for ax 8



robot_zikas = {
    'points_zikas': [False] * 8,
    'start_zikas': 0,
    'busy_zikas': 0,
    'process_done_zikas': 1,
    'current_sensors_values_zikas': {
        'ID1': [0] * 5,  # Pos, Speed, Volt, Load and Temp
        'ID2': [0] * 5,
        'ID3': [1] * 5,
    },
    'Gripper_zikas': True,  # Open  Gripper
}

robot_morad = {
    'points_morad': [False] * 8,
    'start_morad': 0,
    'busy_morad': 0,
    'process_done_morad': 1,
    'current_sensors_values_morad': {
        'ID1': [0] * 4,  # Pos, Speed, Volt, Load and Temp
        'ID2': [0] * 4,
        'ID3': [0] * 4,
    },
    'Gripper_morad': True  # Open  Gripper
}

print(robot_morad)
print(robot_zikas)

portHandler = PortHandler(DEVICENAME)
# Initialize PortHandler instance #Set the port path # Get methods and members of PortHandlerLinux or PortHandlerWindows


# Initialize PacketHandler instance #Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
packetHandler = PacketHandler(PROTOCOL_VERSION)
# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    quit()

# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    quit()

# Initialize GroupSyncWrite instance
groupSyncWrite = GroupSyncWrite(portHandler, packetHandler, ADDR_RX_GOAL_POSITION, LEN_RX_GOAL_POSITION)

for i in range(8):
    # Enable Dynamixel Torque
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ALL_IDS[i], ADDR_RX_TORQUE_ENABLE,
                                                              TORQUE_ENABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        print("Dynamixel:%03d has been successfully connected", DXL_ALL_IDS[i])

for i in range(3):
    pos = threading.Thread(target=packetHandler.read2ByteTxRx, name='thread1',
                           args=(portHandler, DXL_ZIKAS_ID[i], ADDR_RX_PRESENT_POSITION))
    load = threading.Thread(target=packetHandler.read2ByteTxRx, name='thread2',
                            args=(portHandler, DXL_ZIKAS_ID[i], ADDR_RX_PRESENT_LOAD))
    temp = threading.Thread(target=packetHandler.read2ByteTxRx, name='thread3',
                            args=(portHandler, DXL_ZIKAS_ID[i], ADDR_RX_PRESENT_TEMPERATURE))
    volt = threading.Thread(target=packetHandler.read2ByteTxRx, name='thread4',
                            args=(portHandler, DXL_ZIKAS_ID[i], ADDR_RX_PRESENT_VOLTAGE))
    pos.start()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(packetHandler.read2ByteTxRx, 'world!')
        robot_zikas['current_sensors_values_zikas']['ID' + str(i + 1)][0] = future.result()