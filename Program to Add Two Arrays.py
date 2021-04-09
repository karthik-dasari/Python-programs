#Python Program to Add Two Arrays
a1=list()
a2=list()
res=list()
n=int(input("Enter number of elements in array1 and array2:"))
print("Enter the elements for array1:")
for i in range(0,n):
    e1=int(input())
    a1.append(e1)
print("Enter the elements for array2:")
for j in range(0,n):
    e2=int(input())
    a2.append(e2)
print("Sum:")
for k in range(0,n):
    res.append(a1[k]+a2[k])
print(res)