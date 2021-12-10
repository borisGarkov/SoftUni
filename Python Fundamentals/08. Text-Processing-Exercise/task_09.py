text = input()
chars = ""
result = ""

for char in range(len(text)):
    number = ""
    symbol = text[char]
    is_number_gotten = False

    if not symbol.isdigit():
        chars += symbol

    elif symbol.isdigit():
        for i in range(char, len(text)):
            if text[i].isdigit():
                number += text[i]
            else:
                break
            is_number_gotten = True

    if is_number_gotten:
        number = int(number)
        result += (chars.upper() * number)
        chars = ""

print(f"Unique symbols used: {len(set(result))}")
print(result)
