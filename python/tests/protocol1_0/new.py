# *********     Read and Write Example      *********
#
#
# Available DXL model on this example : All models using Protocol 1.0
# This example is tested with a DXL MX-28, and an USB2DYNAMIXEL
# Be sure that DXL MX properties are already set as %% ID : 1 / Baudnum : 34 (Baudrate : 57600)
from dynamixel_sdk import *                    # Uses Dynamixel SDK library
import time
time.sleep(0)

# Control table address
ADDR_RX_TORQUE_ENABLE      = 24               # Control table address is different in Dynamixel model
ADDR_RX_GOAL_POSITION      = 30
ADDR_RX_PRESENT_POSITION   = 36
ADDR_RX_PRESENT_SPEED   = 38
LEN_RX_GOAL_POSITION=4

# Protocol version
PROTOCOL_VERSION            = 1.0               # See which protocol version is used in the Dynamixel

# Default setting
DXL1_ID                      = 1            # Dynamixel ID : 1
DXL2_ID                      = 2            # Dynamixel ID : 2
DXL3_ID                      = 3            # Dynamixel ID : 3
BAUDRATE                    = 57600             # Dynamixel default baudrate : 57600
DEVICENAME                  = 'COM4'    # Check which port is being used on your controller "/dev/ttyS0"
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE               = 1                # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque
#DXL_MINIMUM_POSITION_VALUE  = 1023           # Dynamixel will rotate between this value
#DXL_MAXIMUM_POSITION_VALUE  = 0            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)


index_pos = 0
index_speed = 0

dxl1_goal_position = [100,900]     # Goal position for dxl1
dxl2_goal_position = [200,750]        # Goal position for dxl2
dxl3_goal_position = [400,800]        # Goal position for dxl3
dxl_goal_speed = [50,100,200,300,400,500,600,500,400,300,200,100,50]         # speed profile

# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
packetHandler = PacketHandler(PROTOCOL_VERSION)
# Initialize GroupSyncWrite instance
groupSyncWrite = GroupSyncWrite(portHandler, packetHandler, ADDR_RX_GOAL_POSITION, LEN_RX_GOAL_POSITION)
groupSyncRead =GroupSyncRead(portHandler, packetHandler, ADDR_RX_PRESENT_SPEED, LEN_RX_GOAL_POSITION)
# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    quit()


# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()

# Enable Dynamixel#1 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_RX_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel#%d has been successfully connected" % DXL1_ID)

# Enable Dynamixel#2 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_RX_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel#%d has been successfully connected" % DXL2_ID)

# Enable Dynamixel#3 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL3_ID, ADDR_RX_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel#%d has been successfully connected" % DXL3_ID)
i=0
while 1:

    # Allocate goal position value into byte array
    param_1goal_position = [DXL_LOBYTE(dxl1_goal_position[index_pos]),
                            DXL_HIBYTE(dxl1_goal_position[index_pos]),
                            DXL_LOBYTE(dxl_goal_speed[index_speed]),
                            DXL_HIBYTE(dxl_goal_speed[index_speed])]
    param_2goal_position = [DXL_LOBYTE(dxl2_goal_position[index_pos]),
                            DXL_HIBYTE(dxl2_goal_position[index_pos]),
                            DXL_LOBYTE(dxl_goal_speed[index_speed]),
                            DXL_HIBYTE(dxl_goal_speed[index_speed])]
    param_3goal_position = [DXL_LOBYTE(dxl3_goal_position[index_pos]),
                            DXL_HIBYTE(dxl3_goal_position[index_pos]),
                            DXL_LOBYTE(dxl_goal_speed[index_speed]),
                            DXL_HIBYTE(dxl_goal_speed[index_speed])]

    # Add Dynamixel#1 goal position value to the Syncwrite parameter storage
    dxl_addparam_result = groupSyncWrite.addParam(DXL1_ID, param_1goal_position)
    if dxl_addparam_result != True:
        print("[ID:%03d] groupSyncWrite addparam failed" % DXL1_ID)
        quit()

    # Add Dynamixel#2 goal position value to the Syncwrite parameter storage
    dxl_addparam_result = groupSyncWrite.addParam(DXL2_ID, param_2goal_position)
    if dxl_addparam_result != True:
        print("[ID:%03d] groupSyncWrite addparam failed" % DXL2_ID)
        quit()

    # Add Dynamixel#3 goal position value to the Syncwrite parameter storage
    dxl_addparam_result = groupSyncWrite.addParam(DXL3_ID, param_3goal_position)
    if dxl_addparam_result != True:
        print("[ID:%03d] groupSyncWrite addparam failed" % DXL3_ID)
        quit()

    # Syncwrite goal position
    dxl_comm_result = groupSyncWrite.txPacket()  # send at the same time for all motors
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

    time.sleep(.1)

    # Clear syncwrite parameter storage
    groupSyncWrite.clearParam()

    index_speed = index_speed + 1
    if index_speed == 13:
        index_speed=0
        if index_pos ==0:
            index_pos=1
        else:
            index_pos=0
        time.sleep(2)
        i = i + 1
        if i ==5:
            break

# Disable Dynamixel#1 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_RX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

# Disable Dynamixel#2 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_RX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

# Disable Dynamixel#2 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL3_ID, ADDR_RX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))


# Close port
portHandler.closePort()

