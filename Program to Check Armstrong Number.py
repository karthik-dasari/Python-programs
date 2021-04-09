#Python Program to Check Armstrong Number
a=int(input("Enter a number:"))
n = len(str(a))
sum = 0
temp = a
while temp > 0:
   r = temp % 10
   sum += r ** n
   temp //= 10
if a == sum:
   print("Armstrong number")
else:
   print("not an Armstrong number")
