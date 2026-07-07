n = int(input("Enter a number: "))
i = 2
count=0
while i < n:
    j = 2
    k = 0
    while j < i:
      if i % j == 0:
        k += 1
        break
      j = j + 1

    if k == 0:
     print(i,"is a prime number")
     count = count + 1
    i = i + 1
print("There are total ",count,"prime numbers upto= ",n)