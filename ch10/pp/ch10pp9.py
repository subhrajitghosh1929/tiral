ln=eval(input("enter the no. of  elements for both lists : "))
lisA,lisB=[],[]
for i in range(ln):
    varA=eval(input("enter an element of list A : "))
    lisA.append(varA)
for i in range(ln-1):
    lisB.append(lisA[i])
lisB.insert(0,lisA[ln-1])
print(lisA)
print(lisB)
