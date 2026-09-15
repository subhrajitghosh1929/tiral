lst1=eval(input("Enter list1:"))
lst2=eval(input("Enter list2:"))
mx1=max(lst1)
mx2=max(lst2)
if mx1>=mx2:
    print(mx1,"the maximum is a list1 at index",lst1.index(mx1))
else:
    print(mx2,"the maximum is a list2 at index",lst2.index(mx2))
