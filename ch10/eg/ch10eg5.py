#1
print("#1")
val=[17,24,15,30]
print("The original list is : ",val)
print()
val.extend([34,27])
print("The extended list is : ",val)
#2
#print("#2")
print()
c=int(input("How many elements to be added to the list ?"))
for j in range(c):
    elem=int(input("Element "+str(j+1)+": "))
    val.extend([elem])
print()
print("The further extended list is : ",val)
#3
print("#3")
print()
c=int(input("How many elements to be added to the list ?"))
for j in range(c):
    pos=int(input("Enter element position : "))
    ele=int(input("Enter the element to be inserted/added at position  "+str(pos)+": "))
    val.insert(pos,ele)
print()
print("The changed list is : ",val)

#4
print("#4")
print()
c=int(input("How many elements to be deleted from the list ?"))
for j in range(c):
    pos=int(input("Enter element position : "))
    val.pop(pos-j)
print()
print("The changed list is : ",val)
print("the element at position 3 is ",val[3])

#5
print("#5")
print()
#d=int(input("How many elements to be deleted from the list ?"))
d=int(input("Enter the element to be deleted : "))
for j in range(len(val)):
    if d==val[j]:
        val.remove(d)      
print()
print("The changed list is : ",val)
