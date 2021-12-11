happy_number = int(input())

if happy_number > 9:
    magic_number = 10
else:
    magic_number = happy_number

for first_digit in range(1, magic_number):
    for second_digit in range(1, magic_number):
        for third_digit in range(1, magic_number):
            for forth_digit in range(1, magic_number):

                if (first_digit + second_digit) == (third_digit + forth_digit) \
                        and happy_number % (first_digit + second_digit) == 0:
                    print(f"{first_digit}{second_digit}{third_digit}{forth_digit}", end=" ")