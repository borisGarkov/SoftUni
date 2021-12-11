start_interval = input()
end_interval = input()
skip_letter = input()
count = 0

for first_letter in range(ord(start_interval), ord(end_interval) + 1):
    if first_letter == ord(skip_letter):
        continue
    for second_letter in range(ord(start_interval), ord(end_interval) + 1):
        if second_letter == ord(skip_letter):
            continue
        for third_letter in range(ord(start_interval), ord(end_interval) + 1):
            if third_letter == ord(skip_letter):
                continue
            print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}", end=" ")
            count += 1

print(count)