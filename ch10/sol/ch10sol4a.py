pos=0
sum=0
L=[67,153,311,96,370,4050,371,955,407]
while pos<len(L):
    if L[pos]%2==1:
        sum=sum+L[pos]
    pos=pos+1
print(sum)
