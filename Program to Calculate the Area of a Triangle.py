#Python Program to Calculate the Area of a Triangle
from math import sqrt
a=float(input("Enter side 'a':"))
b=float(input("Enter side 'b':"))
c=float(input("Enter side 'c':"))
s = (a+b+c)/2
area = sqrt(s*(s-a)*(s-b)*(s-c))
print("Area = " ,area)