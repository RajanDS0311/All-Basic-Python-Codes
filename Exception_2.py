try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a / b
except ZeroDivisionError :
    print("Zero division by zero")
except ValueError :
    print("invalid input")
else:
    print(c)
finally:
    print("Code ended successfully")