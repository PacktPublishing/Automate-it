import datetime

#Create two time objects
time_1 = datetime.time(13, 44, 55)
time_2 = datetime.time(13, 44, 55)
print "  Times:", time_1, time_2

#Create two date objects
date_1 = datetime.date.today()
date_2 = date_1 + datetime.timedelta(days=1)
print "  Dates:", date_1, date_2

#Combine date and time objects to datetime objects
datetime_1 = datetime.datetime.combine(date_1, time_1)
datetime_2 = datetime.datetime.combine(date_2, time_2)

#Get the difference between two datetime objects
print "  Datetime Difference:", datetime_2 - datetime_1
