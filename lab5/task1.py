"""
Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
"""

import re 
text="abb abbbb ba ab baa"
pattern =r"\bab*\b" 
match=re.findall(pattern ,text)
print(match)

