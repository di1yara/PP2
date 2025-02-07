"""
Write a function that accepts string from user and print all permutations of that string.

"""
from itertools import permutations
def next_permutations(s):
    for i in permutations(s):
        print(''.join(i))

str = input("Enter a string: ")
next_permutations(str)