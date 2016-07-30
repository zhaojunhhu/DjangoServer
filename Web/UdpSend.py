# -*- coding:utf-8 -*-
from socket import *
HOST = '127.0.0.1'  #与本地server一致
PORT = 60006          #本地server端口
BUFSIZE = 4096

def SendToUdpserver(data):
    ADDR = (HOST, PORT)
    udpCliSock = socket(AF_INET, SOCK_DGRAM)
    udpCliSock.sendto(data,ADDR)
    datas = 'None'
    try:
        data,ADDR = udpCliSock.recvfrom(BUFSIZE)
        if not data:
            udpCliSock.close()
            return  'None'
        else:
            datas =data
    finally:
        udpCliSock.close()
        return  datas