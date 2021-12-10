first_string = input()
second_string = input()

for index in range(len(first_string)):

    if first_string[index] != second_string[index]:

        for second_str_index in range(0, index + 1):
            print(second_string[second_str_index], end="")

        for first_str_index in range(index + 1, len(first_string)):
            print(first_string[first_str_index], end="")

        print()
