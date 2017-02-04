import datetime

#Todays date in ISO format
today = datetime.datetime.today()
print "  ISO datetime: ", today

#Create a new format and represent date in that format
format = "%a %b %d %H:%M:%S %Y"
string_format = today.strftime(format)
print "  Datetime in String format:", string_format

#Get the date from a Unix time
import time
time_1 = time.time()
print "  Datetime from unix timestamp:", datetime.datetime.fromtimestamp(1284101485)

#Convert a given date to Unix time
date_1 = datetime.datetime(2012,4,1,0,0)
print "  Unix timestamp", date_1.strftime('%s')

#Convert date to ordinal format
date_1 = datetime.date.fromordinal(1000)
print "  1000th day from 1 Jan 0001: ", date_1
