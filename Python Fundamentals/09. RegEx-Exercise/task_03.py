import re

string = input().lower()
word_to_check = input().lower()

x = re.findall(r"\b" + word_to_check + r"\b", string)
print(len(x))

