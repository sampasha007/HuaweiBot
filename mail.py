import smtplib
from SAVIAK import *
gmail_user = "bothuawei@gmail.com"
gmail_pwd = "Htipl@1234"
TO = email
SUBJECT = "Mentoring Progress Report"
TEXT = "Hi Sir,\n	I have completed the following topics today"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
BODY = '\r\n'.join(['To: %s' % TO,
        'From: %s' % gmail_user,
        'Subject: %s' % SUBJECT,
        '', TEXT])

#server.sendmail(gmail_user, [TO], BODY)
#print('sending email ......')
#print ('email sent')
