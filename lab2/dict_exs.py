x = {'type' : 'fruit', 'name' : 'banana'}
print(len(x))

#2
#True or False. You can access item values by referring to the key name.
#true

#3
#True or False. You can access item values by referring to the key name.
#true

#4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#5
x = {'type' : 'fruit', 'name' : 'banana'}
print(x['type'])
#fruit

#6
x = {'type' : 'fruit', 'name' : 'banana'}
x['type'] = 'berry'

#7
x = {'type' : 'fruit', 'name' : 'banana'}
x.update({'name': 'apple'})

#8
#Which one of these dictionary methods can be used to add items to a dictionary?

#update()

#9
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#10
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#11

x = {'type' : 'fruit', 'name' : 'apple'}
for i in x.values():
    print(i)
#12
a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}
print(customers['c2']['name'])
      
