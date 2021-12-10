import re
n = int(input())
counter = 0
for _ in range(n):
    registration = input()
    pattern = r"U\$(?P<name>[A-Z][a-z]{2,})U\$P@\$(?P<password>[A-Za-z]{5,}[\d]+)P@\$"
    match = re.match(pattern, registration)
    if match:
        counter += 1
        print("Registration was successful")
        print(f"Username: {match.group('name')}, Password: {match.group('password')}")
    else:
        print("Invalid username or password")

print(f"Successful registrations: {counter}")