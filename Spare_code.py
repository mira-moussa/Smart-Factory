
from Trajectory1 import *    # trajectory functions
import numpy as np
import snap7
from read_motors_sensors import *
#from Master import *
#PLC_start()
#db=plc.db_read(1, START_ADDRESS, 1)
#start=snap7.util.get_int(db,0)
start=1

ADDR_RX_TORQUE_ENABLE = 24
ADDR_RX_PRESENT_POSITION = 36
ADDR_RX_PRESENT_SPEED = 38
ADDR_RX_PRESENT_LOAD = 40
ADDR_RX_PRESENT_TEMPERATURE = 43
ADDR_RX_PRESENT_VOLTAGE = 42
ADDR_RX_GOAL_POSITION = 30
ADDR_AX_GOAL_SPEED_L = 32

LEN_RX_GOAL_POSITION = 4

PROTOCOL_VERSION = 1.0    # Protocol version
BAUDRATE = 57600          # Dynamixel default baudrate : 57600
DEVICENAME = 'COM5'       # Check which port is being used on your controller
# DEVICENAME = '/dev/ttyUSB0'

TORQUE_ENABLE = 1         # Value for enabling the torque
TORQUE_DISABLE = 0        # Value for disabling the torque
ID_INDEX = 0              # index for iteration of different dxl Id
SPEED_INDEX = 0           # index for looping over different speeds

Robot_1_ID = [1, 2, 3]    # used dxl ID
Robot_2_ID = [5, 6, 7]    # used dxl ID
DXL_AX_ID = [4, 8]
DXL_ALL_IDS = [1, 2, 3, 4, 5, 6, 7, 8]  # used dxl ID
ADDR_RX_READINGS= [36, 38, 40, 43, 42, 46]    # pos,speed,load,temp,volt
ax_goal_speed = 100                     # AX_speed
Robot_1_ax_Goal_pos = [880, 980]        # pick and place thetas for ax 7
Robot_2_ax_Goal_Pos = [470, 640]        # pick and place thetas for ax 8
G_Var['Robot'][1]['Start']['Value'] = 1
G_Var['Robot'][0]['Start']['Value'] = 0
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
    quit()

# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
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

home_1 = [0.161, 0.003, 26.399]
lift_off1 = [10.520, 0.184, 21.645]
pick1 = [16.383, 1.433, 14.283]
via_1_r1 = [0, 0, 26.4]
via_2_r1 = [-6.850, 1.208, 24.575]
set_down_1 = [-12.427, 1.526, 21.056]
place_1 = [-14.620, 1.022, 18.849]

home_2 = [-0.749, 3.524, 26.018]
lift_off2 = [-3.497, 16.452, 12.961]
pick2 = [-4.296, 17.230, 9.268]
via_1_r2 = [4.835,6.906,21.514]
via_2_r2 = [8.429,0.147,21.514]
set_down_2 = [16.618,0.580,12.261]
place_2 = [16.846,0.588,11.092]

present_pos = [18, 0, 8.4]
Robot_1_Points = [lift_off1, pick1, lift_off1, via_1_r1, via_2_r1, set_down_1, place_1,set_down_1, home_1]
Robot_2_Points = [lift_off2, pick2, lift_off2, via_1_r2,via_2_r2, set_down_2, place_2, set_down_2, home_2]

# global G_Var
t = [0.6, 0.6, 0.6, 0.6, 1, 0.6, 0.6, 0.6, 1.5, 1]
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
counter=0
while True:

    if (counter < 1):
        print("Robot one %i" %(counter))
        G_Var['Robot'][0]['Busy']['Value'] = 1
        G_Var['Robot'][0]['Done']['Value'] = 0
        G_Var['Robot'][0]['Gripper_Indicator']['Value']=True

        print(G_Var)

        for k in range(9):
            G_Var['Robot'][0]['Robot_Position']['Value'] = k
            # Robot_1_trajectory
            SPEED_INDEX = 0
            if k == 0:
                theta0 = ik(home_1)  # starting position
                # Write goal position
                dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_AX_ID[0], ADDR_AX_GOAL_SPEED_L,
                                                                          ax_goal_speed)
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))
                # Write goal position
                dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_AX_ID[0], ADDR_RX_GOAL_POSITION,
                                                                          Robot_1_ax_Goal_pos[1])
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))
            else:
                theta0 = ik(Robot_1_Points[k - 1])
            DXL_GOAL_POSITION = ik(Robot_1_Points[k])
            [position, dxl_goal_sp, acc] = traj(np.rad2deg(theta0), np.rad2deg(DXL_GOAL_POSITION), t[k], N)

            DXL_GOAL_POSITION = np.rad2deg(DXL_GOAL_POSITION )* (1023 / 300)

            dxl_goal_speed = np.delete(dxl_goal_sp, 0, 0)
            dxl_goal_speed = np.delete(dxl_goal_speed, N - 2, 0)

            for i in range(N - 2):
                for j in range(3):
                    dxl_goal_speed[i][j] = (dxl_goal_speed[i][j] * 9.5493 * 9.2)  # hexa

            # Control table address

            start_time = time.perf_counter()
            while 1:
                for i in range(3):
                    # Allocate goal position value into byte array
                    param_1goal_position = [DXL_LOBYTE(round(DXL_GOAL_POSITION[i])),
                                            DXL_HIBYTE(round(DXL_GOAL_POSITION[i])),
                                            DXL_LOBYTE(round(dxl_goal_speed[SPEED_INDEX][i])),
                                            DXL_HIBYTE(round(dxl_goal_speed[SPEED_INDEX][i]))]

                    # Add Dynamixel#1 goal position value to the Syncwrite parameter storage
                    dxl_addparam_result = groupSyncWrite.addParam(Robot_1_ID[i], param_1goal_position)
                    if dxl_addparam_result != True:
                        print("[ID:%03d] groupSyncWrite addparam failed" % Robot_1_ID[i])
                        quit()

                # Syncwrite goal position
                dxl_comm_result = groupSyncWrite.txPacket()  # send at the same time for all motors - execute movement
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

                time.sleep(ts[k])

                # Clear syncwrite parameter storage
                groupSyncWrite.clearParam()

                SPEED_INDEX = SPEED_INDEX + 1
                print(SPEED_INDEX)
                if SPEED_INDEX == N - 2:
                    # time.sleep()
                    break

            read_R1_motors_sensors(portHandler, Robot_1_ID, ADDR_RX_READINGS, packetHandler)
            print(G_Var['Robot'][0])
            finish = time.perf_counter()
            print(f'Finished in {round(finish - start_time, 2)} second(s)')

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
                                                                          Robot_1_ax_Goal_pos[0])
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))
                G_Var['Robot'][0]['Gripper_Indicator']['Value'] = False
                time.sleep(1)



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
                                                                          Robot_1_ax_Goal_pos[1])
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))
                G_Var['Robot'][0]['Gripper_Indicator']['Value'] = True
                time.sleep(1)
            elif k == 8:
                G_Var['Robot'][0]['Busy']['Value'] = 0
                G_Var['Robot'][0]['Done']['Value'] = 1
                print(G_Var['Robot'][0])
            time.sleep(0.1)
        counter += 1
    elif (counter == 1):
        print('firtst robot second')
        G_Var['Robot'][1]['Busy']['Value'] = 1
        G_Var['Robot'][1]['Done']['Value'] = 0
        G_Var['Robot'][1]['Gripper_Indicator']['Value'] = True
        # zikas_traj
        for k in range(9):
            G_Var['Robot'][1]['Robot_Position']['Value'] = k
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
                                                                          Robot_2_ax_Goal_Pos[1])
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                   print("%s" % packetHandler.getRxPacketError(dxl_error))

            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            else:
                theta0 = ik(Robot_2_Points[k - 1])

            DXL_GOAL_POSITION = ik(Robot_2_Points[k])
            print(DXL_GOAL_POSITION)

            [position, dxl_goal_sp, acc] = traj(np.rad2deg(theta0), np.rad2deg(DXL_GOAL_POSITION), t[k], N)

            DXL_GOAL_POSITION = np.rad2deg(DXL_GOAL_POSITION) * (1023 / 300)

            dxl_goal_speed = np.delete(dxl_goal_sp, 0, 0)
            dxl_goal_speed = np.delete(dxl_goal_speed, N - 2, 0)

            for i in range(N - 2):
                for j in range(3):
                    dxl_goal_speed[i][j] = (dxl_goal_speed[i][j] * 9.5493 * 9.2)  # hexa

            # Control table address

            start_time = time.perf_counter()
            while 1:
                for i in range(3):
                    # Allocate goal position value into byte array
                    param_1goal_position = [DXL_LOBYTE(round(DXL_GOAL_POSITION[i])),
                                            DXL_HIBYTE(round(DXL_GOAL_POSITION[i])),
                                            DXL_LOBYTE(round(dxl_goal_speed[SPEED_INDEX][i])),
                                            DXL_HIBYTE(round(dxl_goal_speed[SPEED_INDEX][i]))]

                    # Add Dynamixel#1 goal position value to the Syncwrite parameter storage
                    dxl_addparam_result = groupSyncWrite.addParam(Robot_2_ID[i], param_1goal_position)
                    if dxl_addparam_result != True:
                        print("[ID:%03d] groupSyncWrite addparam failed" % Robot_2_ID[i])
                        quit()

                # Syncwrite goal position
                dxl_comm_result = groupSyncWrite.txPacket()  # send at the same time for all motors
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

                time.sleep(ts[k])



                groupSyncWrite.clearParam()                 # Clear syncwrite parameter storage

                SPEED_INDEX = SPEED_INDEX + 1
                print(SPEED_INDEX)
                if SPEED_INDEX == N - 2:
                    # time.sleep()
                    break

            finish = time.perf_counter()
            print(f'Finished in {round(finish - start_time, 2)} second(s)')
            read_R2_motors_sensors(portHandler, Robot_2_ID, ADDR_RX_READINGS, packetHandler)
            print(G_Var['Robot'][1])
            # grasp
            if k == 1:
                G_Var['Robot'][1]['Gripper_Indicator']['Value'] = False
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
                                                                          Robot_2_ax_Goal_Pos[0])
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))
                time.sleep(1)


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
                                                                          Robot_2_ax_Goal_Pos[1])
                if dxl_comm_result != COMM_SUCCESS:
                    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
                elif dxl_error != 0:
                    print("%s" % packetHandler.getRxPacketError(dxl_error))
                G_Var['Robot'][1]['Gripper_Indicator']['Value'] = True
                time.sleep(1)

            elif k == 8:
                G_Var['Robot'][1]['Busy']['Value'] = 0
                G_Var['Robot'][1]['Done']['Value'] = 1
                print(G_Var['Robot'])
            time.sleep(0.1)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        break



for i in range(8):
    # Disable Torque for each Dynamixel RX-64 Motor in Zikas Arm
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ALL_IDS[i], ADDR_RX_TORQUE_ENABLE,
                                                              TORQUE_DISABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
portHandler.closePort()          # Close port

