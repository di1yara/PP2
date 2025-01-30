#1
fruits = ('apple', 'banana', 'cherry')
(x, *y) = fruits
print(y)
#['banana','cherry']
#2
fruits = ('apple', 'banana', 'cherry', 'mango')
(x, *y, z) = fruits
print(y)
#['banana', 'cherry']
#3
#What is a correct syntax for looping through the items of a tuple?
#for x in ('apple', 'banana', 'cherry'):
#print(x)

#5
tuple1 = ('a', 'b' , 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple2 + tuple1
#(1, 2, 3, 'a', 'b', 'c')

#6
"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found

"""

