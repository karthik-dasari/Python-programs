#Python Program to Display Fibonacci Sequence Using Recursion
def fib(n):
    if n<=1:
        return(n)
    else:
        return(fib(n-1)+fib(n-2))
nterms=int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(nterms):
   print(fib(i))    