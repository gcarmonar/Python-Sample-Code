#!/usr/bin/python
import time
import datetime
import sys
import gspread
import serial


# Serial settings
port = "/dev/ttyACM0"
baud = 9600
serial_freedom = serial.Serial(port, baud)
serial_freedom.flushInput()


# Google Acoount Details
email = 'email@gmail.com'
password = 'password'
spreadsheet = 'sensor'    # Name of the file

# Login with your Google account
try:
  gc = gspread.login(email, password)
except:
  print "unable to login in. Check your email address/password"
  sys.exit()
  
# Open a worksheet for your spreadsheet using the filename
try:
  wks = gc.open(spreadsheet).sheet1
except:
  print ("unable to open the spredsheet.  Check your filename: %s") % spreadsheet
  sys.exit()

time.sleep(1)

input = 0
  
while True:  
  if (serial_freedom.inWaiting() > 0):
    input = serial_freedom.readline()
    print(input)
    print(datetime.datetime.now(), input)
    print('write angle to gdocs')
    try:
      values = [datetime.datetime.now(), input]
      wks.append_row(values)
    except:
      print ("Unable to append data.  Check your connection?")
      sys.exit()  
    time.sleep(1)



