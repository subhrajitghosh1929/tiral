FILE : CH13pp1

E={}
ans = "y"
while ans == "y" or ans == "Y" :
    name=input("enter the name :")
    vote=int(input("number the vote per candidate :"))
    E[name]=vote
    ans=input("y or n :-")
listA=[]
listB=[]
F=[]
F=sorted(E)
print(E)
print(F)
listA =sorted( E.keys())
listB =sorted(E.items())   
print(listA)
print(listB)

FILE : CH13pp2

# according to last name of recipient 
L = [("Wilhelm Conrad R Ontgen","Physics",1901),("Ronald Ross","Medicine",1902), ("Marie Curie", "Physics",1903), ("Ivan Pavlov","Medicine",1904),("Henryk Sienkiewicz","Literature",1905),("Theodore Roosevelt","Peace",1906)]
st = ''
lst = []
x = 0 
for a in L :
    st = ''
    for b in a[0]:
        if b == ' ' :
            st = ''
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

FILE : CH13pp3

lst = eval(input("Enter a three digit numbers list = "))
length = len(lst)
for i in range(1,length):
    temp = lst[i]%10
    t = lst[i]
    j = i-1
    while j>=0 and temp<(lst[j]%10):
        lst[j+1] = lst[j]
        j = j -1
    lst[j+1] = t
print(lst)

FILE : CH13pp4

a =  eval(input("Enter a list of string = "))
for i in range (len(a)):
    for j in range(len(a)-1):
        if len(a [ j ] ) > len(a [ j + 1 ]) :
            a [ j ] , a [ j + 1 ] = a [ j + 1 ] , a [ j ]
print(a)

FILE : CH13pp5

lst = [(103 , 'Ritika' , 3001),(104 ,'john',2819),(101,'Razai',3451),(105,'Tarandeep',2971)]
for i in range( len( lst ) - 1 ):
    for j in range( len ( lst ) - 1 ):
        if lst [ j ] [ 2 ] < lst [ j + 1 ] [ 2 ] :
            lst [ j ] , lst [ j + 1 ] = lst [ j + 1 ] , lst [ j ]
print(lst)
