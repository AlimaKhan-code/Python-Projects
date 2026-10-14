print("PASSWORD STRENGTH CHECKER")
password=input("Enter password:")
l=len(password)
uppercase=0
lowercase=0
numbers=0
characters=0
minimumlength=10
for i in password:
    if i.isdigit():
        numbers+=1
    if i.islower():
        lowercase+=1
    if i.isupper():
        uppercase+=1
    if i in "!@#$%^&*()-_=+":
        characters+=1
if uppercase==0 or lowercase==0 or numbers==0 or characters==0 or l<minimumlength:
    print("Weak password.")
else:
    print("Strong password.")                    
