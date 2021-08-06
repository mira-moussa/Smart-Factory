from dynamixel_sdk import *  # Uses Dynamixel SDK library
import time

ADDR_RX_TORQUE_ENABLE = 24
ADDR_RX_PRESENT_POSITION = 36
ADDR_RX_PRESENT_SPEED = 38
ADDR_RX_PRESENT_LOAD = 40
ADDR_RX_PRESENT_TEMPERATURE = 43
ADDR_RX_PRESENT_VOLTAGE = 42
ADDR_RX_GOAL_POSITION = 30
ADDR_AX_GOAL_SPEED_L = 32

LEN_RX_GOAL_POSITION = 4
DXL_ID = 7
# Protocol version
PROTOCOL_VERSION = 1.0  # See which protocol version is used in the Dynamixel
BAUDRATE = 57600  # Dynamixel default baudrate : 57600
DEVICENAME = 'COM5'  # Check which port is being used on your controller "/dev/ttyS0"
# DEVICENAME = '/dev/ttyS0'
# ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE = 1  # Value for enabling the torque
TORQUE_DISABLE = 0  # Value for disabling the torque
DXL_GOAL_POSITION = [880,980]
dxl_goal_speed = [50,200]
portHandler = PortHandler(DEVICENAME)

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

# Enable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_RX_TORQUE_ENABLE,
                                                          TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel: %03d has been successfully connected", DXL_ID)
count = 0
while 1:
    for i in range(2):
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_AX_GOAL_SPEED_L,
                                                                  dxl_goal_speed[i])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_RX_GOAL_POSITION,
                                                                  DXL_GOAL_POSITION[i])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))




        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 3, ADDR_AX_GOAL_SPEED_L,
                                                                  dxl_goal_speed[i])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 3, ADDR_RX_GOAL_POSITION,
                                                                  DXL_GOAL_POSITION[i])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        time.sleep(1.5)
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

portHandler.closePort()
