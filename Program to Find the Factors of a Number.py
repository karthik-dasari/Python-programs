#Python Program to Find the Factors of a Number
a=int(input("Enter a number:"))
for i in range(1,a+1):
    print("The factors are:")
    if(a%i==0):
        print(i)