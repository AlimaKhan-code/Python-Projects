expenses=[{"Date":"1/5/2026","Category":"Rent","Description":"Room rent","Amount":5000},{"Date":"3/5/2026","Category":"Education","Description":"Bought books","Amount":500}]

def add_expense():
    date=(input("Enter date(dd/mm/yyyy):"))
    category=input("Enter the category of expense:")
    description=input("Enter the description:")
    amount=float(input("Enter amount:"))
    new_expense={"Date":date,"Category":category,"Description":description,"Amount":amount}    
    expenses.append(new_expense)
    print("Expense added successfully.")

def view_expenses():
    for i,expense in enumerate(expenses, start=1):
        print(i,expense)

def calculate_total():
    total=0 
    for i in expenses:
        amt=i["Amount"]      
        total+=amt
    print("Total amount spent:", total)

def category_total():
    education=0
    entertainment=0
    transport=0
    rent=0
    other=0
    for i in expenses:
        if i["Category"]=="Education":
            amt=i["Amount"]
            education+=amt
        elif i["Category"]=="Entertainment":
            amt=i["Amount"]
            entertainment+=amt 
        elif i["Category"]=="Transport":
            amt=i["Amount"]
            transport+=amt
        elif i["Category"]=="Rent":
            amt=i["Amount"]
            rent+=amt   
        elif i["Category"]=="Other":
            amt=i["Amount"]
            other+=amt
        else:
            print("Invalid categoryu.")


    if education>0:
        print("Education:", education)
    if transport>0:    
        print("Transport:", transport)
    if entertainment>0:    
        print("Entertainment:", entertainment)
    if rent>0:    
        print("Rent:", rent)
    if other>0:    
        print("Other:", other)
    calculate_total()  

def exit_program():
    print("You have exited")

print("EXPENSE TRACKER")
print("TRACK YOUR EXPENSES")
while True:
    choice=input("Press 1:To view expense \n" "2:To add expenses \n" "3:To calculate total \n" "4:To calculate category-wise total \n" "5:To exit program:")
    if choice=="1":
        view_expenses() 
    elif choice=="2":   
        add_expense()
    elif choice=="3":
        calculate_total()
    elif choice=="4":
        category_total()
    elif choice=="5":
        exit_program()
        break
    else:
        print("Invalid choice.") 
        





       

