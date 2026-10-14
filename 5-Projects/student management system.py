import json
import os


students=[{"Name":"Aryan","Marks":{"Maths":80,"Chemistry":90,"Physics":79},"Average":83,"Grade":"B"},{"Name":"Avni","Marks":{"Maths":80,"Chemistry":60,"Physics":80},"Average":73,"Grade":"C"}]

def save_students(students):
    with open("students.json","w")as file:
        json.dump(students,file,indent=4)
    students=load_students()
    print("Student data saved successfully.")

def load_students():
    if os.path.exists("students.json"):
        with open("students.json","r") as file:
            return json.load(file)
    return[]


def view_students():
    for i,student in enumerate(students, start=1):
        print(i,student)

def DETERMINE_GRADE(average):
    if average>=90:
        return "A"
    elif average>=80:
        return"B"    
    elif average>=70:
        return "C"
    elif average>=60:
        return "D"
    else:
        return "F"     


def add_student():
    name=(input("Enter name:"))
    maths=int(input("Enter Maths marks::"))
    chemistry=int(input("Enter chemistry marks"))
    physics=int(input("Enter physics marks"))
    marks={"Maths":maths,"Chemistry":chemistry,"Physics":physics}
    average=(maths+chemistry+physics)//3
    grade=DETERMINE_GRADE(average)
    new_student={"Name":name,"Marks":marks,"Average":average,"Grade":grade}    
    students.append(new_student)
    save_students(students)
    print("Student added and saved successfully.")


def search_student():
    search=input("Enter student name to search student:")
    for i in students:
        if i["Name"]==search:
            print(i)    

def update_student():
    update=input("Enter student name to update:")
    for i in students:
        if i["Name"]==update:
            print(i)
            key=input("Press 1:To update name 2:To update marks ")
            if key=="1":
                newname=input("Enter new name:")
                i["Name"]=newname
                print("Student added successfully.")
                print(i)
            elif key=="2":
                nmaths=int(input("Enter Maths marks::"))
                nchemistry=int(input("Enter chemistry marks"))
                nphysics=int(input("Enter physics marks"))
                newmarks={"Maths":nmaths,"Chemistry":nchemistry,"Physics":nphysics}
                i["Marks"]=newmarks
                naverage=(nmaths+nchemistry+nphysics)//3
                i["Average"]=naverage
                print("Marks updated successfully.")
                newgrade=DETERMINE_GRADE(naverage)
                i["Grade"]=newgrade
                print(i)
            else:
                print("Invalid choice.") 
        else:
            print("Student not found.") 

def delete_student():
    delete=input("Enter student name to delete:")
    for i in students:
        if i["Name"]==delete:
            students.remove(i)
            print("Student deleted successfully.")
            break
        else:
             print("Student not found.")


def exit_program():
    print("You have exited student management system..")


print("STUDENT MANAGEMENT SYSTEM")    
while True:
    choice=input("Press 1:To view students \n" "2:To add new student \n" "3:To search student \n" "4:To delete student \n" "5:To update student\n" "6:To exit program:")
    if choice=="1":
        view_students() 
    elif choice=="2":   
        add_student()
    elif choice=="3":
        search_student()
    elif choice=="4":
        delete_student()
    elif choice=="5":
        update_student()    
    elif choice=="6":
        exit_program()
        break
    else:
        print("Invalid choice.") 

