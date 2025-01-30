#1
mylist = ['apple', 'banana', 'cherry']
print(mylist[1])
#banana

#2
#List items cannot be removed after the list has been created.
#false

#3
thislist = ['apple', 'banana', 'cherry']
print(len(thislist))
#4
mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4])
#['banana', 'cherry', 'orange']

#5
#Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#6
mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])
#banana

#7
mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])
#apple

#8
#Use the insert method to add "lemon" as the second item in the fruits list.
fruits["apple","banana","kiwi"]
fruits.insert(1,"lemon")

#9
mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist)
#apple ,cherry

#10
#What is a correct syntax for looping through the items of a list?
[print(x) for x in ['apple', 'banana', 'cherry']]
#11
fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
#["banana"]

#13
fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]\
#["apple","apple","apple"]

#14

    