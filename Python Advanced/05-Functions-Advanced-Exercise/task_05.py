def sum_odd_even_numbers(command, numbers):
    if command == "Odd":
        odd_numbers = list(filter(lambda x: not x % 2 == 0, numbers))
        print(sum(odd_numbers) * len(numbers))
    else:
        even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
        print(sum(even_numbers) * len(numbers))


command = input()
numbers = list(map(int, input().split()))
sum_odd_even_numbers(command, numbers)