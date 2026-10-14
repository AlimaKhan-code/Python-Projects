tasks=[{"Task":"Attend school", "Status":"Completed"},{"Task":"Shopping", "Status":"Pending"},{"Task":"Tuition class", "Status":"Pending"}]

def view_task():
    print("Tasks")
    for i, task in enumerate(tasks, start=1):
        print(i, task)
       
def add_task():
    new=input("Enter new task:")
    new_task={
        "Task":new,
        "Status":"Pending"
    }
    tasks.append(new_task)  
    print("Task added successfully.")
    view_task()

def delete_task():
    view_task()
    delete=int(input("Enter task number to delete:")) 
    if 1 <= delete <= len(tasks):
        tasks.pop(delete-1) 
        print("Task deleted successfully.") 
    else:
        print("Invalid number.")

def mark_status():
    view_task()
    update=int(input("Enter task number to update:"))
    if 1 <= update <= len(tasks):
        tasks[update-1]["Status"]="Completed"
        print("Task marked as completed")
    else:
        print("Invalid task number.") 

def exit_program():
    print("You have exited")
                

while  True:
    choice=input("Press 1:To view tasks" "\n2:To add task" "\n3:To delete task" "\n4:To update status" "\n5:To exit")
    if choice=="1":
        view_task()
    elif choice=="2":
        add_task()
    elif choice=="3":
        delete_task()
    elif choice=="4":
        mark_status()
    elif choice=="5":
        exit_program()
        break
    else:
        print("Invalid choice")    







