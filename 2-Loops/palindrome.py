a=int(input("Enter a number to know if it is palindrome:"))
b=str(a)
if(b==b[::-1]):
    print(a,"is palindrome.")
else:
    print(a,"is not a palindrome.")    