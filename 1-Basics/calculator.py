a = int(input("Enter First number:"))
b = int(input("Enter Second number:"))
op = input("Enter operation to be performed:")
result = 0
if(op=="+"):
    result+=a+b
elif(op=="-"):
    result+=a-b
elif(op=="*"):
    result+=a*b
elif(op=="/"):
    result+=a/b
else:
    print("Invalid operation")  
print(result)                  