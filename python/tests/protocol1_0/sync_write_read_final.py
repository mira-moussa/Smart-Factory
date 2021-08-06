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

LEN_RX_GOAL_POSITION = 4

# Protocol version
PROTOCOL_VERSION = 1.0               # See which protocol version is used in the Dynamixel
BAUDRATE = 57600             # Dynamixel default baudrate : 57600
DEVICENAME = 'COM4'    # Check which port is being used on your controller "/dev/ttyS0"
# ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE = 1                # Value for enabling the torque
TORQUE_DISABLE = 0                 # Value for disabling the torque


ID_INDEX = 0                        # index for iteration of different dxl Id
POS_INDEX = 0                       # index for looping over differnt poditions
SPEED_INDEX = 0                     # index for looping over different speeds

DXL_ID = [1, 2, 3]                  # used dxl ID
DXL_GOAL_POSITION = [[200, 800], [200, 800], [200, 800]]   # array of goal pos for every dxl
dxl_goal_speed = [0]*20            # array of speeds with length 30
ts = 0.05
initial_speed = 50
increment = 100
for i in range(10):

    if i > 4:
        dxl_goal_speed[i] = initial_speed - increment
        initial_speed = initial_speed - increment
    elif i <= 4:
        dxl_goal_speed[i] = initial_speed + increment
        initial_speed = initial_speed + increment
# Initialize PortHandler instance #Set the port path # Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

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

for i in range(3):
    # Enable Dynamixel Torque
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID[i], ADDR_RX_TORQUE_ENABLE, TORQUE_ENABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        print("Dynamixel:%03d has been successfully connected", DXL_ID[i])
n = 0
while 1:
    for i in range(3):
        # Allocate goal position value into byte array
        param_1goal_position = [DXL_LOBYTE(DXL_GOAL_POSITION[i][POS_INDEX]),
                                DXL_HIBYTE(DXL_GOAL_POSITION[i][POS_INDEX]),
                                DXL_LOBYTE(dxl_goal_speed[SPEED_INDEX]),
                                DXL_HIBYTE(dxl_goal_speed[SPEED_INDEX])]

        # Add Dynamixel#1 goal position value to the Syncwrite parameter storage
        dxl_addparam_result = groupSyncWrite.addParam(DXL_ID[i], param_1goal_position)
        if dxl_addparam_result != True:
            print("[ID:%03d] groupSyncWrite addparam failed" % DXL_ID[i])
            quit()

    # Syncwrite goal position
    dxl_comm_result = groupSyncWrite.txPacket()      # send at the same time for all motors
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

    time.sleep(ts)

    for i in range (3):
        # Read present position
        dxl_present_position, dxl_comm_result, dxl_error, data = packetHandler.read2ByteTxRx(portHandler, DXL_ID[i],
                                                                                       ADDR_RX_PRESENT_POSITION)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        goal_pos = (300/1023)*DXL_GOAL_POSITION[i][POS_INDEX]
        present_pos = (300/1023)*dxl_present_position
        print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID[i], goal_pos, present_pos))

        m = 0
        # read speed
        while 1:
            dxl_present_speed, dxl_comm_result, dxl_error, data = packetHandler.read2ByteTxRx(portHandler, DXL_ID[i],
                                                                                              ADDR_RX_PRESENT_SPEED)

            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            if dxl_present_speed >= 1000:
                dxl_present_speed = dxl_present_speed & 0XFF
            else:
                dxl_present_speed = dxl_present_speed
            goal_speed = dxl_goal_speed[SPEED_INDEX]*0.1
            present_speed = dxl_present_speed*0.1

            print(
                "[ID:%03d] GoalSpeed:%03d  PresSpeed:%03d RPM" % (DXL_ID[i], goal_speed, present_speed))
            m = m + 1
            if m == 3:
                break

        # LOAD
        dxl_present_load, dxl_comm_result, dxl_error, data = packetHandler.read10ByteTxRx(portHandler, DXL_ID[i],
                                                                                          ADDR_RX_PRESENT_LOAD)

        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        if dxl_present_load >= 1000:
            dxl_present_load = dxl_present_load & 0XFF
        else:
            dxl_present_load = dxl_present_load

        present_load = dxl_present_load * 0.01

        print("Present Load is :%03d percentage" % present_load)

        # VOLTAGE
        dxl_present_voltage, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL_ID[i],
                                                                                      ADDR_RX_PRESENT_VOLTAGE)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        print("Present Voltage is : %f Volt." % (dxl_present_voltage / 10))

        # Temperature
        dxl_present_temperature, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL_ID[i],
                                                                                          ADDR_RX_PRESENT_TEMPERATURE)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        print("Present Temperature is %f degrees celesius." % float(dxl_present_temperature))

    # Clear syncwrite parameter storage
    groupSyncWrite.clearParam()

    SPEED_INDEX = SPEED_INDEX + 1
    if SPEED_INDEX == 10:
        SPEED_INDEX = 0
        if POS_INDEX == 0:
            POS_INDEX = 1
        else:
            POS_INDEX = 0
        time.sleep(0.5)
        n = n + 1
        if n == 5:
            break

for i in range (3) :
    # Disable Dynamixel#1 Torque
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID[i], ADDR_RX_TORQUE_ENABLE,
                                                              TORQUE_DISABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))


# Close port
portHandler.closePort()
