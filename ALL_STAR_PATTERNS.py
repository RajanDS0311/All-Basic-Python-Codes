##SQUARE WALA
# n = 5
# for i in range(0,n):
#     for j in range(0,n):
#         print("*",end=" ")
#     print()


##ASCENDING WALA
# n = 5
# for i in range(0,n+1):
#     for j in range(0,i):
#         print("*",end=" ")
#     print()


##DESCENDING WALA
# n = 5
# for i in range(n+1,0,-1):
#     for j in range(0,i):
#         print("* ",end="")
#     print()

##ASCENDING (R-L)
n = 6
for i in range(1,n+1):
    for j in range(n,1,-1):
        if i < j:
            print(" ",end="")
        else:
            print("*",end="")
    print()