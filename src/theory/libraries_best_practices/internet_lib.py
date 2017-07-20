'''
Created on Jul 19, 2017

@author: ToOro
'''
from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.p1') as response:
    for line in response:
        line = line.decode('utf-8') # decode binary to text
        if 'EST' in line or 'EDT' in line: # look for Easten Time
            print(line)
            
# Sending email
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('blablabla@gmail.com',
                """To: bdsfs@example.org
                From: ...
                
                Content ...
                """
                )
server.quit()