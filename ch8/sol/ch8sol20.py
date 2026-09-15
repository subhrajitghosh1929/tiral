x=float(input("enter value of x: "))
n=int(input("enter value of n (for x**n): "))
s=0
for a in range (n+1):
    s+=x**a
print("sum of first",n,"terms :",s)
