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
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1.connect(("8.8.8.8", 80))
IP = (s1.getsockname()[0])
PORT = 1296
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((IP,1296))
print(f"connect clien.py to {IP}"+f"and PORT {PORT}" )
s.listen(5)


msg = "you just got connected"
while True:
    clientsocket,address = s.accept()
    print(f"connection from {address} has been established")
    msg = f"{len(msg):<{HEADERSIZE}}"+msg
    clientsocket.send(bytes(msg,"utf-8"))
    threading.Thread(target = getcommand, args = [clientsocket]).start()

