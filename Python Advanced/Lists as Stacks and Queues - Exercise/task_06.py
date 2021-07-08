line = input()
is_balanced = True
brackets = {
    "{": "}",
    "[": "]",
    "(": ")"
}

data = []

for l in line:
    if l in "{[(":
        data.append(l)
    else:
        if not data:
            is_balanced = False
            break
        last_bracket = data.pop()
        if not l == brackets[last_bracket]:
            is_balanced = False
            break

if is_balanced:
    print("YES")
else:
    print("NO")

