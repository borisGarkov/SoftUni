number = int(input()) + 1

while True:
    year = str(number)
    test = len(set(year))
    if len(set(year)) == len(year):
        print(year)
        break
    number += 1