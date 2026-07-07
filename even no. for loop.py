n = int(input("Enter a number: "))
i = 1
count=0
for i in range(1,n+1):
    if (i % 2 == 0):
        print(i)
        count+=1

print(count," numbers of even numbers upto ",n)
