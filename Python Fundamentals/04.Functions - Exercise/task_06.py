def password_validator(string_input):
    count_digits = 0
    is_valid = True

    if not 6 <= len(string_input) <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")

    for char in string_input:
        if not (char.isdigit() or char.isalpha()):
            is_valid = False
            print("Password must consist only of letters and digits")
            break

        if char.isdigit():
            count_digits += 1

    if count_digits < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid:
        print("Password is valid")


string_input = input()
password_validator(string_input)
