key = int(input())
number_of_lines = int(input())
word = ""

for _ in range(number_of_lines):
    current_char = input()
    char_in_int = ord(current_char) + key
    word += chr(char_in_int)
    char_in_int = 0

print(word)
