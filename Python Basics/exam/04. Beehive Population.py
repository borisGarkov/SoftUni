population = int(input())
years = int(input())
total_bees = 0

for year in range(1, years + 1):
    population += (population // 10) * 2
    if year % 5 == 0:
        population -= (population // 50) * 5

    population -= (population // 20) * 2

print(f"Beehive population: {population}")
