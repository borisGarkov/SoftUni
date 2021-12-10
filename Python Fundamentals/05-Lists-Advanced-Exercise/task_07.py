secret_words = input().split()
decipher_words = []

for word in secret_words:

    get_digit = "".join([char for char in word if char.isdigit()])
    replace_letter = chr(int(get_digit))
    decipher_word = list(word.replace(get_digit, replace_letter))
    decipher_word[1], decipher_word[-1] = decipher_word[-1], decipher_word[1]
    decipher_word = "".join(decipher_word)
    decipher_words.append(decipher_word)

print(*decipher_words)

