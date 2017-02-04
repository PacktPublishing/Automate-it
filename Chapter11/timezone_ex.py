from datetime import datetime, timedelta
#Returns the current local time
now = datetime.now()
print "  Local time now is:", now
#Returns the local time in UTC
utcnow = datetime.utcnow()
print "  UTC time now is:", utcnow

from pytz import timezone
import pytz
#Select a timezone for calculations
utc = pytz.utc
print "  Selected time zone:", utc

#Switching time zones and getting the local time
eastern = timezone('US/Eastern')
print "  Switched to time zone:", eastern
loc_dt = datetime(2016, 11, 27, 12, 0, 0, tzinfo=pytz.utc)
est = loc_dt.astimezone(eastern)
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
print "  Local time in Eastern time zone:", est.strftime(fmt)

#Get local time in a given time zone
from datetime import datetime, timedelta
au_tz = timezone('Australia/Sydney')
local = datetime(2002, 10, 27, 6, 0, 0, tzinfo=au_tz)
print "  Local time in Sydney:", local

#Perform arithematic operations, add or substract time
past = local - timedelta(minutes=10)
print "  10 minutes before time was:", past
future = local + timedelta(hours=18)
print "  18 hours later it is:", future

#Get time in Eastern time with and without Daylight Savings
eastern = timezone('US/Eastern')
dt = datetime(2016, 11, 06, 1, 30, 0)
dt1 = eastern.localize(dt, is_dst=True)
print "  Date time 1 with day light savings:", dt1.strftime(fmt)
dt2 = eastern.localize(dt, is_dst=False)
print "  Date time 2 without day light savings:", dt2.strftime(fmt)

#Helper methods to get available timezones for a country
tz_au = '\n  '.join(pytz.country_timezones['au'])
print "  Time zones in Australia:", tz_au
country_gb, country_fr = pytz.country_names['gb'], pytz.country_names['fr']
print "\n  Country names are:\n", "  ", country_gb, "\n  ", country_fr
