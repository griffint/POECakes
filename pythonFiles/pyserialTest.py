# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 14:14:09 2014

@author: griffint
"""

import time
import serial
ser = serial.Serial('/dev/ttyACM0', 9600,timeout= 10) # Establish the connection on a specific port

def send_and_receive( theinput ):
    """
    This sends a string to arduino through serial.
    It then waits for a response from Arduino.
    """
    ser.write( theinput )
    time.sleep(.3)
    while True:
        time.sleep(.2)
        state = ser.readline()
        if state == "":
            
            print ("Nothing received dawg")
            break
        else:
            print("Yay we got something")
            print len(state)
            return state
        
        
    
if __name__ == "__main__":
    print(send_and_receive("PUTIN"))
    print("putin should be here")
    time.sleep(1)
    print(send_and_receive("CON"))