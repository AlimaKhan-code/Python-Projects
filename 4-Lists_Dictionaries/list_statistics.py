a=[10,8,4,6,20]
b=len(a)
sum=0
average=0
largest=a[0]
smallest=a[0]
for i in a:
    sum=sum+i
    if i>largest:
        largest=i
    if i<smallest:
            smallest=i
average+=sum/b            

print("Sum=",sum)
print("Average=",average)
print("Minimum=",smallest)
print("Maximum=", largest)