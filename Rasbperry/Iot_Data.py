from Diff import * 

def iot_read_data(data_from_iot):
    global G_Var
    G_Var['HMI'][1]['IP'][0]['Value'] = data_from_iot[0][0]
    G_Var['HMI'][1]['IP'][1]['Value'] = data_from_iot[1][0]
    G_Var['HMI'][1]['IP'][2]['Value'] = data_from_iot[2][0]
    G_Var['HMI'][1]['IP'][3]['Value'] = data_from_iot[3][0]
    G_Var['HMI'][1]['Connect']['Value'] = data_from_iot[4][0]
    G_Var['HMI'][1]['Buttons'][0]['Name']['Value'] = data_from_iot[5][0]
    G_Var['HMI'][1]['Buttons'][0]['Val']['Value'] = data_from_iot[6][0]
    G_Var['HMI'][1]['Buttons'][1]['Name']['Value'] = data_from_iot[7][0]
    G_Var['HMI'][1]['Buttons'][1]['Val']['Value'] = data_from_iot[8][0]
    G_Var['HMI'][1]['Buttons'][2]['Name']['Value'] = data_from_iot[9][0]
    G_Var['HMI'][1]['Buttons'][2]['Val']['Value'] = data_from_iot[10][0]
    G_Var['HMI'][1]['Buttons'][3]['Name']['Value'] = data_from_iot[11][0]
    G_Var['HMI'][1]['Buttons'][3]['Val']['Value'] = data_from_iot[12][0]
    G_Var['HMI'][1]['Buttons'][4]['Name']['Value'] = data_from_iot[13][0]
    G_Var['HMI'][1]['Buttons'][4]['Val']['Value'] = data_from_iot[14][0]
    G_Var['HMI'][1]['Buttons'][5]['Name']['Value'] = data_from_iot[15][0]
    G_Var['HMI'][1]['Buttons'][5]['Val']['Value'] = data_from_iot[16][0]
    G_Var['HMI'][1]['Buttons'][6]['Name']['Value'] = data_from_iot[17][0]
    G_Var['HMI'][1]['Buttons'][6]['Val']['Value'] = data_from_iot[18][0]
    G_Var['HMI'][1]['Buttons'][7]['Name']['Value'] = data_from_iot[19][0]
    G_Var['HMI'][1]['Buttons'][7]['Val']['Value'] = data_from_iot[20][0]
    G_Var['HMI'][1]['Buttons'][8]['Name']['Value'] = data_from_iot[21][0]
    G_Var['HMI'][1]['Buttons'][8]['Val']['Value'] = data_from_iot[22][0]
    G_Var['HMI'][1]['Buttons'][9]['Name']['Value'] = data_from_iot[23][0]
    G_Var['HMI'][1]['Buttons'][9]['Val']['Value'] = data_from_iot[24][0]
    G_Var['HMI'][1]['Buttons'][10]['Name']['Value'] = data_from_iot[25][0]
    G_Var['HMI'][1]['Buttons'][10]['Val']['Value'] = data_from_iot[26][0]
    G_Var['HMI'][1]['Buttons'][11]['Name']['Value'] = data_from_iot[27][0]
    G_Var['HMI'][1]['Buttons'][11]['Val']['Value'] = data_from_iot[28][0]
    G_Var['HMI'][1]['Buttons'][12]['Name']['Value'] = data_from_iot[29][0]
    G_Var['HMI'][1]['Buttons'][12]['Val']['Value'] = data_from_iot[30][0]
    G_Var['HMI'][1]['Buttons'][13]['Name']['Value'] = data_from_iot[31][0]
    G_Var['HMI'][1]['Buttons'][13]['Val']['Value'] = data_from_iot[32][0]
    G_Var['HMI'][1]['Buttons'][14]['Name']['Value'] = data_from_iot[33][0]
    G_Var['HMI'][1]['Buttons'][14]['Val']['Value'] = data_from_iot[34][0]
    G_Var['HMI'][1]['Buttons'][15]['Name']['Value'] = data_from_iot[35][0]
    G_Var['HMI'][1]['Buttons'][15]['Val']['Value'] = data_from_iot[36][0]
    G_Var['HMI'][1]['Buttons'][16]['Name']['Value'] = data_from_iot[37][0]
    G_Var['HMI'][1]['Buttons'][16]['Val']['Value'] = data_from_iot[38][0]
    G_Var['HMI'][1]['Buttons'][17]['Name']['Value'] = data_from_iot[39][0]
    G_Var['HMI'][1]['Buttons'][17]['Val']['Value'] = data_from_iot[40][0]
    G_Var['HMI'][1]['Buttons'][18]['Name']['Value'] = data_from_iot[41][0]
    G_Var['HMI'][1]['Buttons'][18]['Val']['Value'] = data_from_iot[42][0]
    G_Var['HMI'][1]['Buttons'][19]['Name']['Value'] = data_from_iot[43][0]
    G_Var['HMI'][1]['Buttons'][19]['Val']['Value'] = data_from_iot[44][0]
    G_Var['HMI'][1]['Buttons'][20]['Name']['Value'] = data_from_iot[45][0]
    G_Var['HMI'][1]['Buttons'][20]['Val']['Value'] = data_from_iot[46][0]


def iot_write_data():
    global G_Var
    data ={ 'values': 
                    [[G_Var['Robot'][0]['ID']['Value']], 
                    [G_Var['Robot'][0]['Error']['Value']], 
                    [G_Var['Robot'][0]['Busy']['Value']], 
                    [G_Var['Robot'][0]['Start']['Value']], 
                    [G_Var['Robot'][0]['Done']['Value']], 
                    [G_Var['Robot'][0]['Gripper_control']['Value']], 
                    [G_Var['Robot'][0]['Gripper_Indicator']['Value']], 
                    [G_Var['Robot'][0]['Robot_Position']['Value']], 
                    [G_Var['Robot'][0]['Motors'][0]['ID']['Value']], 
                    [G_Var['Robot'][0]['Motors'][0]['Position']['Value']], 
                    [G_Var['Robot'][0]['Motors'][0]['Velocity']['Value']], 
                    [G_Var['Robot'][0]['Motors'][0]['Torque']['Value']], 
                    [G_Var['Robot'][0]['Motors'][0]['Temp']['Value']], 
                    [G_Var['Robot'][0]['Motors'][0]['Volt']['Value']], 
                    [G_Var['Robot'][0]['Motors'][1]['ID']['Value']], 
                    [G_Var['Robot'][0]['Motors'][1]['Position']['Value']], 
                    [G_Var['Robot'][0]['Motors'][1]['Velocity']['Value']], 
                    [G_Var['Robot'][0]['Motors'][1]['Torque']['Value']], 
                    [G_Var['Robot'][0]['Motors'][1]['Temp']['Value']], 
                    [G_Var['Robot'][0]['Motors'][1]['Volt']['Value']], 
                    [G_Var['Robot'][0]['Motors'][2]['ID']['Value']], 
                    [G_Var['Robot'][0]['Motors'][2]['Position']['Value']], 
                    [G_Var['Robot'][0]['Motors'][2]['Velocity']['Value']], 
                    [G_Var['Robot'][0]['Motors'][2]['Torque']['Value']], 
                    [G_Var['Robot'][0]['Motors'][2]['Temp']['Value']], 
                    [G_Var['Robot'][0]['Motors'][2]['Volt']['Value']], 
                    [G_Var['Robot'][1]['ID']['Value']], 
                    [G_Var['Robot'][1]['Error']['Value']], 
                    [G_Var['Robot'][1]['Busy']['Value']], 
                    [G_Var['Robot'][1]['Start']['Value']], 
                    [G_Var['Robot'][1]['Done']['Value']], 
                    [G_Var['Robot'][1]['Gripper_control']['Value']], 
                    [G_Var['Robot'][1]['Gripper_Indicator']['Value']], 
                    [G_Var['Robot'][1]['Robot_Position']['Value']], 
                    [G_Var['Robot'][1]['Motors'][0]['ID']['Value']], 
                    [G_Var['Robot'][1]['Motors'][0]['Position']['Value']], 
                    [G_Var['Robot'][1]['Motors'][0]['Velocity']['Value']], 
                    [G_Var['Robot'][1]['Motors'][0]['Torque']['Value']], 
                    [G_Var['Robot'][1]['Motors'][0]['Temp']['Value']], 
                    [G_Var['Robot'][1]['Motors'][0]['Volt']['Value']], 
                    [G_Var['Robot'][1]['Motors'][1]['ID']['Value']], 
                    [G_Var['Robot'][1]['Motors'][1]['Position']['Value']], 
                    [G_Var['Robot'][1]['Motors'][1]['Velocity']['Value']], 
                    [G_Var['Robot'][1]['Motors'][1]['Torque']['Value']], 
                    [G_Var['Robot'][1]['Motors'][1]['Temp']['Value']], 
                    [G_Var['Robot'][1]['Motors'][1]['Volt']['Value']], 
                    [G_Var['Robot'][1]['Motors'][2]['ID']['Value']], 
                    [G_Var['Robot'][1]['Motors'][2]['Position']['Value']], 
                    [G_Var['Robot'][1]['Motors'][2]['Velocity']['Value']], 
                    [G_Var['Robot'][1]['Motors'][2]['Torque']['Value']], 
                    [G_Var['Robot'][1]['Motors'][2]['Temp']['Value']], 
                    [G_Var['Robot'][1]['Motors'][2]['Volt']['Value']], 
                    [G_Var['Raspberry'][0]['Error']['Value']], 
                    [G_Var['Raspberry'][0]['Ready']['Value']], 
                    [G_Var['Raspberry'][0]['IP'][0]['Value']], 
                    [G_Var['Raspberry'][0]['IP'][1]['Value']], 
                    [G_Var['Raspberry'][0]['IP'][2]['Value']], 
                    [G_Var['Raspberry'][0]['IP'][3]['Value']], 
                    [G_Var['PLC'][0]['Name']['Value']], 
                    [G_Var['PLC'][0]['IP'][0]['Value']], 
                    [G_Var['PLC'][0]['IP'][1]['Value']], 
                    [G_Var['PLC'][0]['IP'][2]['Value']], 
                    [G_Var['PLC'][0]['IP'][3]['Value']], 
                    [G_Var['PLC'][0]['Connect']['Value']], 
                    [G_Var['PLC'][0]['Automatic']['Value']], 
                    [G_Var['PLC'][0]['IoT_Allow']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][0]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][0]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][1]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][1]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][2]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][2]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][3]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][3]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][4]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][4]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][5]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][5]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][6]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][6]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][7]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][7]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][8]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][8]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][9]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][9]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][10]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][10]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][11]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][11]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][12]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][12]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][13]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Inputs'][13]['Value']['Value']], 
                    [G_Var['PLC'][0]['Analog_Inputs'][0]['Name']['Value']], 
                    [G_Var['PLC'][0]['Analog_Inputs'][0]['Value']['Value']], 
                    [G_Var['PLC'][0]['Analog_Inputs'][0]['Index']['Value']], 
                    [G_Var['PLC'][0]['Analog_Inputs'][1]['Name']['Value']], 
                    [G_Var['PLC'][0]['Analog_Inputs'][1]['Value']['Value']], 
                    [G_Var['PLC'][0]['Analog_Inputs'][1]['Index']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][0]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][0]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][0]['Direction']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][1]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][1]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][1]['Direction']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][2]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][2]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][2]['Direction']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][3]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][3]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][3]['Direction']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][4]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][4]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][4]['Direction']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][5]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][5]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][5]['Direction']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][6]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][6]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][6]['Direction']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][7]['Name']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][7]['Value']['Value']], 
                    [G_Var['PLC'][0]['Digital_Outputs'][7]['Direction']['Value']], 
                    [G_Var['IoT'][0]['Name']['Value']], 
                    [G_Var['IoT'][0]['Connect']['Value']], 
                    [G_Var['HMI'][0]['IP'][0]['Value']], 
                    [G_Var['HMI'][0]['IP'][1]['Value']], 
                    [G_Var['HMI'][0]['IP'][2]['Value']], 
                    [G_Var['HMI'][0]['IP'][3]['Value']], 
                    [G_Var['HMI'][0]['Connect']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][0]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][0]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][1]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][1]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][2]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][2]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][3]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][3]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][4]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][4]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][5]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][5]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][6]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][6]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][7]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][7]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][8]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][8]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][9]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][9]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][10]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][10]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][11]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][11]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][12]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][12]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][13]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][13]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][14]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][14]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][15]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][15]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][16]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][16]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][17]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][17]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][18]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][18]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][19]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][19]['Val']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][20]['Name']['Value']], 
                    [G_Var['HMI'][0]['Buttons'][20]['Val']['Value']], ]}

    return data