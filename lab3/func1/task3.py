"""
 Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
create function: solve(numheads, numlegs):
"""
def solve(numheads,numlegs):
    Rabbits=(numlegs- 2*numheads)//2
    Chickens=numheads-Rabbits
    return Chickens,Rabbits
heads=(int(input("Enter a num of head: ")))
legs=(int(input("Enter a num  of leg: ")))
result=solve(heads,legs)
print("Chikens:" ,result[0], "Rabbits: " , result[1])


