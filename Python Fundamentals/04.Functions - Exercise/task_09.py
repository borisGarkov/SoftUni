def factorial(num_1, num_2):
    fact_1 = 1
    fact_2 = 1

    for i in range(1, num_1 + 1):
        fact_1 = fact_1 * i

    for i in range(1, num_2 + 1):
        fact_2 = fact_2 * i

    print(f"{fact_1 / fact_2:.2f}")

num_1 = int(input())
num_2 = int(input())
factorial(num_1, num_2)