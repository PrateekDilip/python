#+13853991888 Twilio number
#Type, Date, amount
#RD 2-Feb-2017 5000 SBH
#RD 21-Feb-2017	8000 SBH
#RD 6-Feb-2017 2000 SBH

#RD 22-Nov-2017 4000 Citibank
#RD 9-Feb-2016 10000 CitiBank
#RD 12-Feb-2016	10000 CitiBank
#RD 15-Feb-2016 4000  CitiBank

#EQ 6-Jul-2017 4000 Citibank	
#EQ 14-Nov-2017 4000 Citibank
#EQ 20-Jul-2017 4000 Citibank
#EQ 27-Sep-2017 6000 Citibank

import smtplib
import os, sys
import datetime
from smsapi import SmsApi
#import nexmo

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login( 'halwe.prateek@gmail.com', 'bakethecake!88' )
server.sendmail( 'Prateek', 'prateekd@juniper.net', 'Investment' )

username = "prateek"
password = "prateek123"

sms = SmsApi(username, password)


from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC4d674fa43cae45bd31e49b25dec270c2"
# Your Auth Token from twilio.com/console
auth_token  = "f90fbf023e7857b01b230f3f0d38bff9"

username = "prateek"
password = "prateek123"

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
	            to="+918105088557", 
                    from_="+13853991888",
                    body="Hello from Python!")
		print(message)

