text = input()
result = []
for char in range(len(text) - 1):
    current = text[char]
    if char + 1 in range(len(text)):
        next = text[char + 1]
        if not current == next:
            result.append(current)
    else:
        result.append(current)

print("".join(result))
