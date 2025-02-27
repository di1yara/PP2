import re 
text="abb abbb ba ab baa abb"
pattern =r"ab{2,3}"
match=re.findall(pattern ,text)
print(match)