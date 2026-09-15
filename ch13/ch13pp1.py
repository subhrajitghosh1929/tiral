
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
