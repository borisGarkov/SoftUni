user_input = input()
is_prime = True
sum_prime = 0
sum_complex = 0

while user_input != "stop":
    if int(user_input) < 0:
        print("Number is negative.")
    else:
        for i in range(2, (int(user_input) // 2) + 1):
            if int(user_input) % i == 0:
                is_prime = False

        if is_prime:
            sum_prime += int(user_input)
        else:
            sum_complex += int(user_input)
            is_prime = True

    user_input = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_complex}")