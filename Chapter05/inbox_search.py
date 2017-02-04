import config, imaplib

#Create a IMAP object to read gmail messages
M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
M.login(config.fromaddr, config.password)

#Select Inbox to perform search operation
M.select("INBOX")

#Search emails with a given subject
typ, data = M.search(None, 'SUBJECT', "Email with an attachment")

#Fetach Email message and print
typs, msg = M.fetch(data[0].split()[-1], '(RFC822)')
print "Message is ", msg[0][1]
M.close()

#Logout from gmail account
M.logout()


import gmail, config
from datetime import date

#Login to gmail account
g = gmail.login(config.fromaddr, config.password)

#Search for emails after July 22nd and fetch the first email
mails = g.inbox().mail(after=date(2016, 7, 22))
mails[-1].fetch()

#Get body of the fetched email
print "Email Body:\n", mails[-1].body

#Logout of email account
g.logout()

