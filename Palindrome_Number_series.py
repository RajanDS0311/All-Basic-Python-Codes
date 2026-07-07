n = int(input("Enter a number: "))
i = 0
count = 0
while i <= n:
        temp=i
        rev=0
        while temp>0 :
             rem=temp%10
             rev=rev*10+rem
             temp=temp//10

        if rev ==i:
            print(i,"is a palindrome number")
            count = count+1
        i = i + 1
print("total palindrome no upto ",n ," are", count)