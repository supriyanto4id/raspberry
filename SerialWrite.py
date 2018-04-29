#!/usr/bin/env python
import time
import serial

serialport = serial.Serial("/dev/ttyUSB4", 9600, timeout=0.5)
serialport.write("tes#AAAAAAAA##ADADADD#123")
