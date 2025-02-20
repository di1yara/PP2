#Write a Python program to calculate two date difference in seconds.

from datetime import datetime
import math

day1=datetime(2025,12,30,15,0 ,0)
day2=datetime(2025,12,23,22,10,5)

result=abs((day1-day2).total_seconds())

print(result)