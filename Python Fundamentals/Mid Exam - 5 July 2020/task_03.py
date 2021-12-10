numbers = [int(number) for number in input().split()]
average_number = sum(numbers) / len(numbers)
numbers.sort(reverse=True)
sorted_list = []
count_to_5 = 0

for number in numbers:
    count_to_5 += 1
    if number > average_number and count_to_5 <= 5:
        sorted_list.append(number)

if len(sorted_list) == 0:
    print("No")
else:
    print(*sorted_list)