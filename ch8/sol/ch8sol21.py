x=int(input("enter value of x: "))
n=int(input("enter power of(n): "))
s=0
sign=+1
for a in range(n+1):
    term=(x**a)*sign
    s+=term
    sign*=-1
print("sum of first", n, "terms: ",s)
