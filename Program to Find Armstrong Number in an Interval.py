a=int(input("Enter a lower number:"))
b=int(input("Enter a upper number:"))
for i in range(a,b+1):
    n = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        r = temp % 10
        sum += r ** n
        temp //= 10
    if i == sum:
        print(i)
        