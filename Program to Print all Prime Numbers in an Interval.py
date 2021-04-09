#python Program to Print all Prime Numbers in an Interval
a=int(input("Enter lower number:"))
b=int(input("Enter upper number:"))
for i in range(a,b):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            print(i) 
            break