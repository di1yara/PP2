"""
2.Define a class named Shape and its subclass Square.
 The Square class has an init function which takes a length as argument.
 Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,len):
        super().__init__()
        self.len=len
    def area(self):
        return self.len**2
shape=Shape()
square=Square(6)
print("Shape area:", shape.area())  
print("Square area:", square.area())  
