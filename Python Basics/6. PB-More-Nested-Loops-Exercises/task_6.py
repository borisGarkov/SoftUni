final_sector = input()
rows_number = int(input())
seats_odd_number = int(input())
total_seats_number = 0
counter = 0
final_number = ord(final_sector) + 1
total_rows = rows_number + 1

for sector_number in range(65, final_number):

    for row in range(1, total_rows):

        total_seats_number = 0
        if row % 2 == 0:
            total_seats_number = seats_odd_number + 2
        else:
            total_seats_number = seats_odd_number

        for seat in range(97, 97 + total_seats_number):

            print(f"{chr(sector_number)}{row}{chr(seat)}")
            counter += 1

    total_rows += 1
print(counter)
