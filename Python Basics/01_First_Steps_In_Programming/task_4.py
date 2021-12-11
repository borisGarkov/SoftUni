number_of_pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_time = float(number_of_pages / pages_per_hour)
result = float(total_time / days)

print(result)