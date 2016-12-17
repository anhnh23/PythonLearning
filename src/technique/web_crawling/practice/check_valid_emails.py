'''
Created on Dec 15, 2016

@author: ToOro
'''
import re
import dns.resolver as dr#dnspython package
import socket
import smtplib

email_address='hoanganh8507phone@gmail.com'
addressToVerify = email_address
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
if match==None:
    print('Bad Syntax')
    raise ValueError('Bad Syntax')

# Step 2: getting MX record
## Pull domain name from email address
domain_name = email_address.split('@')[1]

# connect to emailhippo pas RFCs
records = dr.query(domain_name, 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)

#Step 3: ping email server
## Get local server hostname
host = socket.gethostname()
## SMTP lib setup (use debug level for full out put
server = smtplib.SMTP()
server.set_debuglevel(0)
## SMTP conversation
server.connect(mxRecord)
server.helo(host)
server.mail(email_address)
code, message = server.rcpt(str(addressToVerify))
server.quit()

#Assume 250 as success
if code == 250:
    print('Y')
else:
    print('N')

