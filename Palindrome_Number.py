n = int(input("Enter a number: "))
temp=n
rev=0
while temp>0 :
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10

if rev ==n:
    print(n,"is a palindrome number")
else:
    print(n,"is not a palindrome number")