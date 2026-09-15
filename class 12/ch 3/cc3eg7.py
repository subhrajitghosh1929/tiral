def myFunc3(myList):
    print("\t Inside called Function now")
    print("\t List recived :",myList)
    myList.append(2)
    myList.extend([5,1])
    print("\t List after adding some elements:",myList)
    myList.remove(5)
    print("\t List within calling funtion , after all change:",myList)
    return
List1=[1]
print("List before function call:",List1)
myFunc3(List1)
print("\List afrter function call:",List1)
