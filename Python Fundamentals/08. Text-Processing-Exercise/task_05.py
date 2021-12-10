text = input()
emotions = []
emotion = ""
for letter in range(len(text)):
    if text[letter] == ":":
        emotion += text[letter] + text[letter + 1]
        emotions.append(emotion)
        emotion = ""

print("\n".join(emotions))
