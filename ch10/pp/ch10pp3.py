l1=[17,24,15,30,34,27]
print("original list1:",l1)
l2=[27,24,15,30,34,37]
print("original list2: ",l2)
l3=l1.copy()
print("original list3:",l3)
l3.extend(l2)
print("copy of the list after change:",l3)

