# def filter_even_numbers(numbers):
#     return list(filter(lambda x: x % 2 == 0, numbers))
#
#
# numbers = [int(el) for el in input().split()]
# print(filter_even_numbers(numbers))

numbers = filter(lambda x: x % 2 == 0, map(int, input().split()))
print(list(numbers))
