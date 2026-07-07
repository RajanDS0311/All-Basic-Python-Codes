R = open("jay.txt", "w")
ch = "y"
while ch == "y":
    data = input("Enter your Data: ")
    data = data + "\n"
    R.write(data)
    ch = input("Data is written succesfully press y to append more?")
R.close()

R = open("jay.txt","r")
print("---------------Data Written in file is --------------- ")
print(R.read())
R.close()