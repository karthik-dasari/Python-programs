#Python program to find the sum of natural using recursive function
def sum(n):
    if n<=1:
        return n
    else:
        return (n+sum(n-1))
a=int(input("Enter a number:"))
print("The sum is",sum(a))