numbers = [int(el) for el in input().split(", ")]

positives = [el for el in numbers if el >= 0]
negatives = [el for el in numbers if el < 0]
evens = [el for el in numbers if el % 2 == 0]
odds = [el for el in numbers if not el % 2 == 0]

print(f"Positive: {', '.join([str(el) for el in positives])}")
print(f"Negative: {', '.join([str(el) for el in negatives])}")
print(f"Even: {', '.join([str(el) for el in evens])}")
print(f"Odd: {', '.join([str(el) for el in odds])}")
