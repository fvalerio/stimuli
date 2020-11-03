# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 17:12:26 2018

@author: vr1
"""

import socket

UDP_IP = "18.93.15.244"
UDP_PORT = 7000
MESSAGE = "AM01"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
                     
sock.connect((UDP_IP, UDP_PORT))
                     
sock.sendto("AM01", (UDP_IP, UDP_PORT))
sock.sendto("U0000", (UDP_IP, UDP_PORT))
sock.sendto("G", (UDP_IP, UDP_PORT))