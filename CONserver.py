#!/usr/bin/python           # This is server.py file

import socket
import sys               # Import socket module
import threading
import time

def worker():
	         # Now wait for client connection.
	while True:
	   c, addr = s.accept()     # Establish connection with client.
	   print 'Got connection from', addr
	    
	   for i in range(1,10):
	   	p=int(c.recv(2))
		q=int(c.recv(2))
	   	time.sleep(2)
		print('Choice -->',p)
	   	print('Received -->',q)
		print("from ",addr)
		if(p==1):
			port1=2223
			threads1 =[] 
			s2 = socket.socket()    
			s2.bind((host, port1))
  		  	t=threading.Thread(target=worker1)
			threads1.append(t)
	       		s2.listen(5)                 # Close the connection
			t.start()
		elif(p==2):
			port1=2224
		elif(p==3):
			port1=2225

			
		c.send(str(p))
	  # c.send('Thank you for connecting')
	c.close()

def worker1():
	while True:
		c1, addr1 = s2.accept()     # Establish connection with client.
	   	print 'Got connection from', addr1
	       	time.sleep(2)
	   	#print('Received -->',p)
		print("from ",addr)
		q=q+10
		c1.send(p)
	c1.close();



threads =[] 
host = '' # Get local machine name
port = 2222  
s = socket.socket()    
s.bind((host, port))
for i in range (5):
  	
	#print("")
  	t=threading.Thread(target=worker)
	threads.append(t)
	       # Create a socket object
	        		 # Reserve a port for your service.
	        # Bind to the port
	s.listen(5)                 # Close the connection
	
	t.start()
