import math

input_line = input()
best_word = ''
highest_number = 0

while input_line != "End of words":

    sum_letters = 0
    for letter in input_line:
        sum_letters += ord(letter)

    if input_line[0] == 'a' or input_line[0] == 'e' or input_line[0] == 'i' or input_line[0] =='o' \
            or input_line[0] == 'u' or input_line[0] == 'y' or input_line[0] == 'A' \
            or input_line[0] == 'E' or input_line[0] == 'I' or input_line[0] == 'O' \
            or input_line[0] == 'U' or input_line[0] == 'Y':
        sum_letters *= len(input_line)
    else:
        sum_letters /= len(input_line)
        sum_letters = math.floor(sum_letters)

    if sum_letters > highest_number:
        highest_number = sum_letters
        best_word = input_line

    input_line = input()

print(f"The most powerful word is {best_word} - {highest_number}")