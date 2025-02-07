#1
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()
#2
#What is the correct keyword to use inside an empty class, 
#to avoid getting an error?
 #pass
 