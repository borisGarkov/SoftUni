import sys

numbers = list(map(int, input().split(", ")))
index_wanted = int(input())
number_at_index_wanted = numbers[index_wanted]
cycles_count = 0

while True:
    current_min_number = min(numbers)
    current_min_number_index = numbers.index(current_min_number)

    if current_min_number == number_at_index_wanted and current_min_number_index == index_wanted:
        cycles_count += current_min_number
        break

    cycles_count += current_min_number
    numbers[current_min_number_index] = sys.maxsize

print(cycles_count)