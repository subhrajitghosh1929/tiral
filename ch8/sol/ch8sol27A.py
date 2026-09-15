x=int(input("enter the number :"))
y=int(input("enter the number :"))
if x>y:
    smaller=y
else:
    smaller=x
for i in range(1,smaller+1):
    if ((x%i==0)and(y%i==0)):
        hcf=i
lcm=(x*y)/hcf
print("the H.C.F of",x,"and",y,"is",hcf)
print("the L.C.M of",x,"and",y,"is",lcm)
