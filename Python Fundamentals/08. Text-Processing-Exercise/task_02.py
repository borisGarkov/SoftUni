data = input()
str1, str2 = data.split()
sum = 0

if len(str1) >= len(str2):
    higher = str1
    lower = str2
else:
    higher = str2
    lower = str1

for char in range(len(higher)):
    if char in range(len(lower)):
        sum += (ord(higher[char]) * ord(lower[char]))
    else:
        sum += (ord(higher[char]))

print(sum)