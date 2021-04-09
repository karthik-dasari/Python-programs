#Python Program to Count the Number of Each Vowel
a=input("Enter a string:")
count=0
l=len(a)
a=a.casefold()
for i in range(0,l):
    if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u' :
        count+=1
print(count)