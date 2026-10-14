a=input("Enter a number:")
b=len(a)
result=0
for i in a:
    digit=int(i)
    result+=digit**b

if result==int(a):
    print(a,"is an Armstrong number.") 
else:
    print(a,"is not an Armstrong number.")       