#1
thislist = ["apple", "banana", "cherry"]
print(thislist)
#2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#4
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#5
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#6
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#7
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#8
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#9
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#10
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#11
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#12
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#13
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#14
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#15
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#16
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#17
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#18
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#19
thislist = ["apple", "banana", "cherry"]
del thislist
#20
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#21
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#22
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#23
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#24
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#25
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#26
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#27
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#28
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#29
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
#30
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#31
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#32
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
#33
"""
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""