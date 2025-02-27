import re
text = "hello_world some_variable test_Example another_test"
pattern = r"\b[a-z]+_[a-z]+\b"
match = re.findall(pattern, text)
print(match)