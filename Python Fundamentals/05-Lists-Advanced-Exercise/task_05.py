max_number = int(input())
distribution = []
electron_sum = 0

for position in range(1, max_number + 1):
    electron = 2 * position ** 2
    electron_sum += electron
    if electron_sum == max_number:
        distribution.append(electron)
        break
    elif electron_sum > max_number:
        difference = max_number - (electron_sum - electron)
        distribution.append(difference)
        break
    distribution.append(electron)

print(distribution)
