n = int(input())
l = int(input())

for first_number in range(1, n):
    for second_number in range(1, n):

        if first_number > second_number:
            greater_number = first_number + 1
        else:
            greater_number = second_number + 1

        for first_letter in range(1, l + 1):
            for second_letter in range(1, l + 1):
                for last_number in range(greater_number, n + 1):

                    print(str(first_number) + str(second_number) + chr(first_letter + 96) +
                          chr(second_letter + 96) + str(last_number), end=" ")
