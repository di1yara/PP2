import re 
text=" hello, World. Python is good "
pattern=r"[ ,.]"
replacement=":"
match=re.sub(pattern,replacement,text)
print(match)