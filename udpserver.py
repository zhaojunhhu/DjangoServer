#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from socket import *

HOST = '127.0.0.1'
PORT = 60006 
BUFSIZE = 4096

ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
	print 'wating for message...'
	data, addr = udpSerSock.recvfrom(BUFSIZE)
	udpSerSock.sendto('success'+data,addr)
	print '...received from and retuned to:',data,addr

udpSerSock.close()
