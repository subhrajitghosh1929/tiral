L=['q','w','e','r','t','y']
length=len(L)
for a in range(length):
    print("at index",a,"and",(a-length),"element:",L[a])
    
l1,l2=[1,2,3],[1,2,3]
l3=[1,[2,3]]
print(l1==l2)
print(l1==l3)
