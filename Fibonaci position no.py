n = int(input("Enter the position: "))
a = 0
b = 1
count = 0

if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
    print(b)