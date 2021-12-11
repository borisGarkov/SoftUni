number = float(input())

is_number_ok = -100 <= number <= 100 and number != 0

if not is_number_ok:
    print("No")
else:
    print("Yes")

# not number == 0
