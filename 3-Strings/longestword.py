a=input("Enter a sentence to know its longest word:")
b=a.split()
result=" "
for i in b:
    c=len(i)
    if c>len(result):
        result=i
print(result)         
       

    
