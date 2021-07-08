line = input().split()
even_words = [el for el in line if len(el) % 2 == 0]

print("\n".join(even_words))
