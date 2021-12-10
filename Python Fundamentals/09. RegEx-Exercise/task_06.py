import re

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

pattern = r"www\.[a-zA-Z0-9\-]+(\.[a-z]+)+"
urls = re.finditer(pattern, text)
for url in urls:
    print(url.group())
