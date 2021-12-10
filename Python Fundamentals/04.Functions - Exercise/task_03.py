def return_string(char_1, char_2):
    for char in range(ord(char_1) + 1, ord(char_2)):
        print(f"{chr(char)}", end=" ")

char_1 = input()
char_2 = input()

return_string(char_1, char_2)