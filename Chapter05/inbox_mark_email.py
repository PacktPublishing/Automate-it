import gmail, config

#Login to gmail account
g = gmail.login(config.fromaddr, config.password)

#Read all emails whose sender is noreply@glassdoor.com
mails = g.inbox().mail(unread=True, sender='noreply@glassdoor.com')

#Fetch and read the latest email
mails[-1].fetch()
mails[-1].read()

#Logout from gmail account
g.logout()

import gmail, config
from datetime import date

#Read configuration and login to gmail account
g = gmail.login(config.fromaddr, config.password)

#Read emails from amazon from date January 01 2016
mails = g.inbox().mail(unread=True, sender='store-news@amazon.in',
                       after=date(2016, 01, 01))

#Go through all the email and mark them with label
for email in mails:
    email.read()
    email.add_label("AMAZON")

#Logout from gamil account
g.logout()

