def sort_numbers(numbers):
    return sorted(numbers, key=lambda x: x)


numbers = [int(el) for el in input().split()]
print(sort_numbers(numbers))