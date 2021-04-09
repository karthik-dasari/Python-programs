#Python Program to Check Prime Number
a=int(input("Enter a number:"))
for i in range(2,a):
    if a%i==0:
        print("Not prime")
        break
    else:
        print("Prime") 
        break