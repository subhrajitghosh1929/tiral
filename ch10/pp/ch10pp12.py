ln=eval(input("enter the no. of  elements for both lists : "))
num,denum,lis=[],[],[]
for i in range(ln):
    varA=eval(input("enter an element of list A : "))
    varB=eval(input("enter an element of list B : "))
    num.append(varA)
    denum.append(varB)
for i in range(ln):
    lis.append(num[i]/denum[i])
for i in range(ln):    
    print(i,"\t",lis[i])    
print("the minimum fraction in the list is ",min(lis)," at index ", lis.index(min(lis)))
