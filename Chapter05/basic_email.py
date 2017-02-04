import smtplib
import config

#Create SMTP Server instance
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

#Login to your email account
server.login(config.fromaddr, config.password)

#Add a text message and send the email
msg = "Some nice msg"
server.sendmail(config.fromaddr, config.toaddr, msg)

#Verify if the message was delivered
server.verify(config.fromaddr)

#Close Server with quit()
server.quit()
