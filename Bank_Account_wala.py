balance = 0
def deposite(amount):
    global balance
    balance = balance + amount
    print("Amount Deposited = ",amount)
    print("Balance = ",balance)

def withdraw(amount):
    global balance
    if amount > balance:
        raise Exception('Low balance !')
    balance = balance - amount
    print("Amount Withdrawn= ",amount)
    print("Balance = ",balance)

deposite(1000000)

try:
    withdraw(999999999999999)
except Exception as e:
    print(e)

