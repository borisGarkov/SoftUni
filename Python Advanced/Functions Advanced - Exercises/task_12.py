def palindrome(text, index=0, last=-1):
    if index == len(text) // 2:
        return f"{text} is a palindrome"

    if text[index] == text[last]:
        return palindrome(text, index+1, last-1)
    else:
        return f"{text} is not a palindrome"


print(palindrome("abcba", 0))
