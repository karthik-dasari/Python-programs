#Python Program to Find the Largest Among Three Numbers
a=float(input("Enter 1st number:"))
b=float(input("Enter 2nd number:"))
c=float(input("Enter 3rd number:"))
if (a>=b and a>=c):
    print("{} is larger".format(a))
elif (b>=c and b>=a):
    print("{} is larger".format(b))    
elif (c>=a and c>=b):
    print("{} is larger".format(c))

