"""
Write a function that accepts string from user, return a sentence with the words reversed.
We are ready -> ready are We

"""

def reverse(str):
    return ' '.join(str.split()[::-1])
word=input("Enter a word:")
print(reverse(word))

