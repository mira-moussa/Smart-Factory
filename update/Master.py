from iot_final import *
from INI import *
from PLC import *
from Set import *
from Iot_Data import *

import time
iot_write_range='Data!J3'
iot_read_range='Data!k176:k222'



PLC_start()
db=plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)

while True:
    start=time.perf_counter()
    
    db=PLC_reading()

    data = iot_write_data()
    iot_write(id,iot_write_range,data)
    
    
    data_from_iot = iot_read(id,iot_read_range)
    iot_read_data(data_from_iot)

    db=PLC_writing(db)


    end=time.perf_counter()
    print(G_Var['Robot'][0]['Start']['Value'])
    print(end-start)

