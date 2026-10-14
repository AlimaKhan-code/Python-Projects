a=[10,8,4,6,20]
b=[8,6,17,4,14]
c=[]
print("Common elements in the two lists are:")
for i in a:
    for j in b:
        if i==j:
            c.append(i)
print(c)            
