import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config
import email.utils

#Read configuration
fromaddr = config.fromaddr
toaddr = config.toaddr

#Create a MIME message object and fill the required parameters
msg = MIMEMultipart()
msg['Subject'] = "Hello from the Author of Automate It!"
msg['To'] = email.utils.formataddr(('Recipient', toaddr))
msg['From'] = email.utils.formataddr(('Author', fromaddr))
body = "What a wonderful world!"
msgBody = MIMEText(body, 'plain')
msg.attach(msgBody)

#Start SMTP object and login to account
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, config.password)

#Send email contents as text
text = msg.as_string()
print "Text is:", text
server.sendmail(fromaddr, toaddr, text)

#Quit the SMTP Server
server.quit()

