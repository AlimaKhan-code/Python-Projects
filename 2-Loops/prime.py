num=int(input("Enter a number to check if it is prime:"))
a=0
for i in range(2,int(num**0.5)+1):
    if(num%int(i)==0):
        a+=1
if(a<=2):
    print(num,"is a prime number.") 
if(a>2):
    print(num,"is not a prime number.") 
