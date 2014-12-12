# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 14:14:09 2014

@author: griffint
"""

from time import sleep
import serial
ser = serial.Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port
ser.write("PUTIN")