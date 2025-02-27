
import re 
text="axb a__b a123b abc b11b"
pattern =r"\ba[^ ]*b\b"
match=re.findall(pattern ,text)
print(match)