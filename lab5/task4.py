import re
text = "Hello World Python CASE TestCase example"
pattern = r"\b[A-Z][a-z]+\b"
match = re.findall(pattern, text)
print(match)