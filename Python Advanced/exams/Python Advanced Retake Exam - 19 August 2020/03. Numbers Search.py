def numbers_searching(*numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    duplicates = []
    for n in range(min_value + 1, max_value):
        if n in numbers:
            continue
        else:
            missing_number = n

    for n in numbers:
        if numbers.count(n) > 1 and n not in duplicates:
            duplicates.append(n)

    duplicates.sort()
    list_to_return = [missing_number, duplicates]
    return list_to_return


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))