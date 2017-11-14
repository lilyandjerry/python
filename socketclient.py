#!/usr/bin/python
# #coding:utf-8  github test
#filename：socclient.py

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host,port))
print s.recv(1024)
s.close()

def threedigit(st,ed):
    for i in range(st,ed):
        for j in range(st,ed):
            for k in range(st,ed):
                if( i != j ) and ( j != k) and ( k != i):
                    print i,j,k

threedigit(1,10)

print "this is test code"
