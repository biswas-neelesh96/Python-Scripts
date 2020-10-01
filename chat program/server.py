import socket
from datetime import datetime


HOST = input("Enter Server IPv4 Address to start Server :- ")
PORT = 5005
max_size = 1024
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((HOST,PORT))
print("starting the server at: ", datetime.now())
print("Waiting for incoming connection from client ...")
sock.listen(5)
clientsocket, clientaddress = sock.accept()

connection = True
while connection:
   data = clientsocket.recv(max_size)
   data_decoded = data.decode("utf-8")
   print("AT ",datetime.now(),clientaddress , "said", data_decoded)
   if (data_decoded == "Quit") or (data_decoded == "quit"):
       connection = False 
   msg_client = input("Enter a message : ")
   msg_client_encoded = msg_client.encode("utf-8")
   clientsocket.send(msg_client_encoded)

clientsocket.close()
sock.close()
