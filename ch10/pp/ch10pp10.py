ln=eval(input("enter the value of n : "))
lisA=[]
lisA.append(0)
lisA.append(1)
for i in range(2,ln):
    lisA.append(lisA[i-2]+lisA[i-1])        ###
print(lisA)
print(lisA[i-2]+lisA[i-1])
