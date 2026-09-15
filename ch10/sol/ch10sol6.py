lst=eval(input("enter list:"))
length=len(lst)
biggest=secondbiggest=lst[0]
for i in range(1,length):
    if lst[i]>biggest:
        secondbiggest=biggest
        biggest = lst[i]
    elif lst[i] > secondbiggest:
        secondbiggest =lst[i]
print("largest number of the list:",biggest)
print("2nd-largest number of the list:",secondbiggest)
