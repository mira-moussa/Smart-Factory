
# *********     Read and Write Example      *********
#
#
# Available DXL model on this example : All models using Protocol 1.0
# This example is tested with a DXL MX-28, and an USB2DYNAMIXEL
# Be sure that DXL MX properties are already set as %% ID : 1 / Baudnum : 34 (Baudrate : 57600)
from dynamixel_sdk import *                    # Uses Dynamixel SDK library

# Control table address
ADDR_RX_TORQUE_ENABLE      = 24               # Control table address is different in Dynamixel model
ADDR_RX_GOAL_POSITION      = 30
ADDR_RX_PRESENT_POSITION   = 36
ADDR_RX_PRESENT_SPEED = 38

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


index_pos = 0
index_speed = 0

dxl1_goal_position = [100,300]     # Goal position for dxl1
dxl2_goal_position = [300,500]        # Goal position for dxl2
dxl3_goal_position = [500,800]        # Goal position for dxl3
dxl_goal_speed = [20,50,70,100,120,150,150,120,70,50,20,10]         # speed profile

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
    quit()


# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    quit()

# Enable Dynamixel1 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_RX_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel has been successfully connected")

# Enable Dynamixel2 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_RX_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel has been successfully connected")

# Enable Dynamixel3 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL3_ID, ADDR_RX_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel has been successfully connected")

i=0
dt=0.05
dt2=0.1
while 1:


    # Write dxl1 goal position
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL1_ID, ADDR_RX_GOAL_POSITION, dxl1_goal_position[index_pos], dxl_goal_speed[index_speed])
    time.sleep(dt)

    # Write dxl2 goal position
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL2_ID, ADDR_RX_GOAL_POSITION,
                                                                  dxl2_goal_position[index_pos],
                                                                  dxl_goal_speed[index_speed])
    time.sleep(dt)

    # Write dxl3 goal position
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL3_ID, ADDR_RX_GOAL_POSITION,
                                                                  dxl3_goal_position[index_pos],
                                                                  dxl_goal_speed[index_speed])
    time.sleep(dt)



    # Read present speed dx1
    dxl_present_speed, dxl_comm_result, dxl_error, ibrahim_data = packetHandler.read10ByteTxRx(portHandler, DXL1_ID,
                                                                                   ADDR_RX_PRESENT_SPEED)

    print("[ID:%03d]  goalspeed:%03d PresSpeed:%03d" % (DXL1_ID, dxl_goal_speed[index_speed], dxl_present_speed))
    time.sleep(dt)

    # Read present speed dx2
    dxl_present_speed, dxl_comm_result, dxl_error, ibrahim_data = packetHandler.read10ByteTxRx(portHandler, DXL2_ID,
                                                                                   ADDR_RX_PRESENT_SPEED)

    print("[ID:%03d]  goalspeed:%03d PresSpeed:%03d" % (DXL2_ID, dxl_goal_speed[index_speed], dxl_present_speed))
    time.sleep(dt)

    # Read present speed dx3
    dxl_present_speed, dxl_comm_result, dxl_error, ibrahim_data = packetHandler.read10ByteTxRx(portHandler, DXL3_ID,
                                                                                   ADDR_RX_PRESENT_SPEED)

    print("[ID:%03d]  goalspeed:%03d PresSpeed:%03d" % (DXL3_ID, dxl_goal_speed[index_speed], dxl_present_speed))
    time.sleep(dt2)

    index_speed = index_speed + 1
    if index_speed == 12:
        index_speed = 0
        if index_pos == 0:
            index_pos = 1
        else:
            index_pos = 0
        time.sleep(1.5)
        i = i + 1
        if i == 5:
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

# Disable Dynamixel#3  Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL3_ID, ADDR_RX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
# Close port
portHandler.closePort()