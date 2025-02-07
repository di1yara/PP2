"""
You are given list of numbers separated by spaces. 
Write a function filter_prime which will take list of numbers as an agrument and 
returns only prime numbers from the list.

"""

def filter_prime(x):
    if x>1 and all (x%i!=0 for i in  range (2,int(x**0.5)+1)):
        return x
    

numbers=list(map(int,input("Enter numbers:").split()))
prime_numbers=list(filter(filter_prime,numbers))

print(prime_numbers)