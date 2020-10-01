import socket
from datetime import datetime

HOST = input("Enter Server IPv4 Address to connect to server :- ")
PORT  = 5005

max_size = 1024
print("The client is starting at ",datetime.now())
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))

connection = True
while connection:
    msg_server = input("Message to server : ")
    msg_server_encoded = msg_server.encode("utf-8")
    s.send(msg_server_encoded)
    data = s.recv(max_size)
    data_decoded = data.decode("utf-8")
    print("At : ",datetime.now(),"Someone on server replied",data_decoded)
    if (data_decoded == "Quit") or (data_decoded == "quit"):
       connection = False 

s.close()  
