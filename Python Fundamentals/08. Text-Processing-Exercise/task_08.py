data = input().split()
result = 0

for string in data:
    after_letter = False
    is_number_checked = False
    number = ""

    for char in range(len(string)):
        symbol = string[char]
        if symbol.isdigit():
            after_letter = True
            continue

        if is_number_checked == False:
            for num in range(char + 1, len(string) - 1):
                number += string[num]
            is_number_checked = True

        if after_letter:
            if symbol.isupper():
                alphabet_position = (ord(symbol) % 65) + 1
                result -= alphabet_position
            else:
                symbol = symbol.upper()
                alphabet_position = (ord(symbol) % 65) + 1
                result += alphabet_position
            break

        number = int(number)
        if symbol.isupper():
            alphabet_position = (ord(symbol) % 65) + 1
            result += (number / alphabet_position)
        else:
            symbol = symbol.upper()
            alphabet_position = (ord(symbol) % 65) + 1
            result += (number * alphabet_position)

print(f"{result:.2f}")


