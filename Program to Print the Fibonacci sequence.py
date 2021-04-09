#Python Program to Print the Fibonacci sequence
def fab(n):
    x=0
    y=1
    if n==1:
        print(x)
    else:
        print(x)
        print(y)
        for i in range(2,n+1):
            z=x+y
            x=y
            y=z
            print(z)    
a=int(input("Enter a number:"))
fab(a)