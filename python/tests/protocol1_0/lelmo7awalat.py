# *********     Read and Write Example      *********
#
#
# Available DXL model on this example : All models using Protocol 1.0
# This example is tested with a DXL MX-28, and an USB2DYNAMIXEL
# Be sure that DXL MX properties are already set as %% ID : 1 / Baudnum : 34 (Baudrate : 57600)
from dynamixel_sdk import *                    # Uses Dynamixel SDK library
import time

# Control table address
ADDR_RX_TORQUE_ENABLE = 24
ADDR_RX_PRESENT_POSITION = 36
ADDR_RX_PRESENT_SPEED = 38
ADDR_RX_PRESENT_LOAD = 40
ADDR_RX_PRESENT_TEMPERATURE = 43
ADDR_RX_PRESENT_VOLTAGE = 42
ADDR_RX_GOAL_POSITION = 30

LEN_RX_GOAL_POSITION=4

# Protocol version
PROTOCOL_VERSION            = 1.0               # See which protocol version is used in the Dynamixel

# Default setting
DXL1_ID                      = 2            # Dynamixel ID : 1
BAUDRATE                    = 57600             # Dynamixel default baudrate : 57600
DEVICENAME                  = 'COM4'    # Check which port is being used on your controller "/dev/ttyS0"
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE               = 1                # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque

index_pos = 0
index_speed = 0

dxl1_goal_position =[0,1023]    # Goal position for dxl1

dxl_goal_speed = [100,400,700,1000,700,400,100]         # speed profile

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

i=0
while 1:

    # Allocate goal position value into byte array
    param_1goal_position = [DXL_LOBYTE(dxl1_goal_position[index_pos]),
                            DXL_HIBYTE(dxl1_goal_position[index_pos]),
                            DXL_LOBYTE(dxl_goal_speed[index_speed]),
                            DXL_HIBYTE(dxl_goal_speed[index_speed])]
 # Add Dynamixel#1 goal position value to the Syncwrite parameter storage
    dxl_addparam_result = groupSyncWrite.addParam(DXL1_ID, param_1goal_position)
    if dxl_addparam_result != True:
        print("[ID:%03d] groupSyncWrite addparam failed" % DXL1_ID)
        quit()
 # Syncwrite goal position
    dxl_comm_result = groupSyncWrite.txPacket()  # send at the same time for all motors
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    time.sleep(.15)

    # Read present position
    dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL1_ID,
                                                                                   ADDR_RX_PRESENT_POSITION)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL1_ID, dxl1_goal_position[index_pos], dxl_present_position))


    m=0
   # read speed
    while 1:
        dxl_present_speed, dxl_comm_result, dxl_error, data = packetHandler.read2ByteTxRx(portHandler, DXL1_ID,
                                                                                          ADDR_RX_PRESENT_SPEED)
        print(" goalSpeed :%03d " % (dxl_goal_speed[index_speed]), data)

        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        if dxl_present_speed >=999:
           dxl1_present_speed= dxl_present_speed & 0XFF
        else:
            dxl1_present_speed= dxl_present_speed


        print("[ID:%03d] GoalSpeed:%03d  PresSpeed:%03d" % (DXL1_ID, dxl_goal_speed[index_speed], dxl1_present_speed))
        m=m+1
        if m==5:
            break



    # LOAD
    dxl_present_load, dxl_comm_result, dxl_error,data = packetHandler.read10ByteTxRx(portHandler, DXL1_ID,
                                                                               ADDR_RX_PRESENT_LOAD)
    print("load persentage:", data)
    print(data)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    print("          Present Load is :%03d Nm" % dxl_present_load)

    # VOLTAGE
    dxl_present_voltage, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL1_ID,
                                                                                  ADDR_RX_PRESENT_VOLTAGE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    print("Present Voltage is : %f Volt." % (dxl_present_voltage / 10))

    # Temperature
    dxl_present_temperature, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL1_ID,
                                                                                      ADDR_RX_PRESENT_TEMPERATURE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    print("Present Temperature is %f degrees celesius." % float(dxl_present_temperature))

    # Clear syncwrite parameter storage
    groupSyncWrite.clearParam()

    index_speed = index_speed + 1
    if index_speed == 7:
        index_speed = 0
        if index_pos == 0:
            index_pos = 1
        else:
            index_pos = 0
        time.sleep(2)
        i = i + 1
        if i == 3:
            break

# Disable Dynamixel#1 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_RX_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
# Close port
portHandler.closePort()