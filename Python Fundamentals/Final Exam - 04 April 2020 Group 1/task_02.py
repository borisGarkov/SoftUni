import re
data = input()
cool_threshold = 1
emojis_data = []
cool_emojis = []

pattern_digits = r"\d"
digits = re.findall(pattern_digits, data)
for number in digits:
    cool_threshold *= int(number)

pattern_emojis = r"(?P<separator>([:]{2}|[*]{2}))([A-Z][a-z]{2,})(?P=separator)"
emojis = re.finditer(pattern_emojis, data)
for emoji in emojis:
    emojis_data.append(emoji.group())

for emoji in emojis_data:
    pattern_letters = r"\w"
    emoji_letters_data = re.findall(pattern_letters, emoji)
    emoji_ascii_data = [ord(emoji_letter) for emoji_letter in emoji_letters_data]
    if sum(emoji_ascii_data) > cool_threshold:
        cool_emojis.append(emoji)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis_data)} emojis found in the text. The cool ones are:")
print("\n".join(cool_emojis))
