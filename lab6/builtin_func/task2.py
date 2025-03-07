#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

str=input("Enter string: ")
count_upper=0
count_lower=0

for letter in str:
    if letter.isupper():
        count_upper+=1
    elif letter.islower():
        count_lower+=1
        
print(f"Number of upper case: { count_upper}")
print(f"Number of lower case: {count_lower}")
