input_line = input()
list_numbers = []
list_opposite_integers = []
list_numbers = input_line.split(" ")

for index in range(len(list_numbers)):
    list_numbers[index] = int(list_numbers[index]) * -1
    list_opposite_integers.append(list_numbers[index])

print(list_opposite_integers)