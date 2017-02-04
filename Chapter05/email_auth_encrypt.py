#Understanding TLS Sessions
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
try:
    server.set_debuglevel(True)

    print "Sending ehlo"
    server.ehlo()

    if server.has_extn('STARTTLS'):
        print "Starting TLS Session"
        server.starttls()

        print "Sending ehlo again"
        server.ehlo()
finally:
    server.quit()
