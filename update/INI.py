from Diff import *

def INI():
    global G_Var

    G_Var['Robot'][0]['ID']['Value'] = 0;	G_Var['Robot'][0]['ID']['Address'] = 0;	G_Var['Robot'][0]['ID']['Start_bit'] = 0
    G_Var['Robot'][0]['Error']['Value'] = False;	G_Var['Robot'][0]['Error']['Address'] = 2;	G_Var['Robot'][0]['Error']['Start_bit'] = 0
    G_Var['Robot'][0]['Busy']['Value'] = False;	G_Var['Robot'][0]['Busy']['Address'] = 2;	G_Var['Robot'][0]['Busy']['Start_bit'] = 1
    G_Var['Robot'][0]['Start']['Value'] = False;	G_Var['Robot'][0]['Start']['Address'] = 2;	G_Var['Robot'][0]['Start']['Start_bit'] = 2
    G_Var['Robot'][0]['Done']['Value'] = False;	G_Var['Robot'][0]['Done']['Address'] = 2;	G_Var['Robot'][0]['Done']['Start_bit'] = 3
    G_Var['Robot'][0]['Gripper_control']['Value'] = False;	G_Var['Robot'][0]['Gripper_control']['Address'] = 2;	G_Var['Robot'][0]['Gripper_control']['Start_bit'] = 4
    G_Var['Robot'][0]['Gripper_Indicator']['Value'] = False;	G_Var['Robot'][0]['Gripper_Indicator']['Address'] = 2;	G_Var['Robot'][0]['Gripper_Indicator']['Start_bit'] = 5
    G_Var['Robot'][0]['Robot_Position']['Value'] = 0;	G_Var['Robot'][0]['Robot_Position']['Address'] = 4;	G_Var['Robot'][0]['Robot_Position']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][0]['ID']['Value'] = 0;	G_Var['Robot'][0]['Motors'][0]['ID']['Address'] = 6;	G_Var['Robot'][0]['Motors'][0]['ID']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][0]['Position']['Value'] = 0;	G_Var['Robot'][0]['Motors'][0]['Position']['Address'] = 8;	G_Var['Robot'][0]['Motors'][0]['Position']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][0]['Velocity']['Value'] = 0;	G_Var['Robot'][0]['Motors'][0]['Velocity']['Address'] = 12;	G_Var['Robot'][0]['Motors'][0]['Velocity']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][0]['Torque']['Value'] = 0;	G_Var['Robot'][0]['Motors'][0]['Torque']['Address'] = 16;	G_Var['Robot'][0]['Motors'][0]['Torque']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][0]['Temp']['Value'] = 0;	G_Var['Robot'][0]['Motors'][0]['Temp']['Address'] = 20;	G_Var['Robot'][0]['Motors'][0]['Temp']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][0]['Volt']['Value'] = 0;	G_Var['Robot'][0]['Motors'][0]['Volt']['Address'] = 24;	G_Var['Robot'][0]['Motors'][0]['Volt']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][1]['ID']['Value'] = 1;	G_Var['Robot'][0]['Motors'][1]['ID']['Address'] = 28;	G_Var['Robot'][0]['Motors'][1]['ID']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][1]['Position']['Value'] = 0;	G_Var['Robot'][0]['Motors'][1]['Position']['Address'] = 30;	G_Var['Robot'][0]['Motors'][1]['Position']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][1]['Velocity']['Value'] = 0;	G_Var['Robot'][0]['Motors'][1]['Velocity']['Address'] = 34;	G_Var['Robot'][0]['Motors'][1]['Velocity']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][1]['Torque']['Value'] = 0;	G_Var['Robot'][0]['Motors'][1]['Torque']['Address'] = 38;	G_Var['Robot'][0]['Motors'][1]['Torque']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][1]['Temp']['Value'] = 0;	G_Var['Robot'][0]['Motors'][1]['Temp']['Address'] = 42;	G_Var['Robot'][0]['Motors'][1]['Temp']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][1]['Volt']['Value'] = 0;	G_Var['Robot'][0]['Motors'][1]['Volt']['Address'] = 46;	G_Var['Robot'][0]['Motors'][1]['Volt']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][2]['ID']['Value'] = 2;	G_Var['Robot'][0]['Motors'][2]['ID']['Address'] = 50;	G_Var['Robot'][0]['Motors'][2]['ID']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][2]['Position']['Value'] = 0;	G_Var['Robot'][0]['Motors'][2]['Position']['Address'] = 52;	G_Var['Robot'][0]['Motors'][2]['Position']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][2]['Velocity']['Value'] = 0;	G_Var['Robot'][0]['Motors'][2]['Velocity']['Address'] = 56;	G_Var['Robot'][0]['Motors'][2]['Velocity']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][2]['Torque']['Value'] = 0;	G_Var['Robot'][0]['Motors'][2]['Torque']['Address'] = 60;	G_Var['Robot'][0]['Motors'][2]['Torque']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][2]['Temp']['Value'] = 0;	G_Var['Robot'][0]['Motors'][2]['Temp']['Address'] = 64;	G_Var['Robot'][0]['Motors'][2]['Temp']['Start_bit'] = 0
    G_Var['Robot'][0]['Motors'][2]['Volt']['Value'] = 0;	G_Var['Robot'][0]['Motors'][2]['Volt']['Address'] = 68;	G_Var['Robot'][0]['Motors'][2]['Volt']['Start_bit'] = 0
    G_Var['Robot'][1]['ID']['Value'] = 0;	G_Var['Robot'][1]['ID']['Address'] = 72;	G_Var['Robot'][1]['ID']['Start_bit'] = 0
    G_Var['Robot'][1]['Error']['Value'] = False;	G_Var['Robot'][1]['Error']['Address'] = 74;	G_Var['Robot'][1]['Error']['Start_bit'] = 0
    G_Var['Robot'][1]['Busy']['Value'] = False;	G_Var['Robot'][1]['Busy']['Address'] = 74;	G_Var['Robot'][1]['Busy']['Start_bit'] = 1
    G_Var['Robot'][1]['Start']['Value'] = False;	G_Var['Robot'][1]['Start']['Address'] = 74;	G_Var['Robot'][1]['Start']['Start_bit'] = 2
    G_Var['Robot'][1]['Done']['Value'] = False;	G_Var['Robot'][1]['Done']['Address'] = 74;	G_Var['Robot'][1]['Done']['Start_bit'] = 3
    G_Var['Robot'][1]['Gripper_control']['Value'] = False;	G_Var['Robot'][1]['Gripper_control']['Address'] = 74;	G_Var['Robot'][1]['Gripper_control']['Start_bit'] = 4
    G_Var['Robot'][1]['Gripper_Indicator']['Value'] = False;	G_Var['Robot'][1]['Gripper_Indicator']['Address'] = 74;	G_Var['Robot'][1]['Gripper_Indicator']['Start_bit'] = 5
    G_Var['Robot'][1]['Robot_Position']['Value'] = 0;	G_Var['Robot'][1]['Robot_Position']['Address'] = 76;	G_Var['Robot'][1]['Robot_Position']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][0]['ID']['Value'] = 0;	G_Var['Robot'][1]['Motors'][0]['ID']['Address'] = 78;	G_Var['Robot'][1]['Motors'][0]['ID']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][0]['Position']['Value'] = 0;	G_Var['Robot'][1]['Motors'][0]['Position']['Address'] = 80;	G_Var['Robot'][1]['Motors'][0]['Position']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][0]['Velocity']['Value'] = 0;	G_Var['Robot'][1]['Motors'][0]['Velocity']['Address'] = 84;	G_Var['Robot'][1]['Motors'][0]['Velocity']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][0]['Torque']['Value'] = 0;	G_Var['Robot'][1]['Motors'][0]['Torque']['Address'] = 88;	G_Var['Robot'][1]['Motors'][0]['Torque']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][0]['Temp']['Value'] = 0;	G_Var['Robot'][1]['Motors'][0]['Temp']['Address'] = 92;	G_Var['Robot'][1]['Motors'][0]['Temp']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][0]['Volt']['Value'] = 0;	G_Var['Robot'][1]['Motors'][0]['Volt']['Address'] = 96;	G_Var['Robot'][1]['Motors'][0]['Volt']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][1]['ID']['Value'] = 1;	G_Var['Robot'][1]['Motors'][1]['ID']['Address'] = 100;	G_Var['Robot'][1]['Motors'][1]['ID']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][1]['Position']['Value'] = 0;	G_Var['Robot'][1]['Motors'][1]['Position']['Address'] = 102;	G_Var['Robot'][1]['Motors'][1]['Position']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][1]['Velocity']['Value'] = 0;	G_Var['Robot'][1]['Motors'][1]['Velocity']['Address'] = 106;	G_Var['Robot'][1]['Motors'][1]['Velocity']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][1]['Torque']['Value'] = 0;	G_Var['Robot'][1]['Motors'][1]['Torque']['Address'] = 110;	G_Var['Robot'][1]['Motors'][1]['Torque']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][1]['Temp']['Value'] = 0;	G_Var['Robot'][1]['Motors'][1]['Temp']['Address'] = 114;	G_Var['Robot'][1]['Motors'][1]['Temp']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][1]['Volt']['Value'] = 0;	G_Var['Robot'][1]['Motors'][1]['Volt']['Address'] = 118;	G_Var['Robot'][1]['Motors'][1]['Volt']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][2]['ID']['Value'] = 2;	G_Var['Robot'][1]['Motors'][2]['ID']['Address'] = 122;	G_Var['Robot'][1]['Motors'][2]['ID']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][2]['Position']['Value'] = 0;	G_Var['Robot'][1]['Motors'][2]['Position']['Address'] = 124;	G_Var['Robot'][1]['Motors'][2]['Position']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][2]['Velocity']['Value'] = 0;	G_Var['Robot'][1]['Motors'][2]['Velocity']['Address'] = 128;	G_Var['Robot'][1]['Motors'][2]['Velocity']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][2]['Torque']['Value'] = 0;	G_Var['Robot'][1]['Motors'][2]['Torque']['Address'] = 132;	G_Var['Robot'][1]['Motors'][2]['Torque']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][2]['Temp']['Value'] = 0;	G_Var['Robot'][1]['Motors'][2]['Temp']['Address'] = 136;	G_Var['Robot'][1]['Motors'][2]['Temp']['Start_bit'] = 0
    G_Var['Robot'][1]['Motors'][2]['Volt']['Value'] = 0;	G_Var['Robot'][1]['Motors'][2]['Volt']['Address'] = 140;	G_Var['Robot'][1]['Motors'][2]['Volt']['Start_bit'] = 0
    G_Var['Raspberry'][0]['Error']['Value'] = False;	G_Var['Raspberry'][0]['Error']['Address'] = 144;	G_Var['Raspberry'][0]['Error']['Start_bit'] = 0
    G_Var['Raspberry'][0]['Ready']['Value'] = False;	G_Var['Raspberry'][0]['Ready']['Address'] = 144;	G_Var['Raspberry'][0]['Ready']['Start_bit'] = 1
    G_Var['Raspberry'][0]['IP'][0]['Value'] = 192;	G_Var['Raspberry'][0]['IP'][0]['Address'] = 146;	G_Var['Raspberry'][0]['IP'][0]['Start_bit'] = 0
    G_Var['Raspberry'][0]['IP'][1]['Value'] = 168;	G_Var['Raspberry'][0]['IP'][1]['Address'] = 147;	G_Var['Raspberry'][0]['IP'][1]['Start_bit'] = 0
    G_Var['Raspberry'][0]['IP'][2]['Value'] = 1;	G_Var['Raspberry'][0]['IP'][2]['Address'] = 148;	G_Var['Raspberry'][0]['IP'][2]['Start_bit'] = 0
    G_Var['Raspberry'][0]['IP'][3]['Value'] = 150;	G_Var['Raspberry'][0]['IP'][3]['Address'] = 149;	G_Var['Raspberry'][0]['IP'][3]['Start_bit'] = 0
    G_Var['PLC'][0]['Name']['Value'] = 'S7_1200';	G_Var['PLC'][0]['Name']['Address'] = 150;	G_Var['PLC'][0]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['IP'][0]['Value'] = 192;	G_Var['PLC'][0]['IP'][0]['Address'] = 406;	G_Var['PLC'][0]['IP'][0]['Start_bit'] = 0
    G_Var['PLC'][0]['IP'][1]['Value'] = 168;	G_Var['PLC'][0]['IP'][1]['Address'] = 407;	G_Var['PLC'][0]['IP'][1]['Start_bit'] = 0
    G_Var['PLC'][0]['IP'][2]['Value'] = 1;	G_Var['PLC'][0]['IP'][2]['Address'] = 408;	G_Var['PLC'][0]['IP'][2]['Start_bit'] = 0
    G_Var['PLC'][0]['IP'][3]['Value'] = 200;	G_Var['PLC'][0]['IP'][3]['Address'] = 409;	G_Var['PLC'][0]['IP'][3]['Start_bit'] = 0
    G_Var['PLC'][0]['Connect']['Value'] = False;	G_Var['PLC'][0]['Connect']['Address'] = 410;	G_Var['PLC'][0]['Connect']['Start_bit'] = 0
    G_Var['PLC'][0]['Automatic']['Value'] = False;	G_Var['PLC'][0]['Automatic']['Address'] = 410;	G_Var['PLC'][0]['Automatic']['Start_bit'] = 1
    G_Var['PLC'][0]['IoT_Allow']['Value'] = False;	G_Var['PLC'][0]['IoT_Allow']['Address'] = 410;	G_Var['PLC'][0]['IoT_Allow']['Start_bit'] = 2
    G_Var['PLC'][0]['Digital_Inputs'][0]['Name']['Value'] = 'Digital Inputs[0]';	G_Var['PLC'][0]['Digital_Inputs'][0]['Name']['Address'] = 412;	G_Var['PLC'][0]['Digital_Inputs'][0]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][0]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Inputs'][0]['Value']['Address'] = 668;	G_Var['PLC'][0]['Digital_Inputs'][0]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][1]['Name']['Value'] = 'Digital Inputs[1]';	G_Var['PLC'][0]['Digital_Inputs'][1]['Name']['Address'] = 670;	G_Var['PLC'][0]['Digital_Inputs'][1]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][1]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Inputs'][1]['Value']['Address'] = 926;	G_Var['PLC'][0]['Digital_Inputs'][1]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][2]['Name']['Value'] = 'Digital Inputs[2]';	G_Var['PLC'][0]['Digital_Inputs'][2]['Name']['Address'] = 928;	G_Var['PLC'][0]['Digital_Inputs'][2]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][2]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Inputs'][2]['Value']['Address'] = 1184;	G_Var['PLC'][0]['Digital_Inputs'][2]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][3]['Name']['Value'] = 'Digital Inputs[3]';	G_Var['PLC'][0]['Digital_Inputs'][3]['Name']['Address'] = 1186;	G_Var['PLC'][0]['Digital_Inputs'][3]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][3]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Inputs'][3]['Value']['Address'] = 1442;	G_Var['PLC'][0]['Digital_Inputs'][3]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][4]['Name']['Value'] = 'Digital Inputs[4]';	G_Var['PLC'][0]['Digital_Inputs'][4]['Name']['Address'] = 1444;	G_Var['PLC'][0]['Digital_Inputs'][4]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][4]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Inputs'][4]['Value']['Address'] = 1700;	G_Var['PLC'][0]['Digital_Inputs'][4]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][5]['Name']['Value'] = 'Digital Inputs[5]';	G_Var['PLC'][0]['Digital_Inputs'][5]['Name']['Address'] = 1702;	G_Var['PLC'][0]['Digital_Inputs'][5]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][5]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Inputs'][5]['Value']['Address'] = 1958;	G_Var['PLC'][0]['Digital_Inputs'][5]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][6]['Name']['Value'] = 'Digital Inputs[6]';	G_Var['PLC'][0]['Digital_Inputs'][6]['Name']['Address'] = 1960;	G_Var['PLC'][0]['Digital_Inputs'][6]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][6]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Inputs'][6]['Value']['Address'] = 2216;	G_Var['PLC'][0]['Digital_Inputs'][6]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][7]['Name']['Value'] = 'Digital Inputs[7]';	G_Var['PLC'][0]['Digital_Inputs'][7]['Name']['Address'] = 2218;	G_Var['PLC'][0]['Digital_Inputs'][7]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][7]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Inputs'][7]['Value']['Address'] = 2474;	G_Var['PLC'][0]['Digital_Inputs'][7]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][8]['Name']['Value'] = 'Digital Inputs[8]';	G_Var['PLC'][0]['Digital_Inputs'][8]['Name']['Address'] = 2476;	G_Var['PLC'][0]['Digital_Inputs'][8]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][8]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Inputs'][8]['Value']['Address'] = 2732;	G_Var['PLC'][0]['Digital_Inputs'][8]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][9]['Name']['Value'] = 'Digital Inputs[9]';	G_Var['PLC'][0]['Digital_Inputs'][9]['Name']['Address'] = 2734;	G_Var['PLC'][0]['Digital_Inputs'][9]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][9]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Inputs'][9]['Value']['Address'] = 2990;	G_Var['PLC'][0]['Digital_Inputs'][9]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][10]['Name']['Value'] = 'Digital Inputs[10]';	G_Var['PLC'][0]['Digital_Inputs'][10]['Name']['Address'] = 2992;	G_Var['PLC'][0]['Digital_Inputs'][10]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][10]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Inputs'][10]['Value']['Address'] = 3248;	G_Var['PLC'][0]['Digital_Inputs'][10]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][11]['Name']['Value'] = 'Digital Inputs[11]';	G_Var['PLC'][0]['Digital_Inputs'][11]['Name']['Address'] = 3250;	G_Var['PLC'][0]['Digital_Inputs'][11]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][11]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Inputs'][11]['Value']['Address'] = 3506;	G_Var['PLC'][0]['Digital_Inputs'][11]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][12]['Name']['Value'] = 'Digital Inputs[12]';	G_Var['PLC'][0]['Digital_Inputs'][12]['Name']['Address'] = 3508;	G_Var['PLC'][0]['Digital_Inputs'][12]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][12]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Inputs'][12]['Value']['Address'] = 3764;	G_Var['PLC'][0]['Digital_Inputs'][12]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][13]['Name']['Value'] = 'Digital Inputs[13]';	G_Var['PLC'][0]['Digital_Inputs'][13]['Name']['Address'] = 3766;	G_Var['PLC'][0]['Digital_Inputs'][13]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Inputs'][13]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Inputs'][13]['Value']['Address'] = 4022;	G_Var['PLC'][0]['Digital_Inputs'][13]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Analog_Inputs'][0]['Name']['Value'] = 'Analog Inputs[0]';	G_Var['PLC'][0]['Analog_Inputs'][0]['Name']['Address'] = 4024;	G_Var['PLC'][0]['Analog_Inputs'][0]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Analog_Inputs'][0]['Value']['Value'] = 0;	G_Var['PLC'][0]['Analog_Inputs'][0]['Value']['Address'] = 4280;	G_Var['PLC'][0]['Analog_Inputs'][0]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Analog_Inputs'][0]['Index']['Value'] = 0;	G_Var['PLC'][0]['Analog_Inputs'][0]['Index']['Address'] = 4284;	G_Var['PLC'][0]['Analog_Inputs'][0]['Index']['Start_bit'] = 0
    G_Var['PLC'][0]['Analog_Inputs'][1]['Name']['Value'] = 'Analog Inputs[1]';	G_Var['PLC'][0]['Analog_Inputs'][1]['Name']['Address'] = 4286;	G_Var['PLC'][0]['Analog_Inputs'][1]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Analog_Inputs'][1]['Value']['Value'] = 0;	G_Var['PLC'][0]['Analog_Inputs'][1]['Value']['Address'] = 4542;	G_Var['PLC'][0]['Analog_Inputs'][1]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Analog_Inputs'][1]['Index']['Value'] = 0;	G_Var['PLC'][0]['Analog_Inputs'][1]['Index']['Address'] = 4546;	G_Var['PLC'][0]['Analog_Inputs'][1]['Index']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][0]['Name']['Value'] = 'Digital Outputs[0]';	G_Var['PLC'][0]['Digital_Outputs'][0]['Name']['Address'] = 4548;	G_Var['PLC'][0]['Digital_Outputs'][0]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][0]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][0]['Value']['Address'] = 4804;	G_Var['PLC'][0]['Digital_Outputs'][0]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][0]['Direction']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][0]['Direction']['Address'] = 4804;	G_Var['PLC'][0]['Digital_Outputs'][0]['Direction']['Start_bit'] = 1
    G_Var['PLC'][0]['Digital_Outputs'][1]['Name']['Value'] = 'Digital Outputs[1]';	G_Var['PLC'][0]['Digital_Outputs'][1]['Name']['Address'] = 4806;	G_Var['PLC'][0]['Digital_Outputs'][1]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][1]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][1]['Value']['Address'] = 5062;	G_Var['PLC'][0]['Digital_Outputs'][1]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][1]['Direction']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][1]['Direction']['Address'] = 5062;	G_Var['PLC'][0]['Digital_Outputs'][1]['Direction']['Start_bit'] = 1
    G_Var['PLC'][0]['Digital_Outputs'][2]['Name']['Value'] = 'Digital Outputs[2]';	G_Var['PLC'][0]['Digital_Outputs'][2]['Name']['Address'] = 5064;	G_Var['PLC'][0]['Digital_Outputs'][2]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][2]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][2]['Value']['Address'] = 5320;	G_Var['PLC'][0]['Digital_Outputs'][2]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][2]['Direction']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][2]['Direction']['Address'] = 5320;	G_Var['PLC'][0]['Digital_Outputs'][2]['Direction']['Start_bit'] = 1
    G_Var['PLC'][0]['Digital_Outputs'][3]['Name']['Value'] = 'Digital Outputs[3]';	G_Var['PLC'][0]['Digital_Outputs'][3]['Name']['Address'] = 5322;	G_Var['PLC'][0]['Digital_Outputs'][3]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][3]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][3]['Value']['Address'] = 5578;	G_Var['PLC'][0]['Digital_Outputs'][3]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][3]['Direction']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][3]['Direction']['Address'] = 5578;	G_Var['PLC'][0]['Digital_Outputs'][3]['Direction']['Start_bit'] = 1
    G_Var['PLC'][0]['Digital_Outputs'][4]['Name']['Value'] = 'Digital Outputs[4]';	G_Var['PLC'][0]['Digital_Outputs'][4]['Name']['Address'] = 5580;	G_Var['PLC'][0]['Digital_Outputs'][4]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][4]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][4]['Value']['Address'] = 5836;	G_Var['PLC'][0]['Digital_Outputs'][4]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][4]['Direction']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][4]['Direction']['Address'] = 5836;	G_Var['PLC'][0]['Digital_Outputs'][4]['Direction']['Start_bit'] = 1
    G_Var['PLC'][0]['Digital_Outputs'][5]['Name']['Value'] = 'Digital Outputs[5]';	G_Var['PLC'][0]['Digital_Outputs'][5]['Name']['Address'] = 5838;	G_Var['PLC'][0]['Digital_Outputs'][5]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][5]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][5]['Value']['Address'] = 6094;	G_Var['PLC'][0]['Digital_Outputs'][5]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][5]['Direction']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][5]['Direction']['Address'] = 6094;	G_Var['PLC'][0]['Digital_Outputs'][5]['Direction']['Start_bit'] = 1
    G_Var['PLC'][0]['Digital_Outputs'][6]['Name']['Value'] = 'Digital Outputs[6]';	G_Var['PLC'][0]['Digital_Outputs'][6]['Name']['Address'] = 6096;	G_Var['PLC'][0]['Digital_Outputs'][6]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][6]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][6]['Value']['Address'] = 6352;	G_Var['PLC'][0]['Digital_Outputs'][6]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][6]['Direction']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][6]['Direction']['Address'] = 6352;	G_Var['PLC'][0]['Digital_Outputs'][6]['Direction']['Start_bit'] = 1
    G_Var['PLC'][0]['Digital_Outputs'][7]['Name']['Value'] = 'Digital Outputs[7]';	G_Var['PLC'][0]['Digital_Outputs'][7]['Name']['Address'] = 6354;	G_Var['PLC'][0]['Digital_Outputs'][7]['Name']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][7]['Value']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][7]['Value']['Address'] = 6610;	G_Var['PLC'][0]['Digital_Outputs'][7]['Value']['Start_bit'] = 0
    G_Var['PLC'][0]['Digital_Outputs'][7]['Direction']['Value'] = False;	G_Var['PLC'][0]['Digital_Outputs'][7]['Direction']['Address'] = 6610;	G_Var['PLC'][0]['Digital_Outputs'][7]['Direction']['Start_bit'] = 1
    G_Var['IoT'][0]['Name']['Value'] = 'IoT[0]';	G_Var['IoT'][0]['Name']['Address'] = 6612;	G_Var['IoT'][0]['Name']['Start_bit'] = 0
    G_Var['IoT'][0]['Connect']['Value'] = False;	G_Var['IoT'][0]['Connect']['Address'] = 6868;	G_Var['IoT'][0]['Connect']['Start_bit'] = 0
    G_Var['HMI'][0]['IP'][0]['Value'] = 192;	G_Var['HMI'][0]['IP'][0]['Address'] = 6870;	G_Var['HMI'][0]['IP'][0]['Start_bit'] = 0
    G_Var['HMI'][0]['IP'][1]['Value'] = 168;	G_Var['HMI'][0]['IP'][1]['Address'] = 6871;	G_Var['HMI'][0]['IP'][1]['Start_bit'] = 0
    G_Var['HMI'][0]['IP'][2]['Value'] = 1;	G_Var['HMI'][0]['IP'][2]['Address'] = 6872;	G_Var['HMI'][0]['IP'][2]['Start_bit'] = 0
    G_Var['HMI'][0]['IP'][3]['Value'] = 100;	G_Var['HMI'][0]['IP'][3]['Address'] = 6873;	G_Var['HMI'][0]['IP'][3]['Start_bit'] = 0
    G_Var['HMI'][0]['Connect']['Value'] = False;	G_Var['HMI'][0]['Connect']['Address'] = 6874;	G_Var['HMI'][0]['Connect']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][0]['Name']['Value'] = 'Buttons[0]';	G_Var['HMI'][0]['Buttons'][0]['Name']['Address'] = 6876;	G_Var['HMI'][0]['Buttons'][0]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][0]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][0]['Val']['Address'] = 7132;	G_Var['HMI'][0]['Buttons'][0]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][1]['Name']['Value'] = 'Buttons[1]';	G_Var['HMI'][0]['Buttons'][1]['Name']['Address'] = 7134;	G_Var['HMI'][0]['Buttons'][1]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][1]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][1]['Val']['Address'] = 7390;	G_Var['HMI'][0]['Buttons'][1]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][2]['Name']['Value'] = 'Buttons[2]';	G_Var['HMI'][0]['Buttons'][2]['Name']['Address'] = 7392;	G_Var['HMI'][0]['Buttons'][2]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][2]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][2]['Val']['Address'] = 7648;	G_Var['HMI'][0]['Buttons'][2]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][3]['Name']['Value'] = 'Buttons[3]';	G_Var['HMI'][0]['Buttons'][3]['Name']['Address'] = 7650;	G_Var['HMI'][0]['Buttons'][3]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][3]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][3]['Val']['Address'] = 7906;	G_Var['HMI'][0]['Buttons'][3]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][4]['Name']['Value'] = 'Buttons[4]';	G_Var['HMI'][0]['Buttons'][4]['Name']['Address'] = 7908;	G_Var['HMI'][0]['Buttons'][4]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][4]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][4]['Val']['Address'] = 8164;	G_Var['HMI'][0]['Buttons'][4]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][5]['Name']['Value'] = 'Buttons[5]';	G_Var['HMI'][0]['Buttons'][5]['Name']['Address'] = 8166;	G_Var['HMI'][0]['Buttons'][5]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][5]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][5]['Val']['Address'] = 8422;	G_Var['HMI'][0]['Buttons'][5]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][6]['Name']['Value'] = 'Buttons[6]';	G_Var['HMI'][0]['Buttons'][6]['Name']['Address'] = 8424;	G_Var['HMI'][0]['Buttons'][6]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][6]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][6]['Val']['Address'] = 8680;	G_Var['HMI'][0]['Buttons'][6]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][7]['Name']['Value'] = 'Buttons[7]';	G_Var['HMI'][0]['Buttons'][7]['Name']['Address'] = 8682;	G_Var['HMI'][0]['Buttons'][7]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][7]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][7]['Val']['Address'] = 8938;	G_Var['HMI'][0]['Buttons'][7]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][8]['Name']['Value'] = 'Buttons[8]';	G_Var['HMI'][0]['Buttons'][8]['Name']['Address'] = 8940;	G_Var['HMI'][0]['Buttons'][8]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][8]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][8]['Val']['Address'] = 9196;	G_Var['HMI'][0]['Buttons'][8]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][9]['Name']['Value'] = 'Buttons[9]';	G_Var['HMI'][0]['Buttons'][9]['Name']['Address'] = 9198;	G_Var['HMI'][0]['Buttons'][9]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][9]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][9]['Val']['Address'] = 9454;	G_Var['HMI'][0]['Buttons'][9]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][10]['Name']['Value'] = 'Buttons[10]';	G_Var['HMI'][0]['Buttons'][10]['Name']['Address'] = 9456;	G_Var['HMI'][0]['Buttons'][10]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][10]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][10]['Val']['Address'] = 9712;	G_Var['HMI'][0]['Buttons'][10]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][11]['Name']['Value'] = 'Buttons[11]';	G_Var['HMI'][0]['Buttons'][11]['Name']['Address'] = 9714;	G_Var['HMI'][0]['Buttons'][11]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][11]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][11]['Val']['Address'] = 9970;	G_Var['HMI'][0]['Buttons'][11]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][12]['Name']['Value'] = 'Buttons[12]';	G_Var['HMI'][0]['Buttons'][12]['Name']['Address'] = 9972;	G_Var['HMI'][0]['Buttons'][12]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][12]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][12]['Val']['Address'] = 10228;	G_Var['HMI'][0]['Buttons'][12]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][13]['Name']['Value'] = 'Buttons[13]';	G_Var['HMI'][0]['Buttons'][13]['Name']['Address'] = 10230;	G_Var['HMI'][0]['Buttons'][13]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][13]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][13]['Val']['Address'] = 10486;	G_Var['HMI'][0]['Buttons'][13]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][14]['Name']['Value'] = 'Buttons[14]';	G_Var['HMI'][0]['Buttons'][14]['Name']['Address'] = 10488;	G_Var['HMI'][0]['Buttons'][14]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][14]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][14]['Val']['Address'] = 10744;	G_Var['HMI'][0]['Buttons'][14]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][15]['Name']['Value'] = 'Buttons[15]';	G_Var['HMI'][0]['Buttons'][15]['Name']['Address'] = 10746;	G_Var['HMI'][0]['Buttons'][15]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][15]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][15]['Val']['Address'] = 11002;	G_Var['HMI'][0]['Buttons'][15]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][16]['Name']['Value'] = 'Buttons[16]';	G_Var['HMI'][0]['Buttons'][16]['Name']['Address'] = 11004;	G_Var['HMI'][0]['Buttons'][16]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][16]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][16]['Val']['Address'] = 11260;	G_Var['HMI'][0]['Buttons'][16]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][17]['Name']['Value'] = 'Buttons[17]';	G_Var['HMI'][0]['Buttons'][17]['Name']['Address'] = 11262;	G_Var['HMI'][0]['Buttons'][17]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][17]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][17]['Val']['Address'] = 11518;	G_Var['HMI'][0]['Buttons'][17]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][18]['Name']['Value'] = 'Buttons[18]';	G_Var['HMI'][0]['Buttons'][18]['Name']['Address'] = 11520;	G_Var['HMI'][0]['Buttons'][18]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][18]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][18]['Val']['Address'] = 11776;	G_Var['HMI'][0]['Buttons'][18]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][19]['Name']['Value'] = 'Buttons[19]';	G_Var['HMI'][0]['Buttons'][19]['Name']['Address'] = 11778;	G_Var['HMI'][0]['Buttons'][19]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][19]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][19]['Val']['Address'] = 12034;	G_Var['HMI'][0]['Buttons'][19]['Val']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][20]['Name']['Value'] = 'Buttons[20]';	G_Var['HMI'][0]['Buttons'][20]['Name']['Address'] = 12036;	G_Var['HMI'][0]['Buttons'][20]['Name']['Start_bit'] = 0
    G_Var['HMI'][0]['Buttons'][20]['Val']['Value'] = False;	G_Var['HMI'][0]['Buttons'][20]['Val']['Address'] = 12292;	G_Var['HMI'][0]['Buttons'][20]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['IP'][0]['Value'] = 0;	G_Var['HMI'][1]['IP'][0]['Address'] = 12294;	G_Var['HMI'][1]['IP'][0]['Start_bit'] = 0
    G_Var['HMI'][1]['IP'][1]['Value'] = 0;	G_Var['HMI'][1]['IP'][1]['Address'] = 12295;	G_Var['HMI'][1]['IP'][1]['Start_bit'] = 0
    G_Var['HMI'][1]['IP'][2]['Value'] = 0;	G_Var['HMI'][1]['IP'][2]['Address'] = 12296;	G_Var['HMI'][1]['IP'][2]['Start_bit'] = 0
    G_Var['HMI'][1]['IP'][3]['Value'] = 0;	G_Var['HMI'][1]['IP'][3]['Address'] = 12297;	G_Var['HMI'][1]['IP'][3]['Start_bit'] = 0
    G_Var['HMI'][1]['Connect']['Value'] = False;	G_Var['HMI'][1]['Connect']['Address'] = 12298;	G_Var['HMI'][1]['Connect']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][0]['Name']['Value'] = 'Buttons[0]';	G_Var['HMI'][1]['Buttons'][0]['Name']['Address'] = 12300;	G_Var['HMI'][1]['Buttons'][0]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][0]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][0]['Val']['Address'] = 12556;	G_Var['HMI'][1]['Buttons'][0]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][1]['Name']['Value'] = 'Buttons[1]';	G_Var['HMI'][1]['Buttons'][1]['Name']['Address'] = 12558;	G_Var['HMI'][1]['Buttons'][1]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][1]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][1]['Val']['Address'] = 12814;	G_Var['HMI'][1]['Buttons'][1]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][2]['Name']['Value'] = 'Buttons[2]';	G_Var['HMI'][1]['Buttons'][2]['Name']['Address'] = 12816;	G_Var['HMI'][1]['Buttons'][2]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][2]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][2]['Val']['Address'] = 13072;	G_Var['HMI'][1]['Buttons'][2]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][3]['Name']['Value'] = 'Buttons[3]';	G_Var['HMI'][1]['Buttons'][3]['Name']['Address'] = 13074;	G_Var['HMI'][1]['Buttons'][3]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][3]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][3]['Val']['Address'] = 13330;	G_Var['HMI'][1]['Buttons'][3]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][4]['Name']['Value'] = 'Buttons[4]';	G_Var['HMI'][1]['Buttons'][4]['Name']['Address'] = 13332;	G_Var['HMI'][1]['Buttons'][4]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][4]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][4]['Val']['Address'] = 13588;	G_Var['HMI'][1]['Buttons'][4]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][5]['Name']['Value'] = 'Buttons[5]';	G_Var['HMI'][1]['Buttons'][5]['Name']['Address'] = 13590;	G_Var['HMI'][1]['Buttons'][5]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][5]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][5]['Val']['Address'] = 13846;	G_Var['HMI'][1]['Buttons'][5]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][6]['Name']['Value'] = 'Buttons[6]';	G_Var['HMI'][1]['Buttons'][6]['Name']['Address'] = 13848;	G_Var['HMI'][1]['Buttons'][6]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][6]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][6]['Val']['Address'] = 14104;	G_Var['HMI'][1]['Buttons'][6]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][7]['Name']['Value'] = 'Buttons[7]';	G_Var['HMI'][1]['Buttons'][7]['Name']['Address'] = 14106;	G_Var['HMI'][1]['Buttons'][7]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][7]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][7]['Val']['Address'] = 14362;	G_Var['HMI'][1]['Buttons'][7]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][8]['Name']['Value'] = 'Buttons[8]';	G_Var['HMI'][1]['Buttons'][8]['Name']['Address'] = 14364;	G_Var['HMI'][1]['Buttons'][8]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][8]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][8]['Val']['Address'] = 14620;	G_Var['HMI'][1]['Buttons'][8]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][9]['Name']['Value'] = 'Buttons[9]';	G_Var['HMI'][1]['Buttons'][9]['Name']['Address'] = 14622;	G_Var['HMI'][1]['Buttons'][9]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][9]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][9]['Val']['Address'] = 14878;	G_Var['HMI'][1]['Buttons'][9]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][10]['Name']['Value'] = 'Buttons[10]';	G_Var['HMI'][1]['Buttons'][10]['Name']['Address'] = 14880;	G_Var['HMI'][1]['Buttons'][10]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][10]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][10]['Val']['Address'] = 15136;	G_Var['HMI'][1]['Buttons'][10]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][11]['Name']['Value'] = 'Buttons[11]';	G_Var['HMI'][1]['Buttons'][11]['Name']['Address'] = 15138;	G_Var['HMI'][1]['Buttons'][11]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][11]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][11]['Val']['Address'] = 15394;	G_Var['HMI'][1]['Buttons'][11]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][12]['Name']['Value'] = 'Buttons[12]';	G_Var['HMI'][1]['Buttons'][12]['Name']['Address'] = 15396;	G_Var['HMI'][1]['Buttons'][12]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][12]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][12]['Val']['Address'] = 15652;	G_Var['HMI'][1]['Buttons'][12]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][13]['Name']['Value'] = 'Buttons[13]';	G_Var['HMI'][1]['Buttons'][13]['Name']['Address'] = 15654;	G_Var['HMI'][1]['Buttons'][13]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][13]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][13]['Val']['Address'] = 15910;	G_Var['HMI'][1]['Buttons'][13]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][14]['Name']['Value'] = 'Buttons[14]';	G_Var['HMI'][1]['Buttons'][14]['Name']['Address'] = 15912;	G_Var['HMI'][1]['Buttons'][14]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][14]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][14]['Val']['Address'] = 16168;	G_Var['HMI'][1]['Buttons'][14]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][15]['Name']['Value'] = 'Buttons[15]';	G_Var['HMI'][1]['Buttons'][15]['Name']['Address'] = 16170;	G_Var['HMI'][1]['Buttons'][15]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][15]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][15]['Val']['Address'] = 16426;	G_Var['HMI'][1]['Buttons'][15]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][16]['Name']['Value'] = 'Buttons[16]';	G_Var['HMI'][1]['Buttons'][16]['Name']['Address'] = 16428;	G_Var['HMI'][1]['Buttons'][16]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][16]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][16]['Val']['Address'] = 16684;	G_Var['HMI'][1]['Buttons'][16]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][17]['Name']['Value'] = 'Buttons[17]';	G_Var['HMI'][1]['Buttons'][17]['Name']['Address'] = 16686;	G_Var['HMI'][1]['Buttons'][17]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][17]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][17]['Val']['Address'] = 16942;	G_Var['HMI'][1]['Buttons'][17]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][18]['Name']['Value'] = 'Buttons[18]';	G_Var['HMI'][1]['Buttons'][18]['Name']['Address'] = 16944;	G_Var['HMI'][1]['Buttons'][18]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][18]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][18]['Val']['Address'] = 17200;	G_Var['HMI'][1]['Buttons'][18]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][19]['Name']['Value'] = 'Buttons[19]';	G_Var['HMI'][1]['Buttons'][19]['Name']['Address'] = 17202;	G_Var['HMI'][1]['Buttons'][19]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][19]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][19]['Val']['Address'] = 17458;	G_Var['HMI'][1]['Buttons'][19]['Val']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][20]['Name']['Value'] = 'Buttons[20]';	G_Var['HMI'][1]['Buttons'][20]['Name']['Address'] = 17460;	G_Var['HMI'][1]['Buttons'][20]['Name']['Start_bit'] = 0
    G_Var['HMI'][1]['Buttons'][20]['Val']['Value'] = False;	G_Var['HMI'][1]['Buttons'][20]['Val']['Address'] = 17716;	G_Var['HMI'][1]['Buttons'][20]['Val']['Start_bit'] = 0
    
