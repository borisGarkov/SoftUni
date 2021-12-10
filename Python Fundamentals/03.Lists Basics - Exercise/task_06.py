input_integers = input().split(" ")
number_to_remove = int(input())
list_integers = []

for index in range(len(input_integers)):
    list_integers.append(int(input_integers[index]))

for _ in range(number_to_remove):
    list_integers.pop(min(list_integers))

print(list_integers)