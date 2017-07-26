# -*- coding: utf-8 -*-
import socket,struct,os
  
# 目标地址IP/URL及端口
target_host = "127.0.0.1"
target_port = 9998
  
# 创建一个socket对象
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  
# 连接主机
client.connect((target_host,target_port))

FILEPATH = './TempSend/file.txt'
FileInfo_size = struct.calcsize('128sl')
fhead = struct.pack('128sl',os.path.basename(FILEPATH),os.stat(FILEPATH).st_size)
client.send(fhead)
fo = open(FILEPATH,'rb')

while True:
       FileData = fo.read(1024)
       if not FileData:
              break
       client.send(FileData)
fo.close()
