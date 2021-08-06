from dynamixel_sdk import *                    # Uses Dynamixel SDK library

# Control table address
ADDR_MX_TORQUE_ENABLE      = 24              # Control table address is different in Dynamixel model
ADDR_MX_GOAL_POSITION      = 30
ADDR_MX_PRESENT_POSITION   = 36

# Data Byte Length
LEN_MX_GOAL_POSITION       = 4
LEN_MX_PRESENT_POSITION    = 4

# Protocol version
PROTOCOL_VERSION            = 1.0               # See which protocol version is used in the Dynamixel

# Default setting
DXL1_ID                     = 1                 # Dynamixel#1 ID : 1
DXL2_ID                     = 2
DXL3_ID                     = 3
# Dynamixel#1 ID : 2
BAUDRATE                    = 57600             # Dynamixel default baudrate : 57600
DEVICENAME                  = 'COM4'    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE               = 1                 # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque
DXL_1MINIMUM_POSITION_VALUE  =360         # Dynamixel will rotate between this value
DXL_1MAXIMUM_POSITION_VALUE  = 380          # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
DXL_2MINIMUM_POSITION_VALUE  =680         # Dynamixel will rotate between this value
DXL_2MAXIMUM_POSITION_VALUE  = 380          # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
DXL_3MINIMUM_POSITION_VALUE  =1023        # Dynamixel will rotate between this value
DXL_3MAXIMUM_POSITION_VALUE  = 927          # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)




index = 0
dxl_1goal_position = [DXL_1MINIMUM_POSITION_VALUE, DXL_1MAXIMUM_POSITION_VALUE]         # Goal position
dxl_2goal_position = [DXL_2MINIMUM_POSITION_VALUE, DXL_2MAXIMUM_POSITION_VALUE]         # Goal position
dxl_3goal_position = [DXL_3MINIMUM_POSITION_VALUE, DXL_3MAXIMUM_POSITION_VALUE]         # Goal position


# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Initialize GroupSyncWrite instance
groupSyncWrite = GroupSyncWrite(portHandler, packetHandler, ADDR_MX_GOAL_POSITION, LEN_MX_GOAL_POSITION)

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


# Enable Dynamixel#1 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel#%d has been successfully connected" % DXL1_ID)

# Enable Dynamixel#2 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel#%d has been successfully connected" % DXL2_ID)

# Enable Dynamixel#3 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL3_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel#%d has been successfully connected" % DXL3_ID)

while 1:

    # Allocate goal position value into byte array
    param_1goal_position = [DXL_LOBYTE(DXL_LOWORD(dxl_1goal_position[index])), DXL_HIBYTE(DXL_LOWORD(dxl_1goal_position[index])), DXL_LOBYTE(DXL_HIWORD(dxl_1goal_position[index])), DXL_HIBYTE(DXL_HIWORD(dxl_1goal_position[index]))]
    param_2goal_position = [DXL_LOBYTE(DXL_LOWORD(dxl_2goal_position[index])),
                            DXL_HIBYTE(DXL_LOWORD(dxl_2goal_position[index])),
                            DXL_LOBYTE(DXL_HIWORD(dxl_2goal_position[index])),
                            DXL_HIBYTE(DXL_HIWORD(dxl_2goal_position[index]))]
    param_3goal_position = [DXL_LOBYTE(DXL_LOWORD(dxl_3goal_position[index])),
                            DXL_HIBYTE(DXL_LOWORD(dxl_3goal_position[index])),
                            DXL_LOBYTE(DXL_HIWORD(dxl_3goal_position[index])),
                            DXL_HIBYTE(DXL_HIWORD(dxl_3goal_position[index]))]

    # Add Dynamixel#1 goal position value to the Syncwrite parameter storage
    dxl_addparam_result = groupSyncWrite.addParam(DXL1_ID, param_1goal_position)
    if dxl_addparam_result != True:
        print("[ID:%03d] groupSyncWrite addparam failed" % DXL1_ID)
        quit()
    time.sleep(1)
    # Add Dynamixel#2 goal position value to the Syncwrite parameter storage
    dxl_addparam_result = groupSyncWrite.addParam(DXL2_ID, param_2goal_position)
    if dxl_addparam_result != True:
        print("[ID:%03d] groupSyncWrite addparam failed" % DXL2_ID)
        quit()
    time.sleep(1)
    # Add Dynamixel#3 goal position value to the Syncwrite parameter storage
    dxl_addparam_result = groupSyncWrite.addParam(DXL3_ID, param_3goal_position)
    if dxl_addparam_result != True:
        print("[ID:%03d] groupSyncWrite addparam failed" % DXL3_ID)
        quit()
    time.sleep(1)
    # Syncwrite goal position
    dxl_comm_result = groupSyncWrite.txPacket()     # send at the same time for all motors
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

    # Clear syncwrite parameter storage
    groupSyncWrite.clearParam()


    # Read Dynamixel#1 present position
    dxl1_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL1_ID, ADDR_MX_PRESENT_POSITION)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    time.sleep(1)

    # Read Dynamixel#2 present position
    dxl2_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL2_ID, ADDR_MX_PRESENT_POSITION)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    time.sleep(1)


    # Read Dynamixel#3 present position
    dxl3_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL3_ID, ADDR_MX_PRESENT_POSITION)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    time.sleep(1)



    # Change goal position
    if index == 0:
        index = 1
    else:
        index = 0


# Disable Dynamixel#1 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

# Disable Dynamixel#2 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

# Close port
portHandler.closePort()
