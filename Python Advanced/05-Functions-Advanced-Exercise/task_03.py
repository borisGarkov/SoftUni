def print_values(numbers):
    print(f"The minimum number is {min(numbers)}")
    print(f"The maximum number is {max(numbers)}")
    print(f"The sum number is: {sum(numbers)}")


numbers = [int(el) for el in input().split()]
print_values(numbers)
