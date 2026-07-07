try:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = a / b

except ZeroDivisionError:
        print("Division by Zero is not allowed ")
else:
    print(c)

finally:
    print("Code ended successfully !!!")