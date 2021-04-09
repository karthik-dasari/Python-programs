#Python Program to Find Numbers Divisible by Another Number
lst=[]
res=[]
n=int(input("Enter no of elements:"))
for i in range(0, n): 
    ele = int(input("Enter an element:")) 
    lst.append(ele)
a=int(input("Enter a number to divide:"))
#res = list(filter(lambda x: (x % 13 == 0), my_list))
for i in lst:
    if i%a==0:
        res.append(i)
print(res)        