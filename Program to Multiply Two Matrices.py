#Python Program to Multiply Two Matrices
a1=[]
a2=[]
res=[]
n1=int(input("Enter number of rows in array1 and array2:"))
n2=int(input("Enter number of coloums in array1 and array2:"))
print("Enter the elements for array1:")
for i in range(0,n1):
    row=[]
    for j in range(0,n2):
        row.append(int(input()))
    a1.append(row)
print("Enter the elements for array2:")
for i in range(0,n1):
    row=[]
    for j in range(0,n2):
        row.append(int(input()))
    a2.append(row)
for i in range(0,n1):
    row=[]
    for j in range(0,n2):
        row.append(0)
    res.append(row)
for i in range(0,n1):
    for j in range(0,n2):
        res[i][j]+=a1[i][j]*a2[i][j]
print(res)