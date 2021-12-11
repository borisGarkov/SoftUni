start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
counter = 0
is_there_combination = False

for first_number in range(start_interval, end_interval + 1):
    for second_number in range(start_interval, end_interval + 1):
        counter += 1
        if first_number + second_number == magic_number:
            print(f"Combination N:{counter} "
                  f"({first_number} + {second_number} = {magic_number})")
            is_there_combination = True
            break
    if is_there_combination:
        break

if not is_there_combination:
    print(f"{counter} combinations - neither equals {magic_number}")

