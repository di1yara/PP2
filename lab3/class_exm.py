#1 
class MyClass:#class
    x=5
p1=MyClass() #object
print(p1.x)

#2
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age 
p1=Person("john",36)

print(p1.name)
print(p1.age)

#3
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
#4
class Person:
   def __init__(self,name,age):
      self.name=name
      self.age=age
def  __str__(self):
      return f"{self.name}({self.age})"
   
p1=Person("Tom",36)
print(p1)

#5

class Person():
    def __init(self,name,age):
        self.name=name
        self.age=age
def __str__(self):
    print("Hello my name is  " + self.name)

p1=Person("Timma" ,25)
p1.myfunc()
#6
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#7
class Person():
    def __init(self,name,age):
        self.name=name
        self.age=age
def __str__(self):
    print("Hello my name is  " + self.name)

p1=Person("Timma", 25)

p1.age=40
print(p1.age)

#8
class Person():
    def __init(self,name,age):
        self.name=name
        self.age=age
def __str__(self):
    print("Hello my name is  " + self.name)

p1=Person("Timma",25)

del p1.age

#9
class Person():
    def __init(self,name,age):
        self.name=name
        self.age=age
def __str__(self):
    print("Hello my name is  " + self.name)

p1=Person ("Timma",25)
del p1

#10
class Person:
    pass



