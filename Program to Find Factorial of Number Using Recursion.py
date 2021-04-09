#Python Program to Find Factorial of Number Using Recursion
def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)
a=int(input("Enter a number:"))
if a==0:
    print("Factorial is 1")
else:
    print("Factorial is",factorial(a))