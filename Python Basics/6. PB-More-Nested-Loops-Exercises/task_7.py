a = int(input())
b = int(input())
max_number_passwords = int(input())
counter = 0
is_max_reached = False

for first_letter in range(35, 56):
    for second_letter in range(64, 97):
        for third_letter in range(1, a + 1):
            for forth_letter in range(1, b + 1):

                print(f"{chr(first_letter)}{chr(second_letter)}"
                      f"{third_letter}{forth_letter}"
                      f"{chr(second_letter)}{chr(first_letter)}", end="|")

                counter += 1
                first_letter += 1
                second_letter += 1

                if counter >= max_number_passwords:
                    is_max_reached = True
                    break
                if third_letter == a and forth_letter == b:
                    is_max_reached = True
                    break

                if first_letter > 55:
                    first_letter = 35
                if second_letter > 96:
                    second_letter = 64

            if is_max_reached:
                break
        if is_max_reached:
            break
    if is_max_reached:
        break
