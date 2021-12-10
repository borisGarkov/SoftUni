list_numbers_input = input().split(", ")
beggars_number = int(input())
list_integers = []
beggars = []
index = 0

for number in range(len(list_numbers_input)):
    list_integers.append(int(list_numbers_input[number]))

for beggar in range(beggars_number):
    beggars.append(0)

for number in list_integers:
    beggars[index] += number
    index += 1

    if index == beggars_number:
        index = 0

print(beggars)