#Python Program to Remove Punctuations From a String
punctuations = r"""!()-[]{};:'"\,<>./?@#$%^&*_~"""
s=str(input("Enter a string:"))
nps= ""
for i in s:
   if i not in punctuations:
       nps=nps+i
print(nps)