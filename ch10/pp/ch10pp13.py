ln=eval(input("enter the no. of  elements for the list : "))
lisA=[]
lisB=[]
for i in range(ln):
    varA=eval(input("enter an element of list A : "))
    lisA.append(varA)
varB=eval(input("enter the lower index : "))
varC=eval(input("enter the upper index : "))
for i in range(varB,varC+1):
    lisB.append(lisA[i])
print(lisB)
print("the maximum in the list in between index ",varB," and ",varC," is ",max(lisB))
print("the minimum in the list in between index ",varB," and ",varC," is ",min(lisB))

