name = input()
total_games = int(input())
points = 0
wins_count = 0
draws_count = 0
losses_count = 0

for game in range(total_games):
    result = input()

    if result == "W":
        points += 3
        wins_count += 1
    elif result == "D":
        points += 1
        draws_count += 1
    else:
        losses_count += 1

if total_games > 0:
    print(f"{name} has won {points} points during this season.\nTotal stats:\n## W: {wins_count}\n## D: {draws_count}\n## "
      f"L: {losses_count}\nWin rate: {(wins_count / total_games) * 100:.2f}%")
else:
    print(f"{name} hasn't played any games during this season.")
