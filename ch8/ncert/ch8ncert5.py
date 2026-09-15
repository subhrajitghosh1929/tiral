n=int(input("enter list: "))
sign=-1
for  i in range(5,n,5):
    term=i*sign
    sign=sign*-1
    print(term,end=" ")
