a=input("Enter any word to check if it is palindrome:")
if(a==a[::-1]):
    print(a,"is palindrome.")
else:
    print(a,"is not a palindrome.") 