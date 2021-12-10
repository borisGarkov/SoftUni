cards_deck = input().split(" ")
shuffle_count = int(input())
top_card = cards_deck[0]
bottom_card = cards_deck[-1]
shuffled_deck = []
half_deck = len(cards_deck) // 2

for shuffle in range(shuffle_count):
    shuffled_deck = []
    left_deck = []
    right_deck = []

    for index in range(1, half_deck):
        left_deck.append(cards_deck[index])

    for index in range(half_deck, len(cards_deck) - 1):
        right_deck.append(cards_deck[index])

    for index in range(len(left_deck)):
        shuffled_deck.append(right_deck[index])
        shuffled_deck.append(left_deck[index])

    shuffled_deck.append(bottom_card)
    shuffled_deck.insert(0, top_card)

    cards_deck = shuffled_deck

print(shuffled_deck)