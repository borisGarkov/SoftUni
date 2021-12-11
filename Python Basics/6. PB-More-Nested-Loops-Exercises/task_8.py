boundary_hundredths = int(input())
boundary_tens = int(input())
boundary_ones = int(input())

for hundredths in range(1, boundary_hundredths + 1):
    if hundredths % 2 == 0:
        for tens in range(2, boundary_tens + 1):

            is_prime = True
            for i in range(2, (tens // 2) + 1):
                if tens % i == 0:
                    is_prime = False

            if is_prime:
                for ones in range(1, boundary_ones + 1):
                    if ones % 2 == 0:
                        print(f"{hundredths} {tens} {ones}")
                    else:
                        continue
    else:
        continue
