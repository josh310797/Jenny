#!/usr/bin/env python
import sys
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',23))
s.listen(10)

print "[+]-------Jenny BETA-------[+]"

#Sets up telnet sockets
def tel_con():
    while 1:
        conn, addr = s.accept()
        print addr
        printInfo(addr)
    
#Compiles and prints
def printInfo(addr):
     ip = addr
     info = (time.strftime("%d/%m/%Y") + " [" + time.strftime("%H:%M:%S") + "]" + " - " + str(ip))
     print info
     oFile(info)

#Creates output file
def oFile(pInfo):
    oInfo = pInfo
    fileObject = open("logs.txt", "a")
    fileObject.write(oInfo + "\n")
    fileObject.close()
     
tel_con()
#Send Nudes
