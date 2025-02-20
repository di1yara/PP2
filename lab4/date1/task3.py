#Write a Python program to drop microseconds from datetime.


from datetime import datetime

time=datetime.now().replace(microsecond=0)

print("Time without microsecond: " ,time)