money = float(input())
money = money * 100
i = 0

while money >= 200:
    i+=1
    money = money - 200
while money >= 100:
    i+=1
    money = money - 100
while money >= 50:
    i+=1
    money = money - 50
while money >= 20:
    i+=1
    money = money - 20
while money >= 10:
    i+=1
    money = money - 10
while money >= 5:
    i+=1
    money = money - 5
while money >= 2:
    i+=1
    money = money - 2
while money >= 1:
    i +=1
    money = money - 1

print(i)