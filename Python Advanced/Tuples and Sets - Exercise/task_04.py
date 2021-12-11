text = input()
nums_and_occurances = {}

for letter in text:
    if letter not in nums_and_occurances:
        nums_and_occurances[letter] = 0
    nums_and_occurances[letter] += 1

nums_and_occurances = sorted(nums_and_occurances.items(), key=lambda x: x[0])
for key, value in nums_and_occurances:
    print(f"{key}: {value} time/s")
