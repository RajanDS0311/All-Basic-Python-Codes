print("With argument and with returntype")
def SI(P,R,T):
    return (P*R*T)/100
P = int(input("enter principle: "))
R = int(input("enter rate of interest: "))
T = int(input("enter time: "))
result = SI(P,R,T)
print(result)


print("Without argument and without returntype")
def SI():
    P = int(input("enter principle: "))
    R = int(input("enter rate of interest: "))
    T = int(input("enter time: "))
    print((P*R*T)/100)
SI()


print("With argument and without returntype")
def SI(P,R,T):
    print((P*R*T)/100)
P = int(input("enter principle: "))
R = int(input("enter rate of interest: "))
T = int(input("enter time: "))
SI(P,R,T)


print("Without argument and with returntype")
def SI():
    P = int(input("enter principle: "))
    R = int(input("enter rate of interest: "))
    T = int(input("enter time: "))
    return (P*R*T)/100
result3 = SI()
print(result3)


