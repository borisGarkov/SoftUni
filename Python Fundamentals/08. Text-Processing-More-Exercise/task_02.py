start = ord(input())
end = ord(input())
string = input()
sum = 0

for char in string:
    if start < ord(char) < end:
        sum += ord(char)

print(sum)