"""
Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion:
C = (5 / 9) * (F – 32)
"""

def Centigrade(gradus):
    C=(5/9)*(gradus-32)
    return C
gradus=int(input("Enter a Fahrenheit temp: "))

print(Centigrade(gradus))
