a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

c=int(input("Enter your choice (1.Add\n 2.Sub\n 3.Multiply\n 4.Divide): "))
match  c :
    case 1 :  print('sum of ',a,' + ',b,' is ',a+b)
    case 2 : print('sub of ',a,' + ',b,' is ',a-b)
    case 3 : print('multiplication of ',a,' * ',b,' is ',a*b)
    case 4 : print('division of ',a,' / ',b,' is ',a/b)
    case _ : print(c,"is wrong choice ")

