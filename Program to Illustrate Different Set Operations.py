#Python Program to Illustrate Different Set Operations
a1=set()
a2=set()
n1=int(input("Enter number of elements for set1:"))
n2=int(input("Enter number of elements for set2:"))
print("Enter the elements for set1:")
for i in range(0,n1):
        a1.add(int(input()))
print("Enter the elements for set2:")
for i in range(0,n2):
        a2.add(int(input()))
print("Union of set1 and set2 is",a1 | a2)
print("Intersection of set1 and set2 is",a1 & a2)
print("Difference of set1 and set2 is",a1 - a2)
print("Symmetric difference of set1 and set2 is",a1 ^ a2)