"""
Write a Python function that checks whether a word or phrase is palindrome or not. 
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

"""
def check(word):
   return  word==word[::-1]
str=input("Enter a word:" )
print(check(str))
