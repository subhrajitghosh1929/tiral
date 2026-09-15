val=eval(input("enter a list :"))
t=[]
print("the original list is ",val)
for i in val:
    if i not in t :
        t.append(i)
val=list(t)
print("list after removing dupicate: ",val)

[11,3,4,2,6,7,0,7,12,5,0,1]
