n = int(input("Enter a number: "))
i = 0
count = 0
while i <= n:
    temp = i
    rev = 0

    while temp > 0:
        rem = temp%10
        rev = rev + (rem**3)
        temp = temp//10

    if rev == i:
        print(i,"is an amstrong number")
        count = count + 1
    i = i + 1
print("total amstrong no upto ",n ," are", count)