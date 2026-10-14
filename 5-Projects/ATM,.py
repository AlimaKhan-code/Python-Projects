print("ATM")

balance=10000

def check_balance():
    print("Your total balance:", balance)

def deposit():
    global balance
    credit=int(input("Enter amount to deposit:"))
    balance+=credit
    print("Deposit Amount:",credit)
    check_balance()

def withdraw():
    global balance
    debit=int(input("Enter amount to withdraw:"))
    if debit<=balance:
        balance-=debit
        print("Withdrawn amount:",debit)
        check_balance()
    else:
        print("Insufficient balance")
        check_balance()
    

def exit():
    print("You have exited.")

while True:
    choice=input("Press 1: To check balance" "\n2:To deposit amount" "\n3:To withdraw amount" "\n4:To exit:")    

    if choice=="1":
        check_balance()
    elif choice=="2":
        deposit()
    elif choice=="3":
        withdraw()
    elif choice=="4":
        exit()
        break
    else:
        print("Invalid choice.")        
    






         

   