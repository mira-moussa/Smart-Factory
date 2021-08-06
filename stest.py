#DYNAMIXEL global variables

Robot = [
 {  
    'ID'                : int,
    'Error'	         	: bool,
    'Busy'	        	: bool,
    'Start'	        	: bool,
    'Done'	        	: bool,
    'Gripper_control'	: bool,	
    'Gripper_Indicator'	: bool,	
    'Robot_Position'	: int,	
    'Motors'            :   [{
                                'ID'        : int   ,
                                'Position'  : float ,
                                'Velocity'  : float ,
                                'Torque'    : float ,
                                'Temp'      : float ,
                                'Volt'      : float ,
                            }]

 }
]


Robot[0]['Motors'][0]['ID']=5

#Hardware variables
Hardware = [
    {

        'digital_sensors': {

            'prox': int,
            'address': int,
            'start_bit': int,
        },
        'analogue_sensors': {
            'value': int,
            'address':[int, bytes]
        },
        'digital_actuators':{
            'linear_mode': bool,
            'linear_dir' : bool,

            'feeding': bool,
            'conveyor': bool,
            'address':[int, bytes]
        }
    }
]

#cloud global variables
sheets_list = [
    {
        'name': 'Sheet A1  ',
        'connect': bool,
        'JSON': {
        'project_id': "smartfactoryproject",
        'private_key_id': "23eb5939669723a69d8e3ab778cef4f5cc60e231",
        'private_key': "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCZoBIEASyOFUyQ\nN8b6Ey4nhJ6vucJgmhPBOqpPfDHuUFL461W1j5kygi83NlS5EwjhZKd9AxxaqZU3\nFtBFXtxAev6hrD80XbX3Q6vpnuQhhdkoVECxgRpjSF6DNSXobdF+y+rVfl4PHivw\nwOws7XbjGZ1ITeSiRjGycNO/LtaWMYJ11lO7wS1lD0+CcsLewLGdnRYpIMeEwALv\nD+rM0h3fwfHFbGLxsjAT3wKQA36lDtlyRgCI7RwTDdRKB+Uua3iPIowzCpfqFN+p\npqQle1Tik+Xcfk1ryssSZP8JWmIZU34jS/8QQ17r4BhrR7YQO4ELHgxHewV35IW9\ncJ5Y92RXAgMBAAECggEACNYJozxUDToRZMwogDLBOVmp7O6QzRCfqUIQELFSh+QL\n2bBjhiVjyOFvCMxxtBFxtdEdxxV6OIa/g+MmiI7ruTO52J+5JPBs6nN0fGP8uCbk\nNisea3dDBsnfUcmpTAShA5uD/tKdY143Zcoa63yfFXHgN4vvZhwGeL5/l2QAyLOq\ndJtGqVP/epx2HTlZd3drY6n0/nHkCokoqknZ0Z+23GY81YdwsRQfpV2v2MMPqqQx\na/5+hv6lBSff2tSTUaZYbUpXFyP6NWCfNDtNpG4aFH0zgrIBRKS0JRXxk0xkIXAU\nj1j+4v4W2vIbvvGnSqg1oB9nmR/DvxlsCm7rCiueTQKBgQDSSY2XsxOBg8v+HtM4\nU6AQxw+7ualXN0loQNf4NoS0PuaUIFiWLhAzaeAloZWGwczHup7O9A8z1vNTbb/p\nFIn7gqi01/sppY+3eax7rZElknV9Er9uf1O/j40l1cQhF8E7H2SMtrMrcRz8BirY\nLq6u4maiuiqhBDjh/RiBt5sXewKBgQC7BUk5xMm7mDErcmWZFua1NNxKwQncdbjx\nLAb5hBltBCx4/vE3heDB/Msh5qjjXTTSYBWV7KrVz1AwMwLwxzgJ/ne1xhZeP/tA\nyDRvulFPkNI+jYoJXAyAxzEtf+yK+b84flkvl3fUmhtRS8mwzKH08THyf2atQ62Z\ngZhKvNIh1QKBgA2KZu+pvEvOrMgEPB2YZOovpzezUNAo4zUvV7jH6euhUT+ghZPG\nC40D+Eb0DKjMud7yiV9SH9h6sthgbMcZZ3kmhK6Aac/YtVRfJVghaQM+Vwpitqjq\n0f23xKL3DNYErZCdCOB2szrM4czoqMGa3+yq72jzC+OqXe9PWNChff8ZAoGAb2PU\nm13EMcGR96ipLqdfPip/0t5q+y36u1pXxSGS60WDH4XpMgLBPYlNi6GQkesf3PVx\npdxSXAqgXjTj2XkuvXUc491Z0UUWZx1XbfxxFYzSTIOM5co3gDQj7E+3GYdrB0Dp\n6dizfKNVBfS36l/XTsah0ydihmw656UyicEw/wkCgYEApVYifNfLRMzjZ1Pf99eN\nMHENPyj7IiGz4o8wCSgHYHXLR8r8UbXyCEEPpLsgd7Xy58i7WR41AQT6uNM1iyAZ\nE4l0pSrwwkb+WTSodQTjsuoqhtE3cxkxbQRzNbcE7yVivkN6Oik6oTGr+UQEFFFC\nTJvbE1mwvpGVBNc872+Ispc=\n-----END PRIVATE KEY-----\n",
        'client_email': "motorprofile@smartfactoryproject.iam.gserviceaccount.com",
        'client_id': "107366181503673801768",
        },
        'HMI_acc': bool,
    }
]

#Rpi global variables
rpi = {
    'ready': bool,
    'ip': bytes([192, 168, 1, 1]),
}

#HMI
hmi = {
    'ip': bytes([192, 168, 1, 1]),
    'connect': bool,
    'automatic': bool,

    'buttons':[int]
}

#PLC
PLC=[{
'name': 'PLC        ',
        'connect': bool,
        'ip': bytes([192, 168, 1, 1]),},
    {
    'counters':int,
    }


    ]