n = int(input("Enter a number: "))
temp = n
rev = 0

while temp > 0:
    rem = temp%10
    rev = rev + (rem**3)
    temp = temp//10

if rev == n:
    print(n,"is an amstrong number")
else:
    print(n,"is not an amstrong number")