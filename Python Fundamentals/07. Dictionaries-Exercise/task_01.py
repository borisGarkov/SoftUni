text = input()
occurrence = {}
for char in text:
    if char != " ":
        count = text.count(char)
        occurrence[char] = count

for key, value in occurrence.items():
    print(f"{key} -> {value}")
