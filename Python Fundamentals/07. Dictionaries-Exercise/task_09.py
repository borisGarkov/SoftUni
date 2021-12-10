forces = {}
is_break = False

while True:
    data = input()
    if data == "Lumpawaroo":
        break

    data = data.split(" | ")
    if len(data) > 1:
        side, user = data
        for key, value in forces.items():
            if user in value:
                is_break = True
                break
        if is_break:
            break
        if side not in forces:
            forces[side] = [user]
        else:
            if user not in forces[side]:
                forces[side].append(user)
    else:
        user, side = data[0].split(" -> ")
        for key, value in forces.items():
            if user in value:
                forces[key].remove(user)
        if side not in forces:
            forces[side] = [user]
        else:
            if user not in forces[side]:
                forces[side].append(user)
        print(f"{user} joins the {side} side!" )

sorted_forces = sorted(forces.items(), key=lambda x: (-len(x[1]), x[0]))
for side, users in sorted_forces:
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in sorted(users):
            print(f"! {user}")
