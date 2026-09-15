l=input("enter a list :")
m=input("enter another list:")
n=[]
if len(l)==len(m):
    for i in range(len(l)):
        n.append(l[i]+m[i])       
print(n)

