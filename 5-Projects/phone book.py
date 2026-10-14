contacts=[{"Name":"Rahul","Phone":"9876543218", "Email":"rahul12@gmail.com"}, {"Name":"Riya","Phone":"9876833218", "Email":"riya1243@gmail.com"},{"Name":"Sonam","Phone":"8976543328", "Email":"sonam98@gmail.com"}]

def view_contacts():
    for i,contact in enumerate(contacts, start=1):
        print(i,contact)

def add_contact():
    name=(input("Enter name:"))
    email=input("Enter the email:")
    phone=(input("Enter Phone number:"))
    new_contact={"Name":name,"Email":email,"Phone":phone}    
    contacts.append(new_contact)
    print("Contact added successfully.")

def search_contact():
    search=input("Enter contact name to search contact:")
    for i in contacts:
        if i["Name"]==search:
            print(i)    

def update_contact():
    update=input("Enter contact name to update:")
    for i in contacts:
        if i["Name"]==update:
            print(i)
            key=input("Press 1:To update name 2:To update phone 3:To update email:")
            if key=="1":
                newname=input("Enter new name:")
                i["Nmae"]=newname
                print("Contact updated successfully.")
                print(i)
            elif key=="2":
                newphone=input("Enter new phone number:")
                i["Phone"]=newphone
                print("Contact updated successfully.")
                print(i)
            elif key=="3":
                newmail=input("Enter new email:")
                i["Email"]=newmail
                print("Contact updated successfully.")
                print(i)
            else:
                print("Invalid choice.") 
        else:
            print("Contact not found.")              

def delete_contact():
    delete=input("Enter contact name to delete:")
    for i in contacts:
        if i["Name"]==delete:
            contacts.remove(i)
            print("Contact deleted successfully.")
            break
        else:
             print("Contact not found.")     


def exit_program():
    print("You have exited phone book.")

print("PHONE BOOK")    
while True:
    choice=input("Press 1:To view contacts \n" "2:To add new contact \n" "3:To search contact \n" "4:To delete contact \n" "5:To exit program:")
    if choice=="1":
        view_contacts() 
    elif choice=="2":   
        add_contact()
    elif choice=="3":
        search_contact()
    elif choice=="4":
        delete_contact()
    elif choice=="5":
        exit_program()
        break
    else:
        print("Invalid choice.") 
