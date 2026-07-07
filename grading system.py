physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry  marks: "))
maths = float(input("Enter Maths marks: "))

total = physics + chemistry + maths
print("Your total marks are: " ,total)

percentage = (physics + chemistry + maths) / 300 * 100
print("Your got" ,percentage, " %")

if percentage >= 90:
    print("Your grade is A")
elif percentage >= 80:
    print("Your grade is B")
elif percentage >= 70:
    print("Your grade is c")
else:
    print("FAILED")