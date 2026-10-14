s1=input("Enter first string:")
s2=input("Enter second string:")
s1s=s1.replace("","").lower()
s2s=s2.replace("","").lower()
a=len(s1s)
b=len(s2s)
if  a!=b:
    print("These are not anagrams")
if  sorted(s1s)==sorted(s2s):
    print("These are anagrams")      
 
