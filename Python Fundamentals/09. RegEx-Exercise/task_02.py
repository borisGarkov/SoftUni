import re

data = input()
pattern = r"(?<=\s_)[a-zA-Z\d]+\b"
x = re.findall(pattern, data)
print(",".join(x))
