n = int(input("Enter a number: "))
i = 2
count = 0
for i in range (2,n):
    k = 0
    for j in range(2,i):
        if i % j == 0:
          k = k + 1
          break

    if k == 0:
      print(i,"is a prime number")
      count = count + 1
print("There are total ",count,"prime numbers upto= ",n)



