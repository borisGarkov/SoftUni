count = int(input())
salary = int(input())

for i in range(1, count + 1):
    website = input()

    if website == "Facebook":
        salary -= 150
    if website == "Instagram":
        salary -= 100
    if website == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)