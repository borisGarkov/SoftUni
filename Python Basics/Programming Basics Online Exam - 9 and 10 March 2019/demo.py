name1 = input()
name2 = input()
final_points1 = 0
final_points2 = 0

while True:
    card1 = input()
    if card1 == 'End of game':
        print(f'{name1} has {final_points1} points')
        print(f'{name2} has {final_points2} points')
        break
    card2 = int(input())

    card1 = int(card1)

    if card1 > card2:
        final_points1 += (card1 - card2)
    elif card2 > card1:
        final_points2 += (card2 - card1)
    elif card1 == card2:
        print('Number wars!')
        card1 = int(input())
        card2 = int(input())
        if card1 > card2:
            print(f'{name1} is winner with {final_points1} points')
            break
        elif card2 > card1:
            print(f'{name2} is winner with {final_points2} points')
            break


