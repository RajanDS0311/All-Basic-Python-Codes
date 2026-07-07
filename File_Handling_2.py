A = open("student.txt","a")
ch="y"
lst=[]
print("Type of lst=",type(lst))
while(ch=="y"):
    name=input("Enter name to be written on file: ")
    roll=input("Enter roll to be written on file: ")
    fee=input("Enter fee to be written on file: ")
    record=name+" , "+roll+" , "+fee+"\n"
    lst.append(record)
    ch = input("Data is written successfully press y to append more?")

A.writelines(lst)
A.close()

A=open("student.txt","r")
#lst1=[]
print("\n===================Data written of file are===============")
data=A.readlines()
print("type of data= ",type(data))
for line in data :
    print(line,end="")
A.close()