import re

data = input()
pattern = r"\b(?<!\S)(([a-z0-9\-\.]+@[a-z0-9\-]+\.[a-z0-9]+([\.a-z0-9]+)?))\b"
x = re.finditer(pattern, data)
x = [p.group(0) for p in x]
print(f"\n".join(x))
