first_number = int(input())
second_number = int(input())
third_number = int(input())
is_prime = True

for pin_number_1 in range(1, first_number + 1):
    if pin_number_1 % 2 == 0:

        for pin_number_2 in range(2, second_number + 1):
            is_prime = True

            for i in range(2, (pin_number_2 // 2) + 1):
                if pin_number_2 % i == 0:
                    is_prime = False

            if is_prime:
                for pin_number_3 in range(1, third_number + 1):
                    if pin_number_3 % 2 == 0:
                        print(f"{pin_number_1} {pin_number_2} {pin_number_3}")
