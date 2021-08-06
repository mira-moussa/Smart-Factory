from function_smart import Start,read,append

CLIENT_SECRET_FILE = 'SmartFactoryProject-23eb59396697.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
id = '1aMyAFN41-G8ms4tvaeyJhYXroLRzSWgOe64JPN95N1A'
range_name= 'Sheet1!A1:D2'

service = Start(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, *SCOPES)

data = read(service,id,range_name)

append(service,id,range_name, {'values' : data})







