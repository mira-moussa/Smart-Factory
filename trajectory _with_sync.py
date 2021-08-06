from dynamixel_sdk import *                    # Uses Dynamixel SDK library
import time
from Trajectory1 import *
from matplotlib import pyplot as plt

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
                           # index for looping over differnt poditions
SPEED_INDEX = 0                     # index for looping over different speeds

DXL_ID = [1, 2, 3]                  # used dxl ID
portHandler = PortHandler(DEVICENAME)
# Initialize PortHandler instance #Set the port path # Get methods and members of PortHandlerLinux or PortHandlerWindows


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
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID[i], ADDR_RX_TORQUE_ENABLE,
                                                              TORQUE_ENABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        print("Dynamixel:%03d has been successfully connected", DXL_ID[i])


#from matplotlib import pyplot as plt

home=[0, 0,26.4]
point1=[-14.612,4.384,9.125]
point2=[-15.464,4.639,5.858]

point3=[12.195,5.144,17.989]
point4=[6.512,12.186,11.238]
point5=[6.593,12.337,8.147]
present_pos=[18,0,8.4]
points=[point1,point2,point1,point3,point4,point5,point4,home]
figs1=['th1.png','th2.png','th3.png','th4.png','th5.png','th6.png','th7.png','th8.png']
figs2=['p1.png','p2.png','p3.png','p4.png','p5.png','p6.png','p7.png','p8.png']
#figs3=['sp1.png','sp2.png','sp3.png','sp4.png','sp5.png','sp6.png','sp7.png','sp8.png']

t = 1
N = 10
ts = (t / (N - 1))
TIME = [0]*(N-2)
a = 0
for i in range(N-2):
    a = a+ts
    TIME[i] = a
#actual_speed = np.zeros(shape=(3, N-2))
actual_pos = np.zeros(shape=(3, N-2))

for k in range(8):
    # main code
    SPEED_INDEX = 0
    POS_INDEX = 0
    if k==0:
        theta0 = ik(home)
    else:
        theta0 = ik(points[k-1])
    print(theta0)
    DXL_GOAL_POSITION = ik(points[k])
    print(DXL_GOAL_POSITION)


    # شيلت من هنا t,N

    [position,dxl_goal_sp,acc]=traj(np.rad2deg(theta0),np.rad2deg(DXL_GOAL_POSITION),t,N)
    plt.savefig(figs1[k])
    plt.clf()
    DXL_GOAL_POSITION= np.rad2deg(DXL_GOAL_POSITION)*(1023/300)

    #print(dxl_goal_speed)

    dxl_goal_speed = np.delete(dxl_goal_sp, 0, 0)
    dxl_goal_speed = np.delete(dxl_goal_speed, N-2, 0)

    for i in range(N-2):
        for j in range(3):
            dxl_goal_speed[i][j]=(dxl_goal_speed[i][j]*10)/6

    #print(dxl_goal_speed)
    #print(dxl_goal_speed)
    #plt.show()



    # Control table address

    # شيلت ts

    start = time.perf_counter()
    while 1:
        for i in range(3):
            # Allocate goal position value into byte array
            #print("DXL_GOAL_SPEED=%03d"%dxl_goal_speed[SPEED_INDEX][i])
            param_1goal_position = [DXL_LOBYTE(round(DXL_GOAL_POSITION[i])),
                                    DXL_HIBYTE(round(DXL_GOAL_POSITION[i])),
                                    DXL_LOBYTE(round(dxl_goal_speed[SPEED_INDEX][i])),
                                    DXL_HIBYTE(round(dxl_goal_speed[SPEED_INDEX][i]))]

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
        for i in range(3):
            # Read present position
            dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID[i],
                                                                                           ADDR_RX_PRESENT_POSITION)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            goal_pos = (300 / 1023) * DXL_GOAL_POSITION[i]
            present_pos[i] = (300 / 1023) * dxl_present_position
            actual_pos[i][POS_INDEX] = present_pos[i]  # matrix of actual positions
            print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ID[i], goal_pos, present_pos[i]))

        """
        for i in range(3):
            dxl_present_speed, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID[i],
                                                                                              ADDR_RX_PRESENT_SPEED)

            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            if dxl_present_speed >= 1000:
                dxl_present_speed = dxl_present_speed & 0XFF
            else:
                dxl_present_speed = dxl_present_speed
            goal_speed = dxl_goal_speed[SPEED_INDEX][i]/10
            present_speed = dxl_present_speed /10
            actual_speed[i][SPEED_INDEX] = int(present_speed)  # matrix of actual speeds
            print("[ID:%03d] GoalSpeed:%03d  PresSpeed:%03d RPM" % (DXL_ID[i], goal_speed, present_speed))
        """
        # Clear syncwrite parameter storage
        groupSyncWrite.clearParam()

        SPEED_INDEX = SPEED_INDEX + 1
        print(SPEED_INDEX)
        if SPEED_INDEX == N-2:

            #time.sleep()
            break

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
    for i in range(3):
        plot2 = plt.figure(2)
        actual1 = plt.plot(TIME, actual_pos[i][:])
        plt.title("DXL_ACTUAL_pos")
        plt.legend(["theta1", "theta2", "theta3"])
        plt.savefig(figs2[k])
    plt.clf()
    """
    for g in range (3):
        plot3 = plt.figure(3)
        actual2 = plt.plot(TIME, actual_speed[g][:])
        plt.title("DXL_ACTUAL_SPEED")
        plt.legend(["w1", "w2", "w3"])
        plt.savefig(figs3[k])
    plt.clf()
    #plt.show()
    """

    if (points[k]==points[1]):
        time.sleep(.5)
    else:
        time.sleep(.5)


for i in range (3) :
    # Disable Dynamixel#1 Torque
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID[i], ADDR_RX_TORQUE_ENABLE,
                                                              TORQUE_DISABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))


    #Close port
portHandler.closePort()

