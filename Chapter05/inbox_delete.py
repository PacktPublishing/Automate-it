import gmail, config
#Login to gmail account
g = gmail.login(config.fromaddr, config.password)

#Search for emails with sender as junk@xyz.com
emails = g.inbox().mail(sender='junk@xyz.com')

#Iterate through all email objects and delete them
if emails:
    for mail in emails:
        mail.delete()

