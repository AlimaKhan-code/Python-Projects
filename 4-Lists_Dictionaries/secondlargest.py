a=[10,8,4,6,20]
largest=0
second_largest=0
for i in a:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i!=largest:
            second_largest=i
print("Second Largest=", second_largest)