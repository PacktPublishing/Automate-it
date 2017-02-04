import datetime

#Returns today's date with year, month and day
today = datetime.date.today()
print '  Date object:', today 
print '  Year:', today.year
print '  Mon :', today.month
print '  Day :', today.day

#Create a new date object
import datetime
date_1 = datetime.date(2011, 12, 31)
print '  Date is:', date_1

#Update a date with year=2012 and month=January
date_2 = date_1.replace(year=2012, month=1)
print '  New Date is:', date_2
