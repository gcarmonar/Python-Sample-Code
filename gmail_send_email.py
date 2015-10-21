#!/usr/bin/python
 
# Import smtplib for the actual sending function
import smtplib
 
# For guessing MIME type
import mimetypes
 
# Import the email modules we'll need
import email
import email.mime.application
 
#Import sys to deal with command line arguments
import sys
 
# Create a text/plain message
msg = email.mime.Multipart.MIMEMultipart()
msg['Subject'] = 'Hello world!'
msg['From'] = 'your_email@gmail.com'
msg['To'] = 'destination_email@gmail.com'

# Message to be sent
body = email.mime.Text.MIMEText("""Hello, how are you? I am fine.
This is a rather nice letter, don't you think?

Sended from my Raspberry Pi""")
msg.attach(body) 

# send via Gmail server
# NOTE: my ISP, Centurylink, seems to be automatically rewriting
# port 25 packets to be port 587 and it is trashing port 587 packets.
# So, I use the default port 25, but I authenticate.
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login('your_email@gmail.com','password')
s.sendmail('destination_email@gmail.com',['destination_email@gmail.com'], msg.as_string())
s.quit()
