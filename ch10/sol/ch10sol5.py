listA=eval(input("enter a list1:"))
listB=eval(input("enter a list2:"))
len1=len(listA)
len2=len(listB)
for a in range(len1):
    ele=listA[a]
    if ele in listB:
        print("overlapped")
        break
else:
    print("separated")
