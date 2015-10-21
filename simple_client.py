''' 
	simple_client.py
	
	Description:
	Basic program to connect to a server using a socket. Configure
	the server IP address and the port.
	
	Author: Gerardo Carmona
	Version: 1.0
	Date: 16 / Jun / 2014
	e-mail: gcarmonar@gmail.com
'''

#--- Libraries ----------------------------------------------------------------
import socket
import time

#--- Connecting to socket -----------------------------------------------------
#HOST = '10.43.8.135'    	# The remote host
HOST = '10.43.53.161'    	# The remote host
HOST = '10.43.8.135'
PORT = 50008             	# The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#--- Main program -------------------------------------------------------------
cycles = 5 					# Number of of blinks 
while cycles > 0:
	s.send('H')
	data = s.recv(1024)
	print data
	time.sleep(1)
	s.send('L')
	data = s.recv(1024)
	print data
	time.sleep(1)

s.close()					# Close socket connection
print 'Received', repr(data)
