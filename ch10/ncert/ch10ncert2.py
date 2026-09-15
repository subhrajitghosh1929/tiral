val=eval(input("enter a list :"))
plist=[]
nlist=[]
c=0
for i in range (len(val)):
    if val[i] < 0 :
        nlist.append(val[i])
    elif val[i] > 0 :
        plist.append(val[i])
    else:
        c+=1
print("the original list is ",val)
print("the +ive list is ",plist)
print("the -ive list is ",nlist)
print("the no. of zeroes in the list is ",c)
