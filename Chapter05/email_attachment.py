import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Get configuration parameters
import config
fromaddr = config.fromaddr
toaddr = config.toaddr

#Create a MIME Multipart object
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Email with an attachment"
body = "Click to open the attachment"
msg.attach(MIMEText(body, 'plain'))

#Create a file to be attached to the email
filename = "attach.txt"
attachment = open(filename, "rb")

#Create payload object and encode it
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

#Attach the file content to the MIME message object
msg.attach(part)

#Create SMTP Object and Login to your account
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, config.password)

#Convert the message to string and send the email
#using sendmail() method
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)

#Close the server object with quit()
server.quit()
