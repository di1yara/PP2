import re 
text="ThisIsPp"
result=(re.sub(r"([A-Z])",r" \1",text).strip())
print(result)