#Python Program To Display Powers of 2 Using Anonymous Function
n = int(input("Enter upto which term:"))
a = list(map(lambda x: 2 ** x, range(n)))
for i in range(n):
   print("2 raised to power",i,"is",a[i])