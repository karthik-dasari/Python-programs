#Python Program to Find the Factorial of a Number
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
a=int(input("Enter a number:"))
b=fact(a)
print(b)        