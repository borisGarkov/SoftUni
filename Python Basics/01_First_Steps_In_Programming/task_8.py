lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = lenght * width * height
liters = volume * 0.001

result = liters * (1 - (percent * 0.01))

print(result)