print("With argument and with returntype")
def sum(a,b):
    return a+b
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
result = sum(a,b)
print(result)


print("Without argument and without returntype")
def sum():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a+b)
sum()


print("With argument and without returntype")
def sum(c,d):
    print(c + d)
c = int(input("enter c: "))
d = int(input("enter d: "))
sum(c,d)


print("Without argument and with returntype")
def sum():
    c = int(input("Enter c: "))
    d = int(input("Enter d: "))
    return c+d
result3 = sum()
print(result3)


