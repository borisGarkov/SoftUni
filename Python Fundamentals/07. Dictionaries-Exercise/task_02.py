count = 0
elements = {}

while True:
    line = input()
    if line == "stop":
        break
    count += 1

    if count % 2 != 0:
        element = line
    else:
        value = int(line)

        if element not in elements:
            elements[element] = value
        else:
            elements[element] += value

for element, value in elements.items():
    print(f"{element} -> {value}")

