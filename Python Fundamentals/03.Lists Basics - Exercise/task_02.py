factor = int(input())
count = int(input())

incrementor = 1
numbers_count = 0
list_numbers = []

while True:
    if incrementor % factor == 0:
        list_numbers.append(incrementor)
        numbers_count += 1
    if numbers_count == count:
        break

    incrementor += 1

print(list_numbers)