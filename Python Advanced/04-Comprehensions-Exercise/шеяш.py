first_number = int(input())
second_number = int(input())
third_number = int(input())
fourth_number = int(input())
count = 0

for num_one in range(first_number, 9):
    for num_two in range(9, second_number - 1, -1):
        for num_three in range(third_number, 9):
            for num_four in range(9, fourth_number - 1, -1):

                if num_one % 2 == 0 and num_two % 2 != 0 and num_three % 2 == 0 and num_four % 2 != 0 and \
                        (f'{num_one}{num_two}' == f'{num_three}{num_four}'):

                    print(f'Cannot change the same player.')

                elif num_one % 2 == 0 and num_two % 2 != 0 and num_three % 2 == 0 and num_four % 2 != 0 and \
                        (f'{num_one}{num_two}' != f'{num_three}{num_four}'):

                    print(f"{num_one}{num_two} - {num_three}{num_four}")
                    count += 1

                if count == 6:
                    exit()
