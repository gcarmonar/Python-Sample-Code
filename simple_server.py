''' 
	simple_server.py
	
	Description:
	Basic file for a putting a Socket Server. It uses port number 5008, 
	be aware 	that there are some reserved ports (like 80) for other 
	propourses.
	
	Author: Gerardo Carmona
	Version: 1.0
	Date: 16 / Jun / 2014
	e-mail: gcarmonar@gmail.com
'''


#--- Libraries ----------------------------------------------------------------
import socket
import RPi.GPIO as GPIO

#--- Opening socket -----------------------------------------------------------
HOST =''
PORT = 50008
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn, addr = s.accept()
print "Gerardo's Pi", addr

#--- GPIOs --------------------------------------------------------------------
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

#--- Main program -------------------------------------------------------------
while 1:
    data = conn.recv(1024)
    if not data: break
    if data == 'H':
		GPIO.output(25, GPIO.HIGH)
        print "Se recibio la H"
	else
		GPIO.output(25, GPIO.LOW)
    conn.send(data)					# Send recibed data back to the server
conn.close()
