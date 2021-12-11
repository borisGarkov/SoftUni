steps_input = input()
steps = 0
additional_steps = 0

while steps <= 10000:

    if steps_input != "Going home":
        steps += int(steps_input)

    if steps_input == "Going home":
        additional_steps = int(input())
        steps += additional_steps
        if steps >= 10000:
            print(f"Goal reached! Good job!\n{steps - 10000} steps over the goal!")
            break
        else:
            print(f"{10000 - steps} more steps to reach goal.")
            break

    if steps >= 10000:
        print(f"Goal reached! Good job!\n{steps - 10000} steps over the goal!")
        break

    steps_input = input()
