ln=eval(input("enter the no. of  elements for both lists : "))
lisA,lisB=[],[]
for i in range(ln):
    varA=eval(input("enter an element of list A : "))
    varB=eval(input("enter an element of list B : "))
    lisA.append(varA)
    lisB.append(varB)
for i in range(ln):
    if lisA[i]!=lisB[i]:
        print("the list differ at index ",i)
        break    
else:
    print("the list does not differ ")


        
