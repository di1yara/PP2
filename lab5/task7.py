import re
text = "hello_world_example"
result = "".join(word.capitalize() for word in text.split("_"))
print(result)