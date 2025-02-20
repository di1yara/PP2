#Write a Python program to print yesterday, today, tomorrow.


from datetime import datetime ,timedelta

cur_date=datetime.now()
yes_date=cur_date-timedelta(days=1)
tom_date=cur_date+timedelta(days=1)

print("Current Date:", cur_date.strftime("%Y-%m-%d"))
print("Yesturday Date:", yes_date.strftime("%Y-%m-%d"))
print("Tommorow Date:", tom_date.strftime("%Y-%m-%d"))