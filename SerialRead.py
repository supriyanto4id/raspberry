#!/usr/bin/env python
import time
import serial

serialport = serial.Serial("/dev/ttyUSB4", 9600, timeout=0.5)

while True:
        command = serialport.readline()
        print str(command)
        if command != ""  :
        #print command
                url = str(command)
                data = url.split("#")
                print len(data) #3
                print data[0]  # mkyong.com
                print data[1]  # 100
                print data[2]  # 2015-10-1
                print data[3]
                for temp in data:
                        print temp
