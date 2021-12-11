deposit = float(input())
term_of_deposit = int(input())
interest = float(input())

sum = deposit + term_of_deposit * ((deposit * (interest / 100)) / 12)
print(sum)