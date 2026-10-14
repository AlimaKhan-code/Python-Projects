import random
print("GUESSING GAME")
a=random.randint(1,10)
b=int(input("Enter a number between 1 to 10:"))
while a!=b:
    print("Try again.")
    b=int(input("Enter a number again:"))
    

print("Computer :",a)
print("You:",b)
print("You guessed it right.")
    
