# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:09:04 2020

@author: 坤林
"""

from time import time
from socket import *

serverPort=12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1)
while(True):
    command=input(">>")
    if(command=="quit"):
        break
    print("正在%s"%command)
    serverName=command.split()[1]
    for i in range(10):
        message="%d client ping %s"%(i,serverName)
        try:
            start=time()
            clientSocket.sendto(message.encode(),(serverName,serverPort))
            modifiedMessage,serverAddress=clientSocket.recvfrom(2048)
            end=time()
            print("来自%s的回复：字节=%d 时间<1ms RTT=%f"%(serverName,len(modifiedMessage),end-start))
        except:
            print("请求超时。")
clientSocket.close()    