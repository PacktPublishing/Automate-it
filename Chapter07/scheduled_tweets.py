from twython import Twython

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN =''
OAUTH_TOKEN_SECRET = ''
twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

from datetime import datetime
import pytz, time
from pytz import timezone
import tweet_config as config

while True:

    for msg in config.scheduled_messages:
        print msg["timezone"]
        tz = timezone(msg["timezone"])
        utc = pytz.utc
        utc_dt = datetime.utcnow().replace(tzinfo=utc)
        au_dt = utc_dt.astimezone(tz)
        sday = au_dt.strftime('%Y-%m-%d')
        stime = au_dt.strftime('%H:%M')
        print "Current Day:Time", sday, stime

        if sday == msg["day"]:
            if stime == msg["time"]:
                print "Time", stime
                print "Content", msg["content"]
                twitter.update_status(status='%s' % msg["content"] )


    print "Running.. Will try in another min"
    time.sleep(60)
