a=[10,8,4,6,20]
largest=a[0]
smallest=a[0]
for i in a:
    if i>largest:
        largest=i
    if i<smallest:
            smallest=i
print("Largest=",largest)
print("Smallest=", smallest)

