import datetime

#Create a time object and get attributes like hour, minute
#seconds and microseconds
time_obj = datetime.time(13, 2, 23)
print "Time object is:", time_obj
print 'Hour  :', time_obj.hour
print 'Minute:', time_obj.minute
print 'Second:', time_obj.second
print 'Microsecond:', time_obj.microsecond

#Get min and max possible hours for time object
import datetime
print "Time Attributes are:"
print "Earliest time of the day :", datetime.time.min
print "Latest time of the day :", datetime.time.max
