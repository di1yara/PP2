"""
Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points
"""
import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f"Coordinates:({self.x},{self.y})")
    def move(self,new_x,new_y):
        self.x=new_x
        self.y=new_y
    def dist(self,other_point):
        return math.sqrt((self.x-other_point.x)**2+(self.y-other_point.y)**2)
x1=int(input("Enter a x1 value:"))
y1=int(input("Enter a y1 value:"))

point1=Point(x1,y1)
 
x2=int(input("Enter a x2 value:"))
y2=int(input("Enter a y2 value:"))
point2=Point(x2,y2)
print(f"between points:({point1.dist(point2)})")