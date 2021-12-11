male_number = int(input())
female_number = int(input())
tables_max_number = int(input())
counter = 0
are_tables_over = False

for male in range(1, male_number + 1):
    for female in range(1, female_number + 1):
        print(f"({male} <-> {female})", end=" ")
        counter += 1
        if counter >= tables_max_number:
            are_tables_over = True
            break
    if are_tables_over:
        break
