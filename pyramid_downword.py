n = int(input("enter rows: "))
for i in range(0,n):
    for j in range(0,n):
        if i > j:
            print(" ",end=" ")
        else:
            print("*"," ",end=" ")
    print()
