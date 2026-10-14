a=int(input("Enter starting number:"))
b=int(input("Enter ending number:"))
print("Prime numbers in range",a, "to", b, "are:")

for i in range(a,b+1):
    if i>1:
        a=0
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                a+=1
                break
        if a==0:
            print(i)    
