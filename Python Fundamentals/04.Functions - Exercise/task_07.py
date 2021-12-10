def calculate_perfect_number(number):
    is_perfect = False
    required_sum = 0

    if number < 0:
        is_perfect = False
        return is_perfect

    for digit in range(1, number):
        if number % digit == 0:
            required_sum += digit

    if required_sum == number:
        is_perfect = True

    return is_perfect


number = int(input())
if calculate_perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
