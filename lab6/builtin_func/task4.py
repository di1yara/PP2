import math
import time
num=int(input("Enter a number: "))
delay = int(input("Enter a delay in milliseconds: "))
time.sleep(delay/1000)
result = math.sqrt(num)
print(f"Square root of {num} after {delay} milliseconds is {result}")