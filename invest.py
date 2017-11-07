import smtplib
import os, sys
import datetime
from smsapi import SmsApi
#import nexmo

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login( '***@abc.com', '****password***' )
server.sendmail( 'Prateek', '*****@abc.com', 'Investment' )

username = "prateek"
password = "***"

sms = SmsApi(username, password)


from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "***"
# Your Auth Token from twilio.com/console
auth_token  = "***"

username = "prateek"
password = "***"

sms = SmsApi(username, password)

date = []
mylist = []

date = datetime.date.today()
print (date.day)
mylist.append(date)
print (mylist[0]) # print the date object, not the container ;-)

f = open('input.txt','r')
amount = []
word = []
listoflist = []
i = 0
for line in f:
    word.append(line.strip().split(' '))

print (word)

for i in word:
	if int(i[1])==date.day:
		print ("Write code to send sms now")
        	client = Client(account_sid, auth_token)
		message = client.messages.create(
	            to="+91**", 
                    from_="+1**",
                    body="Hello from Python!")
		print(message)

