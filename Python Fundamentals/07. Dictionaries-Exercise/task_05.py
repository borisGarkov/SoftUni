n_commands = int(input())
users = {}
for _ in range(n_commands):
    data = input()
    if data.split()[0] == "register":
        _, username, license_number = data.split()
        if username not in users:
            users[username] = license_number
            print(f"{username} registered {license_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_number}")

    else:
        _, username = data.split()
        if username not in users:
            print(f"ERROR: user {username} not found")
        else:
            users.pop(username)
            print(f"{username} unregistered successfully")

for username, license_number in users.items():
    print(f"{username} => {license_number}")
