import datetime

#Generate two time objects time_1 and time_2
time_1 = datetime.time(8, 9, 10)
print "  Time 1:", time_1
time_2 = datetime.time(13, 19, 50)
print "  Time 2:", time_2

#Compare time objects with <,> operators
print "  Comparing times: time_2 > time_1?", time_2 > time_1

#Generate two date objects date_1 and date_2
date_1 = datetime.date.today()
print "  Date 1:", date_1
date_2 = date_1 + datetime.timedelta(days=2)
print "  Date 2:", date_2

#Compare date objects with <,> operators
print "  Comparing dates: date_1 > date_2?", date_1 > date_2
