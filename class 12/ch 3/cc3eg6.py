def myFunc2(myList):
    print("\n\t Inside CALLED Function now")
    print("\t list received:",myList)
    myList[0]+=2
    print("\t list within called function , after change :",myList)
    return
List1=[1]
print("List before function call :",List1)
myFunc2(List1)
print("\n List after Function call:",List1)
