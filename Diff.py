G_Var = {
'Robot'     : [   
                {  
                    'ID'                : {'Value': int    , 'Address': int , 'Start_bit': int },
                    'Error'	         	: {'Value': bool   , 'Address': int , 'Start_bit': int },
                    'Busy'	        	: {'Value': bool   , 'Address': int , 'Start_bit': int },
                    'Start'	        	: {'Value': bool   , 'Address': int , 'Start_bit': int },
                    'Done'	        	: {'Value': bool   , 'Address': int , 'Start_bit': int },
                    'Gripper_control'	: {'Value': bool   , 'Address': int , 'Start_bit': int },	
                    'Gripper_Indicator'	: {'Value': bool   , 'Address': int , 'Start_bit': int },	
                    'Robot_Position'	: {'Value': int    , 'Address': int , 'Start_bit': int },
                    'Motors'            :   [{
                                                'ID'        : {'Value': int   , 'Address': int , 'Start_bit': int } ,
                                                'Position'  : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Velocity'  : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Torque'    : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Temp'      : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Volt'      : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'ID'        : {'Value': int   , 'Address': int , 'Start_bit': int } ,
                                                'Position'  : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Velocity'  : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Torque'    : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Temp'      : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Volt'      : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'ID'        : {'Value': int   , 'Address': int , 'Start_bit': int } ,
                                                'Position'  : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Velocity'  : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Torque'    : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Temp'      : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Volt'      : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                             },
                                            ] 
                },
                {  
                    'ID'                : {'Value': int    , 'Address': int , 'Start_bit': int },
                    'Error'	         	: {'Value': bool   , 'Address': int , 'Start_bit': int },
                    'Busy'	        	: {'Value': bool   , 'Address': int , 'Start_bit': int },
                    'Start'	        	: {'Value': bool   , 'Address': int , 'Start_bit': int },
                    'Done'	        	: {'Value': bool   , 'Address': int , 'Start_bit': int },
                    'Gripper_control'	: {'Value': bool   , 'Address': int , 'Start_bit': int },	
                    'Gripper_Indicator'	: {'Value': bool   , 'Address': int , 'Start_bit': int },	
                    'Robot_Position'	: {'Value': int    , 'Address': int , 'Start_bit': int },
                    'Motors'            :   [{
                                                'ID'        : {'Value': int   , 'Address': int , 'Start_bit': int } ,
                                                'Position'  : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Velocity'  : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Torque'    : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Temp'      : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Volt'      : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'ID'        : {'Value': int   , 'Address': int , 'Start_bit': int } ,
                                                'Position'  : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Velocity'  : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Torque'    : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Temp'      : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Volt'      : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'ID'        : {'Value': int   , 'Address': int , 'Start_bit': int } ,
                                                'Position'  : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Velocity'  : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Torque'    : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Temp'      : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Volt'      : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                             },
                                            ] 
                }
            ] 
,
'Raspberry' : [
                {  
                    'Error'             : {'Value': bool   , 'Address': int , 'Start_bit': int },
                    'Ready'	         	: {'Value': bool   , 'Address': int , 'Start_bit': int },

                    'IP'                :[{'Value': int    , 'Address': int , 'Start_bit': int },
                                          {'Value': int    , 'Address': int , 'Start_bit': int },
                                          {'Value': int    , 'Address': int , 'Start_bit': int },
                                          {'Value': int    , 'Address': int , 'Start_bit': int },
                                         ],
                }
            ]
,
'PLC'       : [   
                {  
                    'Name'              : {'Value': str    , 'Address': int , 'Start_bit': int },
                    'IP'                :[{'Value': int    , 'Address': int , 'Start_bit': int },
                                          {'Value': int    , 'Address': int , 'Start_bit': int },
                                          {'Value': int    , 'Address': int , 'Start_bit': int },
                                          {'Value': int    , 'Address': int , 'Start_bit': int },
                                         ],
                    'Connect'	      	: {'Value': bool   , 'Address': int , 'Start_bit': int },
                    'Automatic'	       	: {'Value': bool   , 'Address': int , 'Start_bit': int },
                    'IoT_Allow'	       	: {'Value': bool   , 'Address': int , 'Start_bit': int },

                    'Digital_Inputs'    :   [{
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool , 'Address': int , 'Start_bit': int } ,
                                             },
                                            ],

                    'Analog_Inputs'     :   [{
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Index'     : {'Value': int   , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': float , 'Address': int , 'Start_bit': int } ,
                                                'Index'     : {'Value': int   , 'Address': int , 'Start_bit': int } ,
                                             }
                                            ],

                    'Digital_Outputs'   :   [{
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                                'Direction' : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                                'Direction' : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                                'Direction' : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                                'Direction' : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                                'Direction' : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                                'Direction' : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                                'Direction' : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                             },
                                             {
                                                'Name'      : {'Value': str   , 'Address': int , 'Start_bit': int } ,
                                                'Value'     : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                                'Direction' : {'Value': bool  , 'Address': int , 'Start_bit': int } ,
                                             },
                                            ],
                }
            ]
,
'IoT'       : [   
                {  
                    'Name'              : {'Value': str    , 'Address': int , 'Start_bit': int },
                    'Connect'           : {'Value': bool   , 'Address': int , 'Start_bit': int },
                }
            ]
,
'HMI'       : [   
                {
                    'IP'                :[{'Value': int    , 'Address': int , 'Start_bit': int },
                                          {'Value': int    , 'Address': int , 'Start_bit': int },
                                          {'Value': int    , 'Address': int , 'Start_bit': int },
                                          {'Value': int    , 'Address': int , 'Start_bit': int },
                                         ],

                    'Connect'	       	: {'Value': bool   , 'Address': int     , 'Start_bit': int },
                    'Buttons'           :[{
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                         ],

                },
                {
                    'IP'                :[{'Value': int    , 'Address': int , 'Start_bit': int },
                                          {'Value': int    , 'Address': int , 'Start_bit': int },
                                          {'Value': int    , 'Address': int , 'Start_bit': int },
                                          {'Value': int    , 'Address': int , 'Start_bit': int },
                                         ],

                    'Connect'	       	: {'Value': bool   , 'Address': int     , 'Start_bit': int },
                    'Buttons'           :[{
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                          {
                                                'Name'      : {'Value': str   , 'Address': int    , 'Start_bit': int } ,
                                                'Val'       : {'Value': bool  , 'Address': int    , 'Start_bit': int } ,
                                          },
                                         ],

                },

            ]   

}


