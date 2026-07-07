n = int(input("Enter a number: "))
i = 2
k = 0
while i < n:
    if n % i == 0:
        k += 1
        break
    i = i + 1

if k == 0:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")