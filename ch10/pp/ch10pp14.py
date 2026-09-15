l1=[17,24,15,30,34,27]
l2=l1.copy()
print("original list ",l1)
print("created copy of the list:",l2)
l2[0]+=10
l2[-1]+=10
print("copy of the list after change:",l2)
print("original list:",l1)
