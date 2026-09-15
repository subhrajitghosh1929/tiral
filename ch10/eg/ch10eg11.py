lst=eval(input("enter a list:"))
length=len(lst)
element=int(input("enter element to be searched for:"))
for i in range(0,length):
    if element == lst[i]:
        print(element,"found at index",i)
        break
else:
    print(element,"not found in given list")
