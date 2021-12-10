experience_needed = float(input())
battles_count = int(input())
total = 0
did_manage = False

for battle in range(1, battles_count + 1):
    experience_earned_per_battle = float(input())

    if battle % 3 == 0:
        experience_earned_per_battle += experience_earned_per_battle * 0.15
    if battle % 5 == 0:
        experience_earned_per_battle -= experience_earned_per_battle * 0.10
    if battle % 15 == 0:
        experience_earned_per_battle += experience_earned_per_battle * 0.05

    total += experience_earned_per_battle
    if total >= experience_needed:
        did_manage = True
        break

if did_manage:
    print(f"Player successfully collected his needed experience for {battle} battles.")
else:
    print(f"Player was not able to collect the needed experience, {experience_needed - total:.2f} more needed.")