import socket
import sys
import time
s = socket.socket()
host =input(str("please enter the host name of server: "))
port = 8080
s.connect((host,port))
print("connected to chat server")
while 1:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print("server : ",incoming_message)
        print("")
        message = input(str(">>"))
        message = message.encode()
        s.send(message)
        print("message has been sent...")
        print("")
