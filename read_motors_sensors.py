from Diff import *
from dynamixel_sdk import*

def read_R1_motors_sensors(port,ID,addr,packetHandler):
    global G_Var
    for i in range(3):
        # read current POSITION
        dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(port, ID[i], addr[0])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        G_Var['Robot'][0]['Motors'][i]['Position']['Value'] = dxl_present_position * (300 / 1023)

        # SPEED
        dxl_present_speed, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(port, ID[i], addr[1])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        print("          Present Speed is :%03d m/s" % dxl_present_speed)
        G_Var['Robot'][0]['Motors'][i]['Velocity']['Value']= dxl_present_speed * 0.01138

        # LOAD
        dxl_present_load, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(port, ID[i], addr[2])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        print("          Present Load is :%03d Nm" % dxl_present_load)
        G_Var['Robot'][0]['Motors'][i]['Torque']['Value'] = dxl_present_load/1023*100

        # Temperature
        dxl_present_temperature, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(port, ID[i], addr[3])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        G_Var['Robot'][0]['Motors'][i]['Temp']['Value'] = dxl_present_temperature

        # VOLTAGE
        dxl_present_voltage, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(port, ID[i], addr[4])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        G_Var['Robot'][0]['Motors'][i]['Volt']['Value'] = dxl_present_voltage / 10





def read_R2_motors_sensors(port,ID,addr,packetHandler):
    global G_Var
    for i in range(3):
        # read current POSITION
        dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(port, ID[i],
                                                                                       addr[0])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        G_Var['Robot'][1]['Motors'][i]['Position']['Value'] = dxl_present_position * (300 / 1023)

        # SPEED
        dxl_present_speed, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(port, ID[i], addr[1])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        print("          Present Speed is :%03d m/s" % dxl_present_speed)
        G_Var['Robot'][1]['Motors'][i]['Velocity']['Value']= dxl_present_speed * 0.01138

        # LOAD
        dxl_present_load, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(port, ID[i], addr[2])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        print("          Present Load is :%03d Nm" % dxl_present_load)
        G_Var['Robot'][1]['Motors'][i]['Torque']['Value'] = dxl_present_load

        # Temperature
        dxl_present_temperature, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(port, ID[i], addr[3])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        G_Var['Robot'][1]['Motors'][i]['Temp']['Value'] = dxl_present_temperature

        # VOLTAGE
        dxl_present_voltage, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(port, ID[i], addr[4])
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        G_Var['Robot'][1]['Motors'][i]['Volt']['Value'] = dxl_present_voltage / 10




