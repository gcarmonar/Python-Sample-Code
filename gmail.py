# gmail.py
# Searchs for un-read mails.
# Change email address and password

import imaplib
import time
while True:
    obj = imaplib.IMAP4_SSL('imap.gmail.com', '993')  
    obj.login('your_email@gmail.com','your_password')  
    obj.select() 
    print len(obj.search(None,'UnSeen')[1][0].split())
    time.sleep(1)
