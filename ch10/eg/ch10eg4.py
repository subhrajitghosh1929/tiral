lst=[]
r=int(input("how many rows?"))
c=int(input("how many columbs ?"))
for i in range(r):
    row=[]
    for j in range(c):
        elem=int(input("Element in row "+str(i+1)+", col "+str(j+1)+": "))
        row.append(elem)
    lst.append(row)
print("list created is:",lst)
print("---------------------")
print("list create is:")
print("lst=[")
for i in range(r):
    print("\t[",end=" ")
    for j in range(c):
        print(lst[i][j],end=" ")
    print("]")
print("\t]")
# difference between append and extend is that in append 
print("number of rows in list 'lst':",len(lst))
print("number of cols in list 'lst':",len(lst[1]))
#2
l2=[[1,2,3],[5,6]]
print("number of rows in list 'lst':",len(l2))
print("number of cols in list 'lst':",len(l2[0]))
