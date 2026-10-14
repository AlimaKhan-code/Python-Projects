a=[10,8,10,4,4,3,6,20]
newlist=[]
for i in a:
    if i not in newlist:
        newlist.append(i)
print(newlist)        