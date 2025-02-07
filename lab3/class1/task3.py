"""
Define a class named Rectangle which inherits from Shape class from task 2. 
Class instance can be constructed by a length and width. 
The Rectangle class has a method which can compute the area.
"""
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,len,width):
        super().__init__()
        self.len=len
        self.width=width

    def area(self):
        return self.len*self.width
    
shape=Shape()
rectangle=Rectangle(2,3)
print("Rectangle area :" , rectangle.area())
