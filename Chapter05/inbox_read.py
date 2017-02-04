import config, imaplib

#Create an IMAP Object
M = imaplib.IMAP4_SSL("imap.gmail.com", 993)

#Login to Inbox with IMAP Objecy
M.login(config.fromaddr, config.password)

#Select object of type INBOX
M.select('INBOX')
print "Inbox:", M

#Logout from your Inbox
M.logout()
