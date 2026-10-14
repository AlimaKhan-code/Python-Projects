num= int(input("Enter a number for fibonacci series:"))
result=[0,1]
print("Fibonacci series:")
for i in range(num+1):
    a=result[-1]+result[-2]
    result.append(a)
print(result)    
