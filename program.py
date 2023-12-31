# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:04:37 2023

@author: cernym
"""

import time
import serial

ser = serial.Serial(
    port='COM5',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("Program started")

while True:
    print('Reading com messages')
    time.sleep(1)
