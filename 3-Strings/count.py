a=input("Enter string to count:")
spaces=0
vowels=0
consonants=0
digits=0
for i in a:
    if i==" ":
        spaces+=1
    elif i in"0123456789":
        digits+=1
    elif i in"aeiouAEIOU":
        vowels+=1
    elif i.isalpha():
        consonants+=1  
print("digits=", digits)
print("spaces=", spaces)
print("vowels=", vowels)
print("cononants", consonants)                
