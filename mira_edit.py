from dynamixel_sdk import *  # Uses Dynamixel SDK library
import time  # for trajectory timing
from Trajectory1 import *  # trajectory functions
import numpy as np

ADDR_RX_TORQUE_ENABLE = 24
ADDR_RX_PRESENT_POSITION = 36
ADDR_RX_PRESENT_SPEED = 38
ADDR_RX_PRESENT_LOAD = 40
ADDR_RX_PRESENT_TEMPERATURE = 43
ADDR_RX_PRESENT_VOLTAGE = 42
ADDR_RX_GOAL_POSITION = 30
ADDR_AX_GOAL_SPEED_L = 32

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
ZIKAS_AX_GOAL_POS = [580, 640]  # pick and place thetas for ax 8


home_1 = [0, 0, 26.4]
lift_off1 = [13.565, 0.000, 19.461]
pick1 = [16.612, 0.000, 14.025]
via_1_r1 =  [0, 0, 26.4]
via_2_r1 = [-6.850, 1.208, 24.575]
set_down_1 = [-12.427, 1.526, 21.056]
place_1 = [-16.809, 0.587, 14.655]

home_2 = [0.474, -0.412, 26.389]
lift_off2 = [2.963, 15.243, 14.352]
pick2 = [2.625, 14.888, 6.995]
via_1_r2 = [0.474, -0.412, 26.389]
via_2_r2 = [1.628, 11.587, 20.301]

set_down_2 = [15.223, 0.000, 14.450]
place_2 = [14.937, -0.000, 5.682]

present_pos = [18, 0, 8.4]
MORAD_points = [lift_off1, pick1, lift_off1, via_1_r1, via_2_r1, set_down_1, place_1,set_down_1,
                home_1]
ZIKAS_points = [lift_off2, pick2, lift_off2, via_1_r2,via_2_r2, set_down_2, place_2, set_down_2,
                home_2]
"""
t =[0] *8
N = 10

ts = t / (N - 1)
"""
t = [1, 0.7, 0.7, 1, 1.5, 0.7, 0.7, 0.7, 1,1]
N = 10
ts = [0] * 9
for i in range(9):
    ts[i] = t[i] / (N - 1)

TIME = np.zeros(shape=(N - 2, 1))
zero = np.zeros(shape=(1, 3))
actual_pos = np.zeros(shape=(N - 2, 3))
for r in range(0, N - 2):
    a = r * ts[r]
    TIME[r][0] = a

actual_speed = np.zeros(shape=(N - 2, 3))

for k in range(9):
    # morad_traj


    start = time.perf_counter()
    theta0 = ik(MORAD_points[k - 1])

    DXL_GOAL_POSITION = ik(MORAD_points[k])


    [position, dxl_goal_sp, acc] = traj(theta0,DXL_GOAL_POSITION, t[k], N)

    DXL_GOAL_POSITION = DXL_GOAL_POSITION * int(1023 / 300)

    dxl_goal_speed = np.delete(dxl_goal_sp, 0, 0)
    dxl_goal_speed = np.delete(dxl_goal_speed, N - 2, 0)

    for i in range(N - 2):
        for j in range(3):
            dxl_goal_speed[i][j] = (dxl_goal_speed[i][j] * 9.5493 * 9.2)  # hexa

    # Control table address

    end=time.perf_counter()
    print(end-start)
""" 
           # Add Dynamixel#1 goal position value to the Syncwrite parameter storage
            dxl_addparam_result = groupSyncWrite.addParam(DXL_MORAD_ID[i], param_1goal_position)
            if dxl_addparam_result != True:
                print("[ID:%03d] groupSyncWrite addparam failed" % DXL_MORAD_ID[i])
                quit()

        # Syncwrite goal position
        dxl_comm_result = groupSyncWrite.txPacket()  # send at the same time for all motors - execute movement
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

        time.sleep(ts[k])

        for i in range(3):
            dxl_present_speed, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_MORAD_ID[i],
                                                                                        ADDR_RX_PRESENT_SPEED)

            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            if dxl_present_speed >= 1000:
                dxl_present_speed = dxl_present_speed & 0XFF
            else:
                dxl_present_speed = dxl_present_speed
            goal_speed = dxl_goal_speed[SPEED_INDEX][i] / (9.5493 * 9.2)
            present_speed = dxl_present_speed / (9.5493 * 9.2)
            actual_speed[SPEED_INDEX][i] = present_speed  # matrix of actual speeds
            print("[ID:%03d] GoalSpeed:%03d  PresSpeed:%03d RPM" % (DXL_MORAD_ID[i], goal_speed, present_speed))

            # Read present position
            dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_MORAD_ID[i],
                                                                                           ADDR_RX_PRESENT_POSITION)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            goal_pos = position[SPEED_INDEX][i]
            present_pos = (300 / 1023) * dxl_present_position
            actual_pos[SPEED_INDEX][i] = present_pos
            print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_MORAD_ID[i], goal_pos, present_pos))

        # Clear syncwrite parameter storage
        groupSyncWrite.clearParam()

        SPEED_INDEX = SPEED_INDEX + 1
        print(SPEED_INDEX)
        if SPEED_INDEX == N - 2:
            # time.sleep()
            break

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
    # grasp
    if k == 1:
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_AX_ID[0], ADDR_AX_GOAL_SPEED_L,
                                                                  ax_goal_speed)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_AX_ID[0], ADDR_RX_GOAL_POSITION,
                                                                  MORAD_AX_GOAL_POS[0])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        time.sleep(2)



    # release
    elif k == 6:
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_AX_ID[0], ADDR_AX_GOAL_SPEED_L,
                                                                  ax_goal_speed)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        # Write goal position
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_AX_ID[0], ADDR_RX_GOAL_POSITION,
                                                                  MORAD_AX_GOAL_POS[1])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        time.sleep(2)
    time.sleep(0.5)

# zikas_traj

for k in range(9):
    # main code
    SPEED_INDEX = 0
    if k == 0:
        theta0 = ik(home_2)
        # at home position return to home position
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

    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    else:
        theta0 = ik(ZIKAS_points[k - 1])
    print(theta0)
    DXL_GOAL_POSITION = ik(ZIKAS_points[k])
    print(DXL_GOAL_POSITION)

    [position, dxl_goal_sp, acc] = traj(theta0, DXL_GOAL_POSITION, t[k], N)

    DXL_GOAL_POSITION = DXL_GOAL_POSITION * int(1023 / 300)

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

        time.sleep(ts[k])

        for i in range(3):
            dxl_present_speed, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler,
                                                                                        DXL_ZIKAS_ID[i],
                                                                                        ADDR_RX_PRESENT_SPEED)

            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            if dxl_present_speed >= 1000:
                dxl_present_speed = dxl_present_speed & 0XFF
            else:
                dxl_present_speed = dxl_present_speed
            goal_speed = dxl_goal_speed[SPEED_INDEX][i] / (9.5493 * 9.2)
            present_speed = dxl_present_speed / (9.5493 * 9.2)
            actual_speed[SPEED_INDEX][i] = present_speed  # matrix of actual speeds
            print("[ID:%03d] GoalSpeed:%03d  PresSpeed:%03d RPM" % (DXL_ZIKAS_ID[i], goal_speed, present_speed))

            # Read present position
            dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler,
                                                                                           DXL_ZIKAS_ID[i],
                                                                                           ADDR_RX_PRESENT_POSITION)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))
            goal_pos = position[SPEED_INDEX][i]
            present_pos = (300 / 1023) * dxl_present_position
            actual_pos[SPEED_INDEX][i] = present_pos
            print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL_ZIKAS_ID[i], goal_pos, present_pos))

        # Clear syncwrite parameter storage
        groupSyncWrite.clearParam()

        SPEED_INDEX = SPEED_INDEX + 1
        print(SPEED_INDEX)
        if SPEED_INDEX == N - 2:
            # time.sleep()
            break

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')

    # grasp
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


    # release
    elif k == 6:
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
"""