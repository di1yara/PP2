## Python Classes
"""
1. Define a class which has at least two methods:
`getString`: to get a string from console input
`printString`: to print the string in upper case.

"""
class stringinupper:
    def __init__(self):
        self.s=""
    def getString(self):
        self.s=input("Enter string:")

    def printString(self):
        print(self.s.upper())
obj = stringinupper()
obj.getString()  
obj.printString()  


