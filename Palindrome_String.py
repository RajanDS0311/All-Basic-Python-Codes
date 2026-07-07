text = input("Enter a string: ")

if text == text[::-1]:
    print(f"{text} is Palindrome")
else:
    print(f"{text} is Not a Palindrome")