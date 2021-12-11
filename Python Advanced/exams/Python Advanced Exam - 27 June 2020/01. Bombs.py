effects = list(map(int, input().split(", ")))
casings = list(map(int, input().split(", ")))
BOMBS = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}

bombs_created = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}

while True:
    effect = effects[0]
    casing = casings[-1]
    total = effect + casing

    if total in BOMBS:
        bomb_name = BOMBS[total]
        bombs_created[bomb_name] += 1
        effects = effects[1:]
        casings.pop()
    else:
        casings[-1] -= 5

    if not effects or not casings:
        print("You don't have enough materials to fill the bomb pouch.")
        break

    if bombs_created["Datura Bombs"] >= 3 and bombs_created["Cherry Bombs"] >= 3 \
            and bombs_created["Smoke Decoy Bombs"] >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        break


if not effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(map(str, effects))}")

if not casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(map(str, casings))}")

bombs_created = sorted(bombs_created.items(), key=lambda x: x)
for key, value in bombs_created:
    print(f"{key}: {value}")
