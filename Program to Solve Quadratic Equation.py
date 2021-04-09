#Python Program to Solve Quadratic Equation
from math import sqrt
print("The quadratic equation is in the form of ax2 + bx + c = 0, where a, b and c are real numbers and a ≠ 0")
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
d = (b**2) - (4*a*c)
x1=(-b-sqrt(d))/(2*a)
x2=(-b+sqrt(d))/(2*a)
print("The roots are ",x1,"and",x2)