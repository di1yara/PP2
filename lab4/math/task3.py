#Write a Python program to calculate the area of regular polygon.
import math 
v1=int(input("Input number of sides:  "))
v2=int(input("Input the length of a side:"))

area=(v1* v2**2) //(4 * math.tan(math.pi / v1))

print("The area of the polygon is: ",area)