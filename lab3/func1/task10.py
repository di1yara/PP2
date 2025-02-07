"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Note: don't use collection set
"""
def unique(lst):
    for i in lst:
        result = []
    for i in lst:
        if lst.count(i) == 1: 
            result.append(i)  
    return result 

numbers=list(map(int, input("Enter numbers: ").split()))
print(unique(numbers))
