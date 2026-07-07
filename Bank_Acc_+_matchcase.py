balance = 50000
z = "A"

def deposite(amount):
    global balance
    balance = balance + amount
    print("Amount Deposited = ", amount)
    print("Balance = ", balance)


def withdraw(amount):
     global balance
     if amount > balance:
        raise Exception('Low balance !')
     else:
        balance = balance - amount
        print("Amount Withdrawn= ", amount)
        print("Balance = ", balance)

while z == "A":
    try:
        a =int(input("Enter your choice\n1.Deposite\n2.Withdraw\n3.Check Balance\n4.EXIT\n"))
        match a:
                case 1:
                    amount = int(input("Enter amount: "))
                    deposite(amount)

                case 2:
                    amount = int(input("Enter amount: "))
                    withdraw(amount)

                case 3:
                        print("Current balance = ",balance)

                case 4:
                      print("Thank you for your time")

                case _:
                       print("invalid choice")

    except Exception as e:
        print(e)
    print("Press A to continue")
    print("Press anyother key to exit")
    z = input()