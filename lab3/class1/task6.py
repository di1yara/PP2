"""
Write a program which can filter prime numbers in a list by using filter function. 
Note: Use lambda to define anonymous functions.
"""
is_prime=lambda x:x>1 and all (x%i!=0 for i  in range(2,int(x**0.5)+1))
numbers=list(map(int,input("Enter numbers:").split()))
prime_numbers=list(filter(is_prime,numbers))
print(prime_numbers)