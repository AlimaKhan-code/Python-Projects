a=input("Enter a word:")
for i in set (a):
    b=a.count(i)
    print("Frequency of", i ,"in", a,"=", b)