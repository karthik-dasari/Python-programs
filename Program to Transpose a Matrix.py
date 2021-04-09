#Python Program to Transpose a Matrix
a1=[]
res=[]
n1=int(input("Enter number of rows in array:"))
n2=int(input("Enter number of coloums in array:"))
print("Enter the elements for array:")
for i in range(0,n1):
    row=[]
    for j in range(0,n2):
        row.append(int(input()))
    a1.append(row)
for i in range(0,n1):
    row=[]
    for j in range(0,n2):
        row.append(0)
    res.append(row)
for i in range(0,n1):
    for j in range(0,n2):
        res[j][i]=a1[i][j]
print(res)