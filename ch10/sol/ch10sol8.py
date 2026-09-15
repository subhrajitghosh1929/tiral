lst=eval(input("enter a list:"))
item=int(input("enter element to be removed:"))
c=lst.count(item)
if c==0:
    print(item,"not in list")
else:
    while c > 0:
        i=lst.index(item)
        lst.pop(i)
        c=c-1
print("list after removing",item,":",lst)
