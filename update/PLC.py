import snap7
from Diff import *
from INI import *
from Set import *
import time
import threading
    
INI()


IP = '192.168.1.201'
RACK = 0
SLOT = 1

DB_NUMBER = 5
START_ADDRESS = 0
SIZE = 17716 + 1 


plc=snap7.client.Client()

def PLC_start():
    plc.connect(IP,RACK,SLOT,102)




def PLC_reading():
    db=plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
    PLC_Read(db)
    return db

def PLC_writing(db):
    db=PLC_Wrirte(db)
    plc.db_write(DB_NUMBER, 0,db)
    return db

def PLC_off():
    plc.disconnect()





