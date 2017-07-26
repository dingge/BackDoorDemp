# -*- coding: utf-8 -*-
import socket
import threading
import struct
import os
  
# 监听的IP及端口
bind_ip = "127.0.0.1"
bind_port = 9998
  
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  
server.bind((bind_ip,bind_port))
  
server.listen(5)
  
print "[*] Listening on %s:%d" % (bind_ip,bind_port)

def handle_client(client_socket):
  
    #request = client_socket.recv(1024)
    FileInfo = struct.calcsize('128sl')
    print FileInfo
    buf = client_socket.recv(FileInfo)
    print len(buf)
    if buf:
        FileName,FileSize = struct.unpack('128sl',buf)
        print 'FileName is :',FileName,'FileNameSize is :',len(FileName)
        FILEWNAME=os.path.join(('./TempRec/'+FileName).strip('\00'))
        print FILEWNAME,type(FILEWNAME)
        recvd_size=0
        file = open(FILEWNAME,'wb')
        print 'start receiving...'
        while not recvd_size == FileSize:
            if FileSize - recvd_size > 1024:
                rdata = client_socket.recv(1024)
                recvd_size += len(rdata)
            else:
                rdata = client_socket.recv(FileSize - recvd_size)
                recvd_size = FileSize
            file.write(rdata)
        file.close()
        print 'Receive Done!'         
  
while True:
  
    client,addr = server.accept()
  
    print "[*] Accept connection from:%s:%d" % (addr[0],addr[1])
  
    client_handler = threading.Thread(target=handle_client,args=(client,))
  
    client_handler.start()
