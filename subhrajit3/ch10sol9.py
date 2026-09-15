lst=eval(input("enter a list"))
lst2=[]
M,N=eval(input("enters two no. as m,n:"))
for n in lst:
    if(n%M == 0 and n%N == 0 ):
        lst2.append(n)
print("new created list is :",lst2)
