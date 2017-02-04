from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import config, time, gmail

#Auto respond to the customer email
def send_email(strTo):
    strFrom = config.fromaddr
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Thanks for your ticket'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo

    #Add text message to the MIME object
    msgRoot.preamble = 'This is a multi-part message in MIME format.'
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)
    msgText = MIMEText('Hi there, <br><br>Thanks for your query with us today.'
                       ' You can look at our <a href="https://google.com">FAQs</a>'
                       ' and we shall get back to you soon.<br><br>'
                       'Thanks,<br>Support Team<br><br><img src="cid:image1">', 'html')
    msgAlternative.attach(msgText)

    #Add logo image to the auto response
    fp = open('google.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    #Start SMTO Server and respond to the customer
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(config.fromaddr, config.password)
    server.sendmail(config.fromaddr, config.toaddr, msgRoot.as_string())
    server.quit()

#Infinite loop to read the inbox for new emails 
#every 60 seconds (1 minute)
while True:
    g = gmail.login(config.fromaddr, config.password)

    #Pickup unread emails from your inbox	
    mails = g.inbox().mail(unread=True)
    mails[-1].fetch()
    from_ = mails[-1].fr
    
    #Respond to the request that came in
    send_email(from_)

    time.sleep(60)


