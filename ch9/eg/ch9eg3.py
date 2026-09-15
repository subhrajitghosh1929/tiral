string1=input("enter string:")
length=len(string1)
i=0
for a in range(-1,(-length-1 ),-1):
    print(string1[i],"\t",string1[a])
    i+=1
