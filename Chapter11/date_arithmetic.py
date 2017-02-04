from datetime import datetime
import time

#Current Time
now_1 = datetime.now()
print "  Time Now", now_1
time.sleep(5)

#Time after 5 seconds
now_2 = datetime.now()
print "  Time Now", now_2

#Difference in Times
print "  Difference in the times is:", (now_1 - now_2).seconds



