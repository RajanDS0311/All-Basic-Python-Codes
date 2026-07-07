mylist=["Ketan","Pranay","Rajan","Anuj","Ishant","Rajan","Trinkesh"]
print(mylist)

mylist.append("Atharva")
print(mylist)

mylist.insert(2,"Hardik")
print(mylist)

mylist.remove("Anuj")
print(mylist)

mylist.pop(1)
print(mylist)

mylist.sort()
print(mylist)

mylist.reverse()
print(mylist)

mylist.count("Rajan")
print(mylist.count("Rajan"))

m=mylist.index("Rajan")
print(m)

mylist.sort(reverse=True)
print(mylist)

print(len(mylist))

yourlist =[1,2,3,4,5,6]

mylist.extend(yourlist)
print(mylist)


