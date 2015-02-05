#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import time

s = socket.socket()         # Create a socket object		
host = '' # Get local machine name
port = 2222                # Reserve a port for your service.

s.connect((host, port))

print("Enter your Service ID\n 1.Add 10\n 2.Mult by 2 \n 3.echo ")
a = int(input())
q= int(input())
s.send(str(a))
s.send(str(q))
time.sleep(2)
print("Sending -->",q)
p=int(s.recv(2))
print("Received -->",p)
s.close()
                 # Close the socket when done
