print("CALCULATOR")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=input("Enter the operation to be performed:")

def add(a,b,c):
    s=a+b
    print(a,c,b,"=",s)
    return s
def subtract(a,b,c):
    s=a-b  
    print(a,c,b,"=",s)
    return s 
def multiply(a,b,c):
    s=a*b  
    print(a,c,b,"=",s)
    return s 
def divide(a,b,c):
    s=a/b  
    print(a,c,b,"=",s)
    return s     


if c=="+":
    add(a,b,c)
if c=="-":
    subtract(a,b,c)    
if c=="*":
    multiply(a,b,c)     
if c=="/":
    divide(a,b,c)     
    