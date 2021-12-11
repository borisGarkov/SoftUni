import math
first_number = input()
second_number = input()

sum_odd = 0
sum_even = 0

for number in range(int(first_number), int(second_number) + 1):
    number_position = len(str(number))
    initial_number = number

    while number > 0:
        digit = math.floor(number % 10)
        number //= 10

        if number_position % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit

        number_position -= 1
        if number_position == 0:
            break

    if sum_even == sum_odd:
        print(f"{initial_number}", end=" ")
    sum_odd = 0
    sum_even = 0