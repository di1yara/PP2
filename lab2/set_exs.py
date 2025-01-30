#True or False. You can access set items by referring to the index.
#false

#2
fruits = {"apple", "banana", "cherry"}
if "apple"  in fruits:
  print("Yes, apple is a fruit!")

#3
thisset = {'apple', 'banana', 'cherry'}
print('banana' not in thisset)
#false

#4
#What is a correct syntax for adding items to a set?
#add()

#5
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

#6
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#7
#What is a correct syntax for removing an item from a set?
#remove()
#8
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#9
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
#10
#What is a correct syntax for looping through the items of a set?
fruits = {"apple", "banana", "cherry"}
for x in {'apple', 'banana', 'cherry'}:
  print(x)

#11
#True or False. Sets are unordered, so when you loop through the items, the order will be totally random.
#true

#12
#What is a correct syntax for joining set1 and set2 into set3?'
#set3 = set1.union(set2)

#13
#There are many ways to join sets in Python. Which one of the following methods keeps ONLY the duplicates?
#intersection()
