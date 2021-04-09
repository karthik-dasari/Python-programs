#Python Program to Check Whether a String is Palindrome or Not
s=str(input("Enter a string:"))
s=s.casefold()
rs=reversed(s)
if list(s)==list(rs):
    print("Palindrome")
else:
    print("Not palindrome")