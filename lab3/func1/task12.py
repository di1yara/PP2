"""
Define a functino histogram() that takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:

****
*********
*******
"""
def histogram(lst):
    for i in lst:
        print ('*' * i)  
numbers = list(map(int, input("Enter numbers: ").split()))
(histogram(numbers))