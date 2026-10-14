year = int(input("Enter a year:"))
y = str(year)
if (year % 4==0):
    print("This is a leap year.")
elif (y[2] ==0 and y[3] ==0):
    print("This is a leap year.") 
else:
    print("This is not a leap year.")   