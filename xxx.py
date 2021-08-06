from dynamixel_sdk import *  # Uses Dynamixel SDK library
import time

# from matplotlib import pyplot as plt

ADDR_RX_TORQUE_ENABLE = 24
ADDR_RX_PRESENT_POSITION = 36
ADDR_RX_PRESENT_SPEED = 38
ADDR_RX_PRESENT_LOAD = 40
ADDR_RX_PRESENT_TEMPERATURE = 43
ADDR_RX_PRESENT_VOLTAGE = 42
ADDR_RX_GOAL_POSITION = 30

LEN_RX_GOAL_POSITION = 4
DXL_ID=7
# Protocol version
PROTOCOL_VERSION = 1.0  # See which protocol version is used in the Dynamixel
BAUDRATE = 57600  # Dynamixel default baudrate : 57600
DEVICENAME = 'COM4'  # Check which port is being used on your controller "/dev/ttyS0"
# DEVICENAME = '/dev/ttyS0'
# ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE = 1  # Value for enabling the torque
TORQUE_DISABLE = 0  # Value for disabling the torque
DXL_GOAL_POSITION=[880,980]
dxl_goal_speed=[50,200]
# Initialize PacketHandler instance #Set the protocol version
# #Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
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

# Enable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_RX_TORQUE_ENABLE,
                                                          TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel:%03d has been successfully connected", DXL_ID)
count=0
while 1:
    for i in range(2):
        # Allocate goal position value into byte array
        param_1goal_position = [DXL_LOBYTE(round(DXL_GOAL_POSITION[i])),
                                DXL_HIBYTE(round(DXL_GOAL_POSITION[i])),
                                DXL_LOBYTE(round(dxl_goal_speed[i])),
                                DXL_HIBYTE(round(dxl_goal_speed[i]))]

        # Add Dynamixel#1 goal position value to the Syncwrite parameter storage
        dxl_addparam_result = groupSyncWrite.addParam(DXL_ID, param_1goal_position)
        if dxl_addparam_result != True:
            print("[ID:%03d] groupSyncWrite addparam failed" % DXL_ID)
            quit()
        # Syncwrite goal position
        dxl_comm_result = groupSyncWrite.txPacket()  # send at the same time for all motors
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

        time.sleep(3)
    count=count+1
    if count==3:
        break


# Disable Torque for each Dynamixel RX-64 in Morads Arm
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_RX_TORQUE_ENABLE,
                                                          TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))