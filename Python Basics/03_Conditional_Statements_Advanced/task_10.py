import math

year = input()
number_of_holidays = int(input())
weekends_at_home = int(input())

weekends_in_Sofia = 48 - weekends_at_home
games_Saturday_Sofia = weekends_in_Sofia * 0.75
games_Sunday_home = weekends_at_home
games_holidays_Sofia = number_of_holidays * (2 / 3)

total_games = games_Saturday_Sofia + games_Sunday_home + games_holidays_Sofia

if year == "leap":
    total_games = total_games + (total_games * 0.15)

print(math.floor(total_games))