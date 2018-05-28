# -*- coding: utf-8 -*-

import socket
import struct
import subprocess


HOST = '192.168.13.10'
SRC_HOST = '192.168.13.1'
PORT = 999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SRC_HOST, PORT))

res = subprocess.call(['ping', '-I', SRC_HOST, HOST, '-c', '2'])

if res == 0:
    print "ping to ", HOST, "ok"
elif res == 2:
    print "no response from", HOST
else:
    print "ping to", HOST, "failed!"

s.close()