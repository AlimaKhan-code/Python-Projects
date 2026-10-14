n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
a=n1
b=n2
while b:
    a,b = b,a%b
print("GCD=",a) 
c=(n1*n2)//a
print("LCM=",c)
   

