s=input("Enter the string: ")
dsum=0
for a in s:
    if a.isdigit():
        dsum+=int(a)
print("sum of string digits is",dsum)
