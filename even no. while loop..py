n = int(input("Enter a number: "))
count = 0
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
        count += 1
    i+= 1
print(count,"numbers of even numbers upto ",n)