# import concurrent.futures
# import threading
from dynamixel_sdk import *  # Uses Dynamixel SDK library
import time  # for trajectory timing
from Trajectory1 import *  # trajectory functions
import numpy as np
from read_motors_sensors import *


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
ADDR_RX_READINGS= [36, 38, 40, 43, 42]    # pos,speed,load,temp,volt

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

robot_morad = {
    'points_morad': [False] * 8,
    'start_morad': 1,
    'busy_morad': 0,
    'process_done_morad': 1,
    'current_sensors_values_morad': {
        'ID1': [0] * 4,  # Pos, Speed, Volt, Load and Temp
        'ID2': [0] * 4,
        'ID3': [0] * 4,
    },
    'Gripper_morad': True  # Open  Gripper
}

robot_zikas = {
    'points_zikas': [False] * 8,
    'start_zikas': 0,
    'busy_zikas': 0,
    'process_done_zikas': 1,
    'current_sensors_values_zikas': {
        'ID1': [0] * 4,  # Pos, Speed, Volt, Load and Temp
        'ID2': [0] * 4,
        'ID3': [0] * 4,
    },
    'Gripper_zikas': True,  # Open  Gripper
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

MORAD_home = [0, 0, 26.4]
MORAD_point1 = [13.565, 0.000, 19.461]
MORAD_point2 = [16.612, 0.000, 14.025]
MORAD_point3 = [-6.850, 1.208, 24.575]
MORAD_point4 = [-12.427, 1.526, 21.056]
MORAD_point5 = [-16.809, 0.587, 14.655]

ZIKAS_home = [0, 0, 26.4]
ZIKAS_point1 = [15.223, 0.000, 14.450]
ZIKAS_point2 = [14.937, -0.000, 5.682]
ZIKAS_point3 = [1.628, 11.587, 20.301]
ZIKAS_point4 = [2.963, 15.243, 14.352]
ZIKAS_point5 = [2.625, 14.888, 6.995]

present_pos = [18, 0, 8.4]
MORAD_points = [MORAD_point1, MORAD_point2, MORAD_point1, MORAD_point3, MORAD_point4, MORAD_point5, MORAD_point4,
                MORAD_home]
ZIKAS_points = [ZIKAS_point1, ZIKAS_point2, ZIKAS_point1, ZIKAS_point3, ZIKAS_point4, ZIKAS_point5, ZIKAS_point4,
                ZIKAS_home]

t = 1
N = 10
ts = t / (N - 1)

TIME = np.zeros(shape=(N - 2, 1))
zero = np.zeros(shape=(1, 3))
actual_pos = np.zeros(shape=(N - 2, 3))
for r in range(0, N - 2):
    a = r * ts
    TIME[r][0] = a

actual_speed = np.zeros(shape=(N - 2, 3))

while(1):
    if (robot_morad['start_morad']==1) & (robot_zikas['start_zikas']==0):


        for k in range(8):
            # morad_traj
            # main code
            SPEED_INDEX = 0
            if k == 0:
                theta0 = ik(MORAD_home)  # starting position
            else:
                theta0 = ik(MORAD_points[k - 1])
            print(theta0)
            DXL_GOAL_POSITION = ik(MORAD_points[k])
            print(DXL_GOAL_POSITION)

            [position, dxl_goal_sp, acc] = traj(np.rad2deg(theta0), np.rad2deg(DXL_GOAL_POSITION), t, N)

            DXL_GOAL_POSITION = np.rad2deg(DXL_GOAL_POSITION) * (1023 / 300)

            dxl_goal_speed = np.delete(dxl_goal_sp, 0, 0)
            dxl_goal_speed = np.delete(dxl_goal_speed, N - 2, 0)

            for i in range(N - 2):
                for j in range(3):
                    dxl_goal_speed[i][j] = (dxl_goal_speed[i][j] * 9.5493 * 9.2)  # hexa

            # Control table address

            start = time.perf_counter()
            while 1:
                for i in range(3):
                    # Allocate goal position value into byte array
                    param_1goal_position = [DXL_LOBYTE(round(DXL_GOAL_POSITION[i])),
                                            DXL_HIBYTE(round(DXL_GOAL_POSITION[i])),
                                            DXL_LOBYTE(round(dxl_goal_speed[SPEED_INDEX][i])),
                                            DXL_HIBYTE(round(dxl_goal_speed[SPEED_INDEX][i]))]

                    # Add Dynamixel#1 goal position value to the Syncwrite parameter storage
                    dxl_addparam_result = groupSyncWrite.addParam(DXL_MORAD_ID[i], param_1goal_position)
                    if dxl_addparam_result != True:
                        print("[ID:%03d] groupSyncWrite addparam failed" % DXL_MORAD_ID[i])
                        quit()

                # Syncwrite goal position
                dxl_comm_result = groupSyncWrite.txPacket()  # send at the same time for all motors - execute movement
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

                time.sleep(ts)

                for i in range(3):
                    data_read, result, error = packetHandler.read1ByteTxRx(portHandler, DXL_MORAD_ID[i],
                                                                           ADDR_Movement_Status)
                    if data_read == 1:
                        G_Var['Robot'][0]['Busy']['Value'] = 1
                        print('busy value= {}'.format(G_Var['Robot'][0]['Busy']['Value']))
                    elif data_read == 0:
                        G_Var['Robot'][0]['Busy']['Value'] = 0
                        print('busy value= {}'.format(G_Var['Robot'][0]['Busy']['Value']))

                # Clear syncwrite parameter storage
                groupSyncWrite.clearParam()

                SPEED_INDEX = SPEED_INDEX + 1
                print(SPEED_INDEX)
                if SPEED_INDEX == N - 2:
                    # time.sleep()
                    break

            robot_morad['points_morad'][k] = True
            finish = time.perf_counter()
            print(f'Finished in {round(finish - start, 2)} second(s)')

            # PICK
            if k == 1:
                # Write goal position
                dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_AX_ID[0],
                                                                          ADDR_AX_GOAL_SPEED_L,
                                                                          ax_goal_speed)
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))
                # Write goal position
                dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_AX_ID[0],
                                                                          ADDR_RX_GOAL_POSITION,
                                                                          MORAD_AX_GOAL_POS[0])
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))
                time.sleep(2)
                robot_morad['Gripper_morad'] = False



            # PLACE
            elif k == 5:
                # Write goal position
                dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_AX_ID[0],
                                                                          ADDR_AX_GOAL_SPEED_L,
                                                                          ax_goal_speed)
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))
                # Write goal position
                dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_AX_ID[0],
                                                                          ADDR_RX_GOAL_POSITION,
                                                                          MORAD_AX_GOAL_POS[1])
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))
                time.sleep(2)
                robot_morad['Gripper_morad'] = True
            time.sleep(.5)
        robot_morad['process_done_morad'] = 1

        read_R1_motors_sensors(portHandler, DXL_MORAD_ID, ADDR_RX_READINGS,packetHandler)
        break




    elif robot_morad['start_morad'] == 0 & robot_zikas['start_zikas'] == 0:

        for k in range(8):
            # main code
            SPEED_INDEX = 0
            if k == 0:
                theta0 = ik(ZIKAS_home)
            else:
                theta0 = ik(ZIKAS_points[k - 1])
            print(theta0)
            DXL_GOAL_POSITION = ik(ZIKAS_points[k])
            print(DXL_GOAL_POSITION)

            [position, dxl_goal_sp, acc] = traj(np.rad2deg(theta0), np.rad2deg(DXL_GOAL_POSITION), t, N)

            DXL_GOAL_POSITION = np.rad2deg(DXL_GOAL_POSITION) * (1023 / 300)

            dxl_goal_speed = np.delete(dxl_goal_sp, 0, 0)
            dxl_goal_speed = np.delete(dxl_goal_speed, N - 2, 0)

            for i in range(N - 2):
                for j in range(3):
                    dxl_goal_speed[i][j] = (dxl_goal_speed[i][j] * 9.5493 * 9.2)  # hexa

            # Control table address

            start = time.perf_counter()
            while 1:
                for i in range(3):
                    # Allocate goal position value into byte array
                    param_1goal_position = [DXL_LOBYTE(round(DXL_GOAL_POSITION[i])),
                                            DXL_HIBYTE(round(DXL_GOAL_POSITION[i])),
                                            DXL_LOBYTE(round(dxl_goal_speed[SPEED_INDEX][i])),
                                            DXL_HIBYTE(round(dxl_goal_speed[SPEED_INDEX][i]))]

                    # Add Dynamixel#1 goal position value to the Syncwrite parameter storage
                    dxl_addparam_result = groupSyncWrite.addParam(DXL_ZIKAS_ID[i], param_1goal_position)
                    if dxl_addparam_result != True:
                        print("[ID:%03d] groupSyncWrite addparam failed" % DXL_ZIKAS_ID[i])
                        quit()

                # Syncwrite goal position
                dxl_comm_result = groupSyncWrite.txPacket()  # send at the same time for all motors
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

                time.sleep(ts)

                for i in range(3):
                    data_read, result, error = packetHandler.read1ByteTxRx(portHandler, DXL_ZIKAS_ID[i],
                                                                           ADDR_Movement_Status)
                    if data_read == 1:
                        robot_zikas['busy_zikas'] = 1
                    elif data_read == 0:
                        robot_zikas['busy_zikas'] = 0

                # Clear syncwrite parameter storage
                groupSyncWrite.clearParam()

                SPEED_INDEX = SPEED_INDEX + 1
                print(SPEED_INDEX)
                if SPEED_INDEX == N - 2:
                    # time.sleep()
                    break
            robot_zikas['points_zikas'][k] = True
            finish = time.perf_counter()
            print(f'Finished in {round(finish - start, 2)} second(s)')

            # PICK
            if k == 1:
                # Write goal position
                dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_AX_ID[1],
                                                                          ADDR_AX_GOAL_SPEED_L,
                                                                          ax_goal_speed)
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))
                # Write goal position
                dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_AX_ID[1],
                                                                          ADDR_RX_GOAL_POSITION,
                                                                          ZIKAS_AX_GOAL_POS[0])
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))
                time.sleep(2)
                robot_zikas['Gripper_zikas'] = False


            # PLACE
            elif k == 5:
                # Write goal position
                dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_AX_ID[1],
                                                                          ADDR_AX_GOAL_SPEED_L,
                                                                          ax_goal_speed)
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))
                # Write goal position
                dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_AX_ID[1],
                                                                          ADDR_RX_GOAL_POSITION,
                                                                          ZIKAS_AX_GOAL_POS[1])
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))
                time.sleep(2)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

            time.sleep(.5)
            robot_zikas['Gripper_zikas'] = True

        robot_zikas['process_done_zikas'] = 1
        read_R1_motors_sensors(portHandler, DXL_ZIKAS_ID, ADDR_RX_READINGS, packetHandler)
        break
    else:
        break





print(robot_morad)
print(robot_zikas)
for i in range(8):
    # Disable Torque for each Dynamixel RX-64 Motor in Zikas Arm
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ALL_IDS[i], ADDR_RX_TORQUE_ENABLE,
                                                              TORQUE_DISABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    # Close port
portHandler.closePort()
# plt.show()
