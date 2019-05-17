import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.43.205",1257))

while True:
    
    full_msg=""
        
    new_msg = True    
    while True:
        msg = s.recv(16)
        if new_msg:
            msg_len = int(msg[:HEADERSIZE])
            new_msg = False
        
        full_msg += msg.decode("utf-8")
        
        if len(full_msg)-HEADERSIZE==msg_len:
            print("recieved")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ""
            while True:
                g = input()
                s.send(bytes(f"{len(g):<{HEADERSIZE}}"+g,"utf-8"))