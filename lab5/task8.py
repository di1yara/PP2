import re 
text="HelloKbtuStudents"
pattern=r"[A-Z][a-z]*"
match=re.findall(pattern,text)
print(match)
