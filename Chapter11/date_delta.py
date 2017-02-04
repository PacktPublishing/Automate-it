from datetime import datetime, timedelta

#Current time
now = datetime.now()
print "  Time Now is:", now

#Time one day later, thats tomorrow
one_day_later = now + timedelta(days=1)
print "  Tomorrow is:", one_day_later

#Time 365 days back
days_in_past = now - timedelta(days=365, hours=1)
print "  Last year:", days_in_past
