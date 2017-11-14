#!/usr/bin/python
# #coding:utf-8
#filename：socketserver.py

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))

print 'Server start listen!'
s.listen(5)
while True:
    c, addr = s.accept()
    print "Connect address:",addr
    c.send('wellcome!')
    c.close
