import re
mirror_words = []
result = []

line = input()
pattern = r"(?P<symbol>[@|#])[A-Za-z]{3,}(?P=symbol){2}[A-Za-z]{3,}(?P=symbol)"
valid_word = re.finditer(pattern, line)
length_valid_words = sum(1 for _ in re.finditer(pattern, line))
for word in valid_word:
    pattern_letters = f"[A-Za-z]+"
    match = re.findall(pattern_letters, word.group())

    first_word = match[0]
    second_word = match[1]
    if first_word == second_word[::-1]:
        mirror_words.append(first_word)

if length_valid_words > 0:
    print(f"{length_valid_words} word pairs found!")
else:
    print("No word pairs found!")

if len(mirror_words) > 0:
    print("The mirror words are:")
    for word in mirror_words:
        result.append(f"{word} <=> {word[::-1]}")
    print(", ".join(result))
else:
    print("No mirror words!")