def palindrome_check(number):
    for num in number:
        reversed_string = "".join(reversed(num))
        if reversed_string == num:
            print("True")
        else:
            print("False")

number = input().split(", ")
palindrome_check(number)