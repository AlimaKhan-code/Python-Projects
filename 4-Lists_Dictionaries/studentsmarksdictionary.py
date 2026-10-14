a={"Aman":76, "Rahul":90,"Sonam":74,"Aliya":89,"Sam":68}
b=len(a)
total=0
average=0
highest=""
hmarks=0
lowest=""
lmarks=100
for i in a:
    total+=a[i]
    m=a[i]
    if m>hmarks:
        highest=i
        hmarks=a[i]
    if m<lmarks :
        lowest=i
        lmarks=a[i] 
    if m>30:
        print(i,":",a[i],"Result:Pass")
    elif m<30:
        print(i,a[i],"Result:Fail")


average=total//b    
print("Average marks of students:", average)    
print("Highest Scorer :",highest,":",hmarks)
print("Lowest Scorer :",lowest,":",lmarks)