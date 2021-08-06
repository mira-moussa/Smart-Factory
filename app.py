import max30102
import hrcalc
import os
import glob
import time
import threading
import random
import copy
import json
import bluetooth

# Use the following two values
# to connect via mobile+bluetoth
bPort = 9999
bAddress = "B8:27:EB:60:C0:AB" # DON'T CHANGE
sensorMAX30102 = None
deviceFile = None
threadsQueue = []
dataQueue = []
template = {
    "tempC": None,
    "heartRate": None,
    "spo2": None,
    "isTempOK": False,
    "isMaxOK": False,
}
record = copy.copy(template)
noOfReadings = 10
isTurnedOn = False
skipAmount = 35

def Config():
    global sensorMAX30102, deviceFile
    sensorMAX30102 = max30102.MAX30102()

    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
 
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    deviceFile = device_folder + '/w1_slave'

def ReadTempRaw():
    global deviceFile
    f = open(deviceFile, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def ReadTemp():
    temp_c = None
    try:
        lines = ReadTempRaw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        #temp_c, temp_f = None, None
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            #temp_f = temp_c * 9.0 / 5.0 + 32.0
    except:
        pass
    return temp_c # <===== #, temp_f

def ReadMAX30102():
    global sensorMAX30102
    hrb, spb, hr2, sp2 = None, None, None, None
    try:
        red, ir = sensorMAX30102.read_sequential()
        hr, hrb, sp, spb = hrcalc.calc_hr_and_spo2(ir, red)
        if (hrb == True and hr != -999): hr2 = int(hr)
        else: hr2 = None
        if (spb == True and sp != -999): sp2 = int(sp)
        else: sp2 = None
    except:
        pass
    return hrb, spb, hr2, sp2

def TempThread():
    global record, template, dataQueue, noOfReadings, skipAmount, isTurnedOn
    print("Started the 'Temp' thread.")
    while isTurnedOn:
        for i in range(skipAmount):
            time.sleep(0.05)
            ReadTemp()
        counter = 0
        tempCAvg = 0.0
        while (counter < noOfReadings):
            time.sleep(0.15)
            tempC = ReadTemp()
            if (tempC is None): continue
            tempCAvg += tempC
            counter += 1
        tempCAvg /= float(noOfReadings)
        if(not record.get("isTempOK")):
            record["isTempOK"] = True
            record["tempC"] = round(tempCAvg, 3)
            if (record.get("isTempOK") and
                record.get("isMaxOK")):
                dataQueue.append(record)
                record = copy.copy(template)
        #else: continue
        #print(f"Temp oC = {tempC}.")
        
def MAX30102Thread():
    global record, template, dataQueue, noOfReadings, skipAmount, isTurnedOn
    print("Started the 'MAX30102' thread.")
    while isTurnedOn:
        for i in range(skipAmount):
            time.sleep(0.05)
            ReadMAX30102()
        counter = 0
        hr2Avg, sp2Avg = 0.0, 0.0
        while (counter < noOfReadings):
            time.sleep(0.15)
            hrb, spb, hr2, sp2 = ReadMAX30102()
            if (hr2 is None or sp2 is None): continue
            hr2Avg += hr2
            sp2Avg += sp2
            counter += 1
        hr2Avg /= float(noOfReadings)
        sp2Avg /= float(noOfReadings)
        if(not record.get("isMaxOK")):
            record["isMaxOK"] = True
            record["heartRate"] = round(hr2Avg, 3)
            record["spo2"] = round(sp2Avg, 3)
            if (record.get("isTempOK") and
                record.get("isMaxOK")):
                dataQueue.append(record)
                record = copy.copy(template)
        #else: continue
        #print(f"HR Detected = {hrb}, SP Detected = {spb}, Heart Rate = {hr2}, SPO2 = {sp2}.")
    
def BluetoothThread():
    global dataQueue, bAddress, bPort
    print("Started the 'Bluetooth' thread.")
    print("Binding @", (bAddress, bPort))
    bt = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    bt.bind((bAddress, bPort))
    bt.listen(10)
    while True:
        #time.sleep(random.random() + 0.75)
        try:
            client, clientInfo = bt.accept()
            print("Client:", clientInfo)
            while True:
                if (len(dataQueue) <= 0): continue
                ref = dataQueue[-1]
                if (ref.get("isTempOK") and ref.get("isMaxOK")):
                    dataToSend = dataQueue.pop()
                    #print("Normal:", dataToSend)
                    # JSON: {"tempC": 31.937, "heartRate": 95, "spo2": 90, "isTempOK": true, "isMaxOK": true}
                    dataToSend = json.dumps(dataToSend)
                    bt.send(dataToSend)
                    print("Sent:", dataToSend)
        except:
            client.close()

def TestThread():
    global dataQueue
    print("Started the 'Test' thread.")
    while True:
        time.sleep(0.25)
        if (len(dataQueue) <= 0): continue
        ref = dataQueue[-1]
        if (ref.get("isTempOK") and ref.get("isMaxOK")):
            dataToSend = dataQueue.pop()
            dataToSend = json.dumps(dataToSend)
            print("Average Record:", dataToSend)
            
# ========================================
# Configure the environment.
Config()

# Create the threads.
tempThd = threading.Thread(target=TempThread)
maxThd = threading.Thread(target=MAX30102Thread)
blueThd = threading.Thread(target=BluetoothThread)
testThd = threading.Thread(target=TestThread)

# Create a threads queue.
#threadsQueue.extend([tempThd, maxThd, blueThd])
threadsQueue.extend([tempThd, maxThd, testThd])

# Turn the flag to run the threads.
isTurnedOn = True

# Start the threads.
for th in threadsQueue:
    th.start()

# Wait the threads to complete their tasks.
for th in threadsQueue:
    th.join()
# ========================================