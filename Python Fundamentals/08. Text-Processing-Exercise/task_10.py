text = input().replace(' ', '').split(',')
count_winning_symbols_left = 0
highest_count_left = 0
count_winning_symbols_right = 0
highest_count_right = 0
WINNER_SYMBOLS = ["@", "#", "$", "^"]


def get_winning_symbol(ticket):
    return max(((letter, ticket.count(letter)) for letter in ticket), key=lambda x: x[1])[0]


def get_winner(ticket, start, end, counter, highest_counter):
    most_common_winner = max(((letter, ticket.count(letter)) for letter in ticket), key=lambda x: x[1])[0]
    for i in range(start, end):
        char = ticket[i]
        if char in WINNER_SYMBOLS and char == most_common_winner:
            counter += 1
        else:
            if counter > highest_counter:
                highest_counter = counter
            counter = 0

    return max(counter, highest_counter)


for ticket in text:

    if len(ticket) == 20:
        half = len(ticket) // 2
        left_number = get_winner(ticket, 0, half, count_winning_symbols_left, highest_count_left)
        right_number = get_winner(ticket, half, len(ticket), count_winning_symbols_right,
                                  highest_count_right)

        winning_symbol = get_winning_symbol(ticket)
        if left_number == 10 and right_number == 10:
            print(f'ticket "{ticket}" - {left_number}{winning_symbol} Jackpot!')
        elif 10 >= left_number > 5 and 10 >= right_number > 5:
            print(f'ticket "{ticket}" - {min(left_number, right_number)}{winning_symbol}')
        else:
            print(f'ticket "{ticket}" - no match')

    else:
        print("invalid ticket")
