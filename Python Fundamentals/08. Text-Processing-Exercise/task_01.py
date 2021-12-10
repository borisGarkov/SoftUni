usernames = input().split(", ")

for user in usernames:
    is_invalid = False
    if 3 < len(user) < 16:
        for letter in user:
            if letter.isdigit() == False and letter.isalpha() == False \
                    and not letter == "-" and not letter == "_":
                is_invalid = True
        if not is_invalid:
            print(user)
