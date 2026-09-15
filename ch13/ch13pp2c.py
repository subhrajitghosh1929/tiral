# according to first name of recipient 
L = [("Wilhelm Conrad R Ontgen","Physics",1901),("Ronald Ross","Medicine",1902), ("Marie Curie", "Physics",1903), ("Ivan Pavlov","Medicine",1904),("Henryk Sienkiewicz","Literature",1905),("Theodore Roosevelt","Peace",1906)]
st = ''
lst = []
x = 0 
for a in L :
    st = ''
    for b in a[0]:
        if b == ' ' :
            break
        else :
            st = st + b
    lst.insert(x,st)
    x = x + 1
print(lst)
length = len(L)
for i in range (1 , length) :
    temp = lst [ i ]
    extemp = L[ i ]
    j = i - 1
    while j >=0 and temp < lst[j]:
        L[j+1] = L[j]
        lst[j+1] = lst[j]
        j = j - 1
    L[j+1] = extemp
    lst[j+1] = temp
for x in L:
    print(x)
